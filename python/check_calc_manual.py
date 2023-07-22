import itertools
from typing import List, Tuple, Union

DICE_SIDES = 6
SUCCESS_VALUE = int(DICE_SIDES / 2) + 1
MAX_SUCCESS_PERCENTAGE = 70
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


def get_dice_rolls(total_dice: int) -> List[Tuple]:
    if total_dice == 0:
        return [(0,)]

    return list(itertools.product(range(1, DICE_SIDES + 1), repeat=total_dice))


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


def calculate_action_total(action_total: int) -> List[str]:
    action_results: List[str] = []
    print(f"Calculating for {action_total} action dice")
    for danger_total in itertools.count(start=0, step=1):
        print(f"Calculating {action_total} vs {danger_total}")
        percent_success, total_tries = get_success_rate(action_total, danger_total)
        results = "" if percent_success < MAX_SUCCESS_PERCENTAGE else " - Good!"
        result_string = f"{action_total} vs {danger_total} - {percent_success:2.0f}% out of {total_tries:12,} " \
                        f"combinations{results}"
        action_results.append(result_string)
        if percent_success < MAX_SUCCESS_PERCENTAGE:
            # We stop calculating once we're passed this value, so we can go on to the next action total
            break

    print(f"Done calculating for {action_total} action dice")
    return action_results


def main():
    print(f"Starting calculations, attempting all combinations for 1 to {MAX_ACTION_DICE} action dice")
    print("Results will take a long time to generate, please be patient")
    for action_dice in range(1, MAX_ACTION_DICE + 1):
        dice_result = calculate_action_total(action_dice)
        print('\n'.join(dice_result))


if __name__ == '__main__':
    main()
