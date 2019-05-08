#!/usr/local/bin/python3
# Last edited: 19/05/09

from roll import roll
import unittest
from unittest import mock   # pylint: disable=E0611

class TestRoll(unittest.TestCase):

    examples_d100 = [
        {'die_range': 100, 'die_roll': 30, 'modifier': 30, 'difficulty': 40, 'options': ' ', 'roll_result': 'SUCCESS', 'success_level': 20},
        {'die_range': 100, 'die_roll': 60, 'modifier': 30, 'difficulty': 40, 'options': ' ', 'roll_result': 'GREAT SUCCESS', 'success_level': 50},
        {'die_range': 100, 'die_roll': 60, 'modifier': 60, 'difficulty': 40, 'options': ' ', 'roll_result': 'ABSOLUTE SUCCESS', 'success_level': 80},
        {'die_range': 100, 'die_roll': 60, 'modifier': 90, 'difficulty': 40, 'options': ' ', 'roll_result': 'ABSOLUTE SUCCESS', 'success_level': 110},
        {'die_range': 100, 'die_roll': 91, 'modifier': 40, 'difficulty': 120, 'options': ' ', 'roll_result': 'ABSOLUTE SUCCESS', 'success_level': 102},
        {'die_range': 100, 'die_roll': 11, 'modifier': 10, 'difficulty': 40, 'options': ' ', 'roll_result': 'FAIL!', 'success_level': -19},
        {'die_range': 100, 'die_roll': 1, 'modifier': 10, 'difficulty': 40, 'options': ' ', 'roll_result': 'FUMBLE!!', 'success_level': 1},
        {'die_range': 100, 'die_roll': 3, 'modifier': 50, 'difficulty': 40, 'options': ' ', 'roll_result': 'FUMBLE!!', 'success_level': 3},
        {'die_range': 100, 'die_roll': 3, 'modifier': 50, 'difficulty': 40, 'options': '-m', 'roll_result': 'SUCCESS', 'success_level': 13},
        {'die_range': 100, 'die_roll': 20, 'modifier': -30, 'difficulty': 40, 'options': ' ', 'roll_result': 'FAIL!', 'success_level': -50},
        {'die_range': 100, 'die_roll': 60, 'modifier': 50, 'difficulty': 80, 'options': '-r', 'roll_result': 'SUCCESS', 'success_level': 30},
        {'die_range': 100, 'die_roll': 95, 'modifier': 30, 'difficulty': 40, 'options': '-r', 'roll_result': 'ABSOLUTE SUCCESS', 'success_level': 85}
    ]

    examples_d10 = [
        #{'die_range': 10, 'dice_number': 2, 'difficulty': 6, 'die_roll': 6, 'success_rolls': 2}
        {'die_range': 10}
    ]

    def setUp(self):
        pass

    def test_help(self):
        with self.assertRaises(SystemExit) as cm:
            roll([])
        self.assertEqual(0, cm.exception.code)
        with self.assertRaises(SystemExit) as cm:
            roll(['-h'])
        self.assertEqual(0, cm.exception.code)
        with self.assertRaises(SystemExit) as cm:
            roll(['--help'])
        self.assertEqual(0, cm.exception.code)

    def test_wrong_input(self):
        with self.assertRaises(SystemExit) as cm:
            roll(['d15', 10])
        self.assertEqual(1, cm.exception.code)

    @mock.patch('roll.randint')
    def test_d100_working_mock(self, mock_randint):
        mock_randint.return_value = 10
        roll(['d100'])
        self.assertTrue(mock_randint.called)

    @mock.patch('roll.randint')
    def test_d100_test(self, mock_randint):
        for expectation in self.examples_d100:
            mock_randint.return_value = expectation['die_roll']
            actual = roll(['d100', expectation['modifier'], '-d', expectation['difficulty'], expectation['options']])
            test_result(self, expectation, actual)

#    @mock.patch('roll.randint')
#    def test_d10_working_mock(self, mock_randint):
#        mock_randint.return_value = 10
#        roll(['d10', 7])
#        self.assertTrue(mock_randint.called)

#    @mock.patch('roll.randint')
#    def test_d10_test(self, mock_randint):
#        for expectation in self.examples_d6:
#            mock_randint.return_value = expectation['die_roll']
#            actual = roll(['d10', expectation['dice_number'], '-d', expectation['difficulty']])
#            test_result(self, expectation, actual)

def test_result(self, expectation, actual):
    self.assertEqual( expectation['die_range'],   actual['die_range'] )
    # self.assertEqual( expectation['die_roll']+expectation['modifier'],    actual['die_roll'] )
    self.assertEqual( expectation['roll_result'],  actual['roll_result'] )
    self.assertEqual( expectation['success_level'],  actual['success_level'] )

#    if actual['die_range'] == 100:
#        self.assertEqual( expectation['victory_points'], actual['victory_points'] )
#        self.assertEqual( expectation['victory_dice'],   actual['victory_dice'] )
#    elif actual['die_range'] == 10:
#        self.assertEqual( expectation['success_rolls'], actual['success_rolls'] )

if __name__ == '__main__':
    unittest.main()
