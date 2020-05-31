import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    def test_empty_price(self):
        """
        Testing stock_price_summary() function with an empty list.
        """
        actual = a1.stock_price_summary([])
        expected = (0,0)
        self.assertEqual(actual, expected)

    def test_one_pos_item(self):
        """
        Testing stock_price_summary() function with a list containing only one
        positive item.
        """
        actual = a1.stock_price_summary([0.3])
        expected = (0.3,0)        
        self.assertEqual(actual, expected)

    def test_one_neg_item(self):
        """
        Testing stock_price_summary() function with a list containing only one
        negative item.
        """
        actual = a1.stock_price_summary([-0.3])
        expected = (0,-0.3)        
        self.assertEqual(actual, expected)

    def test_several_items(self):
        """
        Testing stock_price_summary() function with several mixed items in 
        the price_changes list.

        """
        actual = a1.stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
        expected = (0.14, -0.17)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(exit=False)
