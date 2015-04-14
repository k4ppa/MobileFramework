
import unittest

import stormtest.ClientAPI as StormTest

from mobile_framework.android_device import AndroidDevice


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        super(Test, self).setUpClass()
        self.device = AndroidDevice("samsung_galaxy_tab_3")
        self.device.connect("Connect with the real server")
        self.device.start("it.sky.river")
        StormTest.WaitSec(3)
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
        StormTest.WaitSec(3)
        self.device.tap(mappedText='closeMenu')
        
        self.assertEqual(isPressed, True, "Tap failed")
        pass
    
    
    def test_tap_element_using_text(self):
        print "TEST TAP ELEMENT USING TEXT"
        self.device.tap(mappedText='openMenu')
        StormTest.WaitSec(3)
        isCinemaPressed = self.device.tap(text='Cinema')
        StormTest.WaitSec(3)
        self.device.tap(mappedText='Home')
        StormTest.WaitSec(5)
        
        self.assertEqual(isCinemaPressed, True, "Tap on Cinema failed")
        pass
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()