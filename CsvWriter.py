from ram import Ram
from cpu import Cpu
from gpu import Gpu
from disk import Disk
import pandas as pd
from datetime import datetime

class CsvWriter(object):
    fileName = "monitoring.csv"


    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(CsvWriter, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        df = pd.DataFrame()

        #time stamp
        df["timestamp"] = None

        #cpu
        cpu = Cpu.initiateMonitorThreat()
        #print(cpu)
        df = pd.concat([df, cpu])
        #ram
        ram = Ram.initiateMonitor()
        #print(ram)
        df = pd.concat([df, ram])

        #gpu
        gpu = Gpu.initiateMonitor()
        df = pd.concat([df, gpu])

        #disk
        disk = Disk.initiateMonitorDisk()
        df = pd.concat([df, disk])


        #create file with headers
        self.dfHeaders = df
        self.dfHeaders.to_csv(CsvWriter.fileName, encoding='utf-8', index = False)

    def update(self, values):
        #cpu
        # cpuCore = values["cpuCore"]
        # cpuCoreFormated = values["cpuCoreFormated"]
        cpuThread = values["cpuThread"]
        cpuThreadFormated = values["cpuThreadFormated"]
        cpuTemp = values["cpuTemp"]
        #cpuErrors = values["cpuErrors"]

        # ram
        ramPercent = values["ramPercent"]
        ramUsed = values["ramUsed"]
        ramTotal = values["ramTotal"]

        # gpu
        gpuLoad = values["gpuLoad"]
        gpuMemory = values["gpuMemory"]
        gpuTemp = values["gpuTemp"]

        #disk
        diskRead = values["diskRead"]
        diskWrite = values["diskWrite"]
        diskTotal = values["diskTotal"]
        diskWait = values["diskWaitTime"]
        diskQueue = values["diskQueue"]
        diskUsage = values["diskUsage"]


        # empty dataframe with headers
        self.dfHeaders.drop(self.dfHeaders.index, inplace=True)

        timestmap = datetime.now().strftime("%H:%M:%S")

        # create new row, can be done better
        newRow = [timestmap] + cpuThread + [cpuTemp] + [ramPercent] + [ramUsed] + [ramTotal] + [gpuLoad] + [gpuMemory] + [gpuTemp] \
                 + [diskRead] + [diskWrite] + [diskTotal] + [diskWait] + [diskQueue] + [diskUsage]

        # add new row
        self.dfHeaders.loc[len(self.dfHeaders)] = newRow

        print(self.dfHeaders)

        # save new row
        self.dfHeaders.to_csv(self.fileName, mode="a", index=False, header=False)
