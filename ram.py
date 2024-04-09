import psutil
import pandas as pd


class Ram:

    @staticmethod
    def initiate_monitor():
        df = pd.DataFrame()
        df["ram used %"] = None
        df["ram used"] = None
        df["ram total"] = None
        return df

    @staticmethod
    def bytes_to_gigabytes(number):
        return number / 1024 / 1024 / 1024

    @staticmethod
    def get_ram_percentage():
        return round(psutil.virtual_memory()[2], 2)

    @staticmethod
    def get_ram_used():
        return round(Ram.bytes_to_gigabytes(psutil.virtual_memory()[3]), 2)

    @staticmethod
    def get_ram_total():
        return round(Ram.bytes_to_gigabytes(psutil.virtual_memory()[0]), 2)

    @staticmethod
    def get_ram_list(self):
        pass

