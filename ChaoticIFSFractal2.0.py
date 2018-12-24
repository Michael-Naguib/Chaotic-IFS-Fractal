'''
# ChaoticIFSFractal2.0
- Code By Michael Sherif Naguib
- license: MIT open source
- Date: 12/20/18
- @University of Tulsa
- Description: VERSION 2.0 of Chaotic IFS fractal..
        Updates: class IFS to store IFS tool functions
        focus: rapid devlopment and testing while maintaining simple usage...
'''
#imports
from IteratedFunctionSystem import IFS
from ChaoticIFSBuilder import ChaoticIFSBuilder
from constants import constants
import numpy as np
import tqdm

#Iterated Function system:
if __name__=="__main__":

    #a gui for asking the user for function settings
    newSystem = ChaoticIFSBuilder(constants,"goldendragon")
    settings = newSystem.run()
    function_set = settings[0]
    points_quantity = settings[1]
    speedup_mode = settings[2]

    #Setup the IFS (SPEEDUP does not take into account theta and instead asks theta to be calculated into the stretch matrix beforehand)
    if(speedup_mode):
        func = IFS.chaoticQuickAffineGenerator(function_set)
    else:
        func = IFS.chaoticAffineGenerator(function_set)

    #Preform the IFS calculations...
    point_data = IFS.run(func,max_points=points_quantity)
  
    #display the data
    IFS.plot(point_data)
    
    '''~ Predefined Constants ~: constants["constant name here"]
        barnsleyTransform
        roseLikeTransform
        nsnTransform
        triangle
        goldenDragon
        symetricBinaryTree
        branch
        pentadentrite
        koch
        ... more...
        note some may not work with chaoticQuickAffineGenerator
        as it does not preform matrix calculation for rotation...
    
    #create the curried function off of the constants
    func = IFS.chaoticAffineGenerator(constants["tree"])

    #Set the number of points to compute
    POINTS_QUANTITY= 100000

    #do the calculation... (note log status defaults true)
    point_data = IFS.run(func,max_points=POINTS_QUANTITY)
    
    #display the data
    IFS.plot(point_data)
    '''

