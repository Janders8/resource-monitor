from ram import Ram
from cpu import Cpu
from gpu import Gpu
import pandas as pd

class CsvWriter(object):
    fileName = "monitoring.csv"


    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(CsvWriter, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        df = pd.DataFrame()

        #cpu
        cpu = Cpu.initiateMonitorCore()
        #print(cpu)
        df = pd.concat([df, cpu])
        #ram
        ram = Ram.initiateMonitor()
        #print(ram)
        df = pd.concat([df, ram])

        #gpu
        gpu = Gpu.initiateMonitor()
        df = pd.concat([df, gpu])

        #todo disk....


        #create file with headers
        self.dfHeaders = df
        self.dfHeaders.to_csv(CsvWriter.fileName, encoding='utf-8', index = False)




if __name__ == "__main__":
    one = CsvWriter()
    two = CsvWriter()
