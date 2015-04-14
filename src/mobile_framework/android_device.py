
import stormtest.ClientAPI as StormTest

from mobile_framework.mobile_device import MobileDevice
from mobile_framework.user_actions_functions import _tapWithText
from mobile_framework.user_actions_functions import _loadDeviceCommands
from mobile_framework.user_actions_functions import _loadAppCommands


class AndroidDevice(MobileDevice):
    
    def __init__(self, deviceName):
        super(AndroidDevice, self).__init__()
        
        self._deviceName = deviceName
        self._appName = ''
        self._commandsModuleName = "mapped_commands.android_commands.{0}".format(self._deviceName)
        
        self._commands = _loadDeviceCommands(self._commandsModuleName)
        pass
    
    
    def start(self, appName=''):
        self._appName = appName
        self._commands = _loadAppCommands(appName, self._commandsModuleName)
                                               
        self._userActionLog.info("Started application %s" % self._appName)
        return StormTest.PressButton("START-ANDROID:" + self._appName)

    
    def stop(self):
        self._userActionLog.info("Stopped application %s" % self._appName)
        return StormTest.PressButton("STOP-ANDROID")

    
    def tap(self, mappedText=None, text=None):
        if text:
            return _tapWithText(text)
        
        return super(AndroidDevice, self).tap(self._commands, mappedText)
    
    
    
    
    




