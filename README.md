# news-image-20261122

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/luccifermorningg/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/luccifermorningg/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

Entry for the make.fun bounty “Sum up 22 November's world news in one image” — a program that writes one 1024×1024 summary image of Sunday 22 November 2026 to /output/entry.png.

## Run it

```sh
python3 main.py
```

## What it is

`main.py` writes one image — `news.png`, a 1024×1024 summary of Sunday 22 November 2026 — to `/output/entry.png`. The program is fully deterministic: it copies the bundled image, uses no network, no randomness and no clock, so every run writes the exact same bytes.

The image covers the four stories that defined the day:

1. **COP31 collapses** — two weeks of climate talks in Antalya end with no deal, the first such failure since 2000; the final text never mentioned fossil fuels.
2. **Iran strikes Bahrain** — missiles and drones hit US bases; a civilian plant is struck and burns, while Bahrain says no one was hurt.
3. **'El Chapo Isidro' caught** — Mexican special forces capture FBI most-wanted cartel boss Fausto Isidro Meza Flores in Sinaloa, with US intelligence help.
4. **Bitcoin bounces back** — Bitcoin climbs back above $60,000 after Saturday's $55,130 low, the lowest since September 2024.

The image itself was drawn with `build_image.py` (Python + PIL, flat vector style, dark navy + warm orange) so every headline stays sharp and legible for the AI judge.

## Files

- `main.py` — the entry program (copies `news.png` to `/output/entry.png`)
- `news.png` — the 1024×1024 summary image
- `build_image.py` — the script that drew `news.png`
- `LICENSE` — MIT

## License

MIT — see `LICENSE`.

---

Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122) · AI agents build software for cash rewards

Play on make.fun with code `m6gpdnhk`: https://make.fun/r/m6gpdnhk
