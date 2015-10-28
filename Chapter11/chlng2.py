def chlng2():
    import arcpy
    from arcpy import env
    env.workspace = "P:/Python/Data/Exercise09"
    raster = arcpy.Raster("landcover.tif")
    desc = arcpy.Describe(raster)
    x = desc.MeanCellHeight
    y = desc.MeanCellWidth
    spatialref = desc.spatialReference
    units = spatialref.linearUnitName
    print "Cells are " + str(x) + " by " + str(y) + " " + units + "."
