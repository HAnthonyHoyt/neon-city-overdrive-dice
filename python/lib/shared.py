from typing import List, Tuple, Union

DICE_SIDES = 6
SUCCESS_VALUE = int(DICE_SIDES / 2) + 1
MAX_SUCCESS_PERC = 70
MAX_ACTION_DICE = 6


def resolve_dice(action_roll: List[int], danger_roll: List[int]) -> List[int]:
    for danger_die in sorted(danger_roll):
        try:
            action_roll.remove(danger_die)
        except ValueError:
            # Sometimes we try to remove a value that doesn't exist and when you do that with Python, it raises this
            # error.  So, we just ignore this error and move on since this is an expected situation.
            pass

    return action_roll


def resolve_roll(action_roll: List[int], danger_roll: Union[List[int], Tuple]) -> int:
    remaining_dice = resolve_dice(action_roll, danger_roll)

    top_result = max(remaining_dice or [0])
    return top_result


def is_success_roll(top_result: int) -> bool:
    return top_result >= SUCCESS_VALUE
