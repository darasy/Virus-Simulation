"""
@author: Darasy Reth
@email: reth.d@northeastern.edu
"""

import logging
import unittest
from main.Virus import Virus
from main.Person import Person
from main.Population import Population


class VirusTest(unittest.TestCase):
    """
    A unittest for Virus class
    """
    
    @classmethod
    def setUpClass(self):
        logging.basicConfig(format='%(asctime)s:%(module)s:%(levelname)s:%(message)s', level=logging.DEBUG)
        logging.info("Testing Virus class...")
        self.Virus = Virus()
        self.Population = Population()

    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    """
    Test Setter and Getter methods
    """
    def testSetAndGetName(self):
        name = "Test"
        self.Virus.setName(name)
        self.assertEqual(self.Virus.getName(),name)
    
    def testSetAndGetK(self):
        k = 0.2
        self.Virus.setK(k)
        self.assertEqual(self.Virus.getK(),k)
        
    def testSetAndGetK2(self):
        k = 0.2
        self.Virus.setK(k)
        self.assertEqual(self.Virus.getK(),k)
        self.Virus.setK(k + 2)
        self.assertEqual(self.Virus.getK(), k + 2)
    
    def testSetAndGetR(self):
        r = 0.5
        self.Virus.setR(r)
        self.assertEqual(self.Virus.getR(),r)
        self.Virus.setR(r + 2)
        self.assertEqual(self.Virus.getR(),r + 2)
        
    def testSetAndGetMaskEffectiveness(self):
        val = 0.2
        self.Virus.setMaskEffectiveness(val)
        self.assertEqual(self.Virus.getMaskEffectiveness(),val)
    
    def testSetAndGetMasksUsage(self):
        val = 0.1
        self.Virus.setMasksUsage(val)
        self.assertEqual(self.Virus.getMasksUsage(),val)
    
    def testSetAndGetPrevalenceContactTracing(self):
        val = 0.4
        self.Virus.setPrevalenceContactTracing(val)
        self.assertEqual(self.Virus.getPrevalenceContactTracing(),val)
    
    def testSetAndGetPrevalenceTesting(self):
        val = 0.2
        self.Virus.setPrevalenceTesting(val)
        self.assertEqual(self.Virus.getPrevalenceTesting(),val)
        
    def testSetAndGetRecoveryRate(self):
        val = 0.2
        self.Virus.setRecoveryRate(val)
        self.assertEqual(self.Virus.getRecoveryRate(),val)
    
    def testSetAndGetDeathRate(self):
        val = 0.2
        self.Virus.setDeathRate(val)
        self.assertEqual(self.Virus.getDeathRate(),val)
    
    def testSetAndGetSocialDistancing(self):
        val = 0.2
        self.Virus.setSocialDistancing(val)
        self.assertEqual(self.Virus.getSocialDistancing(),val)
    
    
    def testrandomBooleanWeightSelect(self):
        """
        Test a method to randomly select True or False using weight
        """
        val = self.Virus.randomBooleanWeightSelect(0.1, 0.9)
        self.assertIsNotNone(val)
        val = self.Virus.randomBooleanWeightSelect(0.9, 0.1)
        self.assertIsNotNone(val)
        val = self.Virus.randomBooleanWeightSelect(0.5, 0.5)
        self.assertIsNotNone(val)
        
    def testCheckIfInfected(self):
        """
        Test a method to determine if the person is likely to be infected
        """
        # Create an infectious person object and add to the population
        person = Person()
        person.setHealthStatus(2) # Infected
        person.setInfectedStatus(True) # Set to be infected
        person.setLocation(self.Population.assignRandomPosition()) # Assign random position
        person.setAge(25) # Set age 
        person.setAliveStatus(True) # Set to be alive
        person.setPreHealthCondition(True) # Set to have a bad prehealth condition
        person.setDeathRate(0.2) # Assign death rate
        person.setChanceOfGettingInfected(0.2) # Assign chance of getting infected (though already infected)
        person.setInfectedLength(1) # Set the starting day of being infected
        
        val = self.Virus.checkIfInfected(person)
        self.assertIsNotNone(val)
        # Set the person to be immune
        person.setImmune(True)
        val = self.Virus.checkIfInfected(person)
        self.assertFalse(val)
    
    def testCheckIfRecover(self):
        """
        Test a method to determine if the person is likely to be infected
        """
        # Create an infectious person object and add to the population
        person = Person()
        person.setHealthStatus(2) # Infected
        person.setLocation(self.Population.assignRandomPosition()) # Assign random position
        person.setAge(25) # Set age 
        person.setAliveStatus(True) # Set to be alive
        person.setPreHealthCondition(True) # Set to have a bad prehealth condition
        person.setDeathRate(0.2) # Assign death rate
        person.setChanceOfGettingInfected(0.2) # Assign chance of getting infected (though already infected)
        
        val = self.Virus.checkIfRecovered(person)
        self.assertIsNotNone(val)
        person.setInfectedStatus(True) # Set to be infected
        person.setInfectedLength(9) # Set the number of day of being infected
        val = self.Virus.checkIfRecovered(person)
        self.assertFalse(val)
        person.setInfectedLength(25) # Set the starting day of being infected
        val = self.Virus.checkIfRecovered(person)
        self.assertTrue(val)
        
    def testCheckIfDead(self):
        """
        Test a method to see if the person is dead
        """
        # Create an infectious person object and add to the population
        person = Person()
        person.setHealthStatus(2) # Infected
        person.setLocation(self.Population.assignRandomPosition()) # Assign random position
        person.setAge(25) # Set age 
        person.setAliveStatus(True) # Set to be alive
        person.setPreHealthCondition(True) # Set to have a bad prehealth condition
        person.setDeathRate(0.2) # Assign death rate
        person.setChanceOfGettingInfected(0.2) # Assign chance of getting infected (though already infected)
        
        val = self.Virus.checkIfRecovered(person)
        self.assertIsNotNone(val)
        person.setInfectedStatus(True) # Set to be infected
        person.setInfectedLength(9) # Set the number of day of being infected
        val = self.Virus.checkIfDead(person)
        self.assertFalse(val) # Set the person to be dead
        person.setAliveStatus(False)
        val = self.Virus.checkIfDead(person)
        self.assertTrue(val)
    