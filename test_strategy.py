import unittest
import strategy

class StrategyTest(unittest.TestCase):

    def test_print_output(self):
        strat0 = strategy.StrategyExample()

        strat1 = strategy.StrategyExample(strategy.execute_replacement1)
        strat1.name = 'Strategy Example 1'

        strat2 = strategy.StrategyExample(strategy.execute_replacement2)
        strat2.name = 'Strategy Example 2'

        first_line = strat0.execute()
        second_line = strat1.execute()
        third_line = strat2.execute()

        self.assertEqual(first_line, 'Strategy Example 0')
        self.assertEqual(second_line, 'Strategy Example 1 from execute 1')
        self.assertEqual(third_line, 'Strategy Example 2 from execute 2')

if __name__ == "__main__":
    unitest.main()
