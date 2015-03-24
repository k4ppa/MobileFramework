
import stormtest.ClientAPI as StormTest


class MobileDevice(object):
    def __init__(self):
        self.__server = ""
        self.__description = ""
        self.__slot = 0
        pass

    


    def connect(self, description=''):
        StormTest.BeginLogRegion('Open Connection')
        
        self.__setUpEnvironment()
        self.__openConnection(self.__server, description)
        return True

    
    def __setUpEnvironment(self):
        if not StormTest.IsUnderDaemon():
            self.__setUpFakeEnvironment()
        else:
            self.__setUpRealEnvironment()
            
    
    def __setUpFakeEnvironment(self):
        from mobile_framework.tests.test_environment import TestEnvironment
        self.__server = TestEnvironment.getServerName()
        self.__slot = TestEnvironment.getSlotNumber()
        
        
    def __setUpRealEnvironment(self):
        slotAllocated = StormTest.GetPhysicalAllocations()
        self.__server = slotAllocated[0].split(':')[0]
        self.__slot = slotAllocated[1][0]
    
    
    def __openConnection(self, server, description):
        try:
            StormTest.ConnectToServer(server, description)
        except SystemExit:
            StormTest.EndLogRegion('Open Connection', StormTest.LogRegionStyle.Fail, comment='Failed to connect to server (%s)' % server)
            raise
        pass
        
    
    def disconnect(self):
        return StormTest.ReleaseServerConnection()
    
    
    
    
    


