import arcpy

# arcpy.env.workspace = r"c:/Users/aaron/documents/ArcGIS/Projects/Mod27/"

gdb = r"c:\Users\aaron\documents\ArcGIS\Projects\Mod27\Mod27.gdb"
# input_raster = "tx_dem_high"
# expression = '"%s" < 200' % input_raster
# output_raster = gdb + "\tx_dem_low"
# # azimuth = 315
# # altitude = 45
# # shadows = "NO_SHADOWS"
# # z_factor = 1
# # arcpy.ddd.HillShade(gdb + "/tx_dem", gdb + "/hillshade_1", 315, 45, "NO_SHADOWS", 1)
output_measurement = "DEGREE"
z_factor = 1
method = "PLANAR"
z_unit = "METER"
arcpy.ddd.Slope(gdb + "/tx_dem", gdb + "/slopes_1","DEGREE", 1, "PLANAR", "METER");
# z_tolerance = 250.3
# max_points = 1500000
# z_factor = 1
# arcpy.ddd.RasterTin(gdb + "/tx_dem", gdb + "/tx_dem_RasterTin2", z_tolerance, max_points, z_factor)
# # NO WORKY
# # arcpy.ia.RasterCalculator(expression, output_raster) 

# # MAYBE WORKY
# #arcpy.conversion.RasterToPolygon(gdb + "/tx_dem_high", gdb + "\RasterT_tx_dem2", "SIMPLIFY", "COUNT", "SINGLE_OUTER_PART", None)


# # WORKY
# arcpy.conversion.RasterToASCII(gdb + "/" + input_raster, r"C:\Users\aaron\AppData\Local\Esri\ArcGISPro\SpatialAnalyst\RasterT_tx_dem2.txt")
# #arcpy.ddd.RasterTin(gdb + "/tx_dem", gdb + "/tx_dem_RasterTin", 250.3, 1500000, 1)
# #arcpy.ddd.HillShade(gdb + "/tx_dem", gdb + "/hillshade_1", 315, 45, "NO_SHADOWS", 1)#out_raster = arcpy.sa.HillShade("tx_dem", 315, 45, "NO_SHADOWS", 1); out_raster.save(r"C:\Users\aaron\Documents\ArcGIS\Projects\Mod27\Mod27.gdb\HillSha_tx_d1")
