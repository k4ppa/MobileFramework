
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
    
    
    def test_connect_device_to_false_server_fail(self):
        print "TEST_CONNECT_DEVICE_TO_THE_SERVER_FAIL"
        TestEnvironment.setUseIncorrectServerName(True)
        isConnected = self.device.connect("Connect with non existing server")
        
        self.assertEqual(isConnected, False, "Connection successful")
        pass
    
    
    def test_connect_device_fail_and_reserve_slot_fail(self):
        print "TEST_CONNECT_DEVICE_FAIL_AND_RESERVE_SLOT_FAIL"
        TestEnvironment.setUseIncorrectServerName(True)
        isConnected = self.device.connect("Connect with the real server")
        
        self.assertEqual(isConnected, False, "Connection successful")
        pass
    
    
    def test_reserve_slot_fail_when_slot_number_is_wrong(self):
        print "TEST_SLOT_FAIL_WHEN_SLOT_NUMBER_IS_WRONG"
        TestEnvironment.setSlotNumber(10)
        isConnected = self.device.connect("Connect with the real server")
        
        self.assertEquals(isConnected, False, "Correct slot number")
        pass
    
    
    def test_disconnect_device_to_the_server(self):
        print "TEST_DISCONNECT_DEVICE_TO_THE_SERVER"
        isDisconnected = self.device.disconnect()  
         
        self.assertEqual(isDisconnected, True, "Device disconnection to the server failed")
        pass
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()