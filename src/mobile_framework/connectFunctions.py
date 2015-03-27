
import stormtest.ClientAPI as StormTest
import stormtest.WarningCenter as WarningCenter


def _getTestRunConfiguration():
    params = WarningCenter.GetTestRun()
    if params == None:      #debug mode - use a hard coded set of parameters
        from mobile_framework.tests.test_environment import TestEnvironment
        params = TestEnvironment.params
        
    return params    


def _setUpEnvironment():
    if not StormTest.IsUnderDaemon():
        return _setUpTestEnvironment()
    else:
        return _setUpRealEnvironment()
        

def _setUpTestEnvironment():
    from mobile_framework.tests.test_environment import TestEnvironment
    server = TestEnvironment.getServerName()
    slot = TestEnvironment.getSlotNumber()
    return server, slot
    
    
def _setUpRealEnvironment(self):
    slotAllocated = StormTest.GetPhysicalAllocations()
    server = slotAllocated[0].split(':')[0]
    slot = slotAllocated[1][0]
    return server, slot


def _establishConnection(server, slot, description):
    isServerConnected = _openConnection(server, description)
    isSlotReserved = _reserveSlot(slot, signalDb='', serialParams=[], videoFlag=True)
    
    return _isConnectionOk(isServerConnected, isSlotReserved)
    

def _openConnection(server, description):
    try:
        StormTest.ConnectToServer(server, description)
    except SystemExit:
        StormTest.EndLogRegion('Open Connection', StormTest.LogRegionStyle.Fail, comment='Failed to connect to server (%s)' % server)
        return False
    return True
    pass


def _reserveSlot(slot, signalDb='', serialParams=[], videoFlag=True):
    isReserved = StormTest.ReserveSlot(slot, signalDb, serialParams, videoFlag)
    if isReserved is 0:    
        StormTest.EndLogRegion('Open Connection', StormTest.LogRegionStyle.Fail, comment='Failed to reserve slot (%d)' % slot)
        
    return isReserved 
    
    
def _isConnectionOk(isServerConnected, isSlotReserved):
    isConnectionOk = False
    if isServerConnected and isSlotReserved:
        isConnectionOk = _OCRCheckRemainingChars()
    return isConnectionOk    
    

def _OCRCheckRemainingChars():
    remainingChars = StormTest.OCRGetRemainingChars()
    print "Remaining OCR chars: " + str(remainingChars)
    
    if remainingChars is 0:    
        StormTest.EndLogRegion('Open Connection', StormTest.LogRegionStyle.Fail, comment='OCR licenses has ran out. Not possible to run tests.')
        return False
    return True



