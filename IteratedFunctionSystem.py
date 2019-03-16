'''
# IteratedFunctionSystem
- Code By Michael Sherif Naguib
- license: MIT open source
- Date: 12/20/18
- @University of Tulsa
- Description: a class for creating iterated function systems


## Documentation
- A lot of the code used here was based on the chaotic fractal code... this is more just an storage than anything else...
- more modular code for rapid testing was the key...
### class ```IFS```: (essentially a static class: collection of functions useful for iterated function systems)
#### method (static)```run(self,vector_func,max_points=50000,stop_func=lambda __,_: False,initial_point=np.array([1,1]),status=True)```
- generates a sequence of points and returns the x and y values as a tuple containing np arrays for x and y respectivly ex. (np.array([1]),np.array([2]))
- ```vector_func```: takes a np array of two nums and returns a new array 
- ```stop_func```: is passed number of points computed and the most recent point and should return true to stop or false to contine
- ```max_points```: is the maximum number of points to compute
- ```initial_point```: is the starting poin defaults to value stated above
- ```status```: logs a progress bar indicating how close it is to finishing...
#### method (static) ```affine(self,x_vect,theta=0,stretch= np.array([[1,1],[1,1]]) ,shift=np.array([0,0]))```
- Preforms an affine transformation on a row vector name x_vect
- ```x_vect```: the input vector as a numpy array ex. x_vect = np.array([0,42])
- ```theta```: the angle to rotate the input vector by... NOTE: the stretch array can influence rotation too
- ```stretch```: a matrix to stretch the x_vect by
- ```shift```: is added to the x_vect to shift it...
#### method (static) ```chaoticAffineGenerator(constants)```:
- function takes a set of constants as described below and builds a new probabilistic function that selects based on the groups of constants
- returns that new function so it can be used throught other programs (curried function...)
- ```constants```: is essentially a list of functions in the form: 
```
[
    [
    np.array([[a,b],[c,d]]),    #stretch x and y using this matrix
    np.array([h,k]),            #add this to the vector (shift x and y)
    t,                          #rotate the vector by this angle
    p,                          #probability as a fraction that this function is selected
    ]
    ... etc ...
    another set of constants
]
```
#### ```plot(points_tuple,x_name="x",y_name="y",title="Graph",heat=False)```:
- takes input values and plots them as a scatter plot...
- ```points_tuple```: where the first item is a np array corresponding to x values and the seccond item the y values 
- ```x_name```: the name of the x axis
- ```y_name```: the name of the y axis
- ```title```: the name title of the graph
- ```heat```: if heat is true a heatmap is plotted instead of a scatterplot
#### method (static) ```quickAffine(self,x_vect,stretch= np.array([[1,1],[1,1]]) ,shift=np.array([0,0]))```
- Preforms an affine transformation on a row vector name x_vect BUT does not explicitly calculate rotation... faster
- ```x_vect```: the input vector as a numpy array ex. x_vect = np.array([0,42])
- ```stretch```: a matrix to stretch the x_vect by
- ```shift```: is added to the x_vect to shift it...
#### method (static) ```chaoticQuickAffineGenerator(constants)```:
- function takes a set of constants as described below and builds a new probabilistic function that selects based on the groups of constants
- returns that new function so it can be used throught other programs (curried function...)...
- gains a speed boost by not calculating rotation by theta...
- ```constants```: is essentially a list of functions .... see ```chaoticAffineGenerator``` constants argument
'''

#imports
import numpy as np
import random
import math
import matplotlib.pyplot as plt
import sys
import tqdm

# IFS class
class IFS:
    #Runs the iterated function system:
    @staticmethod
    def run(vector_func,stop_func = lambda __,_: False,max_points=50000,initial_point=np.array([1,1]),status=True):
        #store the computed points: (add edge case in manually)
        x_cord=[initial_point.item(0)]
        y_cord=[initial_point.item(1)]

        #The loop
        prev_point = initial_point
        created_range = tqdm.tqdm(range(1,max_points+1)) if status else range(1,max_points+1)
        for i in created_range:
            if(stop_func(i,prev_point)): # i is the point count
                break
            #otherwise calc the next point
            prev_point = vector_func(prev_point)
            x_cord.append(prev_point.item(0))
            y_cord.append(prev_point.item(1))
        #return the point cords
        return (np.array(x_cord),np.array(y_cord))
    # Affine Transformation: R(Sx) + m    R Rotation matrix S stretch x vector m shift
    @staticmethod
    def affine(x_vect,theta=0,stretch= np.array([[1,1],[1,1]]) ,shift=np.array([0,0])):
        R = np.array([[np.cos(theta),-np.sin(theta)],[np.sin(theta),np.cos(theta)]])
        return np.add(np.matmul(R,np.matmul(stretch,x_vect)), shift.transpose())
    #builds a function based off the constants and returns it... 
    @staticmethod
    def chaoticAffineGenerator(constants):
        #CONSTANTS: the index locaiton of the desired values in each
        PROBABILITY_INDEX=3
        THETA_INDEX=2
        STRETCH_INDEX=0
        SHIFT_INDEX=1
        # Sum Probabilities of Transforms
        allProbabilities = []
        for constant in constants:
            allProbabilities.append(constant[PROBABILITY_INDEX])
        def curriedFunc(x_vector):
            #recalculate this each time...
            probs = allProbabilities
            transformations = constants
            #select a random transformation
            k = (np.random.choice(len(transformations), 1, p=allProbabilities))[0]
            trans = transformations[k]
            #apply it
            return (IFS.affine(x_vector,theta=trans[THETA_INDEX],stretch=trans[STRETCH_INDEX],shift=trans[SHIFT_INDEX])).transpose()
        return curriedFunc
    #plots the points
    @staticmethod
    def plot(points_tuple,x_name="x",y_name="y",title="Graph",heat=False):
        #setup
        x=points_tuple[0]
        y =points_tuple[1]
        if heat:
            heatmap, xedges, yedges = np.histogram2d(points_tuple[0], points_tuple[1], bins=1000)
            extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
            plt.clf()
            plt.imshow(heatmap.T, extent=extent, origin='lower')
            plt.show()
        else:
            plt.title(title)
            plt.xlabel(x_name)
            plt.ylabel(y_name)
            #Plot the points
            plt.scatter(points_tuple[0], points_tuple[1], c=[(random.random(),random.random(),random.random())], s=np.pi * 3, alpha=0.5)
            plt.show()

    #quick Affine: rotation matrix often not used so cut those operations out to improve speed
    @staticmethod
    def quickAffine(x_vector,stretch= np.array([[1,1],[1,1]]),shift=np.array([0,0])):
        return np.add(np.matmul(stretch,x_vector), shift.transpose())
    #quick affine: ignores calculating rotation matrix: 
    @staticmethod
    def chaoticQuickAffineGenerator(constants):
        #CONSTANTS: the index locaiton of the desired values in each
        PROBABILITY_INDEX=3
        #THETA_INDEX=2 #Quick affine does not use rotation matrix....
        STRETCH_INDEX=0
        SHIFT_INDEX=1
        # Sum Probabilities of Transforms
        allProbabilities = []
        for constant in constants:
            allProbabilities.append(constant[PROBABILITY_INDEX])
        def curriedFunc(x_vector):
            #recalculate this each time...
            probs = allProbabilities
            transformations = constants
            #select a random transformation
            k = (np.random.choice(len(transformations), 1, p=allProbabilities))[0]
            trans = transformations[k]
            #apply it
            return (IFS.quickAffine(x_vector,stretch=trans[STRETCH_INDEX],shift=trans[SHIFT_INDEX])).transpose()
        return curriedFunc
#Begin test
if __name__ == "__main__":
    print("A test of the Iterated function System:")
    # Serenpenski Triangle
    triangle = [
        [np.array([[0.5,0],[0,0.5]]),np.array([0,0]),0,0.33],
        [np.array([[0.5,0],[0,0.5]]),np.array([0.5,0]),0,0.33],
        [np.array([[0.5,0.0],[0.0,0.5]]),np.array([0.25,0.433]),0,0.34]
    ]

    #create the curried function off of the constants or supply a function yourself that takes np.array and returns np.array
    func = IFS.chaoticAffineGenerator(triangle)

    #create the stopping function: stop if the quantity of points is 10000 
    #do_stop = lambda quant,point: quant==1000

    #do the calculation
    point_data = IFS.run(func)#     ,stop_func=do_stop)
    
    #display the data
    IFS.plot(point_data)
