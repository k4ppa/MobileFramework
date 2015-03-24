
import stormtest.ClientAPI as StormTest


class MobileDevice(object):
    def __init__(self):
        self.server = ""
        self.description = ""
        pass

    
    def connect(self, server, description=''):
        StormTest.BeginLogRegion('Open Connection')
        
        self.__openConnection(server, description)
        return True
    
    
    def __openConnection(self, server, description):
        try:
            StormTest.ConnectToServer(server, description)
        except SystemExit:
            StormTest.EndLogRegion('Open Connection', StormTest.LogRegionStyle.Fail, comment='Failed to connect to server (%s)' % server)
            raise
        pass
        
    
    def disconnect(self):
        return StormTest.ReleaseServerConnection()
    
    
    
    
    


