def chlng2():
    import arcpy, os, sys
    from arcpy import env
    env.workspace = "P:/Python/Data/Exercise09"
    outpath = "P:/Python/Data/Exercise09/Results/"
    outname = "rasters.gdb"
    arcpy.CreateFileGDB_management(outpath, outname)
    
    rasters = arcpy.ListRasters("*", "TIFF")
    for raster in rasters:
        rastdesc = arcpy.Describe(raster)
        rastname = rstdesc.basename
        arcpy.CopyRaster_management(raster, "P:/Python/Data/Exercise09/Results/newdata.gdb/" + rastname)
