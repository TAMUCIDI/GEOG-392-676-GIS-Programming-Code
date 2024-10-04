import arcpy
import requests

# r = requests.get('https://api.nasa.gov/planetary/earth/imagery/?lon=100.75&lat=1.5&date=2014-02-01&cloud_score=True&api_key=DEMO_KEY')
# url = r.json()["url"]
# print(url)

# imagery_response = requests.get(url)

# print(imagery_response.headers["content-type"])


# with open("satellite.png", "wb") as f:
#     for chunk in imagery_response.iter_content(chunk_size=1024):
#         if chunk:
#             f.write(chunk)

#https://api.nasa.gov/planetary/earth/imagery/?lon=100.75&lat=1.5&date=2014-02-01&cloud_score=True&api_key=DEMO_KEY
base_url = "https://api.nasa.gov/planetary/earth/imagery"
api_key = "suXhgIFqNAYMioC2t4931gN9gK1rnszM5v76OqkS"
lon = -42.02461
lat = -22.89325
# lon = -96.336350
# lat = 30.616958

the_url = base_url + "/?lon=%s&lat=%s&cloud_score=True&api_key=%s" % (lon, lat, api_key)
print(the_url)
first_response = requests.get(the_url)
print(first_response.text)

image_url = first_response.json()["url"]
second_response = requests.get(image_url)

with open("satellite.png", "wb") as f:
    for chunk in second_response.iter_content(chunk_size=1024):
        if chunk:
            f.write(chunk)