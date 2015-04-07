
import stormtest.ClientAPI as StormTest

from mobile_framework.mobile_device import MobileDevice


class AndroidDevice(MobileDevice):
    
    def __init__(self):
        super(AndroidDevice, self).__init__()
    
    
    def start(self, appName=''):
        return StormTest.PressButton("START-ANDROID:" + appName)

    
    def stop(self):
        return StormTest.PressButton("STOP-ANDROID")

    
    def tap(self, coordinates={'x':None,'y':None}, duration=0):
        if isinstance(coordinates, dict):
            if type(coordinates['x']) is int and type(coordinates['y']) is int:
                return StormTest.PressButton("TAP:" + str(coordinates['x']) + ":" + str(coordinates['y']) + ":" + str(duration))
        
        return False
    
    
    
    
    