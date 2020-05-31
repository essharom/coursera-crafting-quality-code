import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    def test_empty_in(self):
        '''Test swap_k() with an empty list.'''
        nums = []
        a1.swap_k(nums, 0)
        expected = []
        self.assertEqual(nums, expected)

    def test_one_element(self):
        '''Test swap_k() function if the list is only one element'''
        nums = ['7']
        a1.swap_k(nums, 0)
        expected = ['7']
        self.assertEqual(nums, expected)

    def test_k_zero(self):
        """
        Test swap_k() function if k is zero.
        """

        nums = [1, 2, 3, 4, 5, 6]
        a1.swap_k(nums, 0)
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(nums, expected)

    def test_k_one(self):
        """
        Test swap_k() function if k is 1.
        """

        nums = [1, 2, 3, 4, 5, 6]
        a1.swap_k(nums, 1)
        expected = [6, 2, 3, 4, 5, 1]
        self.assertEqual(nums, expected)

    def test_k_first_part(self):
        """
        Test swap_k() function if k is between 0 and len(L)//2.
        """

        nums = [1, 2, 3, 4, 5, 6]
        a1.swap_k(nums, 2)
        expected = [5, 6, 3, 4, 1, 2]
        self.assertEqual(nums, expected)

    def test_k_at_half(self):
        """
        Test swap_k() function if k is len(L)//2 (boundery).
        """

        nums = [1, 2, 3, 4, 5, 6]
        a1.swap_k(nums, 3)
        expected = [4, 5, 6, 1, 2, 3]
        self.assertEqual(nums, expected)

if __name__ == '__main__':
    unittest.main(exit=False)
