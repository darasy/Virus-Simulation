"""
@author: Darasy Reth
@email: reth.d@northeastern.edu
"""


from main.ConfigUtil import ConfigUtil
from main.Virus import Virus

class Covid19(Virus):
    """
    A class representation of the virus which extends from the base class Virus: Covid 19
    
    """

    def __init__(self):
        """
        Constructor
        """
        super().__init__(name="Covid 19", section="Covid19.Factors")
        
    
    
        