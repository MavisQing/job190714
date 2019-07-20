import unittest,os,sys
# from Login import LoginDemo
# suite = unittest.TestSuite()
# tests = [LoginDemo("test_1_login"), LoginDemo("test_2_create_group"), LoginDemo("test_3_create_interface"), LoginDemo("test_4_logout")]
# suite.addTests(tests)
# runner = unittest.TextTestRunner()
# runner.run(suite)
current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)

test_dir=current_directory
discover=unittest.defaultTestLoader.discover(test_dir,pattern='Login*.py')
runner = unittest.TextTestRunner()
runner.run(discover)

