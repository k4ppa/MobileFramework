
import logging

import stormtest.ClientAPI as StormTest
import stormtest.WarningCenter as WarningCenter

log = logging.getLogger('connection')


def _getTestRunConfiguration():
    StormTest.BeginLogRegion('Open Connection')
    params = WarningCenter.GetTestRun()
    if params == None:     
        return _getDeveloperModeParams()
        
    return params    


def _getDeveloperModeParams():
    from mobile_framework.tests.test_environment import TestEnvironment
    log.info("Developer mode - using a hard coded set of parameters")
    
    return TestEnvironment.params


def _setUpEnvironment():
    log.info("SetUp Environment")
    if not StormTest.IsUnderDaemon():
        return _setUpTestEnvironment()
    else:
        return _setUpRealEnvironment()
        

def _setUpTestEnvironment():
    from mobile_framework.tests.test_environment import TestEnvironment
    log.info("Test running under daemon, using test environment")
    server = TestEnvironment.getServerName()
    slot = TestEnvironment.getSlotNumber()
    
    return server, slot
    
    
def _setUpRealEnvironment(self):
    log.info("Test not running under daemon, using real environment")
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
        log.info("Opening connection to server: '%s'" % server)
        StormTest.ConnectToServer(server, description)
    except SystemExit:
        log.error("Failed to connect to server")
        StormTest.EndLogRegion('Open Connection', StormTest.LogRegionStyle.Fail, comment='Failed to connect to server (%s)' % server)
        return False
    
    log.info("Connection established with the server")
    return True


def _reserveSlot(slot, signalDb='', serialParams=[], videoFlag=True):
    log.info("Starting to reserve slot %d" % slot)
    isReserved = StormTest.ReserveSlot(slot, signalDb, serialParams, videoFlag)
    _logReserveSlotResult(slot, isReserved)
    
    return isReserved 
    
    
def _logReserveSlotResult(slot, isReserved):
    if isReserved is 0:    
        StormTest.EndLogRegion('Open Connection', StormTest.LogRegionStyle.Fail, comment='Failed to reserve slot %d' % slot)
        log.error('Failed to reserve slot %d' % slot)
    else:
        log.info("Slot %d reserved" % slot)
    
    
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



