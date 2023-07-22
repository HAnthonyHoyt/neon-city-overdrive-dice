import unittest

from lib import resolve_dice


# We're going to have a stand-alone tests for all the combinations of 'resolve_dice'
class TestResolveDice(unittest.TestCase):

    def test_no_danger(self):
        action_dice = [1, 2, 3]
        danger_dice = []
        expected_result = [1, 2, 3]

        self._check_results(action_dice, danger_dice, expected_result)

    def test_no_matching_danger(self):
        action_dice = [1, 2, 3]
        danger_dice = [4]
        expected_result = [1, 2, 3]

        self._check_results(action_dice, danger_dice, expected_result)

    def test_single_matching(self):
        action_dice = [1, 2, 3]
        danger_dice = [1]
        expected_result = [2, 3]

        self._check_results(action_dice, danger_dice, expected_result)

    def test_multiple_matching(self):
        action_dice = [1, 2, 3]
        danger_dice = [1, 2]
        expected_result = [3]

        self._check_results(action_dice, danger_dice, expected_result)

    def test_multiple_matching_duplicate(self):
        action_dice = [1, 1, 1, 2, 3]
        danger_dice = [1, 1]
        expected_result = [1, 2, 3]

        self._check_results(action_dice, danger_dice, expected_result)

    def test_remove_all_action(self):
        action_dice = [1, 1]
        danger_dice = [1, 1]
        expected_result = []

        self._check_results(action_dice, danger_dice, expected_result)

    def _check_results(self, action_dice, danger_dice, expected_result):
        result_dice = resolve_dice(action_dice, danger_dice)

        self.assertEqual(expected_result, result_dice)


if __name__ == '__main__':
    unittest.main()
