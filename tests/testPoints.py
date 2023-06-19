
# importing the module
import arcpy

try:
    arcpy.analysis.SummarizeWithin(r"tests/pointsTestData/powiaty.shp", r"tests/pointsTestData/points10000000.gpkg/points10000000", r"tests/pointsTest.gdb\powiaty_SummarizeWithin", "KEEP_ALL", None, "ADD_SHAPE_SUM", "SQUAREMETERS", None, "NO_MIN_MAJ", "NO_PERCENT", None)
except Exception as Argument:

    # creating/opening a file
    f = open("errorLog.txt", "a")

    # writing in the file
    f.write(str(Argument))

    # closing the file
    f.close()