def chlng1():
    import arcpy
    from arcpy import env
    env.workspace = "P:/Python/Data/Exercise07"
    fc = "airports.shp"
    rows = arcpy.SearchCursor(fc)
    fields = arcpy.ListFields(fc)
    for field in fields:
        if field.name == "NAME":
            for row in rows:
                print "Name = {0}".format(row.getValue(field.name))
