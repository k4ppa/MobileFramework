
import stormtest.ClientAPI as StormTest

from mobile_framework.mobile_device import MobileDevice
from mobile_framework.user_actions_functions import _tapWithText

import importlib
from mapped_coordinates.android_coordinates.samsung_galaxy_tab_3.it_sky_river_coordinates import itSkyRiverCoordinates


class AndroidDevice(MobileDevice):
    
    def __init__(self, deviceName):
        super(AndroidDevice, self).__init__()
        self._appName = ''
        '''
        #rawData = StormTest.GetFacilityData('S15016HV01')
        #stbField = StormTest.GetStbField(rawData, 'S15016HV01', 1, 'all')
        #print stbField
        #model = stbField['Model'].lower().replace(' ', '_')
        #app = stbField['IRDefinition']
        self.module = "mapped_coordinates.android_coordinates.{0}".format(deviceName)
        try:
            #command_module = __import__(module, globals(), locals(), ['object'], -1)
            command_module = importlib.import_module(self.module) 
        except ImportError:
            print "Fail to import mapped coordinates: {0}".format(self.module)
            # Display error message

        print command_module
        '''
        pass
    
    
    def start(self, appName=''):
        self._appName = appName
        '''
        moduleName = appName.replace(".", "_")
        try:
            self.module += ".{0}_coordinates".format(moduleName)
            command_module = importlib.import_module(self.module)
            self.appCommand = SkyOnlineCoordinates()
            print self.appCommand.commands
            print self.module 
            print command_module
        except ImportError:
            print "Fail to import mapped coordinates: {0}".format(self.module)
        '''
        self._userActionLog.info("Started application %s" % self._appName)
        return StormTest.PressButton("START-ANDROID:" + self._appName)

    
    def stop(self):
        self._userActionLog.info("Stopped application %s" % self._appName)
        return StormTest.PressButton("STOP-ANDROID")

    
    def tap(self, mappedText=None, text=None):
        if text:
            return _tapWithText(text)
        
        skyOnlineCoord = itSkyRiverCoordinates()
        return super(AndroidDevice, self).tap(skyOnlineCoord, mappedText)
    
    
    
    
    




