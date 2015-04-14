
import logging

import stormtest.ClientAPI as StormTest
import importlib


log = logging.getLogger('userAction')

def _loadDeviceCommands(moduleName):
    deviceModule = __importDeviceModule(moduleName)
    return deviceModule.DeviceCommands()


def __importDeviceModule(deviceCommandsModule):
    try:
        return importlib.import_module(deviceCommandsModule + ".device_commands")
    except ImportError:
        print "Fail to import device mapped commands: {0}".format(deviceCommandsModule)
        pass
    

def _loadAppCommands(appName, deviceModuleName):
    appModuleName = __concatModulesName(appName, deviceModuleName)
    appCommandsModule = __importAppModule(appModuleName)
    
    return appCommandsModule.AppCommands()


def __concatModulesName(appName, deviceCommandsModule):
    moduleName = appName.replace(".", "_")
    return deviceCommandsModule + ".{0}_commands".format(moduleName)
    

def __importAppModule(deviceCommandsModule):
    try:
        return importlib.import_module(deviceCommandsModule)
    except ImportError:
        print "Fail to import app mapped commands: {0}".format(deviceCommandsModule)
    pass


def _tapWithText(text):
    log.debug("Tap on {0}".format(text))
    return StormTest.PressButton("TAPELEMENT:text:{0}".format(text))
    
    
    
    
    