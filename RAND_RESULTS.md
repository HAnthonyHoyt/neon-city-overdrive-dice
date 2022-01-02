# Random Roll Results

So here is the output for one run of the `check_random.py` script:

```commandline
1 vs 0 - 50%
2 vs 0 - 75% - Good!
2 vs 1 - 67%
3 vs 0 - 88% - Good!
3 vs 1 - 81% - Good!
3 vs 2 - 74% - Good!
3 vs 3 - 67%
4 vs 0 - 94% - Good!
4 vs 1 - 90% - Good!
4 vs 2 - 84% - Good!
4 vs 3 - 78% - Good!
4 vs 4 - 72% - Good!
4 vs 5 - 65%
5 vs 0 - 97% - Good!
5 vs 1 - 94% - Good!
5 vs 2 - 91% - Good!
5 vs 3 - 86% - Good!
5 vs 4 - 81% - Good!
5 vs 5 - 75% - Good!
5 vs 6 - 69%
6 vs 0 - 98% - Good!
6 vs 1 - 97% - Good!
6 vs 2 - 95% - Good!
6 vs 3 - 91% - Good!
6 vs 4 - 87% - Good!
6 vs 5 - 82% - Good!
6 vs 6 - 77% - Good!
6 vs 7 - 72% - Good!
6 vs 8 - 66%
```

## What the results say

So this results show that on average, you don't want to add more danger die than there are action dice except maybe for
6 action dice. Otherwise, you dip bellow the 70% success rate.

## What is the script doing

This script tries each die combination 1 million times to try and get a general feeling of what is the expected success
rate is for each die pool. The first number is the number of action dice, while the second number is the number of
danger dice. You'll see what's happening here is that we start with one action die and zero danger dice and then keep
adding danger dice until the success rate dips below 70%, then we add an action die and reset the number of danger dice
before trying again.
