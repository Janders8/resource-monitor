# todo
# select all py files from folder "tests" and ...


import os
import time


TESTS_PATH = "tests/"

# path to arcgispro python
arcgisproPythonPath = r'C:\"Program Files"\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python'

#python on my pc
#arcgisproPythonPath = r'C:\Users\janek\AppData\Local\Programs\Python\Python39\python.exe'

class Tests():
    def __init__(self):
        try:
            self.tests = os.listdir(TESTS_PATH)
            print(self.tests)

            temp = []

            for i in self.tests:

                if i[-3:] == ".py":
                    temp.append(i)

            self.tests = temp

        except:
            self.tests = []
        self.__createDict()


    def __createDict(self):
        self.testWithPaths = {}
        for i in self.tests:
            self.testWithPaths[i] = TESTS_PATH + i

        #print(self.testWithPaths)

    def runSelectedScript(self, testPath):
        exec(open(TESTS_PATH+testPath).read())

    def runUsingSpecyficPython(self, test):
        # tutaj mozna mierzyc czas
        start = time.time()
        print(test)
        os.system(fr'cmd /c {arcgisproPythonPath} {TESTS_PATH+test}')

        timeOfTest = time.time() - start

        print("czas testu: ", timeOfTest)

        return timeOfTest


# test = Tests()
#
# test.runUsingSpecyficPython(test.testWithPaths[test.tests[0]])