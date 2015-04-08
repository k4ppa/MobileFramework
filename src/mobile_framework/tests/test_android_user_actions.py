
import unittest

import stormtest.ClientAPI as StormTest

from mobile_framework.android_device import AndroidDevice


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super(Test, cls).setUpClass()
        cls.device = AndroidDevice()
        cls.device.connect("Connect with the real server")
        pass


    @classmethod
    def tearDownClass(cls):
        super(Test, cls).tearDownClass()
        cls.device.stop()
        cls.device.disconnect()
        pass

    
    def test_start_application_by_name_should_be_successfull(self):
        print "TEST START APPLICATION BY NAME SHOULD BE SUCCESSFULL"
        isStarted = self.device.start("it.sky.river")
        
        self.assertEqual(isStarted, True, "App not started")
        pass
    
       
    ''' 
    def test_start_application_with_mapped_name_should_be_successfull(self):
        print "TEST_START_APPLICATION_WITH_MAPPED_NAME_SHOULD_BE_SUCCESSFULL"
        isStarted = self.device.start()
        
        self.assertEqual(isStarted, True, "App not started")
        pass
    '''
   
    
    def test_stop_application(self):
        print "TEST STOP APPLICATION"
        self.device.start("it.sky.river")
        isStopped = self.device.stop()
       
        self.assertEqual(isStopped, True, "App not stopped")
        pass
    
    
    def test_tap_using_coordinates(self):
        print "TEST TAP USING COORDINATES"
        self.device.start("it.sky.river")
        isPressed = self.device.tap({'x':30,'y':50,'time':0})
        
        self.assertEqual(isPressed, True, "Tap failed")
        pass
    
    
    def test_tap_without_using_a_dictionary_should_fail(self):
        print "TEST TAP WITHOUT USING A DICTIONARY SHOULD FAIL"
        self.device.start("it.sky.river")
        isPressed = self.device.tap([30,50,0])
        
        self.assertEqual(isPressed, False, "Tap successful")
        pass
    
    
    def test_tap_using_a_dictionary_with_string_should_fail(self):
        print "TEST TAP USING A DICTIONARY WITH STRING SHOULD FAIL"
        self.device.start("it.sky.river")
        isPressed = self.device.tap({'x':'30','y':'50','time':'0'})
        
        self.assertEqual(isPressed, False, "Tap successful")
        pass
    
    '''    
    def test_tap_using_mapped_text(self):
        print "TEST TAP USING TEXT"
        self.device.start("it.sky.river")
        StormTest.WaitSec(15);
        isPressed = self.device.tap(mappedText='Menu')
        
        self.assertEqual(isPressed, True, "Tap failed")
        pass
    '''  
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()