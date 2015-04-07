
import unittest

from mobile_framework.android_device import AndroidDevice


class Test(unittest.TestCase):


    def setUp(self):
        self.device = AndroidDevice()
        self.device.connect("Connect with the real server")
        
        pass


    def tearDown(self):
        self.device.disconnect()
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
    
    
    def test_tap_with_coordinates(self):
        print "TEST TAP WITH COORDINATES"
        self.device.start("it.sky.river")
        isPressed = self.device.tap(30,50,0)
        
        self.assertEqual(isPressed, True, "Tap not happened")
        pass
   

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()