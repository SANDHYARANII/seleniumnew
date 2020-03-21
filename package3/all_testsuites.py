import unittest
from package1.tc_logintest import logintest
from package1.tc_signuptest import signuptest

from package2.tc_paymenttest import test_paymenttest
from package2.tc_paymentreturns import test_paymentreturntest

t1=unittest.TestLoader().loadTestsFromTestCase(logintest)
t2=unittest.TestLoader().loadTestsFromTestCase(signuptest)
t3=unittest.TestLoader().loadTestsFromTestCase(test_paymenttest)
t4=unittest.TestLoader().loadTestsFromTestCase(test_paymentreturntest)


smokeTest=unittest.TestSuite([t1,t2])
unittest.TextTestRunner(verbosity=2).run(smokeTest)



