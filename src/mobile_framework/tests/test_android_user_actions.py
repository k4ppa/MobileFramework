
import unittest

import stormtest.ClientAPI as StormTest

from mobile_framework.android_device import AndroidDevice


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        super(Test, self).setUpClass()
        self.device = AndroidDevice()
        self.device.connect("Connect with the real server")
        pass


    @classmethod
    def tearDownClass(cls):
        super(Test, cls).tearDownClass()
        cls.device.stop()
        cls.device.disconnect()
        pass


    def setUp(self):
        self.device.start("it.sky.river")
        StormTest.WaitSec(3)
        pass
    
    
    def tearDown(self):
        #self.device.stop()
        pass
    
    
    @unittest.skip("Test useless (no logic involved in code)")
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
   
    @unittest.skip("Test useless (no logic involved in code)")
    def test_stop_application(self):
        print "TEST STOP APPLICATION"
        self.device.start("it.sky.river")
        isStopped = self.device.stop()
       
        self.assertEqual(isStopped, True, "App not stopped")
        pass
    
    
    def test_tap_using_coordinates(self):
        print "TEST TAP USING COORDINATES"
        isPressed = self.device.tap(coordinates={'x':30,'y':50,'time':0})
        StormTest.WaitSec(3)
        self.device.tap(coordinates={'x':320,'y':50,'time':0})
        
        self.assertEqual(isPressed, True, "Tap failed")
        pass
    
    
    def test_tap_without_using_a_dictionary_should_fail(self):
        print "TEST TAP WITHOUT USING A DICTIONARY SHOULD FAIL"
        isPressed = self.device.tap(coordinates=[30,50,0])
        
        self.assertEqual(isPressed, False, "Tap successful")
        pass
    
    
    def test_tap_using_a_dictionary_with_string_should_fail(self):
        print "TEST TAP USING A DICTIONARY WITH STRING SHOULD FAIL"
        isPressed = self.device.tap(coordinates={'x':'30','y':'50','time':'0'})
        
        self.assertEqual(isPressed, False, "Tap successful")
        pass
    
    @unittest.expectedFailure  
    @unittest.skip("Test fail because tap with mapped text doesn't work")  
    def test_tap_using_mapped_text(self):
        print "TEST TAP USING TEXT"
        isPressed = self.device.tap(mappedText='Menu')
        
        self.assertEqual(isPressed, True, "Tap failed")
        pass
    
    
    def test_tap_element_using_text(self):
        print "TEST TAP ELEMENT USING TEXT"
        self.device.tap(coordinates={'x':30,'y':50,'time':0})
        StormTest.WaitSec(3)
        isCinemaPressed = self.device.tap(text='Cinema')
        StormTest.WaitSec(3)
        self.device.tap(coordinates={'x':635,'y':55,'time':0})
        StormTest.WaitSec(5)
        
        self.assertEqual(isCinemaPressed, True, "Tap on Cinema failed")
        pass
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()