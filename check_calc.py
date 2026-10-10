import argparse
import datetime
import itertools
import time
from functools import lru_cache
from math import comb
from typing import List, Tuple

from lib import MAX_SUCCESS_PERC, MAX_ACTION_DICE, DICE_SIDES, SUCCESS_VALUE


@lru_cache(maxsize=None)
def choose_row(total: int) -> Tuple[int, ...]:
    return tuple(comb(total, count) for count in range(total + 1))


@lru_cache(maxsize=None)
def _count_failures_for_faces(successful_faces: int, action_total: int, danger_total: int) -> int:
    """Count failures using the remaining successful faces and all low faces.

    Assign one successful face at a time. The remaining dice form the same
    subproblem for every pool, so cache those counts across calculations.
    """
    low_faces = SUCCESS_VALUE - 1
    if action_total == 0:
        return (low_faces + successful_faces) ** danger_total
    if danger_total == 0 or successful_faces == 0:
        return low_faces ** (action_total + danger_total)

    action_choices = choose_row(action_total)
    danger_choices = choose_row(danger_total)
    return sum(
        action_choices[face_action] * danger_choices[face_danger]
        * _count_failures_for_faces(
            successful_faces - 1, action_total - face_action, danger_total - face_danger
        )
        for face_danger in range(danger_total + 1)
        # A failure requires every successful action face to be cancelled.
        for face_action in range(min(action_total, face_danger) + 1)
    )


def count_failures(action_total: int, danger_total: int) -> int:
    """Count rolls where every successful face is completely cancelled."""
    successful_faces = DICE_SIDES - SUCCESS_VALUE + 1
    return _count_failures_for_faces(successful_faces, action_total, danger_total)


def get_success_rate(action_total: int, danger_total: int) -> Tuple[float, int]:
    total_rolls = DICE_SIDES ** (action_total + danger_total)
    success_rolls = total_rolls - count_failures(action_total, danger_total)
    return 100 * success_rolls / total_rolls, total_rolls


def calculate_action_total(action_total: int) -> List[str]:
    action_results: List[str] = []
    print(f"Calculating for {action_total} action dice")
    for danger_total in itertools.count(start=0, step=1):
        print(f"Calcing {action_total} vs {danger_total}")
        percent_success, total_tries = get_success_rate(action_total, danger_total)
        results = "" if percent_success < MAX_SUCCESS_PERC else " - Good!"
        result_string = f"{action_total} vs {danger_total} - {percent_success:2.0f}% out of {total_tries:12,} " \
                        f"combinations{results}"
        action_results.append(result_string)
        if percent_success < MAX_SUCCESS_PERC:
            # We stop calculating once we're passed this value, so we can go on to the next action total
            break

    print(f"Done calculating for {action_total} action dice")
    return action_results


def main():
    parser = argparse.ArgumentParser(description="Calculate exact dice success rates")
    parser.add_argument("--max-action-dice", type=int, default=MAX_ACTION_DICE)
    args = parser.parse_args()
    if args.max_action_dice < 1:
        parser.error("--max-action-dice must be at least 1")

    print(f"Calculating exact rates for 1 to {args.max_action_dice} action dice")
    for action_total in range(1, args.max_action_dice + 1):
        print('\n'.join(calculate_action_total(action_total)))


if __name__ == '__main__':
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    perf_span = end - start
    time_delta = datetime.timedelta(seconds=int(perf_span))
    print(f"Process took {time_delta} long to process")
