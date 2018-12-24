# Chaotic IFS Fractal
This is a Fractal generator based upon the work done by Michael Barnsley
and is implemented in Numpy

## Dependancies 
+ matplotlib.pyplt
+ numpy
+ pylab
+ scipy.stats
+ tqdm
+ pprint
+ random
+ math
+ sys
+ time
+ pylab (optional)

## Predefined Transformations
+ ```barnsley```: barnsley fern as researched by michael barnsley
+ ```triangle```: A serinpenski triangle
+ ```goldenDragon```: the golden dragon spiral based off of the golden ratio
+ ```tree```: a Symetric Binary tree with no stems scale 0.7 rotation 9 deg
+ ```pentadentrite```: a slice of a branched pentagonal fractal which is a fractal itself
+ ```koch```: Koch curve (approximate)
+ ```branch```: golden dragon rotated by the angles of the triangle conecting the golden dragon's attractors
+ ```rose```: a conch shell like spiraling rose - a neat constant set found...
+ ```nsn```: A galaxy like spiral ascending

## Features
+ Terminal Interface for configuring a Chaotic Iterated Function System: ```python ChaoticIFSFractal2.0.py```

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
#### ```plot(points_tuple,x_name="x",y_name="y",title="Graph")```:
- takes input values and plots them as a scatter plot...
- ```points_tuple```: where the first item is a np array corresponding to x values and the seccond item the y values 
- ```x_name```: the name of the x axis
- ```y_name```: the name of the y axis
- ```title```: the name title of the graph
'''


