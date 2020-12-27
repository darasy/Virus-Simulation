"""
@author: Darasy Reth
@email: reth.d@northeastern.edu
"""


from main.ConfigUtil import ConfigUtil

import random

class Virus:
    """
    A class representation of the virus analysis
    
    """

    def __init__(self, name = "virus", section = "Covid19.Factors"):
        """
        Constructor
        """
        self.config = ConfigUtil()
        self.name = name
        self.section = section

        self.r_factor = None
        self.maskEffectiveness = None
        self.prevalenceTesting       = None
        self.prevalenceContactTracing = None
        self.recoveryRate            = None
        self.deathRate            = None
        self.socialDistancing        = None
        
        self.numberOfCases = None
        self.numberOfRecovery = None
        self.numberOfDeath = None
        self.numberOfTests= None
        
        self.initParameters()
        
    def initParameters(self):
        """
        A method to initialize the parameters using config.props
        """
        self.setK(self.config.getFloat(self.section, "k_factor"))
        self.setR(self.config.getFloat(self.section, "r_factor"))
        
        self.setMaskEffectiveness(self.config.getFloat(self.section, "maskEffectiveness"))
        
        self.setPrevalenceTesting(self.config.getFloat(self.section, "prevalenceTesting"))
        self.setPrevalenceContactTracing(self.config.getFloat(self.section, "prevalenceContactTracing"))
        
        #self.setRecoveryRate(self.config.getFloat(self.section, "numberOfRecovery") / self.config.getFloat(self.section, "numberOfCases"))
        #self.setDeathRate(self.config.getFloat(self.section, "numberOfDeath") / self.config.getFloat(self.section, "numberOfCases"))
        
        self.setSocialDistancing(self.config.getFloat(self.section, "socialDistancing"))
        
        
    """
    Getter methods
    """
    def getName(self):
        return self.name
    
    def getK(self):
        return self.k_factor
    
    def getR(self):
        return self.r_factor
    
    def getMaskEffectiveness(self):
        return self.maskEffectiveness
    
    def getMasksUsage(self):
        return self.masksUsage

    def getPrevalenceContactTracing(self):
        return self.prevalenceContactTracing
    
    def getPrevalenceTesting(self):
        return self.prevalenceTesting    
    
    def getRecoveryRate(self):
        return self.recoveryRate
    
    def getDeathRate(self):
        return self.deathRate
    
    def getSocialDistancing(self):
        return self.socialDistancing
    
    """
    Setter methods
    """
    def setName(self, name):
        self.name = name
    
    def setK(self, k):
        self.k_factor = k
    
    def setR(self, r):
        self.r_factor = r
    
    def setMaskEffectiveness(self, val):
        self.maskEffectiveness = val
    
    def setMasksUsage(self, val):
        self.masksUsage = val

    def setPrevalenceContactTracing(self, val):
        self.prevalenceContactTracing = val
    
    def setPrevalenceTesting(self, val):
        self.prevalenceTesting= val  
    
    def setRecoveryRate(self, val):
        self.recoveryRate = val
        
    def setDeathRate(self, val):
        self.deathRate = val
    
    def setSocialDistancing(self, val):
        self.socialDistancing = val
    
    
    """
    Public methods
    """
    def randomBooleanWeightSelect(self, weightTrue, weightFalse):
        """
        A method to randomly select True or False using weight
        
        @return boolean
        """
        return random.choices([True, False], (weightTrue, weightFalse))[0]
    
    
    def checkIfInfected(self, person) -> bool:
        """
        A method to determine if the person is likely to be infected
        
        @return boolean
        """
        # If the person is immune, cannot get infected
        if person.isImmune(): return False
        
        notWear = self.getMaskEffectiveness() # Chance of getting infected when not wearing mask
        wear = 1 - self.getMaskEffectiveness() # Chance of getting infected when wearing mask
        # Use random choices with weight/bias
        if person.getWearMask():
            return self.randomBooleanWeightSelect(notWear, wear)
        else:
            return True
        
    
    def checkIfRecovered(self, person) -> bool:
        """
        A method to determine if the person is likely to be recovered
        
        @return boolean
        """
        # Days that the person showing symptom is around 17.8 days ~= 18 days        
        if (person.getInfectedLength() >= 23):
            return True
        return False
    
    def checkIfDead(self, person) -> bool:
        """
        A method to determine if the person is likely to be dead
        
        @return boolean
        """
        if person.isAlive() == False: return True
        
        if (person.getInfectedLength() > 18):
            # Formula current death rate = basePersonRecoveryRate ^ (1 / (Number of Days since Infected - 14))
            # The longer the person get infected, the higher risk they get
            # The probability increase exponentially as the day increases
            currentPersonDeathRate = person.getDeathRate()**(1 / (person.getInfectedLength() - 18))
            return self.randomBooleanWeightSelect(currentPersonDeathRate, 1 - currentPersonDeathRate)
        return False
