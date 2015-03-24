
import stormtest.ClientAPI as StormTest
import stormtest.WarningCenter as WarningCenter 


class MobileDevice(object):
    def __init__(self):
        self.__server = ""
        self.__description = ""
        self.__slot = 0
        pass

    
    def connect(self, description=''):
        StormTest.BeginLogRegion('Open Connection')
        
        params = self.__getTestRunConfiguration()
        serviceInfo = params['service']
        
        self.__setUpEnvironment()
        isConnected = self.__openConnection(self.__server, description)
        isReserved = self.__reserveSlot(self.__slot, signalDb='', serialParams=[], videoFlag=True)
        isOCRLicenseOver = self.__OCRCheckRemainingChars()
         
        return self.__connectionEstablished(isConnected, isReserved, isOCRLicenseOver)
        
        
    def __getTestRunConfiguration(self):
        params = WarningCenter.GetTestRun()
        if params == None:      #debug mode - use a hard coded set of parameters
            from mobile_framework.tests.test_environment import TestEnvironment
            params = TestEnvironment.params
            
        return params    

    def __setUpEnvironment(self):
        if not StormTest.IsUnderDaemon():
            self.__setUpTestEnvironment()
        else:
            self.__setUpRealEnvironment()
            
    
    def __setUpTestEnvironment(self):
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
            return False
        return True
        pass
    
    
    def __reserveSlot(self, slot, signalDb='', serialParams=[], videoFlag=True):
        isReserved = StormTest.ReserveSlot(slot, signalDb, serialParams, videoFlag)
        if isReserved is False:    
            StormTest.EndLogRegion('Open Connection', StormTest.LogRegionStyle.Fail, comment='Failed to reserve slot (%d)' % slot)
            
        return isReserved 
        
    
    def __OCRCheckRemainingChars(self):
        remainingChars = StormTest.OCRGetRemainingChars()
        if remainingChars is 0:    
            StormTest.EndLogRegion('Open Connection', StormTest.LogRegionStyle.Fail, comment='OCR licenses has ran out. Not possible to run tests.')
    
        return remainingChars
    
    
    def __connectionEstablished(self, isConnected, isReserved, isOCRLicenseOver):
        if isConnected and isReserved and isOCRLicenseOver:
            return 1
        return isReserved
    
    
    def disconnect(self):
        return StormTest.ReleaseServerConnection()
    
    
    
    
    


