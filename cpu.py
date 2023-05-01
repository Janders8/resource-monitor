import psutil
import pandas as pd
import wmi

class Cpu:

    @staticmethod
    def initiateMonitor():
        df = pd.DataFrame()

        # create df
        for i in range(0, psutil.cpu_count()):
            df["thread_" + str(i) + " Load"] = None

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
    def getLogicalCpus():
        return psutil.cpu_count()

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
