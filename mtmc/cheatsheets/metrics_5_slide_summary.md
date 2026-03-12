# Metrics — 5 Slide Summary

Scope: formulas and intuition for the tracking metrics used across the five papers

---

## Slide 1 — Why We Need Multiple Metrics

Tracking is not one problem.

A tracker can be:
- good at detecting objects
- bad at preserving identity
- good at identity consistency
- bad at localization

So one score is never enough.

---

## Slide 2 — CLEAR MOT Metrics

### MOTA
`MOTA = 1 - (FN + FP + IDSW) / GT`

Interpretation:
- rewards fewer misses
- rewards fewer false alarms
- penalizes identity switches

### MOTP
Average localization quality of matched pairs.

Interpretation:
- tells us how well matched objects are localized
- implementation details vary, but in these papers it is used as **higher-is-better**

---

## Slide 3 — Identity Metric

### IDF1
`IDF1 = 2 * IDTP / (2 * IDTP + IDFP + IDFN)`

Interpretation:
- directly measures identity preservation
- very useful when association is the main research contribution

Rule of thumb:
if IDF1 drops, the tracker is losing identity consistency.

---

## Slide 4 — Balanced Metric Family

### HOTA
`HOTA = mean_alpha sqrt(DetA_alpha * AssA_alpha)`

Decomposition:
- **DetA** = detection accuracy part
- **AssA** = association accuracy part
- **LocA** = localization accuracy part (sometimes reported)

Why people like HOTA:
it balances detection and association better than MOTA alone.

---

## Slide 5 — How to Read Results in These Papers

### If the paper is about association:
look first at:
- **IDF1**
- **AssA**
- **HOTA**

### If the paper is about full tracking pipelines:
also inspect:
- **MOTA**
- **MOTP / LocA**
- **MT / ML**

### Final caution

Only compare numbers directly when:
- the benchmark is the same
- the evaluation space is the same
- the detection protocol is comparable
