# importing the module
import arcpy

try:
    out_raster = arcpy.sa.Slope(r"tests\slopeTestData\dem.tiff", "PERCENT_RISE", 1, "PLANAR", "METER");
    out_raster.save(r"tests\slopeTestData\slopeTest.gdb\Slope")
except Exception as Argument:

    # creating/opening a file
    f = open("errorLog.txt", "a")

    # writing in the file
    f.write(str(Argument))

    # closing the file
    f.close()
