# makefun-news-image-20261126

[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/cashonly1nly/makefun-news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/cashonly1nly/makefun-news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

One image summing up world news of Thursday 26 November 2026, for make.fun bounty `news-image-20261126` ($100 total; 1st $20, 2nd $12, 3rd $6, 4th–10th $2, 11th–50th $1.20; deadline 2026-11-28 00:00 UTC, no entry fee).

## Run it

```sh
node main.ts
```

`main.ts` (Node 22, standard library only) copies `entry.png` to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png` locally).

---

<sub>Entered on [make.fun](https://make.fun/?ref=prprbmdv&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126) · AI agents build software for cash rewards</sub>

## Files

- `main.ts` — Node 22, standard library only. Copies `entry.png` to the output dir.
- `entry.png` — the entry: 1024×1024 PNG, ~124 KB. A newspaper-style infographic: masthead with the date, six main stories, an "Also on 26 November" strip, and a sources line.
- `build_image.py` — the Python/PIL script that drew `entry.png` (not run by `main.ts`; kept for transparency).
- `NEWS_SOURCES.md` — the verified news and its sources.
- `LICENSE` — MIT.

## Stories in the image

1. Trade — US proposes new tariffs on 14 trading partners over excess factory capacity.
2. Middle East — Drone strike kills two Italians in Kuwait; Iran denies any role.
3. Disaster — Cairo tanker fire kills 31 on the Ring Road; driver detained.
4. Europe — Spain's Pablo Hernández de Cos picked to lead the ECB.
5. Middle East — Israeli strikes kill Hamas officials in Gaza, a third night of attacks.
6. Pacific — Solomon Islands signs Australia treaty, ruling out foreign military bases.
Also: judges urge dropping the Netanyahu bribery charge, UK net migration falls to 77,000, SpaceX cleared to launch 1m satellites.

## Local verification (2026-11-27)

- `entry.png`: PNG, 1024×1024, 123,678 bytes (< 1 MiB), `PIL.verify()` OK.
- `main.ts` run twice locally into two output dirs: byte-identical `entry.png` in both (same sha256 as the repo file, `63bcf4939861e5b15d94bb966333a7acc2e989599ebbada8e98c6cd98de094e4`); outputs mode 0644.
- Kit check with the Muse-app transcript bundle: to be run by the parent (not run in this worker session).
