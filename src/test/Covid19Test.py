"""
@author: Darasy Reth
@email: reth.d@northeastern.edu
"""


import logging
import unittest
from main.Covid19 import Covid19
from main.Population import Population
from main.ConfigUtil import ConfigUtil


class Covid19Test(unittest.TestCase):
    """
    A unittest for Virus class
    """
    
    @classmethod
    def setUpClass(self):
        logging.basicConfig(format='%(asctime)s:%(module)s:%(levelname)s:%(message)s', level=logging.DEBUG)
        logging.info("Testing Covid 19 class...")
        self.Virus = Covid19()
        self.Population = Population()
        self.config = ConfigUtil()

    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    """
    Test Setter and Getter methods
    """
    def testGetName(self):
        name = self.Virus.getName()
        self.assertEqual(name, "Covid 19")
    
    def testGetK(self):
        k = self.Virus.getK()
        self.assertEqual(k, self.config.getFloat("Covid19.Factors", "k_factor"))
        
    
    def testGetR(self):
        r = self.Virus.getR()
        self.assertEqual(r, self.config.getFloat("Covid19.Factors", "r_factor"))

        
    def testGetMaskEffectiveness(self):
        r = self.Virus.getMaskEffectiveness()
        self.assertEqual(r, self.config.getFloat("Covid19.Factors", "maskEffectiveness"))
    
    def testGetPrevalenceTesting(self):
        r = self.Virus.getPrevalenceTesting()
        self.assertEqual(r, self.config.getFloat("Covid19.Factors", "prevalenceTesting"))
    
    def testGetPrevalenceContactTracing(self):
        r = self.Virus.getPrevalenceContactTracing()
        self.assertEqual(r, self.config.getFloat("Covid19.Factors", "prevalenceContactTracing"))
        

    