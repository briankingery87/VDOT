# -*- coding: cp1252 -*-

##    BMP_Inspection_AddFields.py
##    Brian Kingery, GISP
##    11/6/2016
##    VDOT
##
##    Create fields for the BMP Inspection sheet

##NON_NULLABLE —The field will not allow null values.
##NULLABLE —The field will allow null values. This is the default.

##NON_REQUIRED —The field is not a required field. This is the default.
##REQUIRED —The field is a required field. Required fields are permanent and can not be deleted.

## Domains that have been created.
##'YesNo'
##'RatingValue'

##'TEXT'
##'SHORT'
##'DATE'

import arcpy, os
##arcpy.env.workspace = r'C:\Users\brian.kingery@vdot.virginia.gov\Desktop\Kingery\Projects\BMP_Inspections\BMPInspection.gdb'
gdb = r'C:\Users\brian.kingery@vdot.virginia.gov\Desktop\Kingery\Projects\BMP_Inspections\BMP_Inspection.gdb'
fc  = gdb + os.sep + 'VDOT_BMP_Inspection_Basins'

#fn = field name
#fa = field alias

fa1 = fn1
fa2 = fn2
fa3 = fn3
fa4 = 'Project Location'
fa5 = "Photo Frame No's"
fa6 = 'Accessibility (Rating 1 to 5)'
fa7 = 'The pond was inaccessible at the time of the inspection'
fa8 = 'Access road eroded or in need of repair'
fa9 = 'Brush or vines on fence'
fa10= 'Fence damaged and repairs needed'
fa11= 'Gate not locked'
fa12= 'Notes on Accessibility'
fa13= 'Inlets, Inlet Channels and Forebay (Rating 1 to 5)'
fa14= 'Erosion of inlet channel'
fa15= 'Erosion at one or more inlet outfall into basin'
fa16= 'Inlet end section or headwall has separated from inlet pipe'
fa17= 'Inlet is blocked with silt, sediment or trash'
fa18= 'Erosion at one or more inlet outfall into forebay'
fa19= 'Silt and sediment has filled in significant portions of sediment forebay'
fa20= 'Forebay embankment or riprap eroded or damaged'
fa21= 'Notes on Inlets'
fa22= 'Dam Embankments'
fa23= 'Dam was found to be largely over grown with briers/weeds'
fa24= 'Trees or brush growing on embankment'
fa25= 'Inadequate vegetation on dam slopes'
fa26= 'Erosion was noted on the dam'
fa27= 'Settlement was noted on the dam'
fa28= 'Piping was noted on the dam'
fa29= 'Slope slippage was noted on the dam'
fa30= 'Animal burrow holes were noted on the dam'
fa31= 'Downstream seepage noted'
fa32= 'Notes on Dam Embankment'

arcpy.AddField_management(fc, 'Inspectors',     'TEXT', '', '', 50, fa1, 'NON_NULLABLE', 'REQUIRED')
arcpy.AddField_management(fc, 'Date',           'DATE', '', '', 50, fa2, 'NON_NULLABLE', 'REQUIRED')
arcpy.AddField_management(fc, 'UniqueID',       'TEXT', '', '', 50, fa3, 'NULLABLE',     'REQUIRED')
arcpy.AddField_management(fc, 'ProjectLocation','TEXT', '', '', 50, fa4, 'NULLABLE',     'REQUIRED')
arcpy.AddField_management(fc, 'PhotoFrameNo',   'TEXT', '', '', 50, fa5, 'NULLABLE',     'REQUIRED')
arcpy.AddField_management(fc, 'ACCESS',         'SHORT','', '', 5, fa6,  'NON_NULLABLE', 'REQUIRED', 'RatingValue')
arcpy.AddField_management(fc, 'access1',        'TEXT', '', '', 5, fa7,  'NULLABLE', 'NON_REQUIRED', 'YesNo')
arcpy.AddField_management(fc, 'access2',        'TEXT', '', '', 5, fa8,  'NULLABLE', 'NON_REQUIRED', 'YesNo')
arcpy.AddField_management(fc, 'access3',        'TEXT', '', '', 5, fa9,  'NULLABLE', 'NON_REQUIRED', 'YesNo')
arcpy.AddField_management(fc, 'access4',        'TEXT','', '', 5, fa10, 'NULLABLE', 'NON_REQUIRED', 'YesNo')
arcpy.AddField_management(fc, 'access5',        'TEXT','', '', 5, fa11, 'NULLABLE', 'NON_REQUIRED', 'YesNo')
arcpy.AddField_management(fc, 'accessNotes',    'TEXT','', '', 150, fa12, 'NULLABLE', 'NON_REQUIRED')
arcpy.AddField_management(fc, 'INLETS',         'SHORT','', '', 5, fa13, 'NON_NULLABLE', 'REQUIRED', 'RatingValue')
arcpy.AddField_management(fc, 'inlets1',        'TEXT','', '', 5, fa14, 'NULLABLE', 'NON_REQUIRED', 'YesNo')
arcpy.AddField_management(fc, 'inlets2',        'TEXT','', '', 5, fa15, 'NULLABLE', 'NON_REQUIRED', 'YesNo')
arcpy.AddField_management(fc, 'inlets3',        'TEXT','', '', 5, fa16, 'NULLABLE', 'NON_REQUIRED', 'YesNo')
arcpy.AddField_management(fc, 'inlets4',        'TEXT','', '', 5, fa17, 'NULLABLE', 'NON_REQUIRED', 'YesNo')
arcpy.AddField_management(fc, 'forebay1',       'TEXT','', '', 5, fa18, 'NULLABLE', 'NON_REQUIRED', 'YesNo')
arcpy.AddField_management(fc, 'forebay2',       'TEXT','', '', 5, fa19, 'NULLABLE', 'NON_REQUIRED', 'YesNo')
arcpy.AddField_management(fc, 'forebay3',       'TEXT','', '', 5, fa20, 'NULLABLE', 'NON_REQUIRED', 'YesNo')
arcpy.AddField_management(fc, 'inletNotes',     'TEXT','', '', 150, fa21, 'NULLABLE', 'NON_REQUIRED')
arcpy.AddField_management(fc, 'DAM',            'SHORT','', '', 5, fa22, 'NON_NULLABLE', 'REQUIRED', 'RatingValue')
arcpy.AddField_management(fc, 'dam1',           'TEXT','', '', 5, fa23, 'NULLABLE', 'NON_REQUIRED', 'YesNo')
arcpy.AddField_management(fc, 'dam2',           'TEXT','', '', 5, fa24, 'NULLABLE', 'NON_REQUIRED', 'YesNo')
arcpy.AddField_management(fc, 'dam3',           'TEXT','', '', 5, fa25, 'NULLABLE', 'NON_REQUIRED', 'YesNo')
arcpy.AddField_management(fc, 'dam4',           'TEXT','', '', 5, fa26, 'NULLABLE', 'NON_REQUIRED', 'YesNo')
arcpy.AddField_management(fc, 'dam5',           'TEXT','', '', 5, fa27, 'NULLABLE', 'NON_REQUIRED', 'YesNo')
arcpy.AddField_management(fc, 'dam6',           'TEXT','', '', 5, fa28, 'NULLABLE', 'NON_REQUIRED', 'YesNo')
arcpy.AddField_management(fc, 'dam7',           'TEXT','', '', 5, fa29, 'NULLABLE', 'NON_REQUIRED', 'YesNo')
arcpy.AddField_management(fc, 'dam8',           'TEXT','', '', 5, fa30, 'NULLABLE', 'NON_REQUIRED', 'YesNo')
arcpy.AddField_management(fc, 'dam9',           'TEXT','', '', 5, fa31, 'NULLABLE', 'NON_REQUIRED', 'YesNo')
arcpy.AddField_management(fc, 'damNotes',       'TEXT','', '', 150, fa32, 'NULLABLE', 'NON_REQUIRED')




































