import os
import time

TESTS_PATH = "tests/"

# path to arcgispro python in CENAGIS ESRI template
arcgispro_python_path = r'C:\"Program Files"\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python'


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
        self.create_dict()

    def create_dict(self):
        self.testWithPaths = {}
        for i in self.tests:
            self.testWithPaths[i] = TESTS_PATH + i


    def run_selected_script(self, testPath):
        exec(open(TESTS_PATH + testPath).read())

    def run_using_specyfic_python(self, test):
        start = time.time()
        print(test)
        os.system(fr'cmd /c {arcgispro_python_path} {TESTS_PATH + test}')

        time_of_test = time.time() - start

        print("czas testu: ", time_of_test)

        return time_of_test
