import arcpy
import time

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "GEOG676_Tools"
        self.alias = "GEOG676_Tools"

        # List of tool classes associated with this toolbox
        self.tools = [BuildingProximity]


class BuildingProximity(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Building Proximity"
        self.description = "Determines which buildings on TAMU's campus are near a targeted building"
        self.canRunInBackground = False # Only used in ArcMap
        self.category = "Building Tools"

    def getParameterInfo(self):
        """Define parameter definitions"""
        param0 = arcpy.Parameter(
            displayName="Building Number",
            name="buildingNumber",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )
        param1 = arcpy.Parameter(
            displayName="Buffer radius",
            name="bufferRadius",
            datatype="GPDouble",
            parameterType="Required",
            direction="Input"
        )
        param1.filter.type = "Range"
        param1.filter.list = [10, 100]
        params = [param0, param1]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        arcpy.AddMessage("Checking building number..")

        for param in parameters:
            if param.name == "buildingNumber":
                buildingNum = param.value

                campus = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/data/modules/17/Campus.gdb"
                where_clause = "Bldg = '%s'" % buildingNum
                structures = campus + "/Structures"
                cursor = arcpy.SearchCursor(structures, where_clause=where_clause)
                iter = (i for i in cursor)
                numOfRows = sum(1 for _ in iter)

                if numOfRows == 0:
                    param.setErrorMessage("Cannot find building %s" % buildingNum)
                    arcpy.AddError("Cannot find building %s" % buildingNum)
                del cursor
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        readTime = 2.5
        loopTime = 0.3
        start = 0
        maximum = 100
        step = 25

        arcpy.SetProgressor("step", "Checking building proximity...", start, maximum, step)
        time.sleep(readTime)
        arcpy.AddMessage("Checking building proximity...")


        campus = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/data/modules/17/Campus.gdb"
        
        # Setup our user input variables
        buildingNumber_input = parameters[0].valueAsText
        bufferSize_input = int(parameters[1].value)

        # Generate our where_clause
        where_clause = "Bldg = '%s'" % buildingNumber_input

        # Check if building exists
        structures = campus + "/Structures"
        cursor = arcpy.SearchCursor(structures, where_clause=where_clause)
        shouldProceed = False

        arcpy.SetProgressorPosition(start + step)
        arcpy.SetProgressorLabel("Validating building number once more...")
        time.sleep(readTime)
        arcpy.AddMessage("Validating building number once more...")

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
            arcpy.SetProgressorPosition(start + step)
            arcpy.SetProgressorLabel("Buffering....")
            time.sleep(readTime)
            arcpy.AddMessage("Buffering...")
            # Clip the structures to our buffered feature
            arcpy.Clip_analysis(structures, campus + buildingBuff, campus + "/clip_%s" % (buildingNumber_input))
            arcpy.SetProgressorPosition(start + step)
            arcpy.SetProgressorLabel("Clipping....")
            time.sleep(readTime)
            arcpy.AddMessage("Clipping...")
            # Remove the feature class we just created
            arcpy.Delete_management(campus + "/building_%s" % (buildingNumber_input))
            arcpy.SetProgressorPosition(maximum)
            arcpy.SetProgressorLabel("Cleaning up files....")
            time.sleep(readTime)
            arcpy.AddMessage("Cleaning up files...")
        else:
            print("Seems we couldn't find the building you entered")
        return None
