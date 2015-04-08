
import stormtest.ClientAPI as StormTest

from mobile_framework.mobile_device import MobileDevice


class AndroidDevice(MobileDevice):
    
    def __init__(self):
        super(AndroidDevice, self).__init__()
        self._appName = ''
        pass
    
    
    def start(self, appName=''):
        self._appName = appName
        
        self._userActionLog.info("Started application %s" % self._appName)
        return StormTest.PressButton("START-ANDROID:" + self._appName)

    
    def stop(self):
        self._userActionLog.info("Stopped application %s" % self._appName)
        return StormTest.PressButton("STOP-ANDROID")

    
    
    
    
    
    
    