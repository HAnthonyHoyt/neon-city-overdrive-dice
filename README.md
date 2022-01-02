# Neon City Overdrive Dice Simulator/Calculator

This is a pair of scripts meant to calculate the success rate for various dice combinations used in the tabletop RPG
game "Neo City Overdrive" (NCO). The scripts were created to show two approaches to determining the chances for
succeeding at a roll. NCO uses a modified version of the Blades in the Dark approach of rolling dice to help determine
if what the player wants is possible. It's an interesting mechanic but one that has some predictable results. The point
of this script though, is to go over what those results might be and demonstrating two ways of coming up with the odds
of success.

## Running the scripts

There are two versions of this script

* Random number generation
* All possible combinations

To run the scripts, you just need to have Python 3 installed and issue one of the following commands

**Random Generator**

> python check_random.py

**All Combinations**

> python check_calc.py

Each script will start with one action die and work it's way up to 6 action dice before quitting. The maximum number of
danger dice is based on the success rate. If the last die poll of action and danger dice resulted in a success rate of
less than 70%, then the script will move up to the next level of action dice and reset the danger dice to 0 to start all
over again.

70% was set based on a quote from a Reddit post
(<https://www.reddit.com/r/rpg/comments/lil3al/statistical_analysis_of_neon_city_overdrives_core/>). The quote is
attributed to Gary Gygax but I haven't found any other source for the quote yet. The quote is

> You want to your players to have a 70% chance of success, and a 30% chance of failure, but you want them to feel as
> though they have a 30% chance of success, and a 70% chance of failure.

Over all, this feels like a fun rule to play by but the question is, how do we make the player feel like they only have
a 30% chance of success. In the above Reddit post, for NCO, it's suggested (and I agree) is to push as much danger dice
on the user to suggest the difficulty while secretly knowing that the player has a better chance then they might
realize.

So the goal here is to just strengthen this argument by allowing first a repeatable test script for all game masters to
try and see for themselves.

## Results

You can see the results using the random method in [Random Die Results](RAND_RESULTS.md) page. Currently, I don't have
the results for the fully calculated results, but I have partial results (up to 5 action dice) in the
[Calculated Die Results](CALC_RESULTS.md) page.