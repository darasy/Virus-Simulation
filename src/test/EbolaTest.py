"""
@author: Darasy Reth
@email: reth.d@northeastern.edu
"""


import logging
import unittest
from main.Ebola import Ebola
from main.Population import Population
from main.ConfigUtil import ConfigUtil


class EbolaTest(unittest.TestCase):
    """
    A unittest for Virus class
    """
    
    @classmethod
    def setUpClass(self):
        logging.basicConfig(format='%(asctime)s:%(module)s:%(levelname)s:%(message)s', level=logging.DEBUG)
        logging.info("Testing Ebola class...")
        self.Virus = Ebola()
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
        self.assertEqual(name, "Ebola")
    
    def testGetK(self):
        k = self.Virus.getK()
        self.assertEqual(k, self.config.getFloat("Ebola.Factors", "k_factor"))
        
    
    def testGetR(self):
        r = self.Virus.getR()
        self.assertEqual(r, self.config.getFloat("Ebola.Factors", "r_factor"))

        
    def testGetMaskEffectiveness(self):
        r = self.Virus.getMaskEffectiveness()
        self.assertEqual(r, self.config.getFloat("Ebola.Factors", "maskEffectiveness"))
    
    def testGetPrevalenceTesting(self):
        r = self.Virus.getPrevalenceTesting()
        self.assertEqual(r, self.config.getFloat("Ebola.Factors", "prevalenceTesting"))
    
    def testGetPrevalenceContactTracing(self):
        r = self.Virus.getPrevalenceContactTracing()
        self.assertEqual(r, self.config.getFloat("Ebola.Factors", "prevalenceContactTracing"))
        

    