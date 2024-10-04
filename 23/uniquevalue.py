import arcpy

project = arcpy.mp.ArcGISProject(r"C:/tmp/ArcGISPython/" + r"\\Mod23.aprx")

campus = project.listMaps('Map')[0]

for lyr in campus.listLayers():
    if lyr.isFeatureLayer:
        print(lyr.name)
        symbology = lyr.symbology
        if hasattr(symbology, 'renderer'):
            # print(symbology.renderer.type)
            if lyr.name == "Structures":
                symbology.updateRenderer('UniqueValueRenderer')
                symbology.renderer.fields = ["Type"]
                lyr.symbology = symbology
            else:
                print("NOT SIMPLE")

project.saveACopy(r"C:/tmp/ArcGISPython/" + r"\\Mod23b.aprx")
