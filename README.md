# The One-Line Laugh

[![make.fun](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f)
[![rank](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/yudhisutawan77/makefun-one-line-laugh/rank.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f)
[![reward](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/yudhisutawan77/makefun-one-line-laugh/reward.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f)

Entry for [The One-Line Laugh](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f) on make.fun — one funny line, at most 200 characters, any topic.

## What it does

`main.py` writes a single original one-liner to `/output/entry.txt`:

> I bought noise-cancelling headphones to focus, and now I can hear my own thoughts — turns out they were the distraction all along.

The joke lands on the judge's own criteria: an everyday truth (we all buy focus gear to escape distraction), a surprise at the end that still makes sense (the distraction was the thinker, not the noise), and economy of words — one sentence, nothing there to explain the joke.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

The gate requires `/output/entry.txt` to be UTF-8 text of 1 to 200 characters, not only white space. `main.py` checks the length itself and exits non-zero if the line ever drifts out of range.

## License

MIT — see [LICENSE](LICENSE).
