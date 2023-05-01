import psutil
import pandas as pd
import wmi

class Cpu:

    @staticmethod
    def initiateMonitorThreat():
        df = pd.DataFrame()

        # create df
        for i in range(0, psutil.cpu_count()):
            df["thread_" + str(i) + " Load"] = None

        df["cpuTemp"] = None

        return df

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
            result += "core_" + str(i) + " :" + str(v) + "\n"

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
        for i in range(num_physical_cores):
            core_usage = (all_core_usage_percent[i * 2] + all_core_usage_percent[i * 2 + 1]) / 2
            physical_core_usage_percent.append(core_usage)


        return physical_core_usage_percent
        # Print the usage of each physical core
        # for i in range(num_physical_cores):
        #     print(f"Physical Core {i + 1} Usage: {physical_core_usage_percent[i]}%")

    @staticmethod
    def getCpusTemp():
        result = ""
        counter = 0
        try:

            w = wmi.WMI(namespace="root\OpenHardwareMonitor")
            temperature_infos = w.Sensor()
            for sensor in temperature_infos:
                if sensor.SensorType == u'Temperature':
                    if sensor.Name == "CPU Package":
                        result+= sensor.Name + str(counter) + " " + str(sensor.Value) + "\n"
                        # print(sensor.Name)
                        # print(sensor.Value)
            return result
        except:
            return ""

print(Cpu.getCoreUsage())

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
