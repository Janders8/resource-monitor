import psutil
import pandas as pd


class Ram:

    @staticmethod
    def initiateMonitor():
        df = pd.DataFrame()
        df["ram used %"] = None

        return df


    @staticmethod
    def getRamPercentage():
        return 'RAM memory used: ' + str(psutil.virtual_memory()[2]) + "%"




#print('The CPU usage is: ', psutil.cpu_percent(interval = 1, percpu=True))

#print(Ram.getRamPercentage())

#print(psutil.cpu_count(logical=False))

#print(psutil.disk_usage('/')[3])