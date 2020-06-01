import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    def test_zero_passenger(self):
        """
        Testing num_buses() function with 0 passenger.
        """
        actual = a1.num_buses(0)
        expected = 0
        self.assertEqual(actual, expected)
        
    def test_one_passenger(self):
        """
        Testing num_buses() function with 1 passenger.
        """
        actual = a1.num_buses(1)
        expected = 1
        self.assertEqual(actual, expected)
        
    def test_boundary_passenger(self):
        """
        Testing num_buses() function with 50 passenger.
        """
        actual = a1.num_buses(50)
        expected = 1
        self.assertEqual(actual, expected)
        
    def test_more_passenger(self):
        """
        Testing num_buses() function with more than 50 passenger.
        """
        actual = a1.num_buses(51)
        expected = 2
        self.assertEqual(actual, expected)
        
    def test_example_passenger(self):
        """
        Testing num_buses() function with 75 passenger.
        """
        actual = a1.num_buses(75)
        expected = 2
        self.assertEqual(actual, expected)
    
    def test_multiple50_passenger(self):
        """
        Testing num_buses() function with 50x passenger.
        """
        actual = a1.num_buses(150)
        expected = 3
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(exit=False)
