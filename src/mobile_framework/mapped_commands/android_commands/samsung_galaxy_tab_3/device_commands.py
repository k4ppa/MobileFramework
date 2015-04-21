
from mobile_framework.mapped_commands.android_commands.android_commands import AndroidCommands


class DeviceCommands(AndroidCommands):

    def __init__(self):
        super(AndroidCommands, self).__init__()
        
        self._commands = {'OpenAssistantMenu':{'x':1230, 'y':435, 'time':0},
                         'CloseAssistantMenu':{'x':1270, 'y':450, 'time':0},
                         'Menu':{'x':1000, 'y':390, 'time':0},
                         'Home':{'x':990, 'y':520, 'time':0},
                         'Back':{'x':1125, 'y':515, 'time':0},
                         'Up':{'x':1225, 'y':360, 'time':0},
                         'Down':{'x':1225, 'y':535, 'time':0},
                         'Settings':{'x':1125, 'y':515, 'time':0},
                         }
        pass
    
    
    def getCommands(self):
        return self._commands  