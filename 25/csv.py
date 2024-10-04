import arcpy

def readInCSV():
    # Read in .csv, add to .gdb
    stadiums = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/code/25/stadiums.csv"
    # file = open(teams, "r")
    # lines = file.readlines()
    # for line in lines:
    #     tokens = line.split(",")
    #     stadium = tokens[0]
    #     stadium_lat = tokens[1]
    #     stadium_lon = tokens[2]
    #     print("%s, lat: %s, lon: %s" % (stadium, stadium_lat, stadium_lon))
    campus = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/data/modules/25/Campus.gdb"
    arcpy.management.MakeXYEventLayer(stadiums, "lon", "lat", campus + "/Stadiums")    
    # arcpy.FeatureClassToGeodatabase_conversion(stadiums, campus)


def exportGdbToCSV():
    # Read in .gdb, export to .csv
    campus = r"D:\DevSource\Tamu\GeoInnovation\_GISProgramming\data\modules\25\Campus.gdb"
    garages = campus + "/GaragePoints"
    garageFile = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/code/25/garagesFromGdb.csv"
    search = arcpy.da.SearchCursor(garages, field_names=["Name", "SHAPE@XY"])
    file = open(garageFile, "w")
    file.write("GarageName,lon,lat\n")
    for row in search:
        print(row)
        file.write("%s,%s,%s\n" % (row[0], row[1][0], row[1][1]))

def csvToTable():
    stadiums = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/code/25/stadiums.csv"
    campus = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/data/modules/25/Campus.gdb"
    arcpy.TableToTable_conversion(stadiums, campus, "StadiumsTable")

def tableToCsv():
    stadiums = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/code/25/stadiumsFromTable.csv"
    campus = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/data/modules/25/Campus.gdb"
    # arcpy.ConvertTableToCsvFile_locref (campus + "/StadiumsTable", stadiums)
    arcpy.stats.ExportXYv("Structures", "Number;BldgAbbr;BldgName", "COMMA", r"D:\DevSource\Tamu\GeoInnovation\_GISProgramming\code\25\FeatureToCSV.csv", "ADD_FIELD_NAMES")


tableToCsv()
