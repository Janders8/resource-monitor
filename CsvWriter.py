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
        ram = Ram.initiateMonitor()
        print(ram)
        df = pd.concat([df, ram])
        cpu = Cpu.initiateMonitor()
        print(cpu)
        df = pd.concat([df, cpu])

        gpu = Gpu.initiateMonitor()
        df = pd.concat([df, gpu])

        #todo disk....


        print(df)

        df.to_csv(CsvWriter.fileName, encoding='utf-8', index = False)


if __name__ == "__main__":
    one = CsvWriter()
