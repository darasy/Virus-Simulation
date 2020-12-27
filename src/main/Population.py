"""
@author: Darasy Reth
@email: reth.d@northeastern.edu
"""


import string, random
import numpy as np
from scipy.stats import gamma

from main.ConfigUtil import ConfigUtil
from main.Person import Person
from main.Covid19 import Covid19 

class Population:
    """
    A class representation of the population (US state, cities, country TBD)
    """

    def __init__(self, name = None, numberOfPeople = 300, virus = Covid19()):
        """
        Constructor
        """
        self.config = ConfigUtil()
        self.virus = virus # Virus instances, Covid19() or Ebola()
        
        self.name = name  # Name of the location 
        self.socialDistancing = self.config.getFloat(self.virus.section, "socialDistancing") # Get social distaning range
        # Get percentage of tested being conducted of the whole population
        self.numberOfTested = self.config.getFloat(self.virus.section, "numberOfTests") / self.config.getFloat(self.virus.section, "numberOfPopulation") 
        self.maskUsage = self.config.getFloat("Location.Info", "masksUsage") # Get percentage of mask usage of the whole population
        
        self.population = {} # A dictionary to store all population
        self.populationSize = numberOfPeople # Size of population
        
        self.x_axis = 1.0 # Maximum x point
        self.y_axis = 1.0 # Maximum y point
        
        # Generate population of size self.populationSize
        self.generatePopulation()
        
        self.infectedPopulation = {} # infected person IDs
        self.deathPopulation = 0 # Count number of death population
        self.recoveredPopulationDaily = 0 # Count number of population recovered from Covid 19
        self.quarantinePopulation = {} # IDs of people who are under quarantine
        
    """
    Getter methods
    """
    def getName(self):
        return self.name

    def getPopulation(self):
        return self.population
    
    def getPerson(self, personID):
        if (personID in self.population):      
            return self.population[personID]
    
    def getInfectedPopulation(self):
        return self.infectedPopulation    
    
    def getNumberOfActiveCases(self):
        return len(self.infectedPopulation.keys())
    
    def getNumberOfDeath(self):
        return self.deathPopulation
    
    def getNumberOfPopulation(self):
        return len(self.population.keys())
    
    """
    Setter methods
    """
    def setName(self, name):
        self.name = name
    
    """
    Public methods
    """
    
    def updateMap(self):
        """
        Get the most recent map updated
        """
        self.recoveredPopulationDaily = 0
        self.updatePopulationMovement()
        self.updateGetInfectedPopulation()


    def updatePopulationMovement(self):
        """
        Get the most recent population movements using RandomWalk
        """
        for people in self.getPopulation().keys():
            if self.population[people].isAlive():
                self.population[people].randomWalk(0.0, self.x_axis, 0.0, self.y_axis)
    
    
    def updateGetInfectedPopulation(self):
        """
        Get the most recent infected population
        """
        tempSet = self.infectedPopulation.copy()
        for infectedPerson in tempSet.keys():

            currentInfectedPerson = self.getPerson(infectedPerson)
            if currentInfectedPerson.isAlive():
                # Check if the current infected person recovers
                if self.virus.checkIfRecovered(currentInfectedPerson):
                    self.population[infectedPerson].setHealthStatus(1)
                    self.population[infectedPerson].setInfectedLength(0)
                    self.population[infectedPerson].setTestedStatus(False)
                    self.population[infectedPerson].setInfectedStatus(False)
                    self.population[infectedPerson].setImmune(True)
                    self.recoveredPopulationDaily += 1
                    self.infectedPopulation.pop(infectedPerson)
                    
                # Else check if the current infected person dies    
                elif self.virus.checkIfDead(currentInfectedPerson):
                    self.population[infectedPerson].setHealthStatus(3)
                    self.population[infectedPerson].setAliveStatus(False)
                    #self.removePerson(infectedPerson)
                    self.deathPopulation += 1
                    self.infectedPopulation.pop(infectedPerson)
    
                # Else check for anybody around the infected person
                else:
                    self.population[infectedPerson].incrementDaysOfInfected()
                    self.updateSurroundNeighbors(currentInfectedPerson)
                

            
    def updateSurroundNeighbors(self, infectedPerson):
        """
        A method to update health status of all the neighbors close to the infected person in less than social distancing range
        """
        r = 0
        r_factor = self.virus.r_factor
        if self.virus.k_factor < 1:
            r_factor = random.randint(0, int(r_factor*(r_factor ** (1- self.virus.k_factor))))
        for p in self.population:
            neighbor = self.getPerson(p)
            if self.distanceBetweenTwoIndividual(infectedPerson, neighbor) < self.virus.getSocialDistancing():
                if (neighbor.isInfected() == False) and neighbor.isAlive() and (not neighbor.isImmune()): 
                    neighborGetInfected = False
                    # Apply K and R factor
                    # If the number of neighbors is less than R, they all get infected   
                    if r < r_factor:
                        neighborGetInfected = True
                    # Else, determine based on their chance of being infected
                    else: neighborGetInfected = self.virus.checkIfInfected(neighbor)
                    # If infected, updated their health status
                    if neighborGetInfected: # If get infected
                        self.population[p].setHealthStatus(2) # Value 2 = Infected (0: Healthy, 1: Immune, 2: Infected, 3: Death)
                        self.population[p].setInfectedStatus(True)
                        self.infectedPopulation[p] = neighbor
                        self.population[p].incrementDaysOfInfected()
                        # A random function to determine if the person get tested when found to be infected
                        self.population[p].setTestedStatus(self.assignGetTestedStatus())
                    
                    r+=1

    def distanceBetweenTwoIndividual(self, personA, personB):
        """
        A method to compute the distance between 2 people
        
        @return float
        """
        A = personA.getLocation()
        B = personB.getLocation()
        # Using Euclean Distance
        distance = (A - B)**2
        distance = np.sum(distance)
        distance = np.sqrt(distance)
        return distance
    
    def addPerson(self, person):
        """
        A method to add the person to the population
        """
        # If the person does not have an ID, assign one randomly generated
        if person.getPersonID() == None:
            personID = self.generatePersonID()
            person.setID(personID)

        if person.getPersonID() not in self.population:
            self.population[person.getPersonID()] = person
            self.populationSize += 1
        if person.isInfected(): 
            self.infectedPopulation[person.getPersonID()] = person
            
            
    def removePerson(self, id):
        """
        A method to remove the person from the population
        """
        self.population.pop(id)
        self.infectedPopulation.pop(id)
                 
    def generatePersonID(self):
        """
        A method to generate an ID for the person
        
        @return String
        """
        
        personID = ''.join(random.choice(string.ascii_letters + string.digits) for r in range(20))
        while (personID in self.population):
            personID = ''.join(random.choice(string.ascii_letters + string.digits) for r in range(20))
        return personID
    
    def generatePopulation(self):
        """
        A method to generate random population
        """
        
        for i in range(self.populationSize):
            person = Person()
            person.setID(self.generatePersonID())
            age = self.assignRandomAge()
            person.setAge(age)
            person.setAliveStatus(True)
            person.setPreHealthCondition(self.assignPreHealthCondition(person.getAge()))
            person.setDeathRate(self.assignPersonDeathRate(person.getAge(), person.getPreHealthCondition()))
            person.setChanceOfGettingInfected(self.assignChanceOfGettingInfected(person.getAge(), person.getPreHealthCondition()))
            person.setGender(random.randint(0, 1)), 
            person.setHealthStatus(random.choices([0, 1], (0.9, 0.1))[0])
            person.setWearMask(self.assignWearMaskStatus())
            person.setLocation(self.assignRandomPosition())
            self.addPerson(person)
            
    def assignRandomPosition(self):
        """
        A function to assign the position of the person randomly
        
        @return np.array([x, y])
        """
        return np.array([random.uniform(0.0, self.x_axis), random.uniform(0.0, self.y_axis)])
        
        
    def assignRandomAge(self):
        """
        Assign age to a person randomly based on the population distribution from the dataset below
        
        @random float 
        """
        # Source: https://en.wikipedia.org/wiki/Demographics_of_the_United_States#:~:text=Structure,-The%20population%20is&text=The%20median%20age%20of%20the,median%20age%20is%2039.5%20years.
        ageGroup = [61175933, 43351778, 128863172, 42179856, 51055052]
        eachAgeGroupSize = 15 # Each age group contains 15 different ages
        eachAgeGroupGap = 14 # Max age - Min age in each group = 14
        ageGroup = np.array(ageGroup, dtype=float)
        ageGroup = ageGroup / sum(ageGroup)
        ageGroup = np.random.choice(a=range(5), size=1, p=ageGroup)[0]
        return eachAgeGroupSize*ageGroup + eachAgeGroupGap*random.uniform(0, 1) 
        
    def assignGetTestedStatus(self):
        """
        A random function to determine if the person get tested when found to be infected
        
        @return boolean
        """
        # 
        return random.choices([True, False], (self.numberOfTested, 1 - self.numberOfTested))[0]
    
    def assignWearMaskStatus(self):
        """
        A random function to determine if the person wear a mask
        
        @return boolean
        """
        
        return random.choices([True, False], (self.maskUsage, 1 - self.maskUsage))[0]
    
        
    def assignPreHealthCondition(self, personAge):
        """
        Randomly assign any prehealth condition of the person based on their age by assuming the younger the less likely he/she has a prehealth condition
        
        @return boolean
        """
        return np.random.rand() < gamma(7, scale=5).cdf(personAge)
        
        
    def assignPersonDeathRate(self, personAge, preHealthCondition):
        """
        Assign person death rate after infection based on their age
        
        @return float
        """
        ### COVID 19
        # Source: https://www.cdc.gov/nchs/nvss/vsrr/covid_weekly/index.htm#AgeAndSex
        # The death rate from all causes
        if self.virus.getName() == "Covid 19":
            if preHealthCondition:
                if personAge <= 14: return 0.002635006
                elif personAge <= 34: return 0.01037904
                elif personAge <= 54: return 0.027782814
                elif personAge <= 74: return 0.10361807
                else: return 0.85558507
            else:
                if personAge <= 14: return 0.000356602
                elif personAge <= 34: return 0.009179495
                elif personAge <= 54: return 0.07000617
                elif personAge <= 74: return 0.338387198
                else: return 0.582038481
        # Source: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4982163/table/T2/?report=objectonly 
        # For preHealth Condition, we make up some numbers as it's not available
        if self.virus.getName() == "Ebola":
            if preHealthCondition:
                if personAge <= 2: return 0.5
                elif personAge <= 4: return 0.3
                elif personAge <= 9: return 0.23
                elif personAge <= 14: return 0.2
                elif personAge <= 19: return 0.25
                elif personAge <= 29: return 0.28
                elif personAge <= 39: return 0.55
                elif personAge <= 49: return 0.78
                else: return 0.9
            else:
                if personAge <= 2: return 0.352
                elif personAge <= 4: return 0.174
                elif personAge <= 9: return 0.115
                elif personAge <= 14: return 0.091
                elif personAge <= 19: return 0.14
                elif personAge <= 29: return 0.169
                elif personAge <= 39: return 0.395
                elif personAge <= 49: return 0.468
                else: return 0.605
    
    def assignChanceOfGettingInfected(self, personAge, preHealthConditions):
        """
        Assign person chance of getting infection based on their age
        
        @return float
        """
        # We make up some numbers as we cannot find the data for both virus
        if self.virus.getName() == "Covid 19":
            # Custom assign value
            if preHealthConditions:
                if personAge <= 14: return 0.3
                elif personAge <= 34: return 0.65
                elif personAge <= 54: return 0.8
                elif personAge <= 74: return 0.9
                else: return 0.99
            else:
                if personAge <= 14: return 0.2
                elif personAge <= 34: return 0.4
                elif personAge <= 54: return 0.7
                elif personAge <= 74: return 0.8
                else: return 0.9
        
        # Source: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4982163/table/T2/?report=objectonly 
        # For preHealth Condition, we make up some numbers as it's not available
        if self.virus.getName() == "Ebola":
            if preHealthConditions:
                if personAge <= 2: return 0.12
                elif personAge <= 4: return 0.2
                elif personAge <= 9: return 0.2
                elif personAge <= 14: return 0.15
                elif personAge <= 19: return 0.08
                elif personAge <= 29: return 0.1
                elif personAge <= 39: return 0.09
                elif personAge <= 49: return 0.06
                else: return 0.1
            else:
                if personAge <= 2: return 0.019
                elif personAge <= 4: return 0.116
                elif personAge <= 9: return 0.115
                elif personAge <= 14: return 0.091
                elif personAge <= 19: return 0.028
                elif personAge <= 29: return 0.078
                elif personAge <= 39: return 0.052
                elif personAge <= 49: return 0.0106
                else: return 0.0
        