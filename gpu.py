import GPUtil
#GPUtil.showUtilization()
import pandas as pd


class Gpu:



    # if exist any gpu
    if GPUtil.getGPUs():
        GPUs = GPUtil.getGPUs()
    else:
        GPUs = [None]

    @staticmethod
    def initiateMonitor():
        df = pd.DataFrame()
        df["Gpu Load %"] = None
        df["Gpu Memory %"] = None
        df["Gpu temp"] = None

        return df





    @staticmethod
    def getGpuLoad():
        try:
            return Gpu.GPUs[0].load * 100
        except:
            return ""

    @staticmethod
    def getGpuMemoryUsed():
        try:
            return round(Gpu.GPUs[0].memoryUtil * 100,1)
        except:
            return ""

    @staticmethod
    def getGpuName():
        try:
            return Gpu.GPUs[0].name
        except:
            return ""
    @staticmethod
    def getGpuTemp():
        try:
            return Gpu.GPUs[0].temperature
        except:
            return ""

#
#
# print(Gpu.getGpuLoad())
# print(Gpu.getGpuMemoryUsed())
#
# print(Gpu.getGpuName())
# print(Gpu.getGpuTemp())