"""
@author: Darasy Reth
@email: reth.d@northeastern.edu
"""


import numpy as np
from main.Population import Population


class Visualization:
    """
    A class representation of data visualization
    """
    healthyColorRep = "lime"
    infectedColorRep = "red"
    deathColorRep = "darkgrey"
    
    
    def getScatterComponents(self, population : Population):
        """
        A method to get the x points, y points and their corresponding color representation
        """
        if population:
            xPoints = [None] * population.getNumberOfPopulation() # X axis of each people
            yPoints = [None] * population.getNumberOfPopulation() # Y axis of each people
            colorGroups = [None] * population.getNumberOfPopulation() # Color representation of each people
            
            i = 0
            for personID in population.getPopulation():
                people = population.getPerson(personID)
                # Separate colors and locations for the agents
                loc = people.getLocation()
                healthStatus = people.getHealthStatus()
                # Store people's location and health status by assigning the representing color
                xPoints[i] = loc[0] 
                yPoints[i] = loc[1]
                colorGroups[i] = self.healthyColorRep # Healthy or immune 
                if healthStatus == 2: colorGroups[i] = self.infectedColorRep # Infected
                if healthStatus == 3: colorGroups[i] = self.deathColorRep # Death
                i+=1   
            return xPoints, yPoints, colorGroups
    
        
    
    def plotPopulation(self, ax, SIRdata, population : Population, quarantineZone = None, quarantineRestriction = False):
        """
        A method to plot the population based on their health status (healthy/immune, infected, dead)
        """
        # General population
        xPoints, yPoints, colorGroups = self.getScatterComponents(population)    
        # Quarantine zone    
        if quarantineRestriction:
            xQPoints, yQPoints, colorQGroups = self.getScatterComponents(quarantineZone)

        
        # Scatter the population
        ax[1].scatter(xPoints, yPoints, c=colorGroups)
        # Set the boundary on the graph far enough to show the person object fully otherwise can cut in half if they're on the edge. 
        ax[1].set_xlim(-0.1, 1.1)
        ax[1].set_ylim(-0.1, 1.1)
        # Scatter the quarantine population  
        if quarantineRestriction:      
            ax[2].scatter(xQPoints, yQPoints, c=colorQGroups)
            ax[2].set_xlim(-0.1, 1.1)
            ax[2].set_ylim(-0.1, 1.1)
        
        # Create x_axis
        numberOfDays = len(SIRdata)
        xAxis = range(numberOfDays)
        # Get the total number of population from booth population and quarantine
        totalNumberOfPopulation = population.getNumberOfPopulation()
        if quarantineRestriction:
            totalNumberOfPopulation += quarantineZone.getNumberOfPopulation()
        # Infected and Death distributions
        infectedDist = [None] * numberOfDays
        deadDist = [None] * numberOfDays
        j = 0
        for i in SIRdata:   
            infectedDist[j] = i[1] /totalNumberOfPopulation
            deadDist[j] = i[2] / totalNumberOfPopulation
            j+=1
        # Convert to Numpy array for plotting
        infectedDist = np.array(infectedDist)
        deadDist = np.array(deadDist)
        # Create stacked color plot based on population proportions
        start, end = infectedDist + deadDist, 1
        ax[0].fill_between(xAxis, start, end, facecolor = self.healthyColorRep, label = 'Susceptible')
        start, end = deadDist, infectedDist + deadDist
        ax[0].fill_between(xAxis, start, end, facecolor = self.infectedColorRep, label = 'Infected')
        start, end = 0, deadDist
        ax[0].fill_between(xAxis, deadDist, facecolor=self.deathColorRep, label = 'Removed') 
        ax[0].legend()
               