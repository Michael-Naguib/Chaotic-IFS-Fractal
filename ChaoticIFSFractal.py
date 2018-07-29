# ======================= Imports ==============================================
print("Getting imports")
import matplotlib.pyplot as plt
import numpy as np
import sys
import time
import random
import math
import scipy.stats as stats
import pylab as pl
na = np.array

# ========================== Predefined Transformations =======================
# Predefined Transformations: [MATRIX as [[A,B],[C,D]], SHIFTS as [X,Y], ROTATION ,PROBABILITY]
# Fern
barnsleyTransform = [
    [na([[0,0],[0,0.16]]),na([0,0]),0,0.01],
    [na([[0.85,0.04],[0-0.04,0.85]]),na([0,1.6]),0,0.85],
    [na([[0.2,0-0.26],[0.23,0.22]]),na([0,1.6]),0,0.07],
    [na([[0-0.15,0.28],[0.26,0.24]]),na([0,0.44]),0,0.07]
]
# Rose
roseLikeTransform = [
    [na([[0,0],[0,0.16]]),na([0,0]),0,0.01],
    [na([[0.85,0.04],[0-0.04,0.85]]),na([0,1.6]),45,0.85],
    [na([[0.2,0-0.26],[0.23,0.22]]),na([0,1.6]),3,0.10],
    [na([[0-0.15,0.28],[0.26,0.24]]),na([0,0.44]),0,0.04]
]
# Galaxy
nsnTransform = [
    [na([[0,0],[0,0.16]]),na([0,0]),0,0.01],
    [na([[0.85,0.04],[0-0.04,0.85]]),na([0,1.6]),60,0.85],
    [na([[0.2,0-0.26],[0.23,0.22]]),na([0,1.6]),5,0.10],
    [na([[0-0.15,0.28],[0.26,0.24]]),na([0,0.44]),0,0.04]
]
# Serenpenski Triangle
triangle = [
    [na([[0.5,0],[0,0.5]]),na([0,0]),0,0.33],
    [na([[0.5,0],[0,0.5]]),na([0.5,0]),0,0.33],
    [na([[0.5,0.0],[0.0,0.5]]),na([0.25,0.433]),0,0.34]
]
# Golden Dragon
goldenDragon = [
    [na([[0.62367,0-0.40337],[0.40337,0.62367]]),na([0,0]),0,0.5],
    [na([[0-0.37633,0-0.40337],[0.40337,0-0.37633]]),na([0.5,0]),0,0.5]
]
# Golden Dragon Variant Branch
branch=[
    [na([[0.62327,0-0.40337],[0.40337,0.62327]]),na([0,0]),32.8938,0.5],
    [na([[0-0.37633,0-0.40337],[0.40337,0-0.37633]]),na([1,0]),133.014178,0.5]
]
# Binary Tree
symetricBinaryTree = [
    [na([[0.7,0],[0,0.7]]),na([0,1]),9,0.33],
    [na([[0.7,0],[0,0.7]]),na([0,1]),0-9,0.33],
    [na([[1,0],[0,1]]),na([0,0]),0,0.34]
]
# Pentadentrite
pentadentrite=[
    [na([[0.341,0-0.071],[0.071,0.341]]),na([0,0]),0,0.17],
    [na([[0.038,0-0.346],[0.346,0.038]]),na([0.341,0.071]),0,0.17],
    [na([[0.341,0-0.071],[0.071,0.341]]),na([0.379,0.418]),0,0.17],
    [na([[0-0.234,0.258],[0-0.258,0-0.234]]),na([0.720,0.489]),0,0.17],
    [na([[0.173,0.302],[0-0.302,0.173]]),na([0.486,0.231]),0,0.16],
    [na([[0.341,0-0.071],[0.071,0.341]]),na([0.659,0-0.071]),0,0.16]
]
# Koch Curve
koch=[
    [na([[0.3,0],[0,0.3]]),na([0,0]),0,0.25],
    [na([[0.16,0-0.23],[0.23,0.16]]),na([0.3,0]),0,0.25],
    [na([[0.16,0.23],[0-0.23,0.16]]),na([0.5,0.23]),0,0.25],
    [na([[0.3,0],[0,0.3]]),na([0.6,0]),0,0.25]
]
# Make predefined easier
allIFS = {}
allIFS["barnsley"] = barnsleyTransform
allIFS["rose"] = roseLikeTransform
allIFS["nsn"] = nsnTransform
allIFS["triangle"] = triangle
allIFS["goldendragon"] = goldenDragon
allIFS["tree"]= symetricBinaryTree
allIFS["branch"]=branch
allIFS["penta"]=pentadentrite
allIFS["koch"]=koch


# ============================================== GUI ==========================================
# Asks the user to specify constants of a Transform one time
def askForTransform(indexd = ""):
    print("-------------- Transform %s ---------------"%indexd)
    a = float(input("Enter A: "))
    b = float(input("Enter B: "))
    c = float(input("Enter C: "))
    d = float(input("Enter D: "))
    xs = float(input("Enter X-Shift: "))
    ys = float(input("Enter Y-Shift: "))
    r =float(input("Enter rotation theta deg: "))
    p = float(input("Enter Probability: "))
    return [np.array([[a,b],[c,d]]),np.array([xs,ys]),r,p]

# Gui for configuring IFS and Transforms
def buildSystem(predefinedSet=barnsleyTransform,allSets=allIFS):
    print("---------------------------------------------------------------------")
    print("Welcome To Chaotic IFS Fractal Generator by Michael N.")
    print("---------------------------------------------------------------------")
    print("Please Provide transformations in the following form:")
    print("  a b   for Stretch       ")
    print("  c d                     ")
    print("ALL p % as a FRACTION must add up to 1 !!! use nice numbers please ex. type 0.5  for 50% ")
    print("Available Presets %s" % allSets.keys())
    print("RECCOMENDED points Quantity: 50000")
    print("--------------------------------------------")
    pointsQuantity = int(input("Number of Points: "))

    usePredefined = str(input("Use Predefined Set? [y/n/name]: "))
    if usePredefined !="n":
        willusethisset = predefinedSet
        if(usePredefined != "y"):
            willusethisset = allSets[str(usePredefined)]
        print("Using this as the set: it may look different...")
        print(str(willusethisset))
        print("--------------------------------------------")
        return willusethisset,pointsQuantity
    print("--------------------------------------------")
    counter = 0
    allTransForms = []
    while True:
        allTransForms.append(askForTransform(indexd=counter+1))
        counter +=1
        c = input("Add another Transform? [y/n]: ")
        if c == "n":
            break
    print("--------------------- All Transforms Set ---------------------------")
    return allTransForms,pointsQuantity

# Progress Bar: DIRECTLY from stack overflow ALL credit for this function to the author at https://stackoverflow.com/questions/3160699/python-progress-bar
def update_progress(progress):

    barLength = 10 # Modify this to change the length of the progress bar
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
        status = "Done...\r\n"
    block = int(round(barLength*progress))
    text = "\rPercent: [{0}] {1}% {2}".format( "#"*block + "-"*(barLength-block), progress*100, status)
    sys.stdout.write(text)
    sys.stdout.flush()


# =================================== Calculations ============================================

# Affine Transformation: R(Sx) + m    R Rotation matrix S stretch x vector m shift
def affine(x,theta=0,stretch= np.array([[1,1],[1,1]]) ,shift=np.array([0,0])):
    R = np.array([[np.cos(theta),-np.sin(theta)],[np.sin(theta),np.cos(theta)]])
    return np.add(np.matmul(R,np.matmul(stretch,x)), shift.transpose())

# Iterated Function System
def ifs(pointsQuantity,transformations,initialPoint=np.array([1,1]),pIndex=3,tIndex=2,sIndex=0,shiftIndex=1,):
    # pIndex: index of the proability in transformations
    # tIndex:

    # Point setup &  storage
    allXCord = [(initialPoint[0:1:1].tolist())[0]]
    allYCord = [(initialPoint[1:2:1].tolist())[0]]
    nextPoint = initialPoint

    # Sum Probabilities of Transforms
    allProbabilities = []
    for m in transformations:
        allProbabilities.append(m[pIndex])

    #Run the calculation
    for i in range(0,pointsQuantity+1):
        update_progress(round((i/(pointsQuantity+1))*100)/100)

        # Select random set based on probability set
        k = (np.random.choice(len(transformations), 1, p=allProbabilities))[0]
        trans = transformations[k]

        # Calculate the next point
        nextPoint = (affine(nextPoint,theta=trans[tIndex],stretch=trans[sIndex],shift=trans[shiftIndex])).transpose()

        # Store the Cords.
        allXCord.append(nextPoint.item(0))
        allYCord.append(nextPoint.item(1))

    return allXCord, allYCord

#Calculate the Points
def calcIfs(transformSet,quantity=5* int(math.pow(10,4))):
    print("[Beginning Calculation] points=%s"%quantity)
    x,y = ifs(quantity,transformSet)
    sys.stdout.flush()
    print("End")
    return x,y


# ======================================== Statistics =========================================

#Find Ratio between  x+1 to x
def findRatios(x,y):
    #calculate the consecutive ratios:
    allXRatios = []
    allYRatios = []
    for i in range(0,len(x)-1):
        if (x[i] != 0) & (y[i] !=0):
            ratioX = x[i+1]/x[i]
            ratioY = y[i+1]/y[i]
            allXRatios.append(ratioX)
            allYRatios.append(ratioY)
            #print("For item X-ratio: %s  Y-ratio: %s"%(str(ratioX),str(ratioY)))
    return allXRatios,allYRatios

# Average: average of items in the np array
def findAverage(allX):
    return sum(allX)/len(allX)

# Plot Scatter: cords x against y
def fractalPlot(x,y,color=(0,0,0),pointByPoint=False):
    plt.title('Chaotic IFS Fractal: Graph')
    plt.xlabel('x-Axis')
    plt.ylabel('y-Axis')
    #Plot the points
    if pointByPoint:
        plt.ion()
        for i in range(0,len(x)):
            plt.scatter(x[i], y[i], c=color, s=np.pi * 3, alpha=0.5)
            plt.pause(0.0001)
        while True:
            plt.pause(0.05)
    else:
        plt.scatter(x,y,c=color,s=np.pi*3,alpha=0.5)
        plt.show()

# Plot Histogram: the ratios in the list px
def distributionPlot(px,name=""):
#Find the ratios
    dispx = sorted(px)
    fit = stats.norm.pdf(dispx, np.mean(dispx), np.std(dispx))
    pl.title("%s Ratio Distribution"%name)
    pl.plot(dispx,fit,'-o')
    pl.hist(dispx,normed=True)
    pl.show()


# ==================================== Run the Calculations ===================================
if __name__ == "__main__":
    # Storage
    x = []
    y=[]

    # Run one St of calculations
    for i in range(0,1):
        transformsU,quantity = buildSystem()
        xpart,ypart = calcIfs(transformsU)
        x.extend(xpart)
        y.extend(ypart)

    # Plot the set of calculations
    fractalPlot(x,y,color=(random.random(),random.random(),random.random()),pointByPoint=False)

    # Statistical Info
    rx,ry = findRatios(x,y)
    s = []
    for i in range(0,len(rx)):
        s.append(math.sqrt(math.pow(x[i],2) + math.pow(y[i],2)))
    distributionPlot(s,"Slope length or ratio")
    distributionPlot(rx,"x")
    distributionPlot(ry,"y")

