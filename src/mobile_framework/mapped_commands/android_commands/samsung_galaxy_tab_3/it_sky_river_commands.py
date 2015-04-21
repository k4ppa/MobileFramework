
from mobile_framework.mapped_commands.android_commands.samsung_galaxy_tab_3.device_commands import DeviceCommands


class AppCommands(DeviceCommands):
    
    
    def __init__(self):
        DeviceCommands.__init__(self)
        
        self._appCommands = {
                    'openMenu':{'x':30, 'y':50, 'time':0},
                    'closeMenu':{'x':320,'y':50,'time':0},
                    'Home':{'x':635,'y':55,'time':0}
                    #'':{'x':, 'y':, 'time':}
                    } 
        pass
    
    
    def getCommands(self):
        allCommands = self._appCommands.copy()
        allCommands.update(self._commands)
        return allCommands
    
    