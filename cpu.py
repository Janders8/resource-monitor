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


# df = Cpu.initiateMonitor()
#
# df.loc[len(df)] = Cpu.getThreadUsage()
#
# print(df)