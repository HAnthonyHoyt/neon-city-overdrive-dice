import datetime
import itertools
import time
from multiprocessing import Pool, cpu_count
from typing import List, Set, Tuple

from lib import resolve_roll, is_success_roll, MAX_SUCCESS_PERC, MAX_ACTION_DICE, DICE_SIDES

dice_rolls = {}


def get_dice_rolls(total_dice: int) -> Set[Tuple]:
    # To save a little time, we're going to generate each sequence once and then reuse it as much as possible
    # This happens once per thread though, so it doesn't save as much time as I want. That being said, I'm not going to
    # bother with shared thread memory when the amount of time and memory it takes to generate even the largest product
    # is fairly trivial.
    if total_dice not in dice_rolls:
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
    print(f"Starting calculations, attempting all combinations for 1 to {MAX_ACTION_DICE} action dice")
    print("Results will take a long time to generate, please be patient")
    with Pool(cpu_count() - 1) as proc_pool:
        dice_results = proc_pool.map(calculate_action_total, range(1, MAX_ACTION_DICE + 1))
        proc_pool.close()
        proc_pool.join()

    for dice_result in dice_results:
        print('\n'.join(dice_result))


if __name__ == '__main__':
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    perf_span = end - start
    time_delta = datetime.timedelta(seconds=int(perf_span))
    print(f"Process took {time_delta} long to process")
