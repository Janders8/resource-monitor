import psutil
import pandas as pd


class Ram:

    @staticmethod
    def initiateMonitor():
        df = pd.DataFrame()
        df["ram used %"] = None
        df["ram used"] = None
        df["ram total"] = None
        return df

    @staticmethod
    def bytesToGigabytes(int):
        return int / 1024 / 1024 / 1024

    @staticmethod
    def getRamPercentage():
        return round(psutil.virtual_memory()[2], 2)

    @staticmethod
    def getRamUsed():
        return round(Ram.bytesToGigabytes(psutil.virtual_memory()[3]),2)

    @staticmethod
    def getRamTotal():
        return round(Ram.bytesToGigabytes(psutil.virtual_memory()[0]),2)

    @staticmethod
    def getRamList(self):
        pass







#print('The CPU usage is: ', psutil.cpu_percent(interval = 1, percpu=True))

#print(Ram.getRamPercentage())

#print(psutil.cpu_count(logical=False))

#print(psutil.disk_usage('/')[3])

