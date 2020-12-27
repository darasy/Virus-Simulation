"""
@author: Darasy Reth
@email: reth.d@northeastern.edu
"""

import configparser
import logging
import os


class ConfigUtil:
    """
    A class representation of the configuration class
    """
    
    def __init__(self):
        """
        Constructor for ConfigUtil.
        """
        self.configFile = "../../config/config.props"
        self.configParser = configparser.ConfigParser()
        self.isLoaded = False
        self.loadConfig()
        logging.info("Created instance of ConfigUtil: " + str(self))
            
    """
        public methods
    """

    def getBoolean(self, section: str, key: str):
        """
        Get a boolean value
        
        @return a boolean value
        """
        return self.getConfig().getboolean(section, key)
        
    def getInteger(self, section: str, key: str):
        """
        Get an integer value
        
        @return an int value
        """
        return self.getConfig().getint(section, key)
    
    def getFloat(self, section: str, key: str):
        """
        Get a float value
        
        @return a float value
        """
        return self.getConfig().getfloat(section, key)
        
    def loadConfig(self):
        """
        A method for loading configuration file
        """
        if (os.path.exists(self.configFile) and os.path.isfile(self.configFile)):            
            self.configParser.read(self.configFile)
            self.isLoaded = True
        else:
            logging.info("Config file %s doesn't exist.")
        
    def getConfig(self) -> configparser:
        """
        Returns the entire configuration object. If the config file hasn't
        yet been loaded, it will be loaded.
        
        @param forceReload Defaults to false; if true, will reload the config.
        @return The entire configuration file.
        """
        if (not self.isLoaded):
            self.loadConfig()
        
        return self.configParser

    