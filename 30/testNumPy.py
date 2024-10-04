import arcpy
import numpy

# out_fc = 'C:/tmp/ArcGISPython/DC.gdb/pointlocations'


# # Create a numpy array with an id field, and a field with a tuple 
# #  of x,y coordinates
# arr = numpy.array([(1, (471316.3835861763, 5000448.782036674)),
#                    (2, (470402.49348005146, 5000049.216449278))],
#                   numpy.dtype([('idfield', numpy.int32),('XY', '<f8', 2)]))

# # Define a spatial reference for the output feature class
# spatial_ref = arcpy.Describe('C:/tmp/ArcGISPython/DC.gdb/removed_trees').spatialReference

# # Export the numpy array to a feature class using the XY field to
# #  represent the output point feature
# arcpy.da.NumPyArrayToFeatureClass(arr, out_fc, ['XY'], spatial_ref)

fc = 'C:/tmp/ArcGISPython/DC.gdb/pointlocations'
fields = ["idfield"]
arr = arcpy.da.FeatureClassToNumPyArray(fc, fields, skip_nulls=True)
