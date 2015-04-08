
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
        self._connectionLog = logging.getLogger('connection')
        self._userActionLog = logging.getLogger('userAction')
        pass

    
    def connect(self, description=''):
        self._connectionLog.info(description)
        self._connectionLog.info("Started connection with the server")    
        serviceInfo = _getTestRunConfiguration()['service']
        
        self._server, self._slot = _setUpEnvironment()
        self._connectionLog.debug("server:slot = {}:{}".format(self._server, self._slot))
        return _establishConnection(self._server, self._slot, description)
         
    
    
    def disconnect(self):
        self._connectionLog.info("Closing connection with the server")
        logging.shutdown()
        return StormTest.ReleaseServerConnection()
    
    
    def tap(self, coordinates={'x':None,'y':None, 'time':0}, mappedText=''):
        self._userActionLog.debug("Tap on ", coordinates)
        if _checkCoordinates(coordinates):
            return StormTest.PressButton("TAP:" + str(coordinates['x']) + ":" + str(coordinates['y']) + ":" + str(coordinates['time']))
        
        self._userActionLog.warning("Parameter coordinates passed in function are not a dictionary with int values")
        return False
    

    


