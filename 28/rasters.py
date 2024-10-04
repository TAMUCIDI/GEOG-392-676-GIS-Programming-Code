import arcpy


input_raster = arcpy.sa.Raster(r"D:\DevSource\Tamu\GeoInnovation\_GISProgramming\data\modules\28\tx_dem")
# print("Raster mean: %f" % input_raster.maximum)

raster2 = input_raster > 3.0
raster3 = arcpy.sa.Shrink(raster2, 1, 1)
raster4 = arcpy.sa.Expand(raster3, 1, 1)


print ("HIYA")