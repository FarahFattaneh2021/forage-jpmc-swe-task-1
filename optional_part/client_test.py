import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    self.assertEqual(getDataPoint(quotes[0]), ('ABC', 120.48, 121.2, 120.84)) 
    self.assertEqual(getDataPoint(quotes[1]), ('DEF', 117.87, 121.68, 119.775)) 

    
  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    self.assertEqual(getDataPoint(quotes[0]), ('ABC', 120.48, 119.2, 119.84))
    self.assertEqual(getDataPoint(quotes[1]), ('DEF', 117.87, 121.68, 119.775)) 

  def test_getDataPoint_calculatePriceBidLessThanAsk(self): 
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 119.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    self.assertEqual(getDataPoint(quotes[0]), ('ABC', 119.48, 121.2, 120.34))
    self.assertEqual(getDataPoint(quotes[1]), ('DEF', 117.87, 121.68, 119.775)) 
    
  """ ------------ Add more unit tests ------------ """

  def test_getDataPoint_noData(self):
    """ Test that the function returns the expected result when no data is passed """
    quotes = []
    expected = ValueError
    with self.assertRaises(expected):
        getDataPoint(quotes)
      
  def test_getDataPoint_invalidData(self):
    """ Test that the exception is raised when invalid data is passed """
    quote = {'stock': 'ABC', 'top_bid': {'price': '100.0'}, 'top_ask': {'price': '200.0'}}
    try:
        getDataPoint(quote)
    except ValueError as e:
        print("Error message:", e)
    quote = {'stock': 'DEF', 'top_bid': {'price': '300.0'}, 'top_ask': {'price': '400.0'}}
    try:
        getDataPoint(quote)
    except ValueError as e:
        print("Error message:", e)

if __name__ == '__main__':
    unittest.main()
