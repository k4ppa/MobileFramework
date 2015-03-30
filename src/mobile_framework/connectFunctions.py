
import logging

import stormtest.ClientAPI as StormTest
import stormtest.WarningCenter as WarningCenter

log = logging.getLogger('connection')


def _getTestRunConfiguration():
    params = WarningCenter.GetTestRun()
    if params == None:     
        from mobile_framework.tests.test_environment import TestEnvironment
        params = TestEnvironment.params
        log.info("Developer mode - using a hard coded set of parameters")
        
    return params    


def _setUpEnvironment():
    if not StormTest.IsUnderDaemon():
        log.info("Test running under daemon")
        return _setUpTestEnvironment()
    else:
        log.info("Test not running under daemon")
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
        log.info("Starting connection to server '%s'" % server)
        StormTest.ConnectToServer(server, description)
    except SystemExit:
        StormTest.EndLogRegion('Open Connection', StormTest.LogRegionStyle.Fail, comment='Failed to connect to server (%s)' % server)
        log.error("Failed to connect to server")
        return False
    
    log.info("Connection established with server")
    return True


def _reserveSlot(slot, signalDb='', serialParams=[], videoFlag=True):
    log.info("Starting reserver slot for slot %d" % slot)
    isReserved = StormTest.ReserveSlot(slot, signalDb, serialParams, videoFlag)
    if isReserved is 0:    
        StormTest.EndLogRegion('Open Connection', StormTest.LogRegionStyle.Fail, comment='Failed to reserve slot %d' % slot)
        log.error('Failed to reserve slot %d' % slot)
        return False
    
    log.info("Slot %d reserved" % slot)
    return True 
    
    
def _isConnectionOk(isServerConnected, isSlotReserved):
    isConnectionOk = False
    if isServerConnected and isSlotReserved:
        isConnectionOk = _OCRCheckRemainingChars()
    return isConnectionOk    
    

def _OCRCheckRemainingChars():
    remainingChars = StormTest.OCRGetRemainingChars()
    log.info("Remaining OCR chars in license: %d" % remainingChars)
    
    if remainingChars is 0:    
        StormTest.EndLogRegion('Open Connection', StormTest.LogRegionStyle.Fail, comment='OCR licenses has ran out. Not possible to run tests')
        log.error("OCR licenses has ran out. Not possible to run tests")
        return False
    
    log.info("Connection established")
    return True



