import unittest
import subprocess

class StrategyTest(unittest.TestCase):

    def test_print_output(self):
        output = subprocess.check_output(["python", "strategy.py"])
        expected_output = 'Strategy Example 0\r\n\
Strategy Example 1 from execute 1\r\n\
Strategy Example 2 from execute 2\r\n'
        # byte representation required due to EOF returned subprocess
        expected_output_as_bytes = expected_output.encode(encoding='UTF-8')
        self.assertEqual(output, expected_output_as_bytes)

if __name__ == "__main__":
    unitest.main()
