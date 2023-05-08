import psutil
import pandas as pd
import wmi
import time
import clr
clr.AddReference("OpenHardwareMonitorLib")
from OpenHardwareMonitor.Hardware import *

class Cpu:
    computer = Computer()
    computer.CPUEnabled = True
    computer.Open()

    _oldErrors = 0

    w = wmi.WMI()




    @staticmethod
    def initiateMonitorThreat():
        df = pd.DataFrame()

        # create df
        for i in range(0, psutil.cpu_count()):
            df["thread_" + str(i) + " Load"] = None

        df["cpuTemp"] = None
        df["cpuErrors"] = None

        return df

    # includes I/O waiting time
    @staticmethod
    def getCpuIdleTimeOld():
        cpu_count = psutil.cpu_count()
        load_avg = psutil.getloadavg()

        idleTime = max(0, (cpu_count * load_avg[0]) - psutil.cpu_count())
        return idleTime

    @staticmethod
    def getCpuIdleTime():
        result = []
        for status in Cpu.w.Win32_PerfFormattedData_PerfOS_Processor():
            result.append(status.PercentIdleTime)

        return result

    @staticmethod
    #todo
    def getCpuErrors():
        cpu_stats = psutil.cpu_stats()
        # Ilość przełączeń kontekstu procesora
        ctx_switches = cpu_stats.ctx_switches
        # Ilość przerwań obsługiwanych przez procesor
        interrupts = cpu_stats.interrupts
        # Obliczenie liczby błędów procesora jako suma przełączeń kontekstu i przerwań
        newErrors = ctx_switches + interrupts

        result = newErrors - Cpu._oldErrors
        Cpu._oldErrors = newErrors
        return result



    @staticmethod
    def initiateMonitorCore():
        df = pd.DataFrame()

        # create df
        for i in range(0, psutil.cpu_count(logical=False)):
            df["Core_" + str(i) + " Load"] = None

        df["cpuTemp"] = None

        return df

    @staticmethod
    def getThreadUsage():
        return psutil.cpu_percent(interval=0.1, percpu=True)



    @staticmethod
    def getFormatedThreadUsage(ThreadUsage):
        result = ""

        for i, v in enumerate(ThreadUsage):
            result += "thread_" + str(i) + " :" + str(v) + "\n"

        return result

    @staticmethod
    def getFormatedCoreUsage(CoreUsage):
        result = ""

        for i, v in enumerate(CoreUsage):
            result += "core_" + str(i) + " :" + str(round(v,3)) + "\n"

        return result

    @staticmethod
    def getLogicalCpus():
        return psutil.cpu_count()

    @staticmethod
    def getCoreUsage():
        print(cpu_usage_percent = psutil.cpu_percent(interval=0.5, percpu=True))

    @staticmethod
    def getCoreUsage():
        # Get the usage of all cores (including hyper-threading cores)
        all_core_usage_percent = psutil.cpu_percent(interval=0.5, percpu=True)

        # Get the number of physical cores
        num_physical_cores = psutil.cpu_count(logical=False)

        # Group the usage of hyper-threading cores with their corresponding physical core
        physical_core_usage_percent = []
        # check if there is hyper-threading
        if (len(all_core_usage_percent) == 2* num_physical_cores):
            for i in range(num_physical_cores):
                core_usage = (all_core_usage_percent[i * 2] + all_core_usage_percent[i * 2 + 1]) / 2
                physical_core_usage_percent.append(core_usage)
        else:
            physical_core_usage_percent = all_core_usage_percent


        return physical_core_usage_percent
        # Print the usage of each physical core
        # for i in range(num_physical_cores):
        #     print(f"Physical Core {i + 1} Usage: {physical_core_usage_percent[i]}%")

    @staticmethod
    def getCpusTemp():

        for hardware in Cpu.computer.Hardware:

            if hardware.HardwareType == HardwareType.CPU:
                hardware.Update()
                for sensor in hardware.Sensors:
                    if sensor.SensorType == SensorType.Temperature and sensor.Name == "CPU Package":
                        return sensor.Value

print(Cpu.getCpuIdleTime())
# i = 0
# while True:
#     i+=1
#     print(Cpu.getCpuIdleTime(),i)
#     time.sleep(1)
# prev = Cpu.getCpuErrors()
# while True:
#     new = Cpu.getCpuErrors()
#     print(new-prev)
#     prev = new
#     time.sleep(1)
#
# print(Cpu.getCpuErrors())
#print(Cpu.getCoreUsage())

#print (Cpu.getThreadUsage())
# print(Cpu.getCpusTemp())

# df = Cpu.initiateMonitor()
#
# df.loc[len(df)] = Cpu.getThreadUsage()
#
# print(df)

#print(Cpu.getFormatedThreadUsage())

#import clr # the pythonnet module.
#clr.AddReference(r'OpenHardwareMonitorLib')
# e.g. clr.AddReference(r'OpenHardwareMonitor/OpenHardwareMonitorLib'), without .dll

# from OpenHardwareMonitor.Hardware import Computer
#
# c = Computer()
# c.CPUEnabled = True # get the Info about CPU
# c.HDDEnabled = True
# c.Open()

#print(c.Hardware)


# for i in c.Hardware:
#     i.Update()
#     print(i)
#     for sensor in i.Sensors:
#         print(sensor)
#
