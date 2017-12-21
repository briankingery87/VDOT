#-------------------------------------------------------------------------------
# Name:         List.py
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

file = open(r"C:\Users\brian.kingery@vdot.virginia.gov\Desktop\Kingery\Python\DataDictionary\20171221_GISP_FileLog.txt", "w")
print "Started: %s\n" % ExecutionStartTime.strftime('%A, %B %d, %Y %I:%M:%S %p')
file.write("Started: %s\n\n" % ExecutionStartTime.strftime('%A, %B %d, %Y %I:%M:%S %p') + "\n")
file.write("The following is a list of feature datasets and feature classes that are located in " + env.workspace + "\n")

fdslist = arcpy.ListDatasets()
fdscount = len(fdslist)
totalfc = 0
for fds in fdslist:
    fds_fclist = arcpy.ListFeatureClasses("","",fds)
    fdsfc_count = len(fds_fclist)
    totalfc += fdsfc_count
file.write("There are " + str(fdscount) + " datasets in the geodatabase with a total of " + str(totalfc) + " feature classes." + "\n")

fclist = arcpy.ListFeatureClasses()
fccount = len(fclist)
file.write("There are " + str(fccount) + " feature classes outside of feature datasets." + "\n")

tablelist = arcpy.ListTables()
tcount = len(tablelist)
file.write("There are " + str(tcount) + " tables." + "\n")

## Scanning datasets and their feature classes
file.write("\nThe following are the feature datasets and their feature classes\n" + "\n")
fdnum = 1
fcnum = 1
for fds in fdslist:
    fds_describe = arcpy.Describe(fds)
    file.write(str(fdnum) + " FD Name: " + fds_describe.name + "\n")
    fds_fclist = arcpy.ListFeatureClasses("","",fds)
    for fc in fds_fclist:
        fc_describe = arcpy.Describe(fc)
        file.write("\t" + str(fdnum) + "." + str(fcnum)+ fc_describe.name + "\n")
        file.write("\tPath:         {0}".format(fc_describe.catalogPath) + "\n")
        file.write("\tShape Type:   {0}".format(fc_describe.shapeType) + "\n")
        file.write("\tDescription:     " + "\n")
        fieldlist = arcpy.ListFields(fc)
        fieldnum = 1
        for field in fieldlist:
            # Print field properties
            file.write("\t\t" + str(fdnum) + "." + str(fcnum)+ "." + str(fieldnum)+ " " + field.name + "\n")
            file.write("\t\t\tAlias:       {0}".format(field.aliasName) + "\n")
            file.write("\t\t\tType:        {0}".format(field.type) + "\n")
            file.write("\t\t\tIs Editable: {0}".format(field.editable) + "\n")
            file.write("\t\t\tRequired:    {0}".format(field.required) + "\n")
            file.write("\t\t\tScale:       {0}".format(field.scale) + "\n")
            file.write("\t\t\tPrecision:   {0}".format(field.precision) + "\n")
            file.write("\t\t\tDescription:    " + "\n")
            fieldnum+=1
        fcnum+=1
    fdnum+=1

## Scanning feature classes outside of datasets
file.write("\nThe following are feature classes outside of datasets\n" + "\n")
for fc in fclist:
    fc_describe = arcpy.Describe(fc)
    file.write("\t" + str(fcnum)+ fc_describe.name + "\n")
    file.write("\tPath:         {0}".format(fc_describe.catalogPath) + "\n")
    file.write("\tShape Type:   {0}".format(fc_describe.shapeType) + "\n")
    file.write("\tDescription:     " + "\n")
    fieldlist = arcpy.ListFields(fc)
    fieldnum = 1
    for field in fieldlist:
        # Print field properties
        file.write("\t\t" + str(fcnum)+ "." + str(fieldnum)+ " " + field.name + "\n")
        file.write("\t\t\tAlias:       {0}".format(field.aliasName) + "\n")
        file.write("\t\t\tType:        {0}".format(field.type) + "\n")
        file.write("\t\t\tIs Editable: {0}".format(field.editable) + "\n")
        file.write("\t\t\tRequired:    {0}".format(field.required) + "\n")
        file.write("\t\t\tScale:       {0}".format(field.scale) + "\n")
        file.write("\t\t\tPrecision:   {0}".format(field.precision) + "\n")
        file.write("\t\t\tDescription:    ")
        fieldnum+=1
    fcnum+=1

## Scanning tables
file.write("\nThe following are tables in " + env.workspace + "\n\n")
tnum = 1
for table in tablelist:
    try:
        t_describe = arcpy.Describe(table)
        file.write(str(tnum)+ " " + t_describe.name + "\n")
        file.write("\tPath: {0}".format(t_describe.catalogPath) + "\n")
        fieldlist = arcpy.ListFields(table)
        fieldnum = 1
        for field in fieldlist:
            # Print field properties
            file.write("\t" + str(tnum)+ "." + str(fieldnum)+ " " + field.name + "\n")
            file.write("\t\tAlias:       {0}".format(field.aliasName) + "\n")
            file.write("\t\tType:        {0}".format(field.type) + "\n")
            file.write("\t\tIs Editable: {0}".format(field.editable) + "\n")
            file.write("\t\tRequired:    {0}".format(field.required) + "\n")
            file.write("\t\tScale:       {0}".format(field.scale) + "\n")
            file.write("\t\tPrecision:   {0}".format(field.precision) + "\n")
            file.write("\t\tDescription:    " + "\n")
            fieldnum+=1
    except:
        file.write("Error: " + table + "\n")
    tnum+=1

ExecutionEndTime = datetime.datetime.now()
ElapsedTime = ExecutionEndTime - ExecutionStartTime
print "Ended: %s\n" % ExecutionEndTime.strftime('%A, %B %d, %Y %I:%M:%S %p')
print "Elapsed Time: %s" % str(ElapsedTime).split('.')[0]
file.write("\n\nEnded: %s\n" % ExecutionEndTime.strftime('%A, %B %d, %Y %I:%M:%S %p'))
file.write("Elapsed Time: %s\n" % str(ElapsedTime).split('.')[0])

file.close()
