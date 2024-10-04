import arcpy
import requests


def jsonToFeature():
    response_format = "pjson"
    where_clause = "objectid+>+0"
    query_url = "https://gis.tamu.edu/arcgis/rest/services/FCOR/BaseMap_051118/MapServer/9/query?where=%s&f=%s" % (where_clause, response_format)
    response = requests.get(query_url)
    # print(response.json())
    response_json = response.json()
    with open(r"C:/tmp/ArcGISPython/json_response.json", "wb") as file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)
    arcpy.JSONToFeatures_conversion(r"C:/tmp/ArcGISPython/json_response.json", r"C:/tmp/ArcGISPython/Test.gdb/trees")


def featureToJSON():
    feature_path = r"C:/tmp/ArcGISPython/Test.gdb/trees"
    json_path = r"C:/tmp/ArcGISPython/trees_json.json"
    arcpy.FeaturesToJSON_conversion(feature_path, json_path)
    with open(json_path, "r") as file:
        json_content = file.read()
        base_url = "SOMEARCSERVER"
        request = requests.post(base_url, data=json_content)



featureToJSON()
