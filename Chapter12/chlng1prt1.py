import arcpy  
      
def countstringfields(layer = "streets.shp"):
    arcpy.env.workspace = "P:/Python/Data/Exercise12"
    
    if layer == None:  
        return None  
      
    n = 0  
    for field in arcpy.ListFields(layer):  
        if field.type == "String":  
            n += 1  
      
    return n  
