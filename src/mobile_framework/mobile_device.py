
import logging.config

import stormtest.ClientAPI as StormTest

from mobile_framework.connect_functions import _getTestRunConfiguration
from mobile_framework.connect_functions import _setUpEnvironment
from mobile_framework.connect_functions import _establishConnection

from mobile_framework.user_actions_functions import _checkCoordinates


class MobileDevice(object):
    def __init__(self):
        self._server = ""
        self._description = ""
        self._slot = 0
        
        logging.config.fileConfig('C:\workspace\MobileFramework\src\mobile_framework/log.conf')
        self._log = logging.getLogger('connection')
        self._userActionLog = logging.getLogger('userAction')
        
        pass

    
    def connect(self, description=''):
        self._log.info(description)
        self._log.info("Started connection with the server")    
        serviceInfo = _getTestRunConfiguration()['service']
        
        self._server, self._slot = _setUpEnvironment()
        self._log.debug("server:slot = {}:{}".format(self._server, self._slot))
        return _establishConnection(self._server, self._slot, description)
         
    
    
    def disconnect(self):
        self._log.info("Closing connection with the server")
        logging.shutdown()
        return StormTest.ReleaseServerConnection()
    
    
    def tap(self, coordinates={'x':None,'y':None}, duration=0):
        if _checkCoordinates(coordinates):
            return StormTest.PressButton("TAP:" + str(coordinates['x']) + ":" + str(coordinates['y']) + ":" + str(duration))
        
        return False
    

    


