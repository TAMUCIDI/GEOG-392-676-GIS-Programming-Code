# import arcpy

# # Define our geodatabase
# campus = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/data/modules/20/Campus.gdb"
# # Define the fields we want
# fields = ['Name', 'LotType', 'LotName']
# # Define our search cursor 
# searchCursor = arcpy.da.SearchCursor(campus + "/GaragePoints", fields)
# for row in searchCursor:
#     print(u'{0}, {1}, {2}'.format(row[0], row[1], row[2]))

# del searchCursor


import arcpy

# Define our geodatabase
campus = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/data/modules/20/Campus.gdb"
# Define the fields we want
fields = ['Name', 'LotType', 'LotName']
# Define our search cursor 
searchCursor = arcpy.da.SearchCursor(campus + "/GaragePoints", fields)
try:
    row = next(searchCursor)
    while row:
        print(u'{0}, {1}, {2}'.format(row[0], row[1], row[2]))
        row = next(searchCursor)
except StopIteration:
    print("No more records")

del searchCursor
