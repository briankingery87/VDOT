##    Brian Kingery, GISP
##    11/6/2016
##    VDOT
##
##    Create Domain for districts and residencies

import arcpy, os

districts = r'C:\Users\brian.kingery@vdot.virginia.gov\Desktop\Kingery\VITA_Broadband\Data\Broadband.gdb\Districts'
residencies = r'C:\Users\brian.kingery@vdot.virginia.gov\Desktop\Kingery\VITA_Broadband\Data\Broadband.gdb\Residencies'

districtName = 'DISTRICT_NAME'
residencyName = 'RESIDENCY_NAME'

DISTRICTS = []
RESIDENCIES = []

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

##print 'Districts\n'
##for x in DISTRICTS:
##    print x
##
##print '\nResidencies\n'
##for x in RESIDENCIES:
##    print x

arcpy.env.workspace = r'C:\Users\brian.kingery@vdot.virginia.gov\Desktop\Kingery'

domName_District = "Districts"
domName_Residency = "Residencies"
gdb = 'The_FGDB.gdb'
##inFeatures = gdb + os.sep + "Districts"
##inField = "Material"

# Process: Create the coded value domain
arcpy.CreateDomain_management(gdb, domName_District, "VDOT Districts", "TEXT", "CODED")
arcpy.CreateDomain_management(gdb, domName_Residency, "VDOT Residencies", "TEXT", "CODED")

#Store all the domain values in a dictionary with the domain code as the "key" and the domain description as the "value" (domDict[code])
domDict_Districts = {}
domDict_Residencies = {}

for x in DISTRICTS:
    domDict_Districts[x] = x

for x in RESIDENCIES:
    domDict_Residencies[x] = x

# Process: Add valid material types to the domain use a for loop to cycle through all the domain codes in the dictionary
for code in domDict_Districts:        
    arcpy.AddCodedValueToDomain_management(gdb, domName_District, code, domDict_Districts[code])

for code in domDict_Residencies:        
    arcpy.AddCodedValueToDomain_management(gdb, domName_Residency, code, domDict_Residencies[code])

### Process: Constrain the material value of distribution mains
##arcpy.AssignDomainToField_management(inFeatures, inField, domName_District)
##arcpy.AssignDomainToField_management(inFeatures, inField, domName_Residency)

