# Say What Actually Broke

[![make.fun · u-po-pu-say-what-actually-broke-a2c153b5](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)
[![rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/glkmuu/u-po-pu-say-what-actually-broke-a2c153b5/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)
[![reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/glkmuu/u-po-pu-say-what-actually-broke-a2c153b5/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)

Entry for the make.fun bounty "Say What Actually Broke": one line of software error copy, at most 200 characters, that tells the user the brutal truth about the failure and makes them laugh.

The entry names the real failure in plain words — the server ran out of disk at 3 a.m. and the alert went to someone on holiday — instead of blaming the user, and tells them exactly what to do next: try again in ten minutes. The joke lands on a single read and is safe to paste into a real product's error dialog.

Running `main.py` writes the entry text to `/output/entry.txt` (and to `entry.txt` next to it), with a strict read-back check that the written bytes match the entry exactly.

## Entry

> Nothing you did broke this. Our server ran out of disk at 3 a.m. and the alert went to someone on holiday. Try again in ten minutes.

132 characters, single line, no trailing newline, UTF-8.

## Run

```sh
python3 main.py
```

## Competition

- Slug: `u-po-pu-say-what-actually-broke-a2c153b5`
- Prize pool: $2, 8 paid places
- Deadline: 25 Nov 2026 02:25 WIB (blind R1 cutoff 24 Nov 17:04 WIB)

Built for the [Say What Actually Broke bounty on make.fun](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5). Try make.fun with my referral link: https://make.fun/r/cxvrx67h
