import arcpy

def geoJSONToGdb():
    # Read geojson, export to geodatabase
    teams = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/code/25/teams.csv"
    file = open(r"D:\DevSource\Tamu\GeoInnovation\_GISProgramming\code\25\outputgeojson.json", "r")
    geojson = file.read()
    geometry = arcpy.AsShape(geojson)
    # print(geojson)


def exportGdbToGeoJSON():
    # Export geodatabase to geojson
    campus = r"D:\DevSource\Tamu\GeoInnovation\_GISProgramming\data\modules\25\Campus.gdb"
    output = r"D:\DevSource\Tamu\GeoInnovation\_GISProgramming\code\25\outputgeojson.json"
    arcpy.FeaturesToJSON_conversion(campus + "/GarageParking", output, format_json=False, geoJSON=True)


geoJSONToGdb()
