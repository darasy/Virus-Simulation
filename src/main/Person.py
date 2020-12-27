"""
@author: Darasy Reth
@email: reth.d@northeastern.edu
"""


import logging
import random
import numpy as np

class Person:
    """
    A class representation of the person
    """

    def __init__(self):
        """
        Constructor
        """
        self.age = None  # int value from 0 to 100
        self.gender = None  # 0: men, 1: female
        self.infectedStatus = False  # True: Infected, False: Not infected
        self.aliveStatus = True  # True: Alive, False: Dead
        self.immuneStatus = False # True: Immune, False: Not Immune
        self.healthStatus = 0  # 0: Healthy, 1: Immune, 2: Infected, 3: Dead
        self.location = np.array([-1, -1])  # A location he/she is currently at on the graph
        self.personID = None # Identification number of the person
        self.wearMask = True # A boolean to check if the person is wearing a mask
        self.preHealthCondition = False # A boolean indicating whether a person has a preexisting condition or not
        self.infectedLength = 0 # Length of when the person is infected

        self.personDeathRate = 0.0 # A person death rate
        self.personRecoveryRate = 0.0 # A person recovery rate
        
        self.chanceOfGettingInfected = 0.0 # Chance that the person can get infected
        
        self.getTested = False # A boolean to determine if the person get tested when infected
        
        
    """
    Setter methods
    """

    def setAge(self, age):
        if (age >= 0 and age <= 100):
            self.age = age
        
    def setGender(self, gender):
        if (gender >= 0 and gender <= 1):
            self.gender = gender
    
    def setInfectedStatus(self, status):
        self.infectedStatus = status
    
    def setAliveStatus(self, status):
        self.aliveStatus = status
    
    def setImmune(self, status):
        self.immuneStatus = status
            
    def setHealthStatus(self, status):
        if (status >= 0 and status <= 3): 
            self.healthStatus = status
            if (self.healthStatus == 0):
                self.aliveStatus = True;
                self.infectedLength = 0;
                self.infectedStatus = False;
            if (self.healthStatus == 1): 
                self.immuneStatus = True;
                self.aliveStatus = True;
            if (self.healthStatus == 2): 
                self.infectedStatus = True;
                self.aliveStatus = True;
            if (self.healthStatus == 3): 
                self.aliveStatus = False;
        else:
            logging.warn("Invalid health status")
            
    def setLocation(self, loc):
        self.location = loc
        
    def setID(self, personID):
        self.personID = personID
        
    def setWearMask(self, val):
        self.wearMask = val    
        
    def setInfectedLength(self, val):
        self.infectedLength = val
    
    def incrementDaysOfInfected(self):
        self.infectedLength += 1
    
    def setPreHealthCondition(self, val):
        self.preHealthCondition = val
        
    def setNumberOfDaysTillDeadAfterInfected(self, val):
        self.numberOfDaysTillDeadAfterInfected = val
        
    def setDeathRate(self, val):
        self.personDeathRate = val
        
    def setChanceOfGettingInfected(self, val):
        self.chanceOfGettingInfected = val
        
    def setTestedStatus(self, val = True):
        self.getTested = val
            
    """
    Getter methods
    """    

    def getAge(self) -> int:
        return self.age
    
    def getGender(self) -> int:
        return self.gender
    
    def getInfectedStatus(self) -> bool:
        return self.infectedStatus
    
    def getAliveStatus(self) -> bool:
        return self.aliveStatus
    
    def getImmuneStatus(self) -> bool:
        return self.immuneStatus
        
    def getHealthStatus(self) -> int:
        return self.healthStatus
    
    def getLocation(self):
        return self.location
    
    def getPersonID(self):
        return self.personID
    
    def getWearMask(self):
        return self.wearMask
    
    def getInfectedLength(self):
        return self.infectedLength
    
    def getPreHealthCondition(self):
        return self.preHealthCondition
    
    def getNumberOfDaysTillDeathAfterInfected(self):
        return self.numberOfDaysTillDeadAfterInfected
    
    def getDeathRate(self):
        return self.personDeathRate
    
    def getChanceOfGettingInfected(self):
        return self.chanceOfGettingInfected
    
    def getTestedStatus(self):
        return self.getTested
    
    """
    is* methods()
    """
    def isAlive(self):
        """
        Check if the person is alive

        @return boolean
        """
        return self.aliveStatus
    
    def isImmune(self):
        """
        Check if the person is immune
        
        @return boolean
        """
        return self.immuneStatus
    
    def isInfected(self):
        """
        Check if the person is infected
        
        @return boolean
        """
        return self.infectedStatus 
    
    """
    Public methods
    """
    def randomWalk(self, x_min, x_max, y_min, y_max):
        """
        A random walk mechanism for the person object to move left, right, up or down
        """
        ns = bool(random.getrandbits(1))
        stepDistance = random.uniform(0.01, 0.1)
        step = stepDistance if bool(random.getrandbits(1)) else -stepDistance
        loc = self.getLocation()
        if ns: 
            x = loc[0] + step
            if x >= x_max:
                self.setLocation(np.array([x - stepDistance, loc[1]]))
            elif x <= x_min:
                self.setLocation(np.array([x + stepDistance, loc[1]]))
            else:
                self.setLocation(np.array([x, loc[1]]))
            
        else:
            y = loc[1] + step
            if y >= y_max:
                self.setLocation(np.array([loc[0], y - stepDistance]))
            elif y <= y_min:
                self.setLocation(np.array([loc[0], y + stepDistance]))
            else:
                self.setLocation(np.array([loc[0], y]))
  