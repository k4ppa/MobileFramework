
def _checkCoordinates(coordinates):
    if isinstance(coordinates, dict):
        if __coordinatesAreInt(coordinates):
            return True
    
    return False


def __coordinatesAreInt(coordinates):
    return type(coordinates['x']) is int and type(coordinates['y']) is int