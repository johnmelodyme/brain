import unittest
import mock

from brain.core.NeuronModule import NeuronModule

from brain.neurons.system_time_date import System_time_date


class TestSystem_time_date(unittest.TestCase):

    def setUp(self):
        pass

    def test_date_is_returned(self):
        """
        Check that the neuron return consistent values
        :return:
        """

        with mock.patch.object(NeuronModule, 'say', return_value=None) as mock_method:
            system_time_date = Systemdate()
            # check returned value
            self.assertTrue(0 <= int(system_time_date.message["hours"]) <= 24)
            self.assertTrue(0 <= int(system_time_date.message["minutes"]) <= 60)
            self.assertTrue(0 <= int(system_time_date.message["weekday"]) <= 6)
            self.assertTrue(1 <= int(system_time_date.message["day_month"]) <= 31)
            self.assertTrue(1 <= int(system_time_date.message["month"]) <= 12)
            self.assertTrue(2016 <= int(system_time_date.message["year"]) <= 3000)


if __name__ == '__main__':
    unittest.main()
