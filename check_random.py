import itertools
import random

from lib import resolve_roll, is_success_roll, MAX_SUCCESS_PERC, MAX_ACTION_DICE

TOTAL_ATTEMPTS = 1000000


def roll_die() -> int:
    return random.randint(1, 6)


def get_success_rate(action_total: int, danger_total: int) -> float:
    good_results = 0
    for _ in range(TOTAL_ATTEMPTS):
        action_dice = [roll_die() for _ in range(action_total)]
        danger_dice = [roll_die() for _ in range(danger_total)]

        top_result = resolve_roll(action_dice, danger_dice)
        is_successful = is_success_roll(top_result)
        good_results += is_successful

    percent_success = good_results / TOTAL_ATTEMPTS * 100
    return percent_success


def main():
    for action_total in range(1, MAX_ACTION_DICE + 1):
        for danger_total in itertools.count(start=0, step=1):
            percent_success = get_success_rate(action_total, danger_total)
            results = "" if percent_success < MAX_SUCCESS_PERC else " - Good!"
            print(f"{action_total} vs {danger_total} - {percent_success:2.0f}%{results}")
            if percent_success < MAX_SUCCESS_PERC:
                # We stop calculating once we're passed this value, so we can go on to the next action total
                break


if __name__ == '__main__':
    main()
