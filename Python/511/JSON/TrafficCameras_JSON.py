'''
-------------------------------------------------------------------------------
 Name:         TrafficCameras_JSON.py

 Purpose:      Creates a file geodatabase containing a feature class with all VA
               511 Traffic Cameras and their feeds.

 Author:       Brian Kingery

 Created:      4/16/2018
 -------------------------------------------------------------------------------
'''

import urllib, json, csv, arcpy, datetime
from arcpy import env

def writeCSV(workarea,name,datalist):
    with open(workarea + '/' + name + '.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile)
        for item in datalist:
            try:
                writer.writerow(item)
            except UnicodeEncodeError:
                pass
    csvfile.close()
    print name + '.csv','created'

def createFileGeodatabase(workarea,gdbname):
    gdb = workarea + "/" + gdbname + ".gdb"
    if arcpy.Exists(gdb):
        arcpy.Delete_management(gdb)
    arcpy.CreateFileGDB_management(workarea, gdbname)
    print gdbname + '.gdb','created'
    
def createPoints(workarea,gdbname,csvname,fcname,latfield,longfield):
    input_table  = workarea + "/" + csvname + '.csv'
    output_points  = gdbname + ".gdb/" + fcname
    x_field  = longfield
    y_field  = latfield
    input_format = 'DD_2'
    output_format = 'DD_2'
    id_field = ''
    spatial_ref = arcpy.SpatialReference('WGS 1984')
    arcpy.ConvertCoordinateNotation_management(input_table, output_points, x_field, y_field, input_format, output_format, id_field, spatial_ref)
    print 'Point feature class created'

#-------------------------------------------------------------------------------

ExecutionStartTime = datetime.datetime.now()
print "Started: %s" % ExecutionStartTime.strftime('%A, %B %d, %Y %I:%M:%S %p')
print "Processing\n"

## Target Locations
projectFolder = "C:/Users/brian.kingery/Desktop/Kingery/Projects/511/JSON"
env.workspace = projectFolder
env.overwriteoutput = True

DATA = []
## Column Headers for CSV file
ID = 'ID'
Latitude = 'Latitude'
Longitude = 'Longitude'
Direction = 'Direction'
MRM = 'MRM'
Jurisdiction = 'Jurisdiction'
Route = 'Route'
Description = 'Description'
DeviceID = 'DeviceID'
RTMP_URL = 'RTMP_URL'
IOS_URL = 'IOS_URL'
RTSP_URL = 'RTSP_URL'
IMAGE_URL = 'Image_URL'
Active = 'Active'

headers = ID, Latitude, Longitude, Direction, MRM, Jurisdiction, Route, Description, DeviceID, RTMP_URL, IOS_URL, RTSP_URL, IMAGE_URL, Active
DATA.append(headers)


url = "http://api.skyvdn.com/1.0/streams/getAll/?X-API-KEY=UwgAM46IH8Z5fno7cOyWKh9JlnX6ef11&format=json"
htmlfile = urllib.urlopen(url)
data = json.load(htmlfile)

# let the big dawg eat
CountTrafficCamera=0
i=1
while i<1500:
    try:
        Id = data["features"][i]["properties"]["id"]
        latitude = data["features"][i]["geometry"]["coordinates"][1]
        longitude = data["features"][i]["geometry"]["coordinates"][0]
        direction = data["features"][i]["properties"]["direction"]
        mrm = data["features"][i]["properties"]["mrm"]
        jurisdiction = data["features"][i]["properties"]["jurisdiction"]
        route = data["features"][i]["properties"]["route"]
        description = data["features"][i]["properties"]["description"]
        deviceid = data["features"][i]["properties"]["deviceid"]
        rtmp_url = data["features"][i]["properties"]["rtmp_url"]
        ios_url = data["features"][i]["properties"]["ios_url"]
        rtsp_url = data["features"][i]["properties"]["rtsp_url"]
        image_url = data["features"][i]["properties"]["image_url"]
        active = data["features"][i]["properties"]["active"]

        entry = Id, latitude, longitude, direction, mrm, jurisdiction, route, description, deviceid, rtmp_url, ios_url, rtsp_url, image_url, active
        DATA.append(entry)
        i+=1
        CountTrafficCamera+=1
    except:
        i+=1
        pass
print 'Traffic Cameras Processed:',CountTrafficCamera

geodatabaseName = 'VA511TrafficCameras'
csvName = geodatabaseName
featureClassName = geodatabaseName

writeCSV(projectFolder,csvName,DATA)
createFileGeodatabase(projectFolder,geodatabaseName)
createPoints(projectFolder,geodatabaseName,csvName,featureClassName,Latitude,Longitude)

ExecutionEndTime = datetime.datetime.now()
ElapsedTime = ExecutionEndTime - ExecutionStartTime
print "\nEnded: %s" % ExecutionEndTime.strftime('%A, %B %d, %Y %I:%M:%S %p')
print "Elapsed Time: %s" % str(ElapsedTime).split('.')[0]











