#!/usr/bin/env python3
"""
Forecast ledger — the measurement instrument (layer two, front end).

What it does (the CERTAIN benefit, per METHOD.md's map): it turns a model's
forecasts from ephemeral claims into a scored track record. A single session
cannot score a forecast — the outcome resolves later. This ledger logs
(forecast, probability, resolution criterion, due date, reference class),
resolves each against reality when due, and scores the record: Brier, a
reliability curve, calibration error (ECE), discrimination, and per-class /
per-arm breakdowns.

It does NOT, by itself, make the model forecast better. Whether feeding the
scored track record back improves calibration is the *improvement bet*, which is
pre-registered separately (PRE-REGISTRATION-improvement-bet.md) and NOT assumed
here. Build and trust this as a measurement instrument first.

Record schema (one JSON object per line in the store):
  id                  str   unique
  logged_at           str   ISO date the forecast was made
  question            str
  reference_class     str   for per-class calibration (e.g. "sports-final")
  forecast_prob       float 0..1  (probability the claim resolves TRUE)
  resolution_criterion str  how it will be marked right/wrong
  due_date            str   ISO date the outcome is knowable
  status              str   "open" | "resolved"
  outcome             int   1 | 0 | null (null while open)
  resolved_at         str   ISO date resolved (null while open)
  source              str   free tag, e.g. "run15 full-spec / opus"
  arm                 str   optional grouping (e.g. "spec" | "bare")

CLI:
  python ledger.py log     --q "..." --prob 0.6 --due 2026-12-31 --crit "..." [--refclass X] [--arm spec] [--source ...]
  python ledger.py resolve --id f0007 --outcome 1
  python ledger.py open                     # list unresolved, past-due first
  python ledger.py report  [--arm spec]     # scored track record
"""
import json, sys, argparse, pathlib, datetime

STORE = pathlib.Path(__file__).with_name("forecasts.jsonl")


def _load():
    if not STORE.exists():
        return []
    return [json.loads(l) for l in STORE.read_text(encoding="utf-8").splitlines() if l.strip()]


def _save(rows):
    STORE.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + ("\n" if rows else ""), encoding="utf-8")


def _next_id(rows):
    n = 1 + max([int(r["id"][1:]) for r in rows if r["id"][1:].isdigit()], default=0)
    return f"f{n:04d}"


def log(args):
    rows = _load()
    rec = {
        "id": _next_id(rows),
        "logged_at": args.logged_at or datetime.date.today().isoformat(),
        "question": args.q,
        "reference_class": args.refclass or "",
        "forecast_prob": float(args.prob),
        "resolution_criterion": args.crit or "",
        "due_date": args.due or "",
        "status": "open",
        "outcome": None,
        "resolved_at": None,
        "source": args.source or "",
        "arm": args.arm or "",
    }
    assert 0.0 <= rec["forecast_prob"] <= 1.0, "forecast_prob must be a probability in [0,1]"
    rows.append(rec)
    _save(rows)
    print(f"logged {rec['id']}: p={rec['forecast_prob']} due={rec['due_date']!r} — {rec['question'][:70]}")


def resolve(args):
    rows = _load()
    hit = next((r for r in rows if r["id"] == args.id), None)
    if not hit:
        sys.exit(f"no forecast with id {args.id}")
    hit["outcome"] = int(args.outcome)
    hit["status"] = "resolved"
    hit["resolved_at"] = args.resolved_at or datetime.date.today().isoformat()
    _save(rows)
    b = (hit["forecast_prob"] - hit["outcome"]) ** 2
    print(f"resolved {hit['id']}: outcome={hit['outcome']} (forecast {hit['forecast_prob']}) Brier={b:.3f}")


def open_cmd(args):
    rows = [r for r in _load() if r["status"] == "open"]
    rows.sort(key=lambda r: r["due_date"] or "9999")
    if not rows:
        print("no open forecasts."); return
    print(f"{len(rows)} open forecast(s), earliest-due first:")
    for r in rows:
        print(f"  {r['id']}  due {r['due_date'] or '?':10}  p={r['forecast_prob']:.2f}  {r['question'][:66]}")


def _brier(rs):
    xs = [(r["forecast_prob"] - r["outcome"]) ** 2 for r in rs]
    return sum(xs) / len(xs) if xs else None


def _reliability(rs, bins=(0, .1, .3, .5, .7, .9, 1.0001)):
    out = []
    for lo, hi in zip(bins, bins[1:]):
        b = [r for r in rs if lo <= r["forecast_prob"] < hi]
        if not b:
            out.append((f"[{lo:.1f},{hi:.1f})", 0, None, None)); continue
        mean_p = sum(r["forecast_prob"] for r in b) / len(b)
        rate = sum(r["outcome"] for r in b) / len(b)
        out.append((f"[{lo:.1f},{hi:.1f})", len(b), mean_p, rate))
    return out


def _ece(rs):
    # expected calibration error: |mean_prob - resolve_rate| weighted by bin size
    n = len(rs); tot = 0.0
    for _, cnt, mp, rate in _reliability(rs):
        if cnt:
            tot += (cnt / n) * abs(mp - rate)
    return tot


def _discrimination(rs):
    # crude AUC proxy: resolve rate among top-half vs bottom-half forecasts by prob.
    if len(rs) < 4:
        return None
    s = sorted(rs, key=lambda r: r["forecast_prob"])
    half = len(s) // 2
    lo = sum(r["outcome"] for r in s[:half]) / half
    hi = sum(r["outcome"] for r in s[-half:]) / half
    return hi - lo  # >0 means higher-prob forecasts resolve TRUE more often (good)


def report(args):
    rows = [r for r in _load() if r["status"] == "resolved"]
    if args.arm:
        rows = [r for r in rows if r.get("arm") == args.arm]
    allrows = _load()
    print(f"=== FORECAST LEDGER REPORT ===")
    print(f"records: {len(allrows)} total | {len(rows)} resolved{' (arm='+args.arm+')' if args.arm else ''} | "
          f"{sum(1 for r in allrows if r['status']=='open')} open")
    if not rows:
        print("no resolved forecasts to score yet."); return
    b = _brier(rows)
    print(f"\nBrier score: {b:.3f}   (0 = perfect, 0.25 = always-50%, lower is better)")
    print(f"ECE (calibration error): {_ece(rows):.3f}   (0 = perfectly calibrated)")
    disc = _discrimination(rows)
    print(f"Discrimination (top-half minus bottom-half resolve rate): {disc:+.2f}" if disc is not None
          else "Discrimination: n<4")
    print(f"\nReliability curve (forecast bin -> how often it actually resolved TRUE):")
    print(f"  {'bin':10} {'n':>4} {'mean p':>7} {'resolved':>9}  calibration")
    for lbl, cnt, mp, rate in _reliability(rows):
        if not cnt:
            continue
        gap = rate - mp
        flag = "ok" if abs(gap) <= .1 else ("OVERCONFIDENT" if gap < 0 else "underconfident")
        print(f"  {lbl:10} {cnt:>4} {mp:>7.2f} {rate:>9.2f}  {gap:+.2f} {flag}")
    # per reference class
    classes = sorted({r["reference_class"] for r in rows if r["reference_class"]})
    if classes:
        print(f"\nPer reference class (Brier, n):")
        for c in classes:
            sub = [r for r in rows if r["reference_class"] == c]
            print(f"  {c:22} Brier {_brier(sub):.3f}  (n={len(sub)})")
    # per arm (if mixed)
    arms = sorted({r.get("arm", "") for r in rows if r.get("arm")})
    if len(arms) > 1 and not args.arm:
        print(f"\nPer arm (the judge-free way to compare specs/models on forecast quality):")
        for a in arms:
            sub = [r for r in rows if r.get("arm") == a]
            print(f"  {a:10} Brier {_brier(sub):.3f}  ECE {_ece(sub):.3f}  disc {(_discrimination(sub) or 0):+.2f}  (n={len(sub)})")


def main():
    p = argparse.ArgumentParser(description="Forecast ledger — measurement instrument")
    sub = p.add_subparsers(dest="cmd", required=True)
    lg = sub.add_parser("log"); lg.set_defaults(fn=log)
    lg.add_argument("--q", required=True); lg.add_argument("--prob", required=True)
    lg.add_argument("--due"); lg.add_argument("--crit"); lg.add_argument("--refclass")
    lg.add_argument("--arm"); lg.add_argument("--source"); lg.add_argument("--logged-at", dest="logged_at")
    rs = sub.add_parser("resolve"); rs.set_defaults(fn=resolve)
    rs.add_argument("--id", required=True); rs.add_argument("--outcome", required=True)
    rs.add_argument("--resolved-at", dest="resolved_at")
    op = sub.add_parser("open"); op.set_defaults(fn=open_cmd)
    rp = sub.add_parser("report"); rp.set_defaults(fn=report); rp.add_argument("--arm")
    args = p.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
