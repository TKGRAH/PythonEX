import arcpy
import fileinput
import string
import os
from arcpy import env
env.workspace = "C:/EsriPress/Python/Data/Exercise08"
env.overwriteOutput = True
outpath = "P:/Python/Data/Exercise08"
newfc = "Results/square.shp"
arcpy.CreateFeatureclass_management(outpath, newfc, "square")
parts = line.split(" ")
id = parts[0]
coord1 = "({0})
coord2 =
coord3 =
coord4 =
cursor = arcpy.da.InsertCursor(newfc, ["SHAPE@"])
array = arcpy.Array()
for line in fileinput.input(infile):
    ID, X, Y = string.split(line," ")
    array.add(arcpy.Point(X, Y))
cursor.insertRow([arcpy.Polyline(array)])
fileinput.close()
del cursor
