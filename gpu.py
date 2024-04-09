import time
import pynvml
import pandas as pd

class Gpu:
    pynvml.nvmlInit()

    @staticmethod
    def initiate_monitor():
        df = pd.DataFrame()
        df["Gpu Load %"] = None
        df["Gpu Memory %"] = None
        df["Gpu temp"] = None

        return df

    @staticmethod
    def get_gpu_load():
        try:
            handle = pynvml.nvmlDeviceGetHandleByIndex(0)
            return pynvml.nvmlDeviceGetUtilizationRates(handle).gpu
        except Exception as e:
            print(e)
            return ""

    @staticmethod
    def get_gpu_memory_used():
        try:
            handle = pynvml.nvmlDeviceGetHandleByIndex(0)
            return round(
                pynvml.nvmlDeviceGetMemoryInfo(handle).used / pynvml.nvmlDeviceGetMemoryInfo(handle).total * 100, 2)
        except Exception as e:
            print(e)
            return ""

    @staticmethod
    def get_gpu_name():
        try:
            handle = pynvml.nvmlDeviceGetHandleByIndex(0)
            return pynvml.nvmlDeviceGetName(handle)
        except Exception as e:
            print(e)
            return ""

    @staticmethod
    def get_gpu_temp():
        try:
            handle = pynvml.nvmlDeviceGetHandleByIndex(0)
            return pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU)
        except Exception as e:
            print(e)
            return ""
