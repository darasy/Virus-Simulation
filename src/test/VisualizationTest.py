"""
@author: Darasy Reth
@email: reth.d@northeastern.edu
"""


import logging
import unittest
from main.Visualization import Visualization
from main.Population import Population
from main.Covid19 import Covid19

class VisualizationTest(unittest.TestCase):
    """
    A unittest for Virus class
    """
    
    @classmethod
    def setUpClass(self):
        logging.basicConfig(format='%(asctime)s:%(module)s:%(levelname)s:%(message)s', level=logging.DEBUG)
        logging.info("Testing Visualization class...")
        self.visualization = Visualization()
        self.population = Population("City 1", 20, Covid19())

    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def testGetScatterComponents(self):
        """
        Test a method to get the x points, y points and their corresponding color representation
        """
        x, y, g = self.visualization.getScatterComponents(self.population)
        
        self.assertEqual(20, len(x))
        self.assertEqual(20, len(y))
        self.assertEqual(20, len(g))
        
        nonExists = False
        for i in x:
            if i == None: nonExists = True
        self.assertFalse(nonExists)
        
        for i in y:
            if i == None: nonExists = True
        self.assertFalse(nonExists)
        
        otherThanLimeColor = False
        for i in g:
            if i != 'lime': otherThanLimeColor = True
        self.assertFalse(otherThanLimeColor)
        
        
        