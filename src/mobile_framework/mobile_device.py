
import stormtest.ClientAPI as StormTest
from mobile_framework.connectFunctions import _getTestRunConfiguration
from mobile_framework.connectFunctions import _setUpEnvironment
from mobile_framework.connectFunctions import _openConnection
from mobile_framework.connectFunctions import _reserveSlot
from mobile_framework.connectFunctions import _OCRCheckRemainingChars
from mobile_framework.connectFunctions import _connectionEstablished


class MobileDevice(object):
    def __init__(self):
        self._server = ""
        self._description = ""
        self._slot = 0
        pass

    
    def connect(self, description=''):
        StormTest.BeginLogRegion('Open Connection')
        
        params = _getTestRunConfiguration()
        serviceInfo = params['service']
        
        self._server, self._slot = _setUpEnvironment()
        isServerConnected = _openConnection(self._server, description)
        isSlotReserved = _reserveSlot(self._slot, signalDb='', serialParams=[], videoFlag=True)
        
        isConnectionOk = False
        if isServerConnected and isSlotReserved:
            isConnectionOk = _OCRCheckRemainingChars()
            
        return _connectionEstablished(isConnectionOk) 
         
    
    
    def disconnect(self):
        return StormTest.ReleaseServerConnection()
    
    
    

    


