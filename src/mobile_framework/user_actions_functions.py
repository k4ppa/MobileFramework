
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
        log.error("Fail to import device mapped commands: {0}".format(deviceCommandsModule))
        raise 
    

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
        log.error("Fail to import app mapped commands: {0}".format(deviceCommandsModule))
        raise


def _tapWithText(text):
    log.debug("Tap on text {0}".format(text))
    return StormTest.PressButton("TAPELEMENT:text:{0}".format(text))
    
    
def _tapWithDesc(desc):
    log.debug("Tap on desc{0}".format(desc))
    return StormTest.PressButton("TAPELEMENT:desc:{0}".format(desc))
    
    
def _tapWithIndex(index):
    log.debug("Tap on index {0}".format(index))
    return StormTest.PressButton("TAPELEMENT:index:{0}".format(index))


def _tapWithMappedText(commands, mappedText):
        log.debug("Tap on {0}".format(commands[mappedText]))
        
        command = commands[mappedText]
        return StormTest.PressButton('TAP:{0}:{1}:{2}'.format(command['x'], command['y'], command['time']))





    