
import logging.config

import stormtest.ClientAPI as StormTest

from mobile_framework.connectFunctions import _getTestRunConfiguration
from mobile_framework.connectFunctions import _setUpEnvironment
from mobile_framework.connectFunctions import _establishConnection


class MobileDevice(object):
    def __init__(self):
        self._server = ""
        self._description = ""
        self._slot = 0
        
        logging.config.fileConfig('C:\workspace\MobileFramework\src\mobile_framework/log.conf')
        self._log = logging.getLogger('connection')
        
        pass

    
    def connect(self, description=''):
        StormTest.BeginLogRegion('Open Connection')
        
        params = _getTestRunConfiguration()
        serviceInfo = params['service']
        
        self._server, self._slot = _setUpEnvironment()
        return _establishConnection(self._server, self._slot, description)
         
    
    
    def disconnect(self):
        logging.shutdown()
        self._log.info("Closing connection with the server")
        return StormTest.ReleaseServerConnection()
    
    
    

    


