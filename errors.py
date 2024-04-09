import ctypes
import pandas as pd


class errors():

    @staticmethod
    def get_whea_value():
        kernel32 = ctypes.windll.kernel32
        current_error_mode = kernel32.GetErrorMode()
        whea_value = current_error_mode & 0x4 != 0
        return whea_value

    @staticmethod
    def initiate_monitor_errors():
        df = pd.DataFrame()
        df["wheaError"] = None
        return df


if __name__ == "__main__":
    print("whea value: ", errors.get_whea_value())
