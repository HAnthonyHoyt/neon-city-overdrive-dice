# Calculated Roll Results

A heads-up, this script takes so long, that I've not had the patience to wait for it to complete all the possible
results with 6 action dice. What I have here for now, is up to 6 action dice and 6 danger dice. As soon as I learn the
results of all the other combinations, I'll post them here:

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

If you looked at the random results first, you'll notice that the results line up nearly perfectly between the two. And
like with the random result, the conclusion is the same. Don't add more danger dice than action dice. Otherwise, the
player will have less than a 70% chance of success.

## What is the script doing

For this version of the script, it's attempting to go through every single die combination for the entire pool of dice.
Each time you add a new die, you increase the number of combinations by 6 times. So once the player has 7 dice in
total (A combination of action and danger dice) we're talking about over a million dice combinations. So that takes a
pretty long time to calculate all the combinations. I've had to create a separate script to calculate the final values
and once that's done, I'll update this message.
