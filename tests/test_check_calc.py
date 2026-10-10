import itertools
import unittest

from check_calc import count_failures, get_success_rate
from lib import DICE_SIDES, is_success_roll, resolve_roll


class TestExactCalculation(unittest.TestCase):
    def test_small_pools_match_roll_enumeration(self):
        for action_total in range(4):
            for danger_total in range(4):
                with self.subTest(action=action_total, danger=danger_total):
                    failures = 0
                    for roll in itertools.product(range(1, DICE_SIDES + 1), repeat=action_total + danger_total):
                        action = list(roll[:action_total])
                        danger = roll[action_total:]
                        failures += not is_success_roll(resolve_roll(action, danger))
                    self.assertEqual(failures, count_failures(action_total, danger_total))

    def test_seven_danger_dice_remain_above_threshold_for_six_action_dice(self):
        rate, total = get_success_rate(6, 7)
        self.assertEqual(6 ** 13, total)
        self.assertAlmostEqual(71.86633, rate, places=4)

    def test_large_pools_match_reference_counts(self):
        # Exact counts from the previous calculator, on either side of 70%.
        expected_failures = {
            48: 87174485291373534168920904631026272725449449606519545756261149086724,
            49: 567415323111919482333489825215961423321876774117667603675919236155384,
        }
        for danger_total, failures in expected_failures.items():
            with self.subTest(danger=danger_total):
                self.assertEqual(failures, count_failures(40, danger_total))


if __name__ == "__main__":
    unittest.main()
