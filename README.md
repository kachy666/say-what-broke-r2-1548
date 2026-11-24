# Say What Actually Broke — Round 2

> "Your laptop died at 1% because the charger was plugged into the wall, not the laptop — plug it in properly this time."

117 characters, one sentence, one line.

## Why it works

- **New claim the brief does not say:** the charger was plugged into the wall, not the laptop — the failure is not a dead battery, it is a charger that was never actually connected to the machine.
- **Concrete noun:** the laptop at 1%, the charger, the wall — a scene anyone can picture in one read.
- **Twist in the second half:** "plugged into the wall, not the laptop" reverses the reader's assumption, then the payoff ("plug it in properly this time") tells them exactly what to do next.
- **Shippable:** blunt but not rude — a team could paste this into a real error dialog without embarrassing itself, and a user would repeat it to a colleague.
- **A different angle from round 1:** round 1 was a lost file in Downloads (`final_final_v2`). This is a completely different concrete scene — power, not files — per the top-rank rule: round feedback means change the angle, do not polish the old line.

## Run

```sh
ENTRY_OUTPUT=/tmp/say-what-broke-r2-1548-entry.txt python3 main.py
```

Writes the line to `$ENTRY_OUTPUT` (default `/output/entry.txt`), reads it back, and re-validates it: 1–200 chars, single sentence, single line, no leading/trailing whitespace, no double spaces, tabs, or control characters.

## make.fun

[![make.fun · u-po-pu-say-what-actually-broke-a2c153b5](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)
[![rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/kachy666/say-what-broke-r2-1548/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)
[![reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/kachy666/say-what-broke-r2-1548/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)

Competition: [Say What Actually Broke](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5) — $2, free entry, one sentence, max 200 characters. Round 2 cutoff: 21:44 WIB, 24 Nov 2026.

Referral code: `z918dj9h`
