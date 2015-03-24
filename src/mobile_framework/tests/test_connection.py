
import unittest

from mobile_framework.tests.test_environment import TestEnvironment
from mobile_framework.mobile_device import MobileDevice

class TestConnection(unittest.TestCase):
    

    def setUp(self):
        self.device = MobileDevice()
        pass

    
    def tearDown(self):
        self.device.disconnect()
        pass

    
    def test_connect_device_to_the_server(self):
        print "TEST_CONNECT_DEVICE_TO_THE_SERVER"
        isConnected = self.device.connect("Connect with the real server")
        
        self.assertEqual(isConnected, True, "Device connection to the server failed")
        pass
    
    
    def test_connect_device_to_false_server_raise_exception(self):
        print "TEST_CONNECT_DEVICE_TO_THE_SERVER_RAISE_EXCEPTION"
        TestEnvironment.setUseIncorrectServerName(True)
        isConnected = self.device.connect("Connect with non existing server")
        
        self.assertEqual(isConnected, False, "Connection successful")
        pass
    
    '''
    def test_connect_device_and_reserve_slot(self):
        print "TEST_CONNECT_DEVICE_AND_RESERVE_SLOT"
        isConnected = self.device.connect("Connect with the real server")
        pass
    '''
    
    def test_disconnect_device_to_the_server(self):
        print "TEST_DISCONNECT_DEVICE_TO_THE_SERVER"
        isDisconnected = self.device.disconnect()  
         
        self.assertEqual(isDisconnected, True, "Device disconnection to the server failed")
        pass
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()