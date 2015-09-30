# -*- coding: cp1252 -*-
#challenge 1
import arcpy
from arcpy import env
env.workspace = "P:/Python/Data/Exercise06"
fclist = arcfpy.ListFeatureClasses()
for fc in fclist:
    fcdescribe = arcpy.Describe(fc)
    print “Name: “ + fcdescribe.name
    print “Data type: “ = fcdescribe.dataType
#challenge 2
import arcpy
from arcpy import env
env.workspace = "P:/Python/Data/Exercise06"
arcpy.CreateFileGDB_management(“P:/Python/Data/Exercise06/Results”, “NM.gdb”)
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
    fcdesc = arcpy.Describe(fc)
    arcpy.CopyFeatures_management(fc, “P:/Python/Data/Exercise06/Results/NM.gdb/” + fcdesc.basename)
