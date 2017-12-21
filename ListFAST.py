#-------------------------------------------------------------------------------
# Name:         ListFAST.py
# Location:     C:\Users\brian.kingery@vdot.virginia.gov\Desktop\Kingery\Python\DataDictionary
# Purpose:      List all items in GISP.sde
# Author:       Brian Kingery
# Created:      12/21/2017
#-------------------------------------------------------------------------------

import arcpy, time, datetime
from arcpy import env

## Target Locations
env.workspace = "Database Connections\GISP.sde"
env.overwriteOutput = True

ExecutionStartTime = datetime.datetime.now()

print "Started: %s\n" % ExecutionStartTime.strftime('%A, %B %d, %Y %I:%M:%S %p')
print "The following is a list of feature datasets and feature classes that are located in " + env.workspace + "\n"

fdslist = arcpy.ListDatasets()
fdscount = len(fdslist)
totalfc = 0
for fds in fdslist:
    fds_fclist = arcpy.ListFeatureClasses("","",fds)
    fdsfc_count = len(fds_fclist)
    totalfc += fdsfc_count
print "There are " + str(fdscount) + " datasets in the geodatabase with a total of " + str(totalfc) + " feature classes."

fclist = arcpy.ListFeatureClasses()
fccount = len(fclist)
print "There are " + str(fccount) + " feature classes outside of feature datasets."

tablelist = arcpy.ListTables()
tcount = len(tablelist)
print "There are " + str(tcount) + " tables."

## Looking at Datasets and their FCs
print "The following are the feature datasets (FD) and their feature classes (FC)\n"
fdnum = 1
fcnum = 1
for fds in fdslist:
    fds_describe = arcpy.Describe(fds)
    print str(fdnum) + " FD Name: " + fds_describe.name
    fds_fclist = arcpy.ListFeatureClasses("","",fds)
    for fc in fds_fclist:
        fc_describe = arcpy.Describe(fc)
        print("\t" + str(fdnum) + "." + str(fcnum)+ fc_describe.name)
        print("\tPath:         {0}".format(fc_describe.catalogPath))
        print("\tShape Type:   {0}".format(fc_describe.shapeType))
        print("\tDescription:     ")
        fieldlist = arcpy.ListFields(fc)
        fieldnum = 1
        for field in fieldlist:
            # Print field properties
            print("\t\t" + str(fdnum) + "." + str(fcnum)+ "." + str(fieldnum)+ " " + field.name)
            print("\t\t\tAlias:       {0}".format(field.aliasName))
            print("\t\t\tType:        {0}".format(field.type))
            print("\t\t\tIs Editable: {0}".format(field.editable))
            print("\t\t\tRequired:    {0}".format(field.required))
            print("\t\t\tScale:       {0}".format(field.scale))
            print("\t\t\tPrecision:   {0}".format(field.precision))
            print("\t\t\tDescription:    ")
            fieldnum+=1
        fcnum+=1
    fdnum+=1    

## Looking at FCs outside of Datasets
print "\nThe following are feature classes outside of datasets\n"
for fc in fclist:
    fc_describe = arcpy.Describe(fc)
    print("\t" + str(fcnum)+ fc_describe.name)
    print("\tPath:         {0}".format(fc_describe.catalogPath))
    print("\tShape Type:   {0}".format(fc_describe.shapeType))
    print("\tDescription:     ")
    fieldlist = arcpy.ListFields(fc)
    fieldnum = 1
    for field in fieldlist:
        # Print field properties
        print("\t\t" + str(fcnum)+ "." + str(fieldnum)+ " " + field.name)
        print("\t\t\tAlias:       {0}".format(field.aliasName))
        print("\t\t\tType:        {0}".format(field.type))
        print("\t\t\tIs Editable: {0}".format(field.editable))
        print("\t\t\tRequired:    {0}".format(field.required))
        print("\t\t\tScale:       {0}".format(field.scale))
        print("\t\t\tPrecision:   {0}".format(field.precision))
        print("\t\t\tDescription:    ")
        fieldnum+=1
    fcnum+=1

## Looking at Tables
print "\nThe following are tables in " + env.workspace + "\n"
tnum = 1
for table in tablelist:
    try:
        t_describe = arcpy.Describe(table)
        print(str(tnum)+ " " + t_describe.name)
        print("\tPath: {0}".format(t_describe.catalogPath))
        fieldlist = arcpy.ListFields(table)
        fieldnum = 1
        for field in fieldlist:
            # Print field properties
            print("\t" + str(tnum)+ "." + str(fieldnum)+ " " + field.name)
            print("\t\tAlias:       {0}".format(field.aliasName))
            print("\t\tType:        {0}".format(field.type))
            print("\t\tIs Editable: {0}".format(field.editable))
            print("\t\tRequired:    {0}".format(field.required))
            print("\t\tScale:       {0}".format(field.scale))
            print("\t\tPrecision:   {0}".format(field.precision))
            print("\t\tDescription:    ")
            fieldnum+=1
    except:
        print("Error: " + table)
    tnum+=1

ExecutionEndTime = datetime.datetime.now()
ElapsedTime = ExecutionEndTime - ExecutionStartTime
print "Ended: %s\n" % ExecutionEndTime.strftime('%A, %B %d, %Y %I:%M:%S %p')
print "Elapsed Time: %s" % str(ElapsedTime).split('.')[0]
