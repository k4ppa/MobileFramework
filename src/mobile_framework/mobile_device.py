
import stormtest.ClientAPI as StormTest

class MobileDevice(object):
    def __init__(self):
        self.server = ""
        self.description = ""
        pass

    
    def openConnection(self, server, description=''):
        StormTest.BeginLogRegion('Open Connection')
        
        try:
            StormTest.ConnectToServer(server, description)
        except SystemExit:
            StormTest.EndLogRegion('Open Connection', StormTest.LogRegionStyle.Fail, comment='Failed to connect to server (%s)' % server)
            raise
        
        return True

    
    def closeConnection(self):
        return StormTest.ReleaseServerConnection()
    
    
    
    
    


