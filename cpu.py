import psutil
import pandas as pd
import wmi
# from pyspectator.processor import Cpu as CpuInfo
import clr
import time

clr.AddReference("OpenHardwareMonitorLib")
from OpenHardwareMonitor.Hardware import *


class Cpu:
    computer = Computer()
    computer.CPUEnabled = True
    computer.Open()

    _oldErrors = 0

    w = wmi.WMI()

    @staticmethod
    def initiate_monitor_threat():
        df = pd.DataFrame()

        # create df
        for i in range(0, psutil.cpu_count()):
            df["thread_" + str(i) + " Load"] = None

        df["cpuTemp"] = None

        return df

    @staticmethod
    def get_cpu_idle_time():
        result = []
        for status in Cpu.w.Win32_PerfFormattedData_PerfOS_Processor():
            result.append(status.PercentIdleTime)

        return result

    @staticmethod
    def initiate_monitor_core():
        df = pd.DataFrame()

        # create df
        for i in range(0, psutil.cpu_count(logical=False)):
            df["Core_" + str(i) + " Load"] = None

        df["cpuTemp"] = None

        return df

    @staticmethod
    def get_thread_usage():
        return psutil.cpu_percent(interval=0.1, percpu=True)

    @staticmethod
    def get_formated_thread_usage(thread_usage):
        result = ""

        for i, v in enumerate(thread_usage):
            result += "thread_" + str(i) + " :" + str(v) + "\n"

        return result

    @staticmethod
    def get_formated_core_usage(core_usage):
        result = ""

        for i, v in enumerate(core_usage):
            result += "core_" + str(i) + " :" + str(round(v, 3)) + "\n"

        return result

    @staticmethod
    def get_logical_cpus():
        return psutil.cpu_count()

    @staticmethod
    def get_core_usage():
        # Get the usage of all cores (including hyper-threading cores)
        all_core_usage_percent = psutil.cpu_percent(interval=0.5, percpu=True)

        # Get the number of physical cores
        num_physical_cores = psutil.cpu_count(logical=False)

        # Group the usage of hyper-threading cores with their corresponding physical core
        physical_core_usage_percent = []
        # check if there is hyper-threading
        if len(all_core_usage_percent) == 2 * num_physical_cores:
            for i in range(num_physical_cores):
                core_usage = (all_core_usage_percent[i * 2] + all_core_usage_percent[i * 2 + 1]) / 2
                physical_core_usage_percent.append(core_usage)
        else:
            physical_core_usage_percent = all_core_usage_percent

        return physical_core_usage_percent

    @staticmethod
    def get_cpus_temp():

        for hardware in Cpu.computer.Hardware:

            if hardware.HardwareType == HardwareType.CPU:
                hardware.Update()
                for sensor in hardware.Sensors:
                    if sensor.SensorType == SensorType.Temperature and sensor.Name == "CPU Package":
                        return sensor.Value
