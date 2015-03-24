
class TestEnvironment(object):
    
    useIncorrectServerName = False
    serverName = "s15016hv01"
    slotNumber = 1
    
    
    def __init__(self):
        pass

    
    @staticmethod
    def setUseIncorrectServerName(isCorrect):
        TestEnvironment.useIncorrectServerName = isCorrect
        pass
    

    @staticmethod
    def getServerName():
        if TestEnvironment.useIncorrectServerName is True:
            TestEnvironment.useIncorrectServerName = False
            return "Incorrect server"
        return TestEnvironment.serverName
    
    
    @staticmethod
    def getSlotNumber():
        return TestEnvironment.slotNumber






