"""
@author: Darasy Reth
@email: reth.d@northeastern.edu
"""


import logging
import unittest
from main.Simulation import Simulation
from main.Covid19 import Covid19

class SimulationTest(unittest.TestCase):
    """
    A unittest for Simulation class
    """
    
    @classmethod
    def setUpClass(self):
        logging.basicConfig(format='%(asctime)s:%(module)s:%(levelname)s:%(message)s', level=logging.DEBUG)
        logging.info("Testing Simulation class...")
        self.simulation = Simulation(Covid19(), 10, 10)

    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def testCreateInfectedPerson(self):
        """
        Test a method to create infected person
        """
        self.assertIsNotNone(self.simulation.createInfectiousPerson())
    
    def testRunSimulation(self):
        """
        Test a method to run a simulation
        """
        error = False
        try :
            self.simulation.run()
        except Exception:
            error = True
        self.assertFalse(error)