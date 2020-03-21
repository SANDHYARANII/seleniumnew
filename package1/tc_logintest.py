import unittest
class logintest(unittest.TestCase):
    def test_loginbyemail(self):
        print("this is login by email test")
        self.assertTrue(True)
    def test_loginbyfacebook(self):
        print("this is login by facebook test")
        self.assertTrue(True)
if __name__=="__main__":
    unittest.main()
    unittest.main()
