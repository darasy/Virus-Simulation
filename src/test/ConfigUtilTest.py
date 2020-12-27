"""
@author: Darasy Reth
@email: reth.d@northeastern.edu
"""


import logging
import unittest
from main.ConfigUtil import ConfigUtil

class ConfigUtilTest(unittest.TestCase):
    """
    A unittest for ConfigUtil class
    """
    
    @classmethod
    def setUpClass(self):
        logging.basicConfig(format='%(asctime)s:%(module)s:%(levelname)s:%(message)s', level=logging.DEBUG)
        logging.info("Testing ConfigUtil class...")
        self.configUtil = ConfigUtil()

    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    def testLoadCofig(self):
        self.assertEqual(self.configUtil.isLoaded, True)

    def testGetIntegerProperty(self):
        populationDensity = self.configUtil.getInteger("Location.Info", "populationDensity")
        self.assertEqual(type(populationDensity), type(1))
    
    def testGetFloatProperty(self):
        """
        Test for Covid 19 parameters
        """
        k_factor = self.configUtil.getFloat("Covid19.Factors", "k_factor")
        self.assertEqual(type(k_factor), type(1.0))
    
        r_factor = self.configUtil.getFloat("Covid19.Factors", "r_factor")
        self.assertEqual(type(r_factor), type(1.0))
        
        maskEffectiveness = self.configUtil.getFloat("Covid19.Factors", "maskEffectiveness")
        self.assertEqual(type(maskEffectiveness), type(1.0))
        
        prevalenceTesting = self.configUtil.getFloat("Covid19.Factors", "prevalenceTesting")
        self.assertEqual(type(prevalenceTesting), type(1.0))
        
        prevalenceContactTracing = self.configUtil.getFloat("Covid19.Factors", "prevalenceContactTracing")
        self.assertEqual(type(prevalenceContactTracing), type(1.0))
        
        numberOfCases = self.configUtil.getFloat("Covid19.Factors", "numberOfCases")
        self.assertEqual(type(numberOfCases), type(1.0))
        
        numberOfRecovery = self.configUtil.getFloat("Covid19.Factors", "numberOfRecovery")
        self.assertEqual(type(numberOfRecovery), type(1.0))
        
        numberOfDeath = self.configUtil.getFloat("Covid19.Factors", "numberOfDeath")
        self.assertEqual(type(numberOfDeath), type(1.0))
        
        numberOfTests = self.configUtil.getFloat("Covid19.Factors", "numberOfTests")
        self.assertEqual(type(numberOfTests), type(1.0))
        
        numberOfPopulation = self.configUtil.getFloat("Covid19.Factors", "numberOfPopulation")
        self.assertEqual(type(numberOfPopulation), type(1.0))
        
        socialDistancing = self.configUtil.getFloat("Covid19.Factors", "socialDistancing")
        self.assertEqual(type(socialDistancing), type(1.0))
        
        """
        Test for Ebola parameters
        """
        k_factor = self.configUtil.getFloat("Ebola.Factors", "k_factor")
        self.assertEqual(type(k_factor), type(1.0))
    
        r_factor = self.configUtil.getFloat("Ebola.Factors", "r_factor")
        self.assertEqual(type(r_factor), type(1.0))
        
        maskEffectiveness = self.configUtil.getFloat("Ebola.Factors", "maskEffectiveness")
        self.assertEqual(type(maskEffectiveness), type(1.0))
        
        prevalenceTesting = self.configUtil.getFloat("Ebola.Factors", "prevalenceTesting")
        self.assertEqual(type(prevalenceTesting), type(1.0))
        
        prevalenceContactTracing = self.configUtil.getFloat("Ebola.Factors", "prevalenceContactTracing")
        self.assertEqual(type(prevalenceContactTracing), type(1.0))
        
        numberOfCases = self.configUtil.getFloat("Ebola.Factors", "numberOfCases")
        self.assertEqual(type(numberOfCases), type(1.0))
        
        numberOfRecovery = self.configUtil.getFloat("Ebola.Factors", "numberOfRecovery")
        self.assertEqual(type(numberOfRecovery), type(1.0))
        
        numberOfDeath = self.configUtil.getFloat("Ebola.Factors", "numberOfDeath")
        self.assertEqual(type(numberOfDeath), type(1.0))
        
        numberOfTests = self.configUtil.getFloat("Ebola.Factors", "numberOfTests")
        self.assertEqual(type(numberOfTests), type(1.0))
        
        numberOfPopulation = self.configUtil.getFloat("Ebola.Factors", "numberOfPopulation")
        self.assertEqual(type(numberOfPopulation), type(1.0))
        
        socialDistancing = self.configUtil.getFloat("Ebola.Factors", "socialDistancing")
        self.assertEqual(type(socialDistancing), type(1.0))
        
    def testGetBooleanProperty(self):
        travelRestriction = self.configUtil.getBoolean("Location.Info", "travelRestriction")
        self.assertEqual(type(travelRestriction), type(True))
        quarantineRestriction = self.configUtil.getBoolean("Location.Info", "quarantineRestriction")
        self.assertEqual(type(quarantineRestriction), type(True))

    
