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
roads_covered       = 'Roads_BroadbandCovered'
roads_uncovered     = 'Roads_NoBroadbandCoverage'
broadband_covered   = 'BroadbandCovered'
broadband_uncovered = 'NoBroadbandCoverage'

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
            out_feature_class = 'Clip_' + lyr + '_' + item + '_' + Master_FC

            # Execute Clip
            arcpy.Clip_analysis(in_features, clip_features, out_feature_class)
            print 'Complete: ' + out_feature_class

myClip(districts, DISTRICTS, districtName)
myClip(residencies, RESIDENCIES, residencyName)
