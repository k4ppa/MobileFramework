
import logging

import stormtest.ClientAPI as StormTest
import importlib


log = logging.getLogger('userAction')

'''
def __coordinatesAreInt(coordinates):
    return type(coordinates['x']) is int and type(coordinates['y']) is int


def _tapWithCoordinates(coordinates):
    log.debug("Tap on {0}".format(coordinates))
    #if __checkCoordinates(coordinates):
        #return StormTest.PressButton("TAP:" + str(coordinates['x']) + ":" + str(coordinates['y']) + ":" + str(coordinates['time']))

    log.warning("Parameter coordinates passed in function are not a dictionary with int values")
    return False


def __checkCoordinates(coordinates):
    if isinstance(coordinates, dict):
        if __coordinatesAreInt(coordinates):
            return True
    return False


def _tapWithMappedText(mappedText):
    log.debug("Tap on {0}".format(mappedText))
    return StormTest.PressButton(mappedText)
'''

def _importDeviceCommands(deviceName):
    deviceCommandsModule = "mapped_commands.android_commands.{0}".format(deviceName)
    try:
        importlib.import_module(deviceCommandsModule + ".device_commands") 
    except ImportError:
        print "Fail to import device mapped commands: {0}".format(deviceCommandsModule)
    return deviceCommandsModule


def _tapWithText(text):
    log.debug("Tap on {0}".format(text))
    return StormTest.PressButton("TAPELEMENT:text:{0}".format(text))
    
    
    
    
    