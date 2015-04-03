
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
        self._log.info("Started connection with the server")    
        serviceInfo = _getTestRunConfiguration()['service']
        
        self._server, self._slot = _setUpEnvironment()
        self._log.debug("server:slot = {}:{}".format(self._server, self._slot))
        return _establishConnection(self._server, self._slot, description)
         
    
    
    def disconnect(self):
        self._log.info("Closing connection with the server")
        logging.shutdown()
        return StormTest.ReleaseServerConnection()
    
    
    

    


