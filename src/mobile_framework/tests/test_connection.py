
import unittest

from mobile_framework.mobile_device import MobileDevice

class TestConnection(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_connect_device_to_the_server(self):
        device = MobileDevice()
        isConnected = device.openConnection()
        
        self.assertEqual(isConnected, True, "Device connection to the server failed")
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()