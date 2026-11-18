[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/Goresalink/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/Goresalink/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

# 17 November 2026 — The World in One Day

Entry for the make.fun bounty
[news-image-20261117](https://make.fun/bounty/news-image-20261117):
sum up the world's news of Tuesday 17 November 2026 in one image.

## The image

`frontpage.png` (1024×1024, PNG, under 1 MiB) is a front page of the day's
four top stories, each with a real news photo and a caption:

1. **Iran fires drones at a U.S. radar in Bahrain** — Iran's Revolutionary
   Guards fired drones at the U.S. military radar at Sheikh Isa base;
   Bahrain said the attack was intercepted, with no casualties or damage.
2. **Ukraine strike damages Crimea Bridge** — Ukraine severely damaged the
   bridge linking Russia to Crimea; Russia hit bridges in Kyiv in return.
3. **Trump to Asia for nuclear talks with Xi and Putin** — Trump travelled
   to Asia for APEC in Shenzhen and a planned trilateral meeting on nuclear
   issues and Ukraine.
4. **Japan scrambles jets as Russian planes enter airspace** — Japan launched
   fighter jets and protested after two suspected Russian aircraft violated
   its airspace.

## The program

`main.py` (Python 3.13) writes the image to `/output/entry.png`. It needs no
network: it copies the bundled `frontpage.png`, so two runs write identical
bytes.

```sh
python3 main.py   # writes /output/entry.png
```

Photo sources: news photos found via public image search (see `photos/` for
the four source photos). The composed front page was built with Pillow.

## License

MIT — see `LICENSE`.
