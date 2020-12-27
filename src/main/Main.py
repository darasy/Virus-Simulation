"""
@author: Darasy Reth
@email: reth.d@northeastern.edu
"""

import sys
sys.path.append("../../src")

from main.Simulation import Simulation
from main.Covid19 import Covid19
from main.Ebola import Ebola


def Main():
    """
    A main function to run the simulation
    """
    numberOfPopulation = 350
    numberOfDays = 60
    
    simulation = Simulation(Covid19(), numberOfPopulation, numberOfDays, "Covid 19 Simulation")
    simulation.run()    
    simulation = Simulation(Ebola(), numberOfPopulation, numberOfDays, "Ebola Simulation")
    simulation.run()
    
if __name__ == "__main__":
    """
    Run the program
    """
    Main()
    
