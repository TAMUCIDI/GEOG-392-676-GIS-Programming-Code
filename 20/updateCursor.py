# import arcpy

# # Define our geodatabase
# campus = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/data/modules/20/Campus.gdb"
# # Define the fields we want
# fields = ['Name', 'LotType', 'LotName']
# # Define our search cursor 
# updateCursor = arcpy.da.UpdateCursor(campus + "/GaragePoints", field_names=fields)

# for row in updateCursor:
#     if row[1] == "Garage":
#         # row.setValue("LotType", "Garage Visitor")
#         row[1] = "Garage Visitor"
#         updateCursor.updateRow(row)

import arcpy

# Define our geodatabase
campus = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/data/modules/20/Campus.gdb"
# Define the fields we want
fields = ['Name', 'LotType', 'LotName']
# Define our search cursor 
updateCursor = arcpy.da.UpdateCursor(campus + "/GaragePoints", field_names=fields)

for row in updateCursor:
    if row[2] == "CENTURY SQUARE":
        updateCursor.deleteRow()
del row
del updateCursor