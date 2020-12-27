"""
@author: Darasy Reth
@email: reth.d@northeastern.edu
"""


from main.ConfigUtil import ConfigUtil
from main.Virus import Virus

class Ebola(Virus):
    """
    A class representation of the virus which extends from the base class Virus: Ebola
    
    """

    def __init__(self):
        """
        Constructor
        """
        super().__init__(name="Ebola", section="Ebola.Factors")
        
    
    
        