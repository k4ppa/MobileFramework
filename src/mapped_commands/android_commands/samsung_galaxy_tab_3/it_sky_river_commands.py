
import logging

import stormtest.ClientAPI as StormTest

from mapped_commands.android_commands.samsung_galaxy_tab_3.device_commands import DeviceCommands


log = logging.getLogger('userAction')

class AppCommands(DeviceCommands):
    
    
    def __init__(self):
        super(DeviceCommands, self).__init__()
        
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
  
        
    
    