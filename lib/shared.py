from typing import List, Tuple, Union

DICE_SIDES = 6
SUCCESS_VALUE = int(DICE_SIDES / 2) + 1
MAX_SUCCESS_PERC = 70
MAX_ACTION_DICE = 6


def resolve_dice(action_dice: List[int], danger_dice: List[int]) -> List[int]:
    for danger_die in sorted(danger_dice):
        try:
            action_dice.remove(danger_die)
        except ValueError:
            # Sometimes we try to remove a value that doesn't exist, that's fine here, just move on
            pass

    return action_dice


def resolve_roll(action_dice: List[int], danger_dice: Union[List[int], Tuple]) -> int:
    result_dice = resolve_dice(action_dice, danger_dice)

    top_result = max(result_dice or [0])
    return top_result


def is_success_roll(top_result: int) -> bool:
    return top_result >= SUCCESS_VALUE
