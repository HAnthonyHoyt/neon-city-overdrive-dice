# Maximum Danger Dice by Action Dice

This table shows the largest number of danger dice that keeps the chance of success at least **70%**,
for pools of 1 to 40 action dice. Adding one more danger die drops the success rate below that threshold.

The limits are calculated from exact roll counts using [check_calc.py](check_calc.py). Percentages are rounded to two
decimal places; the limits use the unrounded counts.

One action die has only a 50% chance of success with zero danger dice, so it cannot meet the 70% threshold.

| Action dice | Maximum danger dice | Success at maximum | Success with one more danger die |
| ---: | ---: | ---: | ---: |
| 1 | None | — | — |
| 2 | 0 | 75.00% | 66.67% |
| 3 | 2 | 74.31% | 67.10% |
| 4 | 4 | 72.04% | 65.52% |
| 5 | 5 | 75.18% | 69.22% |
| 6 | 7 | 71.87% | 66.26% |
| 7 | 8 | 73.85% | 68.62% |
| 8 | 10 | 70.50% | 65.50% |
| 9 | 11 | 72.04% | 67.30% |
| 10 | 12 | 73.33% | 68.82% |
| 11 | 14 | 70.13% | 65.75% |
| 12 | 15 | 71.27% | 67.07% |
| 13 | 16 | 72.27% | 68.23% |
| 14 | 17 | 73.16% | 69.27% |
| 15 | 19 | 70.20% | 66.36% |
| 16 | 20 | 71.04% | 67.33% |
| 17 | 21 | 71.80% | 68.20% |
| 18 | 22 | 72.50% | 69.01% |
| 19 | 23 | 73.14% | 69.75% |
| 20 | 25 | 70.43% | 67.05% |
| 21 | 26 | 71.06% | 67.77% |
| 22 | 27 | 71.65% | 68.44% |
| 23 | 28 | 72.20% | 69.06% |
| 24 | 29 | 72.71% | 69.65% |
| 25 | 31 | 70.20% | 67.14% |
| 26 | 32 | 70.71% | 67.72% |
| 27 | 33 | 71.20% | 68.26% |
| 28 | 34 | 71.66% | 68.78% |
| 29 | 35 | 72.10% | 69.27% |
| 30 | 36 | 72.51% | 69.74% |
| 31 | 38 | 70.18% | 67.40% |
| 32 | 39 | 70.60% | 67.87% |
| 33 | 40 | 71.00% | 68.31% |
| 34 | 41 | 71.39% | 68.74% |
| 35 | 42 | 71.75% | 69.15% |
| 36 | 43 | 72.10% | 69.54% |
| 37 | 44 | 72.44% | 69.92% |
| 38 | 46 | 70.28% | 67.74% |
| 39 | 47 | 70.62% | 68.12% |
| 40 | 48 | 70.95% | 68.49% |

To explore these pools and their individual success rates:

```sh
python check_calc.py --max-action-dice 40
```
