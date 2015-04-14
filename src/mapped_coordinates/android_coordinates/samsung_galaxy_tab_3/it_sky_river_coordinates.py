
import logging

import stormtest.ClientAPI as StormTest

from mapped_coordinates.android_coordinates.samsung_galaxy_tab_3.device_coordinates import DeviceCoordinates


log = logging.getLogger('userAction')

class itSkyRiverCoordinates(DeviceCoordinates):
    
    
    def __init__(self):
        super(DeviceCoordinates, self).__init__()
        
        self.commands = {
                    'openMenu':{'x':30, 'y':50, 'time':0},
                    'closeMenu':{'x':320,'y':50,'time':0},
                    'Home':{'x':635,'y':55,'time':0}
                    #'':{'x':, 'y':, 'time':}
                    } 
        
        pass
    
    
    def _tapWithMappedText(self, mappedText):
        log.debug("Tap on {0}".format(self.commands[mappedText]))
        
        command = self.commands[mappedText]
        return StormTest.PressButton('TAP:{0}:{1}:{2}'.format(command['x'], command['y'], command['time']))
  
        
    
    