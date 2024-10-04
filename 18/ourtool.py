# 1. Take user's input as the building number AND buffer distance
# 2. Check to make sure building is present in Structures
# 3. Buffer the building with the distance given
# 4. Clip the resulting layer with the Structures feature class

import arcpy
arcpy.env.workspace = "C:/tmp/ArcGISPython"

# Define our geodatabase
campus = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/data/modules/18/Campus.gdb"

# Setup our user input variables
buildingNumber_input = input("Please enter a building number: ")
bufferSize_input = int(input("Please enter a buffer size: "))

# Generate our where_clause
where_clause = "Bldg = '%s'" % buildingNumber_input

# Check if building exists
structures = campus + "/Structures"
cursor = arcpy.SearchCursor(structures, where_clause=where_clause)
shouldProceed = False

for row in cursor:
    if row.getValue("Bldg") == buildingNumber_input:
        shouldProceed = True

# If we shouldProceed do so
if shouldProceed:
    # Generate the name for our generated buffer layer
    buildingBuff = "/building_%s_buffed_%s" % (buildingNumber_input, bufferSize_input)
    # Get reference to building
    buildingFeature = arcpy.Select_analysis(structures, campus + "/building_%s" % (buildingNumber_input), where_clause)
    # Buffer the selected building
    arcpy.Buffer_analysis(buildingFeature, campus + buildingBuff, bufferSize_input)
    # Clip the structures to our buffered feature
    arcpy.Clip_analysis(structures, campus + buildingBuff, campus + "/clip_%s" % (buildingNumber_input))
    # Remove the feature class we just created
    arcpy.Delete_management(campus + "/building_%s" % (buildingNumber_input))
    
else:
    print("Seems we couldn't find the building you entered")