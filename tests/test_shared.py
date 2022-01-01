import unittest

from lib import resolve_roll, is_success_roll


class TestShared(unittest.TestCase):

    def test_resolve_roll(self):
        # We should get the highest value remaining after all dice matching the danger dice have been removed
        action_dice = [1, 2, 3, 4]
        danger_dice = [1, 2]
        expected_result = 4

        self._check_resolve_roll(action_dice, danger_dice, expected_result)

    def test_resolve_roll_all_dice_removed(self):
        # If we remove all danger dice, then we treat this as a 'zero'
        action_dice = [1, 2]
        danger_dice = [1, 2]
        expected_result = 0

        self._check_resolve_roll(action_dice, danger_dice, expected_result)

    def test_resolve_roll_highest_value_check(self):
        # We're removing values over and under the remaining values, but we should still get the proper highest value
        action_dice = [1, 2, 3, 4, 5]
        danger_dice = [1, 2, 5]
        expected_result = 4

        self._check_resolve_roll(action_dice, danger_dice, expected_result)

    def test_resolve_roll_multiple_same_value(self):
        # We sometimes have to remove multiple dice of the same value, but we should still leave any remaining dice of
        # the same value if we happen to see them
        action_dice = [4, 4, 4]
        danger_dice = [4, 4]
        expected_result = 4

        self._check_resolve_roll(action_dice, danger_dice, expected_result)

    def test_is_success_roll(self):
        # Give all the possible values from a d6, verify what should be marked as a success or not
        values = [(1, False), (2, False), (3, False),
                  (4, True), (5, True), (6, True)]
        for (value, expected_result) in values:
            self.assertEqual(expected_result, is_success_roll(value))

    def _check_resolve_roll(self, action_dice, danger_dice, expected_result):
        result = resolve_roll(action_dice, danger_dice)

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
