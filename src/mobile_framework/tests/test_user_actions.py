
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
        print "TEST_START_APPLICATION_BY_NAME_SHOULD_BE_SUCCESSFULL"
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
   
   
   

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()