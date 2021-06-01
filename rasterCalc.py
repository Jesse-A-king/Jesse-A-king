##################################################################
#
# This script takes two input Ascii grid files representing
# rasters , performs a user-selected map algebra operation on
# them, and writes the result to a Ascii grid file
#
# Author: Jess King
# 
# ----------------------------------------------------------------

##################################################################
# +++++++++++++++++++++++ HELPER SECTION +++++++++++++++++++++++ #
##################################################################

# imports
import sys


# header(asciiFile) -> header (list of strings)
def header(inAscii):
    f = open(inAscii, 'r')
    raw = f.readlines()
    f.close()
    header = raw[:6]
    return header

# for reading grid bodies made up of int numbers
def bodyInt(inAscii):
    f = open(inAscii, 'r')
    raw = f.readlines()
    f.close()
    body = raw[6:]
    array2D = []
    for line in body:
        line = line.strip()
        line = line.split()
        line = map(int,line)
        row = list(line)
        array2D.append(row)
    return array2D

# for reading grid bodies made up of float numbers
def bodyFloat(inAscii):
    """ bodyFloat(asciiFile) -> 2D Array (list) of floats """
    f = open(inAscii, 'r')
    raw = f.readlines()
    f.close()
    body = raw[6:]
    array2D = []
    for line in body:
        row = list(map(float,line.strip().split()))
        array2D.append(row)
    return array2D

# to write grids to a file
def toAscii(name, header, body):
    # open a file
    fname = name + ".txt"
    print("Creating output ASCII file " + fname)
    f = open(fname, 'w')
    # save header
    f.writelines(header)
    # create the body content
    contentString = ""
    for row in body:
        line = ""
        for cell in row:
            line = line + str(cell) + " "
        line = line[:-1] + "\n"
        contentString = contentString + line

    # removes the last new line character
    contentString = contentString[:-1]

    # saving body
    f.write(contentString)
    f.close()
    print("... Done!")

####################################
# New Functions
####################################

def printGrid(ras1):
    print("------"*4)
    for i in ras1:
        print(i)
    print("------"*4)

    

def checkSize(ras1, ras2):
    row1 = len(ras1)
    row2 = len(ras2)
    col1 = len(ras1[0])
    col2 = len(ras2[0])
    rowcheck = 0
    colcheck = 3
    sizecheck = 0
    if row1 == row2:
        rowcheck = 1
    if col1 == col2:
        colcheck = 1
    if rowcheck == colcheck:
        sizecheck = 1 
        print("raster sizes are the same")
    else:
        print("Raster sizes are not the same, cannot procede with calculations")
        escape
    return sizecheck

def gridSum(ras1, ras2):
    sums= []
    for i in range(0,len(ras1)):
        sumgrid = []
        for j in range(0,len(ras2[0])):
            s = 0
            for k in range(len(ras1[0])):                
                s = ras1[i][j]+ras2[i][j]
            sumgrid.append(s)
        sums.append(sumgrid)
    return sums
    
def gridDiff(ras1, ras2):
    difs = []
    for i in range(0,len(ras1)):
        difgrid = []
        for j in range(0,len(ras2[0])):
            s = 0
            for k in range(len(ras1[0])):                
                s = ras1[i][j]-ras2[i][j]
            difgrid.append(s)
        difs.append(difgrid)
    return difs

def gridMult(ras1, ras2):
    mult = []
    for i in range(0,len(ras1)):
        mulgrid = []
        for j in range(0,len(ras2[0])):
            s = 0
            for k in range(len(ras1[0])):                
                s = ras1[i][j]*ras2[i][j]
            mulgrid.append(s)
        mult.append(mulgrid)
    return mult

def gridDiv(ras1, ras2):
    div = []
    for i in range(0,len(ras1)):
        difgrid = []
        for j in range(0,len(ras2[0])):
            s = 0
            for k in range(len(ras1[0])):
                if ras2[i][j] == 0:
                    s = -9999
                else:
                    s = ras1[i][j]/ras2[i][j]
            difgrid.append(round(s,2))
        div.append(difgrid)
    return div

def fakeNDVI(ras1, ras2):
    indi = []
    diff = gridDiff(ras1,ras2)
    sums = gridSum(ras1,ras2)
    for i in range(0,len(diff)):
        indigrid = []
        for j in range(0,len(sums[0])):
            s = 0
            for k in range(len(diff[0])):
                if sums[i][j] == 0:
                    s = -9999
                else:
                    s = diff[i][j]/sums[i][j]
            indigrid.append(round(s,2))
        indi.append(indigrid)
    return indi

        
#############################################################
# Invocation Section
#############################################################
    
grid1Path = "rasterA.txt"
grid2Path = "rasterB.txt"

#Uncomment lines of code below for testing

grid1 = bodyFloat(grid1Path)

printGrid(grid1)

grid2 = bodyFloat(grid2Path)

printGrid(grid2)

checkSize(grid1, grid2)
gridSum(grid1, grid2)
gridDiff(grid1, grid2)
gridMult(grid1, grid2)
gridDiv(grid1, grid2)
fakeNDVI(grid1, grid2)
print("Operation choices:")
print("<1> Sum")
print("<2> Difference")
print("<3> Multiply")
print("<4> Divide")
print("<5> NDVI")
print()

operationChoice = input("Pick an operation from the choices above: ")
print("")
resGrid = ["I am an empty list"]
if operationChoice == '1':
    resGrid = gridSum(grid1, grid2)
elif operationChoice == '2':
    resGrid = gridDiff(grid1, grid2)
elif operationChoice == '3':
    resGrid = gridMult(grid1, grid2)
elif operationChoice == '4':
    resGrid = gridDiv(grid1, grid2)
elif operationChoice == '5':
    resGrid = fakeNDVI(grid1, grid2)

printGrid(resGrid)
print ("")
resHeader = header(grid1Path)

outputName = input("Specify the output grid file name (minus file extension): ")

toAscii(outputName, resHeader, resGrid)
            
                
                
                    
                           
        
        

    
            
                

        
