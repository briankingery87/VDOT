##    Brian Kingery, GISP
##    11/10/2016
##    VDOT
##
##    Cycle through districts and residencies clipping features to their extents

import arcpy, os

arcpy.env.workspace = r'C:\Users\brian.kingery@vdot.virginia.gov\Desktop\Kingery\Projects\VITA_Broadband\Data\VITA_Broadband.gdb'

# Master FCs
districts           = 'Districts'
residencies         = 'Residencies'
roads_covered       = 'Roads_Covered'
roads_uncovered     = 'Roads_Uncovered'
broadband_covered   = 'Area_Covered'
broadband_uncovered = 'Area_Uncovered'

CLIP = [roads_covered,roads_uncovered,broadband_covered,broadband_uncovered]

# Build the lists of names for Districts and Residencies
DISTRICTS = []
RESIDENCIES = []

districtName = 'DISTRICT_NAME'
residencyName = 'RESIDENCY_NAME'

with arcpy.da.SearchCursor(districts, districtName) as cursor:
    for row in cursor:
        DISTRICTS.append(row[0])
DISTRICTS.sort()
del cursor

with arcpy.da.SearchCursor(residencies, residencyName) as cursor:
    for row in cursor:
        RESIDENCIES.append(row[0])
RESIDENCIES.sort()
del cursor


# Define function to clip each item
def myClip(featureClass, LIST, fieldName):
    print 'Starting clip process'
    
    fc = featureClass
    lyr = fc

    # Make a layer from the feature class
    arcpy.MakeFeatureLayer_management(fc, lyr)

    # Selection loop
    for item in LIST:
        where_clause = '"'+ fieldName + '" = ' + "'" + item + "'"
        arcpy.SelectLayerByAttribute_management(lyr, "NEW_SELECTION", where_clause)

        # Set local variables for clipping
        for Master_FC in CLIP:
            in_features = Master_FC
            clip_features = lyr
            out_feature_class = 'Clip_' + lyr + '_' + item.replace(' ','') + '_' + Master_FC

            # Execute Clip
            arcpy.Clip_analysis(in_features, clip_features, out_feature_class)
            print 'Complete: ' + out_feature_class
            
myClip(districts, DISTRICTS, districtName)
myClip(residencies, RESIDENCIES, residencyName)

##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################

##    http://desktop.arcgis.com/en/arcmap/10.3/manage-data/tables/calculate-field-examples.htm
##    !shape.length@miles!
##    !shape.area@squaremiles!

def CoveredRoads_Analysis():
    print 'Covered Roads'
    # Find amount of mileage that is broadband covered
    coveredRoads = arcpy.ListFeatureClasses('Clip*_Roads_C*')
    for fc in coveredRoads:
        newfieldName = 'Clip_mileage'
        arcpy.AddField_management(fc, newfieldName, 'DOUBLE')
        arcpy.CalculateField_management(fc,newfieldName,'!shape.length@miles!',"PYTHON_9.3")

        mileage = 0
        with arcpy.da.SearchCursor(fc, newfieldName) as cursor:
            for row in cursor:
                mileage += row[0]
        del cursor
        print mileage
CoveredRoads_Analysis()
        
def UncoveredRoads_Analysis():
    print 'Uncovered Roads'
    # Find amount of mileage that is NOT broadband covered
    uncoveredRoads = arcpy.ListFeatureClasses('Clip*_Roads_U*')
    for fc in uncoveredRoads:
        newfieldName = 'Clip_mileage'
        arcpy.AddField_management(fc, newfieldName, 'DOUBLE')
        arcpy.CalculateField_management(fc,newfieldName,'!shape.length@miles!',"PYTHON_9.3")

        mileage = 0
        with arcpy.da.SearchCursor(fc, newfieldName) as cursor:
            for row in cursor:
                mileage += row[0]
        del cursor
        print mileage
UncoveredRoads_Analysis()

def Covered_Analysis():
    print 'Covered Areas'
    # Find amount of mileage that is NOT broadband covered
    covered = arcpy.ListFeatureClasses('Clip*_Area_C*')
    for fc in covered:
        newfieldName = 'Clip_sqmi'
        arcpy.AddField_management(fc, newfieldName, 'DOUBLE')
        arcpy.CalculateField_management(fc,newfieldName,'!shape.area@squaremiles!',"PYTHON_9.3")

        SqMi = 0
        with arcpy.da.SearchCursor(fc, newfieldName) as cursor:
            for row in cursor:
                SqMi += row[0]
        del cursor
        print SqMi
Covered_Analysis()

def Uncovered_Analysis():
    print 'Uncovered Areas'
    # Find amount of mileage that is NOT broadband covered
    uncovered = arcpy.ListFeatureClasses('Clip*_Area_U*')
    for fc in uncovered:
        newfieldName = 'Clip_sqmi'
        arcpy.AddField_management(fc, newfieldName, 'DOUBLE')
        arcpy.CalculateField_management(fc,newfieldName,'!shape.area@squaremiles!',"PYTHON_9.3")

        SqMi = 0
        with arcpy.da.SearchCursor(fc, newfieldName) as cursor:
            for row in cursor:
                SqMi += row[0]
        del cursor
        print SqMi
Uncovered_Analysis()
