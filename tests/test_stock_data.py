import unittest
from unittest.mock import patch
from io import StringIO

# Import the module containing the functions to be tested
from your_module_name import getDataPoint, getRatio

class TestStockData(unittest.TestCase):

    @patch('urllib.request.urlopen')
    def test_getDataPoint(self, mock_urlopen):
        # Mock response data
        mock_response = StringIO('{"stock": "ABC", "top_bid": {"price": 99.75, "size": 100}, "top_ask": {"price": 99.80, "size": 50}}')
        mock_urlopen.return_value = mock_response

        # Call the function under test
        quote = json.loads(mock_urlopen('http://localhost:8080/query?id=0.123456789').read())
        stock, bid_price, ask_price, price = getDataPoint(quote)

        # Assert the expected values
        self.assertEqual(stock, "ABC")
        self.assertEqual(bid_price, 99.75)
        self.assertEqual(ask_price, 99.80)
        self.assertEqual(price, 99.775)

    def test_getRatio(self):
        # Test when the denominator is zero
        ratio = getRatio(100.0, 0.0)
        self.assertIsNone(ratio)

        # Test when both values are non-zero
        ratio = getRatio(100.0, 50.0)
        self.assertEqual(ratio, 2.0)

        ratio = getRatio(75.0, 150.0)
        self.assertEqual(ratio, 0.5)

if __name__ == '__main__':
    unittest.main()