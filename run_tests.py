import sys
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
sys.path.append("./db_fixture")
sys.path.append("./interface")



test_dir = "./interface"
discover = unittest.defaultTestLoader.discover(test_dir, pattern="*_test.py")


now_time = time.strftime("%Y-%m-%d_%H_%M_%S")
filename = "./report/" + now_time + "_bitsoda_result.html"
report_file = open(filename,"wb")
runner = HTMLTestRunner(stream=report_file, verbosity=2, title="Bitsoda Interface Auto Test Report", description="macOS Mojave version:10.14.6")

runner.run(discover)
report_file.close()


