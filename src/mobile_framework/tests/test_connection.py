
import unittest

from mobile_framework.mobile_device import MobileDevice

class TestConnection(unittest.TestCase):
    

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_connect_device_to_the_server(self):
        device = MobileDevice()
        isConnected = device.openConnection("s15016hv01", "Service Monitoring")
        
        self.assertEqual(isConnected, True, "Device connection to the server failed")
        pass
    
    
    def test_disconnect_device_to_the_server(self):
        device = MobileDevice()
        isDisconnected = device.closeConnection()
        
        self.assertEqual(isDisconnected, True, "Device disconnection to the server failed")
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()