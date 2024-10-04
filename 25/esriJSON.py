import arcpy

def esriJsonToGdb():
    # Read in .csv, add to .gdb
    campus = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/data/modules/25/Campus.gdb"
    arcpy.JSONToFeatures_conversion(r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/code/25/testjson.json", campus + "/TestJSON")


def gdbToEsriJson():
    # Read in .gdb, export to .csv
    campus = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/data/modules/25/Campus.gdb"
    arcpy.FeaturesToJSON_conversion(campus + "/GarageParking", "C:/tmp/ArcGISPython/garage.json", format_json=True)
    

gdbToEsriJson()
