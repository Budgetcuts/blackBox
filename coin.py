class Coin:
    def __init__(self, iComp, avgComp, sysNum):
        self.iComp = iComp
        self.avgComp = avgComp
        self.sysNum = sysNum


    def addCoins(self):
        pVal = self.iComp/(self.avgComp * self.sysNum)
        return pVal

    def coinVal(self):
        oVal = self.avgComp * self.sysNum
        return oVal

    def updateAll(self,iComp, avgComp, sysNum):
        self.iComp = iComp
        self.avgComp = avgComp
        self.sysNum = sysNum

    def updateMyComp(self, iComp):
        self.iComp = iComp

    def updateSysComp(self, avgComp):
        self.avgComp = avgComp

    def updateUsers(self, sysNum):
        self.sysNum = sysNum

    def string(self):
        print("Personal Computational Power:", self.iComp)
        print("Average Computational Power of the network:", self.avgComp)
        print("Number of active systems on the network:", self.sysNum)