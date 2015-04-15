
import unittest

import stormtest.ClientAPI as StormTest

from mobile_framework.android_device import AndroidDevice
from stormtest.ClientAPI import PressButton


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        super(Test, self).setUpClass()
        self.device = AndroidDevice("samsung_galaxy_tab_3")
        self.device.connect("Connect with the real server")
        self.device.start("it.sky.river")
        StormTest.WaitSec(4)
        pass


    @classmethod
    def tearDownClass(cls):
        super(Test, cls).tearDownClass()
        cls.device.stop()
        cls.device.disconnect()
        pass
    
    
    def test_tap_using_mapped_text(self):
        print "TEST TAP USING COORDINATES"
        isPressed = self.device.tap(mappedText='openMenu')
        StormTest.WaitSec(4)
        self.device.tap(mappedText='closeMenu')
        
        self.assertEqual(isPressed, True, "Tap failed")
        pass
    
    
    def test_tap_element_using_text(self):
        print "TEST TAP ELEMENT USING TEXT"
        self.device.tap(mappedText='openMenu')
        StormTest.WaitSec(4)
        isCinemaPressed = self.device.tap(text='Cinema')
        StormTest.WaitSec(4)
        self.device.tap(mappedText='Home')
        StormTest.WaitSec(6)
        
        self.assertEqual(isCinemaPressed, True, "Tap on Cinema failed")
        pass
    
    
    def test_import_non_existent_device_commands_module_should_throw_an_exception(self):
        print "TEST IMPORT NON EXISTENT DEVICE COMMANDS MODULE SHOULD THROW AN EXCEPTION"
        
        self.assertRaises(ImportError, AndroidDevice, "samsung_galaxy_fake")
        pass
    
    
    def test_import_non_existent_app_commands_module_should_throw_an_exception(self):
        print "TEST IMPORT NON EXISTENT APP COMMANDS MODULE SHOULD THROW AN EXCEPTION"
        newDevice = AndroidDevice("samsung_galaxy_tab_3")
        
        self.assertRaises(ImportError, newDevice.start, "fake_app")
        pass
    
    
    @unittest.expectedFailure
    def test_tap_element_using_desc(self):
        print "TEST TAP ELEMENT USING DESC"
        self.device.stop()
        StormTest.WaitSec(2)
        isPressed = PressButton("TAPELEMENT:text:Sky Online")
        
        self.device.start("it.sky.river")
        self.assertEqual(isPressed, True, "Tap failed")
        pass
    
    
    @unittest.expectedFailure
    def test_tap_element_using_index(self):
        print "TEST TAP ELEMENT USING INDEX"
        self.device.stop()
        StormTest.WaitSec(4)
        isPressed = self.device.tap(index=3)
        StormTest.WaitSec(4)
        
        self.assertEqual(isPressed, True, "Tap failed")
        pass
    
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()