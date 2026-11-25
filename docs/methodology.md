# Maintenance ranking

Metrics come from GitHub GraphQL: stars, reachable history commits on the default branch in the last 30 and 90 days, the most recent default-branch commit, archive status, and so on. Time windows are computed from the snapshot in UTC; pushes to other branches are not counted.

1. Tier by maintenance status first: commits within the last 90 days, no commits for 91–365 days, no commits for over 365 days, and archived or explicitly historical reference.
2. Balanced maintenance score = 100 × (0.40 × star term + 0.35 × activity term + 0.25 × recency term). The star term is log1p(stars) / log1p(100000) and the activity term is log1p(90-day commits) / log1p(500), both capped at 1; the recency term is exp(-days since the last commit / 90).
3. Four views are provided — balanced, stars, 90-day commits, and last commit — with ties ordered stably by stars, then repository name. The active-core shortlist additionally requires a verified open code license.

Stars measure attention; commit counts are affected by repository size, history migrations and documentation updates. Repository metrics do not describe the maintenance of an individual Skill, nor output quality, replication fidelity, accessibility or commercial usability.

The maintenance workflow periodically refreshes metrics, README, CSV and project details. Feature and license verification keep their manual verification date and pinned-commit evidence, and are not rewritten automatically with the snapshot.
