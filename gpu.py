import time
import pynvml
import pandas as pd

print("initiatedddd")

class Gpu:
    pynvml.nvmlInit()

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
            handle = pynvml.nvmlDeviceGetHandleByIndex(0)
            return pynvml.nvmlDeviceGetUtilizationRates(handle).gpu
        except Exception as e:
            print(e)
            return ""

    @staticmethod
    def getGpuMemoryUsed():
        try:
            handle = pynvml.nvmlDeviceGetHandleByIndex(0)
            return pynvml.nvmlDeviceGetMemoryInfo(handle).used / pynvml.nvmlDeviceGetMemoryInfo(handle).total * 100
        except Exception as e:
            print(e)
            return ""

    @staticmethod
    def getGpuName():
        try:
            handle = pynvml.nvmlDeviceGetHandleByIndex(0)
            return pynvml.nvmlDeviceGetName(handle)
        except Exception as e:
            print(e)
            return ""

    @staticmethod
    def getGpuTemp():
        try:
            handle = pynvml.nvmlDeviceGetHandleByIndex(0)
            return pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU)
        except Exception as e:
            print(e)
            return ""

# while True:
#     time.sleep(2)
#
#     print(Gpu.getGpuLoad())
#     print(Gpu.getGpuMemoryUsed())
#     print(Gpu.getGpuName())
#     print(Gpu.getGpuTemp())
#     print("\n")
