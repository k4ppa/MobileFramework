
import logging

log = logging.getLogger('userAction')

def _checkCoordinates(coordinates):
    if isinstance(coordinates, dict):
        if __coordinatesAreInt(coordinates):
            return True
    
    log.warning("Parameter coordinates passed in function are not a dictionary with int values")
    return False


def __coordinatesAreInt(coordinates):
    return type(coordinates['x']) is int and type(coordinates['y']) is int