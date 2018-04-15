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
