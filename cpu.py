import psutil
import pandas as pd

class Cpu:

    @staticmethod
    def initiateMonitor():
        df = pd.DataFrame()

        # create df
        for i in range(0, psutil.cpu_count()):
            df["thread_" + str(i)] = None

        return df


    @staticmethod
    def getThreadUsage():
        return psutil.cpu_percent(interval=0.1, percpu=True)

    @staticmethod
    def getFormatedThreadUsage():
        result = ""
        values = Cpu.getThreadUsage()
        for i, v in enumerate(values):
            result += "thread_" + str(i) + " :" + str(v) + "\n"

        return result

    @staticmethod
    def getLogicalCpus():
        return psutil.cpu_count()


# df = Cpu.initiateMonitor()
#
# df.loc[len(df)] = Cpu.getThreadUsage()
#
# print(df)

print(Cpu.getFormatedThreadUsage())