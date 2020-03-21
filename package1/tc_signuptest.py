import unittest
class signuptest(unittest.TestCase):
    def test_signupbyemail(self):
        print("this is signup by email test")
        self.assertTrue(True)
    def test_signupbyfacebook(self):
        print("this is signup by facebook")
        self.assertTrue(True)
if __name__=="__main__":
    unittest.main()