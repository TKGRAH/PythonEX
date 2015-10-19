def chlng1():
    import arcpy
    arcpy.CheckOutExtension("spatial")
    from arcpy import env
    env.workspace = "P:/Python/Data/Exercise09"
    outraster = arcpy.sa.Slope("elevation")
    desc = arcpy.Describe(outraster)
    print desc.permanent
    outraster.save("slope")
    from arcpy.sa import *
    outraster2 = Aspect("elevation")
    outraster2.save("aspect")
    elevraster = arcpy.Raster("elevation")
    outraster3 = elevraster * 3.281
    outraster3.save("elev_ft")
    slope = arcpy.sa.Slope(elevraster)
    goodslope = 5 < slope < 20 and 150 < slope < 270
    goodfinal = goodslope
    goodfinal.save("final")

    if arcpy.CheckExtension("spatial") == "Available":
        arcpy.CheckOutExtension("spatial")
        myremap = RemapValue([[41], [42], [43]])
        outreclass = Reclassify("landcover.tif", "VALUE", myremap, "NODATA")
        outreclass.save("lc_recl")
        arcpy.CheckInExtension("spatial")
    else:
        print "Spatial Analyst license is not available."
    
