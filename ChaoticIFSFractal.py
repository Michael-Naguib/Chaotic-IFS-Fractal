#Imports
import matplotlib.pyplot as plt
import numpy as np
import sys
import time
import random
import math
import scipy.stats as stats
import pylab as pl
na = np.array

#Settings recomended 10^4
quantity = int(math.pow(10,4))
initial = np.array([1,1])

#Sets

#fern
barnsleyTransform = [
    [na([[0,0],[0,0.16]]),na([0,0]),0,0.01],
    [na([[0.85,0.04],[0-0.04,0.85]]),na([0,1.6]),0,0.85],
    [na([[0.2,0-0.26],[0.23,0.22]]),na([0,1.6]),0,0.07],
    [na([[0-0.15,0.28],[0.26,0.24]]),na([0,0.44]),0,0.07]
]

#rose like y distribution around 1.6
roseLikeTransform = [
    [na([[0,0],[0,0.16]]),na([0,0]),0,0.01],
    [na([[0.85,0.04],[0-0.04,0.85]]),na([0,1.6]),45,0.85],
    [na([[0.2,0-0.26],[0.23,0.22]]),na([0,1.6]),3,0.10],
    [na([[0-0.15,0.28],[0.26,0.24]]),na([0,0.44]),0,0.04]
]

nsnTransform = [
    [na([[0,0],[0,0.16]]),na([0,0]),0,0.01],
    [na([[0.85,0.04],[0-0.04,0.85]]),na([0,1.6]),60,0.85],
    [na([[0.2,0-0.26],[0.23,0.22]]),na([0,1.6]),5,0.10],
    [na([[0-0.15,0.28],[0.26,0.24]]),na([0,0.44]),0,0.04]
]

#DIRECTLY from stack overflow ALL credit for this function to the author at https://stackoverflow.com/questions/3160699/python-progress-bar
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

#Generalized Affine Transformation: R(Sx) + m    R Rotation matrix S stretch x vector m shift
def affine(x,theta=0,stretch= np.array([[1,1],[1,1]]) ,shift=np.array([0,0])):
    R = np.array([[np.cos(theta),-np.sin(theta)],[np.sin(theta),np.cos(theta)]])
    return np.add(np.matmul(R,np.matmul(stretch,x)), shift.transpose())

#Iterated Function System
def ifs(pointsQuantity,transformations,deterministic=False,initialPoint=np.array([1,1]),pIndex=3,tIndex=2,sIndex=0,shiftIndex=1,):
    allXCord = [(initialPoint[0:1:1].tolist())[0]]
    allYCord = [(initialPoint[1:2:1].tolist())[0]]
    nextPoint = initialPoint
    allProbabilities = []
    for m in transformations:
        allProbabilities.append(m[pIndex])
    for i in range(0,pointsQuantity+1):
        update_progress(round((i/(pointsQuantity+1))*100)/100)
        k = (np.random.choice(len(transformations), 1, p=allProbabilities))[0]
        trans = transformations[k]
        nextPoint = (affine(nextPoint,theta=trans[tIndex],stretch=trans[sIndex],shift=trans[shiftIndex])).transpose()
        allXCord.append(nextPoint.item(0))
        allYCord.append(nextPoint.item(1))
    return allXCord, allYCord

#Calculate the Points
def calcIfs(transformSet):
    print("[Begin] points=%s"%quantity)
    x,y = ifs(quantity,transformSet)
    sys.stdout.flush()
    print("End")
    return x,y

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

def findAverage(allX):
    return sum(allX)/len(allX)

def fractalPlot(x,y,color=(0,0,0)):
    #Plot the points
    plt.title('Chaotic IFS Fractal: Graph')
    plt.xlabel('x-Axis')
    plt.ylabel('y-Axis')
    plt.scatter(x,y,c=color,s=np.pi*3,alpha=0.5)
    plt.show()

def distributionPlot(px,name):
#Find the ratios
    dispx = sorted(px)
    fit = stats.norm.pdf(dispx, np.mean(dispx), np.std(dispx))
    pl.title("%s Ratio Distribution"%name)
    pl.plot(dispx,fit,'-o')
    pl.hist(dispx,normed=True)
    pl.show()

#Run calculations
x = []
y=[]
for i in range(0,1):
    xpart,ypart = calcIfs(barnsleyTransform)
    x.extend(xpart)
    y.extend(ypart)

fractalPlot(x,y,color=(random.random(),random.random(),random.random()))
#rx,ry = findRatios(x,y)
#distributionPlot(rx,"x")
#distributionPlot(ry,"y")

