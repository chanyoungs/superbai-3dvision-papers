# Metrics — Cheat Sheet

Scope: metrics used across the five papers

---

## Why metrics matter

Tracking metrics do not all reward the same thing.

Some emphasize:
- detection coverage
- localization quality
- identity consistency
- balanced detection + association quality

So a strong tracker should be read with **multiple metrics together**, not just one number.

---

## Core Metrics

### 1. MOTA

Formula:
`MOTA = 1 - (FN + FP + IDSW) / GT`

Where:
- `FN` = false negatives
- `FP` = false positives
- `IDSW` = identity switches
- `GT` = total ground-truth objects

High-level meaning:
**How many overall tracking mistakes are made?**

Rewards:
- good detection coverage
- low false alarms
- low ID switches

Weakness:
can be dominated by detection errors and may hide association quality.

---

### 2. MOTP

Generic form:
`MOTP = (1 / number_of_matches) * sum(match_localization_quality)`

In some implementations, this is written using average overlap / similarity.
In others, it is average localization error.

High-level meaning:
**How well are matched objects localized?**

Important note:
implementation details vary.
In the papers here, reported MOTP is used as **higher-is-better**.

---

### 3. IDF1

Formula:
`IDF1 = 2 * IDTP / (2 * IDTP + IDFP + IDFN)`

Where:
- `IDTP` = identity true positives
- `IDFP` = identity false positives
- `IDFN` = identity false negatives

High-level meaning:
**How consistently does the tracker preserve the correct identity?**

This is often the most intuitive identity metric.

---

## HOTA Family

### 4. HOTA

Formula:
`HOTA = mean_alpha sqrt(DetA_alpha * AssA_alpha)`

High-level meaning:
**Balanced score between detection quality and association quality.**

Why useful:
it avoids rewarding a tracker that is strong on detection but weak on identity, or vice versa.

---

### 5. DetA

Formula:
`DetA_alpha = TP_alpha / (TP_alpha + FP_alpha + FN_alpha)`

Meaning:
**Detection accuracy component inside HOTA.**

---

### 6. AssA

Formal idea:
for each true positive match, measure how well the corresponding trajectory is associated over time.

Compact form:
`AssA_alpha = mean over matched detections of association accuracy`

Meaning:
**How well identities stay linked across time.**

This is often the key metric for association-heavy papers.

---

### 7. LocA

Used in some 3D tracking settings.

Meaning:
**Localization accuracy of matched detections** inside the HOTA decomposition.

In practice:
higher LocA means the predicted object locations are closer to ground truth.

---

## Trajectory Coverage Metrics

### 8. MT (Mostly Tracked)

Formula:
`MT = number of GT trajectories tracked for >= 80% of lifespan / number of GT trajectories`

Meaning:
how many full trajectories are mostly recovered.

### 9. ML (Mostly Lost)

Formula:
`ML = number of GT trajectories tracked for <= 20% of lifespan / number of GT trajectories`

Meaning:
how many trajectories are largely missed.

---

## Practical Reading Guide

- **High MOTA + low IDF1** → detection is fine, identity consistency is weak.
- **High IDF1 + lower MOTA** → identity preservation is strong, but coverage / false positives may still be an issue.
- **High HOTA** → good overall balance between detection and association.
- **High AssA** specifically means the association head is doing real work.

---

## Important Comparison Note

Metrics are only fairly comparable when:
- the same benchmark is used
- the same evaluation space is used (2D box vs ground plane vs 3D world)
- the same detection protocol is roughly comparable

---

## One-Sentence Takeaway

Use **IDF1 / AssA / HOTA** to judge identity quality, and use **MOTA / MOTP / MT / ML** to understand overall coverage and localization behavior.
