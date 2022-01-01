import itertools
from typing import Tuple, Set

from lib import resolve_roll, is_success_roll, MAX_SUCCESS_PERC, MAX_ACTION_DICE, DICE_SIDES

dice_rolls = {}


def get_dice_rolls(total_dice: int) -> Set[Tuple]:
    # With this method, we're hoping to avoid calculating all the possible dice combinations over and over.
    # Also, we're not returning 'duplicate' combinations.  For example: [1, 2] and [2, 1] are the same, so we don't
    # need to check twice when we know the outcome should be same for both.
    if total_dice not in dice_rolls:
        # dice_rolls[total_dice] = set(itertools.combinations_with_replacement(range(1, DICE_SIDES + 1), total_dice))
        dice_rolls[total_dice] = list(itertools.product(range(1, DICE_SIDES + 1), repeat=total_dice))

    return dice_rolls[total_dice]


def get_success_rate(action_total: int, danger_total: int) -> Tuple[float, int]:
    action_rolls = get_dice_rolls(action_total)
    danger_rolls = get_dice_rolls(danger_total)
    success_rolls = 0
    total_rolls = 0
    for action_roll in action_rolls:
        for danger_roll in danger_rolls:
            top_result = resolve_roll(list(action_roll), danger_roll)
            is_successful = is_success_roll(top_result)
            success_rolls += is_successful
            total_rolls += 1

    percent_success = success_rolls / total_rolls * 100
    return percent_success, total_rolls


def main():
    for action_total in range(1, MAX_ACTION_DICE + 1):
        for danger_total in itertools.count(start=0, step=1):
            percent_success, total_tries = get_success_rate(action_total, danger_total)
            results = "" if percent_success < MAX_SUCCESS_PERC else " - Good!"
            print(f"{action_total} vs {danger_total} - {percent_success:2.0f}% out of {total_tries:12,} tries{results}")
            if percent_success < MAX_SUCCESS_PERC:
                # We stop calculating once we're passed this value, so we can go on to the next action total
                break


if __name__ == '__main__':
    main()
