import unittest
from Login import LoginDemo
suite = unittest.TestSuite()
tests = [LoginDemo("test_1_login"), LoginDemo("test_2_create_group"), LoginDemo("test_3_create_interface"), LoginDemo("test_4_logout")]
suite.addTests(tests)
runner = unittest.TextTestRunner()
runner.run(suite)

