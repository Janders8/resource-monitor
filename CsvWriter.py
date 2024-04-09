from ram import Ram
from cpu import Cpu
from gpu import Gpu
from disk import Disk
from errors import errors
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

        # time stamp
        df["timestamp"] = None

        # cpu
        cpu = Cpu.initiate_monitor_threat()
        # print(cpu)
        df = pd.concat([df, cpu])
        # ram
        ram = Ram.initiate_monitor()
        # print(ram)
        df = pd.concat([df, ram])

        # gpu
        gpu = Gpu.initiate_monitor()
        df = pd.concat([df, gpu])

        # disk
        disk = Disk.initiateMonitorDisk()
        df = pd.concat([df, disk])

        # errors
        whea = errors.initiate_monitor_errors()
        df = pd.concat([df, whea])

        # create file with headers
        self.dfHeaders = df
        self.dfHeaders.to_csv(CsvWriter.fileName, encoding='utf-8', index=False)

    def update(self, values):
        # cpu
        # cpuCore = values["cpuCore"]
        # cpuCoreFormated = values["cpuCoreFormated"]
        cpu_thread = values["cpu_thread"]
        cpu_thread_formated = values["cpu_thread_formated"]
        cpu_temp = values["cpu_temp"]
        # cpuErrors = values["cpuErrors"]

        # ram
        ram_percent = values["ram_percent"]
        ram_used = values["ram_used"]
        ram_total = values["ram_total"]

        # gpu
        gpu_load = values["gpu_load"]
        gpu_memory = values["gpu_memory"]
        gpu_temp = values["gpu_temp"]

        # disk
        disk_read = values["disk_read"]
        disk_write = values["disk_write"]
        disk_total = values["disk_total"]
        disk_wait = values["disk_wait_time"]
        disk_queue = values["disk_queue"]
        disk_usage = values["disk_usage"]

        # errors
        whea = values["whea_error"]

        # empty dataframe with headers
        self.dfHeaders.drop(self.dfHeaders.index, inplace=True)

        timestamp = datetime.now().strftime("%H:%M:%S")

        # create new row, can be done better
        new_row = [timestamp] + cpu_thread + [cpu_temp] + [ram_percent] + [ram_used] + [ram_total] + [gpu_load] + [
            gpu_memory] + [gpu_temp] \
                  + [disk_read] + [disk_write] + [disk_total] + [disk_wait] + [disk_queue] + [disk_usage] + [whea]

        # add new row
        self.dfHeaders.loc[len(self.dfHeaders)] = new_row

        print(self.dfHeaders)

        # save new row
        self.dfHeaders.to_csv(self.fileName, mode="a", index=False, header=False)
