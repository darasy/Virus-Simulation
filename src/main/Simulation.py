"""
@author: Darasy Reth
@email: reth.d@northeastern.edu
"""


from main.Population import Population
from main.Person import Person
from main.ConfigUtil import ConfigUtil
from main.Visualization import Visualization
import  matplotlib.pyplot as plt


class Simulation():
    """
    A class representation of disease spread simulation
    """
    
    def __init__(self, virus, pSize, nDays, name = "Disease Simulation"):
        """
        Constructor
        """
        # params
        self.config = ConfigUtil()
        self.virus = virus
        self.visualization = Visualization()
        
        self.sampleSize = pSize
        self.quarantineRestriction = self.config.getBoolean("Location.Info", "quarantineRestriction")
        self.population = Population("City 1", self.sampleSize, self.virus)
        self.quarantineZone = Population("Quarantine Zone", 0, self.virus)
    
        self.day = 0
        self.nDays = nDays
        self.totalHealthy = 0
        self.totalActiveCase = 0
        self.totalDeath = 0
        self.totalRecovery = 0
        self.name = name
        
    def createInfectiousPerson(self):
        """
        Create an infected object
        
        @return Person
        """
        person = Person()
        person.setHealthStatus(2) # Infected
        person.setInfectedStatus(True) # Set to be infected
        person.setLocation(self.population.assignRandomPosition()) # Assign random position
        person.setAge(25) # Set age 
        person.setAliveStatus(True) # Set to be alive
        person.setPreHealthCondition(True) # Set to have a bad prehealth condition
        person.setDeathRate(0.2) # Assign death rate
        person.setChanceOfGettingInfected(0.2) # Assign chance of getting infected (though already infected)
        person.setInfectedLength(1) # Set the starting day of being infected
        return person
        
    def run(self):
        """
        Main function to run the simulation
        """
        
        print(self.virus.getName() + " Simulation")
        
        # Initialize the plot using matplotlib.pyplot
        plt.ion()
        _, ax = None, None
        if self.quarantineRestriction:
            _, ax = plt.subplots(3, 1)
        else:
            _, ax = plt.subplots(2, 1)
             
        # Susceptible, Infected, Removed (not the typical SIR where R is recovered)
        SIRdata = []
        self.day = 0
        # Run for n days
        while self.day < self.nDays:
            # Create an infectious person here and add into the population
            if self.day == 0:
                # Create an infectious person object and add to the population
                person = self.createInfectiousPerson()
                self.sampleSize+=1 # increase sample size by 1
                self.population.addPerson(person) # Insert the infectious person into a population
            
            else:
                # Update the map
                self.population.updateMap() 
                # If quarantine rule applied, check for infected person and put in quarantine (90% chance of putting the person in quarantine)
                if self.quarantineRestriction:        
                    tempSet = self.population.getInfectedPopulation().copy()
                    for infectedPerson in tempSet:
                        # Assume 15% chance the person who tested are not put into quarantine zone
                        # Source https://thehill.com/changing-america/well-being/medical-advances/491760-3-in-4-americans-say-they-are-self-isolating-in
                        if (self.virus.randomBooleanWeightSelect(0.85, 0.15)) and (self.population.getPerson(infectedPerson).getTestedStatus() == True):
                            self.quarantineZone.addPerson(self.population.getPerson(infectedPerson))
                            self.population.removePerson(infectedPerson)
                    # update quarantine zone
                    self.quarantineZone.updateMap()
            
            # Updates the total number of active cases, death, and remaining healthy individuals 
            self.totalActiveCase = self.population.getNumberOfActiveCases() + self.quarantineZone.getNumberOfActiveCases()
            self.totalDeath = self.population.getNumberOfDeath() + self.quarantineZone.getNumberOfDeath()
            self.totalRecovery = self.population.recoveredPopulationDaily + self.quarantineZone.recoveredPopulationDaily       
            self.totalHealthy = self.sampleSize - (self.totalActiveCase + self.totalDeath)
            if self.day > 0:
                print("Day {} \t Total Cases: {} \t Total Death: {} \t Total Daily Recovery: {}".format(self.day, self.totalActiveCase, self.totalDeath, self.totalRecovery))
                
            # Append the data for day N
            SIRdata.append((self.totalHealthy, self.totalActiveCase, self.totalDeath))
            # Visualize the result
            self.visualization.plotPopulation(ax, SIRdata, self.population, self.quarantineZone, self.quarantineRestriction)
            # Apply the title for the plot
            ax[0].set_title('Susceptible, Infected, Removed Stats')
            ax[1].set_title(self.virus.getName() + ": Day " + str(self.day + 1))
            if self.quarantineRestriction:
                ax[2].set_title("Quarantine/Recovered Zone")
            # Show the graph
            plt.show()
            plt.pause(.5)
            # Clear the previous frame
            ax[0].clear()
            ax[1].clear()
            if self.quarantineRestriction:
                ax[2].clear()
                    
            self.day+=1
        

