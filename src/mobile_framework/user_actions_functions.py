
def _checkCoordinates(coordinates):
    if isinstance(coordinates, dict):
        if type(coordinates['x']) is int and type(coordinates['y']) is int:
            return True
    return False