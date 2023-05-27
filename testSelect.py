# todo
# select all py files from folder "tests" and ...


import os
import time


TESTS_PATH = "tests/"

# path to arcgispro python
arcgisproPythonPath = r'C:\"Program Files"\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python'
class findTests():
    def __init__(self):
        try:
            self.tests = os.listdir(TESTS_PATH)
        except:
            self.tests = []
        self.createDict()


    def createDict(self):
        self.testWithPaths = {}
        for i in self.tests:
            self.testWithPaths[i] = TESTS_PATH + i

        #print(self.testWithPaths)

    def runSelectedScript(self, testPath):
        exec(open(TESTS_PATH+testPath).read())

    def runUsingSpecyficPython(self, testPath):
        # tutaj mozna mierzyc czas
        start = time.time()
        os.system(fr'cmd /c {arcgisproPythonPath} {testPath}')

        timeOfTest = time.time() - start

        print("czas testu: ", timeOfTest)

        return timeOfTest


# test = findTests()
#
# test.runUsingSpecyficPython(test.testWithPaths[test.tests[0]])