import unittest
class test_paymenttest(unittest.TestCase):
    def test_paymentindollars(self):
        print("payment in dollars")
        self.assertTrue(True)
    def test_paymentinrupess(self):
        print("payment in rupess")
        self.assertTrue(True)
if __name__=="__main__":
    unittest.main()