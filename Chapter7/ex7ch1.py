"""Write a script that creates a 15,000-meter buffer around features in the
airports.shp feature class classified as an airport and a 7,500-meter buffer around features classified as a seaplane
base. The results should be two separate feature classes, one for each
airport type."""

import arcpy
from arcpy import env
env.workspace = "P:/Python/Data/Exercise07"
fc = "airports.shp"
aCursor = arcpy.da.SearchCursor(fc, ["NAME"], '"FEATURE" = \'Airport\'')                             
afc = arcpy.CreateUniqueName("Results/AirportBuffer.shp")
bCursor = arcpy.da.SearchCursor(fc, ["NAME"], '"FEATURE" = \'Seaplane Base\'')
bfc = arcpy.CreateUniqueName("Results/bBuffer.shp")
arcpy.Buffer_analysis(aCursor, afc, "15000 METERS")
arcpy.Buffer_analysis(bCursor, bfc, "7500 METERS")
