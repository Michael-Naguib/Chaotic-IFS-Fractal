'''
# ChaoticIFSBuilder
- Code By Michael Sherif Naguib
- license: MIT open source
- Date: 12/23/18
- @University of Tulsa
- Description: This file is a terminal GUI for ChaoticIFSFractal2.0.py which creates custom IFS Fractals...
'''
import numpy as np
import pprint
class ChaoticIFSBuilder():
    def __init__(self,predefined_constants_dict,default_constant_name):
        #Internal
        self.constants = predefined_constants_dict
        self.defult_constant_name  = default_constant_name
    def run(self):
        #ask...
        self.showTitle()
        constant_selected = self.getSetConstants()
        print("-------------------------- Selected Set -----------------------------")
        pprint.pprint(constant_selected)
        quant = self.askPointQuant()

        #return
        return (constant_selected,quant)
    #title
    def showTitle(self):
        print("---------------------------------------------------------------------")
        print("Welcome To Chaotic IFS Fractal Generator by Michael Naguib 12/23/18")
    #asks for a transform...
    def askForTransform(self,indexd = ""):
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
    #asks the user to create a function set
    def buildSetConstants(self):
        print("-------------------------------------------")
        print("     Stretch Transformations Matrix Form: ")
        print("       |a b|   ")
        print("       |c d|   ")
        print("               ")
        print("     Specify Probaility as fraction:")
        print("     Note! all fractions must add up to 1")
        print("     example: type 0.5 for 50% ")
        counter = 0
        allTransForms = []
        while True:
            allTransForms.append(self.askForTransform(indexd=counter+1))
            counter +=1
            c = input("Add another Transform? [y/n]: ")
            if c[0:1].lower() == "n":
                break
        print("------------- All Transforms Set ----------")
        return allTransForms
    #gets the constants
    def getSetConstants(self):
        while True:
            print("---------------------------------------------------------------------")
            print("     The available constant sets are: ")
            print("     "+str(self.constants.keys()))
            print("                         ")
            print("     The default selected set is {0}".format(self.defult_constant_name))
            res = input("  Use default set (d), create a new set (c), or select from the above (s): [d/c/s]")
            if res[0:1].lower() == "d":
                return self.constants[self.defult_constant_name]
            elif res[0:1].lower() == "c":
                return self.buildSetConstants()
            elif res[0:1].lower() == "s":
                return self.constants[str(input("  Please type the name of the set:")).lower()]
            else:
                continue#loop
    #gets Point quantity
    def askPointQuant(self):
         print("---------------------------------------------------------------------")
         return int(input("    Point Quantity (recomended 50000):"))

        