"""
@author: Darasy Reth
@email: reth.d@northeastern.edu
"""


import logging
import unittest
from main.Population import Population
from main.Person import Person
import numpy as np
from  main.Covid19 import Covid19
from main.Ebola import Ebola

class PopulationTest(unittest.TestCase):
    """
    A unittest for Population class
    """
    
    @classmethod
    def setUpClass(self):
        logging.basicConfig(format='%(asctime)s:%(module)s:%(levelname)s:%(message)s', level=logging.DEBUG)
        logging.info("Testing Population class...")
        self.population = Population()

    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def testSetAndGetName(self):
        name = "Test"
        self.population.setName(name)
        self.assertEqual(self.population.getName(),name)
    
    def testDistanceBetweenTwoIndividual(self):
        """
        A method to compute the distance between 2 people
        
        @return float
        """
        personA = Person()
        personA.setLocation(np.array([1., 1.]))
        personB = Person()
        personB.setLocation(np.array([1., 1.]))
        distance = self.population.distanceBetweenTwoIndividual(personA, personB)
        self.assertEqual(distance, 0)
        
        personA.setLocation(np.array([-1., -1.]))
        personB.setLocation(np.array([1., 1.]))
        distance = self.population.distanceBetweenTwoIndividual(personA, personB)
        self.assertEqual(distance, 2.8284271247461903)
        
    def testGetTestedStatus(self):
        self.population.numberOfTested = 1.0
        self.assertEqual(self.population.assignGetTestedStatus(),True)
        
    def testAssignWearMaskStatus(self):
        self.population.maskUsage = 1.0
        self.assertEqual(self.population.assignWearMaskStatus(),True)
    
    def testAssignPersonDeathRate(self):
        personAge = 20
        preHealthCondition = True
        result = 0.01037904
        self.assertEqual(self.population.assignPersonDeathRate(personAge, preHealthCondition),result)
    
    def testAssignChanceOfGettingInfected(self):
        personAge = 20
        preHealthCondition = True
        result = 0.65
        self.assertEqual(self.population.assignChanceOfGettingInfected(personAge, preHealthCondition),result)
                
    def testAddPerson(self):
        """
        Test adding a person to the population
        """
        # Create an infectious person object and add to the population
        # With ID attached
        person = Person()
        person.setID(self.population.generatePersonID())
        person.setHealthStatus(0) # Infected
        person.setInfectedStatus(False) # Set to be infected
        person.setLocation(self.population.assignRandomPosition()) # Assign random position
        person.setAge(25) # Set age 
        person.setAliveStatus(True) # Set to be alive
        person.setPreHealthCondition(True) # Set to have a bad prehealth condition
        person.setDeathRate(0.2) # Assign death rate
        person.setChanceOfGettingInfected(0.2) # Assign chance of getting infected (though already infected)
        person.setInfectedLength(1) # Set the starting day of being infected
        self.population.addPerson(person)
        self.assertTrue(person.getPersonID() in self.population.getPopulation())
        self.assertIsNotNone(self.population.getPerson(person.getPersonID()))
        # Without ID
        person = Person()
        person.setHealthStatus(0) # Infected
        person.setInfectedStatus(False) # Set to be infected
        person.setLocation(self.population.assignRandomPosition()) # Assign random position
        person.setAge(25) # Set age 
        person.setAliveStatus(True) # Set to be alive
        person.setPreHealthCondition(True) # Set to have a bad prehealth condition
        person.setDeathRate(0.2) # Assign death rate
        person.setChanceOfGettingInfected(0.2) # Assign chance of getting infected (though already infected)
        person.setInfectedLength(1) # Set the starting day of being infected
        self.population.addPerson(person)
        self.assertTrue(person.getPersonID() in self.population.getPopulation())

        
    def testRemovePerson(self):
        """
        Test reoving a person from a population
        """
        # Create an infectious person object and add to the population
        person = Person()
        person.setID(self.population.generatePersonID())
        person.setHealthStatus(0) # Infected
        person.setInfectedStatus(True) # Set to be infected
        person.setLocation(self.population.assignRandomPosition()) # Assign random position
        person.setAge(25) # Set age 
        person.setAliveStatus(True) # Set to be alive
        person.setPreHealthCondition(True) # Set to have a bad prehealth condition
        person.setDeathRate(0.2) # Assign death rate
        person.setChanceOfGettingInfected(0.2) # Assign chance of getting infected (though already infected)
        person.setInfectedLength(1) # Set the starting day of being infected
        self.population.addPerson(person)
        self.assertTrue(person.getPersonID() in self.population.getPopulation())
        self.population.removePerson(person.getPersonID())
        self.assertFalse(person.getPersonID() in self.population.getPopulation())
        
        
    def testGeneratePopulation(self):
        """
        Test generating a population
        """
        self.population = Population("Boston", 100, Covid19())
        self.assertEqual(self.population.getNumberOfPopulation(), 100)
        
        self.population = Population("Boston", 100, Ebola())
        self.assertEqual(self.population.getNumberOfPopulation(), 100)
        
        
    def testGetRandomAge(self):
        """
        Test a method to assign random age
        """
        age = self.population.assignRandomAge()
        withinRange = True if age < 101 and age >= 0 else False
        self.assertTrue(withinRange)
        
    def testAssignTestStatus(self):
        """
        Test a method to assign whether people get tested
        """
        s = self.population.assignGetTestedStatus()
        self.assertIsNotNone(s)
        
    def testAssignWearMaskStatus2(self):
        """
        Test a method to assign whether people wear a mask
        """
        s = self.population.assignWearMaskStatus()
        self.assertIsNotNone(s)
        
    def testAssignRandomPosition(self):
        """
        Test a method to assign a random position
        """
        s = self.population.assignRandomPosition()
        self.assertIsNotNone(s)
        
    def testAssignPreHealthCondition(self):
        """
        Test a method to assign a prehealth condition
        """
        s = self.population.assignPreHealthCondition(12)
        self.assertIsNotNone(s)
        
    def testGeneratePersonID(self):
        """
        Test a method to assign a prehealth condition
        """
        s = self.population.generatePersonID()
        self.assertEqual(len(s), 20)
        
    def testGetInfectedPopulation(self):
        """
        Test adding a person to the population
        """
        # Create an infectious person object and add to the population
        self.population = Population()
        person = Person()
        person.setID(self.population.generatePersonID())
        person.setHealthStatus(2) # Infected
        person.setInfectedStatus(True) # Set to be infected
        self.population.addPerson(person)
        self.assertEqual(len(self.population.getInfectedPopulation()), 1)
        
        
    def testGetNUmberOfDeath(self):
        self.assertEqual(self.population.getNumberOfDeath(), 0)
        
    def testGetNumberOfActiveCases(self):
        self.population = Population()
        person = Person()
        person.setID(self.population.generatePersonID())
        person.setHealthStatus(2) # Infected
        person.setInfectedStatus(True) # Set to be infected
        self.population.addPerson(person)
        self.assertEqual(self.population.getNumberOfActiveCases(), 1)
        
    