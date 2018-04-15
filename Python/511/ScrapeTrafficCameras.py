import urllib, csv, arcpy, datetime
import os.path as path
import xml.etree.ElementTree as ElementTree
from arcpy import env
from time import strftime

xmlfile = 'C:/Users/brian.kingery/Desktop/Kingery/Projects/511/XML/TrafficCameras_20180414.xml'

tree = ElementTree.parse(xmlfile)
root = tree.getroot()
features = root.getchildren()[0]
TrafficCameras = features.getchildren()

for camera in TrafficCameras:
    #print camera.getchildren() #--> type, geometry, and properties
    #print camera.find('type').text #--> Feature

####Get Lat/Long
##    geometry = camera.getchildren()[1]
##    for x in geometry:
##        Coordinates = x.getchildren()
##        for LatLong in Coordinates:
##            print LatLong.text


##Get Properties
    Direction = camera.getchildren()[2].find('direction').text
    MRM = camera.getchildren()[2].find('mrm').text
    ID = camera.getchildren()[2].find('id').text
    Jurisdiction = camera.getchildren()[2].find('jurisdiction').text
    Route = camera.getchildren()[2].find('route').text
    Description = camera.getchildren()[2].find('description').text
    DeviceID = camera.getchildren()[2].find('deviceid').text
    RTMP_URL = camera.getchildren()[2].find('rtmp_url').text
    IOS_URL = camera.getchildren()[2].find('ios_url').text
    RTSP_URL = camera.getchildren()[2].find('rtsp_url').text
    IMAGE_URL = camera.getchildren()[2].find('image_url').text
    Active = camera.getchildren()[2].find('active').text
    print str(Direction)+'~'+str(MRM)+'~'+str(ID)+'~'+str(Jurisdiction)+'~'+str(Route)+'~'+str(Description)+'~'+str(DeviceID)+'~'+str(RTMP_URL)+'~'+str(IOS_URL)+'~'+str(RTSP_URL)+'~'+str(IMAGE_URL)+'~'+str(Active)





##############################################################################




##    ImageURL = camera.getchildren()[2].find('image_url').text
##    print ImageURL
    
##direction
##mrm
##id
##jurisdiction
##route
##description
##deviceid
##rtmp_url
##ios_url
##rtsp_url
##image_url
##active
##direction
##mrm
##id
##jurisdiction
##route
##description
##deviceid
##rtmp_url
##ios_url
##rtsp_url
##image_url
##active


    
##    for x in properties:
##        ID = x.find('id').text
##        print ID

        

##        for y in CameraGeometry:
##            z = y.findall('coordinates')
##            print z


##        lat = x.getchildren()[1].getchildren()#find('coordinate')
##        #lon = x.getchildren()[0].find('coordinate')
##        print lat
##        LatLong = x.getchildren()
##        print LatLong
##        for Lat in LatLong:
##            lat = Lat.find('coordinate')
##            print lat
##        lat = x.getchildren()[1]
##        lon = x.getchildren()[0]
##        print lat




##for x in rootchildren:
##    TrafficCameras = x.findall('feature')
##    for camera in TrafficCameras:
##        #print camera.getchildren()
##        CameraGeometry = camera.findall('geometry')
##        for y in CameraGeometry:
##            z = y.findall('coordinates')
##            print z
