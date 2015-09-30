# -*- coding: cp1252 -*-
#challenge 2
import arcpy
from arcpy import env
env.workspace = "P:/Python/Data/Exercise05"
fc = "hospitals.shp"
arcpy.AddXY_management(“hospitals.shp”)

#challenge 3
import arcpy
from arcpy import env
env.workspace = "P:/Python/Data/Exercise05"
arcpy.Dissolve_management(“parks.shp”,
“P:/Python/output.gdb/parks_dissolved”, [“PARK_TYPE”], “”, “SINGLE_PART”, “”)

#challenge 4
import arcpy
from arcpy import env
env.workspace = "P:/Python/Data/Exercise05"
if arcpy.CheckExtension(“3DAnalyst”) == “Available”:
    print “3D Analyst available.”
    else:
        print “3D Analyst not available” 
if arcpy.CheckExtension(“NetworkAnalyst”) == “Available”:
    print “Network Analyst available.”
    else:
        print “Network Analyst not available”
if arcpy.CheckExtension(“Spatial”) == “Available”:
    print “Spatial available.”
    else:
        print “Spatial not available”
