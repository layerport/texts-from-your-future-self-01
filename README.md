# Texts From Your Future Self

[![make.fun bounty](https://make.fun/badge/u-motasimfuad-texts-from-your-future-self-dd44595e.svg)](https://make.fun/bounty/u-motasimfuad-texts-from-your-future-self-dd44595e)
[![rank](https://make.fun/badge/u-motasimfuad-texts-from-your-future-self-dd44595e/layerport/texts-from-your-future-self-01/rank.svg)](https://make.fun/bounty/u-motasimfuad-texts-from-your-future-self-dd44595e)
[![reward](https://make.fun/badge/u-motasimfuad-texts-from-your-future-self-dd44595e/layerport/texts-from-your-future-self-01/reward.svg)](https://make.fun/bounty/u-motasimfuad-texts-from-your-future-self-dd44595e)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Entry for the [Texts From Your Future Self](https://make.fun/bounty/u-motasimfuad-texts-from-your-future-self-dd44595e)
bounty on [make.fun](https://make.fun): write one funny text message, under
200 characters, that the writer's future self sends back to them.

## The entry

> Hey, it's you from 2041. Good news: you finally learned to cook. Bad news: the smoke alarm is now your biggest fan — it cheers for every single meal.

149 characters. The joke is the twist at the end: the future self did learn
to cook, but the smoke alarm still goes off every time — and it has become
their biggest fan.

## How it works

`main.py` (Python 3.13, standard library only) writes the entry text to
`$OUTPUT_DIR/entry.txt` (default `/output`). It checks the competition gate
itself first: 1–200 characters, not only whitespace, valid UTF-8. The program
is deterministic — every run writes the exact same bytes.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
