
import stormtest.ClientAPI as StormTest

from mobile_framework.mobile_device import MobileDevice


class AndroidDevice(MobileDevice):
    
    def __init__(self):
        super(AndroidDevice, self).__init__()
    
    
    def start(self, appName=''):
        return StormTest.PressButton("START-ANDROID:" + appName)

    
    def stop(self):
        return StormTest.PressButton("STOP-ANDROID")

    
    def tap(self, x, y, duration):
        return StormTest.PressButton("TAP:" + str(x) + ":" + str(y) + ":" + "duration")
        pass
    
    
    
    
    