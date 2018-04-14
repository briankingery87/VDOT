'''
-------------------------------------------------------------------------------
 Name:         TrafficCameras.py

 Purpose:      Creates a file geodatabase containing a feature class with all
               Traffic Cameras in Virginia.

 Author:       Brian Kingery

 Created:      4/13/2018
 
 Website:      http://api.skyvdn.com/1.0/streams/getAll/?X-API-KEY=UwgAM46IH8Z5fno7cOyWKh9JlnX6ef11&format=xml
-------------------------------------------------------------------------------
'''

import urllib, csv, arcpy, datetime
import os.path as path
import xml.etree.ElementTree as ElementTree
from arcpy import env
from time import strftime

def createXML(workarea,url,name):
    global xmlDoc
    xmlDoc = name +'_'+strftime('%Y%m%d')+'.xml'
    xml_file = path.join(workarea, xmlDoc)
    urllib.urlretrieve(url, xml_file)
    print 'Retrieved:',xmlDoc

def xmlParser(xmlfile):
    datalist = []
    # column headers for CSV file

    columnLat       = "Latitude"
    columnLon       = "Longitude"

    longitude
    latitude
    direction
    mrm
    cameraid
    jurisdiction
    route
    description
    image_url
    
    columnID        = "ID"
    columnCompany   = "Company"
    columnAddress   = "Address"
    columnCity      = "City"
    columnState     = "State"
    columnZipcode   = "Zipcode"
    columnCountry   = "Country"
    columnPhone     = "Phone"
    columnMType     = "Member_Type"
    columnType      = "Type"
    columnURL       = "URL"
    columnLat       = "Latitude"
    columnLon       = "Longitude"
    headers = columnID, columnCompany, columnAddress, columnCity, columnState, columnZipcode, columnCountry, columnPhone, columnMType, columnType, columnURL, columnLat, columnLon
    datalist.append(headers)

    i=0
    tree = ElementTree.parse(xmlfile)
    for node in tree.findall('marker'):
        ID      = node.attrib.get('id')
        company = node.attrib.get('company')
        address = node.attrib.get('address')
        city    = node.attrib.get('city')
        state   = node.attrib.get('state')
        zipcode = node.attrib.get('zip')
        country = node.attrib.get('country')
        #phone   = data["ProviderFinderResult"][i]["Phone"].replace(" ","").replace("(","").replace(")","").replace("-","")
        phone   = node.attrib.get('phone')
        mType   = node.attrib.get('member_type')
        _type   = node.attrib.get('type')
        url     = node.attrib.get('url')
        lat     = node.attrib.get('lat')
        lon     = node.attrib.get('lng')

        entry = ID, company, address, city, state, zipcode, country, phone, mType, _type, url, lat, lon
        datalist.append(entry)
        i+=1

    print 'Items:    ',i
    return datalist

#-------------------------------------------------------------------------------

ExecutionStartTime = datetime.datetime.now()
print "Started: %s" % ExecutionStartTime.strftime('%A, %B %d, %Y %I:%M:%S %p')
print "Processing\n"

projectFolder    = 'C:/Users/brian.kingery/Desktop/Kingery/Projects/511/XML'
TrafficCameraXML = 'http://api.skyvdn.com/1.0/streams/getAll/?X-API-KEY=UwgAM46IH8Z5fno7cOyWKh9JlnX6ef11&format=xml'
outputName       = 'TrafficCameras'

xmlDocument      = outputName

createXML(projectFolder, TrafficCameraXML, xmlDocument)

ExecutionEndTime = datetime.datetime.now()
ElapsedTime = ExecutionEndTime - ExecutionStartTime
print "\nEnded: %s" % ExecutionEndTime.strftime('%A, %B %d, %Y %I:%M:%S %p')
print "Elapsed Time: %s" % str(ElapsedTime).split('.')[0]
