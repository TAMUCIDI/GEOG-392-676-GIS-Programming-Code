import arcpy


def kmlToGdb():
    # Reads in a .kml, creates a .gdb containing the data
    campus = r"D:\DevSource\Tamu\GeoInnovation\_GISProgramming\data\modules\25\Campus.gdb"
    teams = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/code/25/stadiums.kml"
    # arcpy.KMLToLayer_conversion(teams, "C:/tmp/ArcGISPython/")


def exportGdbToKML():
    # Take a layer and export to .kml
    stadiums = r"C:/tmp/ArcGISPython/stadiums.lyrx"
    kml = r"C:/tmp/ArcGISPython/stadiums.kmz"
    arcpy.LayerToKML_conversion(stadiums, kml)

kmlToGdb()
