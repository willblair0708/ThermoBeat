import unittest
import simulation
import harvested_energy_estimation

'''
This script contains test cases for the ThermoBeat system simulation and harvested energy estimation functions. It tests the teg_output, ltc3108_output, and energy_harvested functions using sample input data, and checks whether the output values match the expected values within a certain tolerance.

To run the tests, execute the following command from the software/tests folder:
python -m unittest test_thermobeat.py

If all tests pass, you should see output similar to the following:
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
'''

class TestThermoBeat(unittest.TestCase):
    def test_teg_output(self):
        temperature_gradient = 3.0
        E1 = 50.4
        I1max = 3.11

        output_voltage, output_current = simulation.teg_output(temperature_gradient, E1, I1max)
        expected_voltage = 151.2
        expected_current = 9.33

        self.assertAlmostEqual(output_voltage, expected_voltage, places=1)
        self.assertAlmostEqual(output_current, expected_current, places=2)

    def test_ltc3108_output(self):
        input_voltage = 151.2
        input_current = 9.33

        output_voltage, output_current = simulation.ltc3108_output(input_voltage, input_current)
        expected_voltage = 3300
        expected_current = 101.8

        self.assertAlmostEqual(output_voltage, expected_voltage, places=0)
        self.assertAlmostEqual(output_current, expected_current, places=1)

    def test_energy_harvested(self):
        temperature_gradient = 3.0
        duration = 2.0
        output_voltage = 3300
        output_current = 101.8

        energy = harvested_energy_estimation.energy_harvested(temperature_gradient, duration, output_voltage, output_current)
        expected_energy = 672

        self.assertAlmostEqual(energy, expected_energy, places=0)

if __name__ == '__main__':
    unittest.main()
