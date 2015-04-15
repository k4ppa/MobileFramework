
import stormtest.ClientAPI as StormTest

from mobile_framework.mobile_device import MobileDevice
from mobile_framework.android_user_actions_functions import _tapWithText, _tapWithIndex, _tapWithDesc
from mobile_framework.common_user_actions_functions import _loadDeviceCommands, _loadAppCommands


class AndroidDevice(MobileDevice):
    
    def __init__(self, deviceName):
        super(AndroidDevice, self).__init__()
        
        self._deviceName = deviceName
        self._appName = ''
        self._commandsModuleName = "mapped_commands.android_commands.{0}".format(self._deviceName)
        
        self._appCommands = _loadDeviceCommands(self._commandsModuleName)
        pass
    
    
    def start(self, appName=''):
        self._appName = appName
        self._appCommands = _loadAppCommands(appName, self._commandsModuleName)
                             
        self.connect('')
                          
        self._userActionLog.info("Started application %s" % self._appName)
        return StormTest.PressButton("START-ANDROID:" + self._appName)

    
    def stop(self):
        self._userActionLog.info("Stopped application %s" % self._appName)
        if not StormTest.PressButton("STOP-ANDROID"):
            self._userActionLog.error("Stop application failed. Disconnection will continue")
        return self.disconnect()
        

    
    def tap(self, mappedText=None, text=None, desc=None, index=None):
        if text:
            return _tapWithText(text)
        
        if desc:
            return _tapWithDesc(desc)
        
        if index:
            return _tapWithIndex(index)
        
        return super(AndroidDevice, self).tap(self._appCommands, mappedText)
    
    
    
    
    




