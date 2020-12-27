"""
@author: Darasy Reth
@email: reth.d@northeastern.edu
"""


import logging
import unittest
import numpy as np
from main.Person import Person

class PersonTest(unittest.TestCase):
    """
    A unittest for Person class
    """
    
    @classmethod
    def setUpClass(self):
        logging.basicConfig(format='%(asctime)s:%(module)s:%(levelname)s:%(message)s', level=logging.DEBUG)
        logging.info("Testing Person class...")
        self.person = Person()

    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    def testSetAndGetAge(self):
        age = 25
        self.person.setAge(age)
        self.assertEqual(self.person.getAge(), age)

    def testSetAndGetGender(self):
        gender = 0
        self.person.setGender(gender)
        self.assertEqual(self.person.getGender(), gender)
            
    def testSetAndGetInfectedStatus(self):
        status = True
        self.person.setInfectedStatus(status)
        self.assertEqual(self.person.getInfectedStatus(), status)
        
    def testSetAndGetAliveStatus(self):
        status = True
        self.person.setAliveStatus(status)
        self.assertEqual(self.person.getAliveStatus(), status)

    def testSetHealthStatus(self):
        status = 2
        self.person.setHealthStatus(status)
        self.assertEqual(self.person.getHealthStatus(), status)
        self.assertEqual(self.person.getAliveStatus(), True)
        self.assertEqual(self.person.getInfectedStatus(), True)
        
    def testSetAndGetImmuneStatus(self):
        status = True
        self.person.setImmune(status)
        self.assertEqual(self.person.getImmuneStatus(),status)
    
    def testSetAndGetLocation(self):
        loc = 100
        self.person.setLocation(loc)
        self.assertEqual(self.person.getLocation(),loc)
        
    def testSetAndGetPersonID(self):
        personID = 1
        self.person.setID(personID)
        self.assertEqual(self.person.getPersonID(),personID)
    
    def testSetAndGetWearMask(self):
        val = True
        self.person.setWearMask(val)
        self.assertEqual(self.person.getWearMask(),val)
        
    def testSetAndGetInfectedLength(self):
        val = 10
        self.person.setInfectedLength(val)
        self.assertEqual(self.person.getInfectedLength(),val)
    
    def testSetAndGetPreHealthCondition(self):
        val = True
        self.person.setPreHealthCondition(val)
        self.assertEqual(self.person.getPreHealthCondition(),val)
        
    def testSetAndGetNumberOfDaysTillDeathAfterInfected(self):
        val = 1
        self.person.setNumberOfDaysTillDeadAfterInfected(val)
        self.assertEqual(self.person.getNumberOfDaysTillDeathAfterInfected(),val)
        
    def testSetAndGetDeathRate(self):
        val = 0.2
        self.person.setDeathRate(val)
        self.assertEqual(self.person.getDeathRate(),val)
    
    def testSetAndGetChanceOfGettingInfected(self):
        val = 0.2
        self.person.setChanceOfGettingInfected(val)
        self.assertEqual(self.person.getChanceOfGettingInfected(),val)
        
    def testRandomWalk(self):
        self.person.setLocation(np.array([0.5, 0.5]))
        self.person.randomWalk(0, 1, 0, 1)
        locX = self.person.getLocation()[0]
        locY = self.person.getLocation()[1]
        stayWIthinRangeX = locX <= 1.0 and locX >= 0.0
        stayWIthinRangeY = locY <= 1.0 and locY >= 0.0
        self.assertTrue(stayWIthinRangeX)
        self.assertTrue(stayWIthinRangeY)
        
        