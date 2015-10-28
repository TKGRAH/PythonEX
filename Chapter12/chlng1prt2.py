import sys
sys.path.append(r"P:/gitprojects/PythonEX/Chapter12")

import chlng1prt1

streetsLayer = arcpy.mapping.Layer("streets")
#saying "streets" is an invalid data source. Tried different methods, same error.
#Not sure what is wrong.
numberOfFieldsTypeString = chlng1prt1.countstringfields(streetsLayer)
del streetsLayer

print numberOfFieldsTypeString
