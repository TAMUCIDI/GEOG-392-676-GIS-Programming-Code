import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Mod26"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [ValueList, Multivalue, Composite, Derived]


class ValueList(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "ValueList"
        self.description = "Example of a tool with a list of inputs"
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        param0 = arcpy.Parameter(
            displayName='Input Features',
            name='in_features',
            datatype="GPFeatureLayer",
            parameterType='Required',
            direction='Input')

        param1 = arcpy.Parameter(
            displayName='Statistics Field(s)',
            name='stat_fields',
            datatype='GPValueTable',
            parameterType='Required',
            direction='Input')

        param1.parameterDependencies = [param0.name]
        param1.columns = [['Field', 'Field'], ['String', 'Statistic Type']]
        param1.filters[1].type = 'ValueList'
        param1.values = [['NAME', 'SUM']]
        param1.filters[1].list = ['SUM', 'MIN', 'MAX', 'STDEV', 'MEAN']
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
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        for param in parameters:
            paramText = param.valueAsText
            tokens = paramText.split(" ")
            layer = tokens[0]
            field = tokens[1]
            stat_field = tokens[2]
            
        return


class Multivalue(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Multivalue"
        self.description = "Example of a multivalue parameter tool"
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        param0 = arcpy.Parameter(
            displayName="Input Features",
            name="in_features",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Input",
            multiValue=True)

        params = [param0]
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
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        for param in parameters:
            #arcpy.AddMessage(param.value)
            paramVal = param.valueAsText
            tokens = paramVal.split(";")
            for token in tokens:
                arcpy.AddMessage(token)
        return


class Composite(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Composite"
        self.description = "Example of a composite parameter"
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        param0 = arcpy.Parameter(
            displayName="Input Features",
            name="in_features",
            datatype=[
                "GPFeatureLayer", "GPLayer", "GPRasterDataLayer", "GPLong"
            ],
            parameterType="Required",
            direction="Input")

        params = [param0]
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
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        for param in parameters:
            arcpy.AddMessage(param.value)
        return


class Derived(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Derived"
        self.description = "Example of a derived parameter"
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        param0 = arcpy.Parameter(
            displayName="Input Features",
            name="in_features",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Input")

        param1 = arcpy.Parameter(
            displayName="Output Features",
            name="out_features",
            datatype="GPFeatureLayer",
            parameterType="Derived",
            direction="Output")

        params = [param0, param1]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        param0 = parameters[0]
        param1 = parameters[1]

        param1.parameterDependencies = [param0.name]
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        for param in parameters:
            arcpy.AddMessage(param.valueAsText)
        return
