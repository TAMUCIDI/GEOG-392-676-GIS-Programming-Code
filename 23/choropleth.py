import arcpy

project = arcpy.mp.ArcGISProject(r"C:/tmp/ArcGISPython/" + r"\\Mod23.aprx")

campus = project.listMaps('Map')[0]

for layer in campus.listLayers():
    if layer.isFeatureLayer:
        symbology = layer.symbology
        if hasattr(symbology, 'renderer'):
            if layer.name == "GarageParking":
                symbology.updateRenderer('GraduatedColorsRenderer')
                symbology.renderer.classificationField = "Shape_Area"
                symbology.renderer.breakCount = 5
                symbology.renderer.colorRamp = project.listColorRamps('Oranges (5 Classes)')[0]
                
                layer.symbology = symbology
            else:
                print("NOT GarageParking")

project.saveACopy(r"C:/tmp/ArcGISPython/" + r"\\Mod23c.aprx")
