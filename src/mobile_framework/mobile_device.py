
import stormtest.ClientAPI as StormTest

class MobileDevice(object):
    def __init__(self):
        self.server = ""
        self.description = ""
        pass

    
    def openConnection(self, server, description=''):
        return StormTest.ConnectToServer(server, description)

    
    def closeConnection(self):
        return StormTest.ReleaseServerConnection()
    
    
    
    
    


