import ctypes
import pandas as pd

class errors():

    @staticmethod
    def getWheaValue():
        kernel32 = ctypes.windll.kernel32
        currentErrorMode = kernel32.GetErrorMode()
        WheaValue = currentErrorMode & 0x4 !=0
        return WheaValue

    @staticmethod
    def initiateMonitorErrors():
        df = pd.DataFrame()
        df["wheaError"] = None
        return df

if __name__ == "__main__":
    print("whea value: ", errors.getWheaValue())

