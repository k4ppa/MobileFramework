
import stormtest.ClientAPI as StormTest

from mobile_framework.mobile_device import MobileDevice
from mobile_framework.user_actions_functions import _tapWithText
from mobile_framework.user_actions_functions import _importDeviceCommands

import importlib


class AndroidDevice(MobileDevice):
    
    def __init__(self, deviceName):
        super(AndroidDevice, self).__init__()
        self._appName = ''
        self._appCommands = None
        
        self.deviceCommandsModule = _importDeviceCommands(deviceName)
        pass
    
    
    def start(self, appName=''):
        self._appName = appName
        
        moduleName = appName.replace(".", "_")
        try:
            self.deviceCommandsModule += ".{0}_commands".format(moduleName)
            self.appCommandsModule = importlib.import_module(self.deviceCommandsModule)
        except ImportError:
            print "Fail to import app mapped commands: {0}".format(self.deviceCommandsModule)
        
        self._appCommands = self.appCommandsModule.appCommands()
        self._userActionLog.info("Started application %s" % self._appName)
        return StormTest.PressButton("START-ANDROID:" + self._appName)

    
    def stop(self):
        self._userActionLog.info("Stopped application %s" % self._appName)
        return StormTest.PressButton("STOP-ANDROID")

    
    def tap(self, mappedText=None, text=None):
        if text:
            return _tapWithText(text)
        
        return super(AndroidDevice, self).tap(self._appCommands, mappedText)
    
    
    
    
    




