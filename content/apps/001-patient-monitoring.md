---
title: Patient-self-initiated long-term monitoring
date: 2026-10-25
tag: Health
summary: A patient-owned, longitudinal symptom-and-physiology log, compressed by AI into a one-page pre-consultation brief — so a 10-minute appointment starts from evidence, not recall.
status: published
---

## The pain

A clinical visit is a compression problem done badly. Months of lived symptoms get squeezed into whatever the patient happens to remember in the first ninety seconds of a consultation — filtered by anxiety, recency bias, and the doctor's first question. The diagnostic record starts from anecdote, not data.

Meanwhile the objectively collectible signal — sleep, resting heart rate, symptom onset times, medication adherence, diet, pain scores — is either sitting in five disconnected apps or nowhere at all.

## The blueprint

A patient-owned longitudinal log with three layers:

1. **Capture** — passive where possible (wearables, phone sensors), active where necessary (30-second structured check-ins: symptom, severity, context, photo). The design constraint is burden: if daily entry takes more than a minute, adherence dies in week three.
2. **Structure** — raw entries normalized into a timeline with tagged episodes. Correlations surfaced, not concluded: "headache episodes cluster 24–48h after poor sleep" is a hypothesis for the clinician, not a diagnosis.
3. **Brief** — before each visit, AI compresses the timeline into a one-page pre-consultation summary: chief complaints by frequency and trajectory, episode clusters, what changed since last visit, and the patient's own three questions. Exportable as PDF, owned by the patient.

## Smallest useful version

No app store, no integrations. A structured notes template plus a weekly AI summary prompt, printed before the visit. If that alone changes the consultation, the platform is worth building. If it doesn't, no amount of engineering would have saved it.

## What would kill it

- **Clinician rejection** — if doctors won't read a one-pager, nothing else matters. Test this first.
- **Adherence decay** — the graveyard of health apps is filled with beautiful day-4 abandonment curves.
- **Liability gravity** — the moment the product interprets rather than organizes, it drifts toward medical-device regulation. Stay on the right side of that line deliberately.
