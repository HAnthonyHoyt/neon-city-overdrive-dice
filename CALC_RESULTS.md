# Calculated Roll Results

These are sample results. The calculated script now counts matching die-face totals and can compute larger pools quickly.
Run `python check_calc.py --max-action-dice 40` to explore beyond this table:

```commandline
1 vs 0 - 50% out of              6 combinations
2 vs 0 - 75% out of             36 combinations - Good!
2 vs 1 - 67% out of            216 combinations
3 vs 0 - 88% out of            216 combinations - Good!
3 vs 1 - 81% out of          1,296 combinations - Good!
3 vs 2 - 74% out of          7,776 combinations - Good!
3 vs 3 - 67% out of         46,656 combinations
4 vs 0 - 94% out of          1,296 combinations - Good!
4 vs 1 - 90% out of          7,776 combinations - Good!
4 vs 2 - 84% out of         46,656 combinations - Good!
4 vs 3 - 78% out of        279,936 combinations - Good!
4 vs 4 - 72% out of      1,679,616 combinations - Good!
4 vs 5 - 66% out of     10,077,696 combinations
5 vs 0 - 97% out of          7,776 combinations - Good!
5 vs 1 - 94% out of         46,656 combinations - Good!
5 vs 2 - 91% out of        279,936 combinations - Good!
5 vs 3 - 86% out of      1,679,616 combinations - Good!
5 vs 4 - 81% out of     10,077,696 combinations - Good!
5 vs 5 - 75% out of     60,466,176 combinations - Good!
5 vs 6 - 69% out of    362,797,056 combinations
6 vs 0 - 98% out of         46,656 combinations - Good!
6 vs 1 - 97% out of        279,936 combinations - Good!
6 vs 2 - 94% out of      1,679,616 combinations - Good!
6 vs 3 - 91% out of     10,077,696 combinations - Good!
6 vs 4 - 87% out of     60,466,176 combinations - Good!
6 vs 5 - 83% out of    362,797,056 combinations - Good!
6 vs 6 - 77% out of  2,176,782,336 combinations - Good!
6 vs 7 - 72% out of 13,060,694,016 combinations - Good!
```

## What the results say

The random and calculated results agree closely. The 70% cutoff depends on the pool: six action dice and seven danger
dice still succeed about 71.87% of the time.

## What is the script doing

The script counts dice by face value. For each face that can succeed (4, 5, or 6), it counts how many action and danger
dice show that value. A roll fails when the danger count is at least the action count for all three faces. The remaining
dice can show any of the three lower values. These weighted counts give the same exact total as enumerating every roll
without generating billions of individual combinations.
