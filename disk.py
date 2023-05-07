import psutil
import time
import pandas as pd

class Disk:


    # def __init__(self):
    #     startingValues = psutil.disk_io_counters()
    #
    #     self.oldRead = startingValues.read_count
    #     self.oldWrite = startingValues.write_count


    @staticmethod
    def initiateMonitorDisk():
        df = pd.DataFrame()
        df["Disk read speed"] = None
        df["Disk write speed"] = None
        df["Disk total speed"] = None

        return df

    @staticmethod
    def diskIOSpeed():
        disk_io_before = psutil.disk_io_counters()
        time.sleep(0.5)  # Wait for 1 second
        disk_io_after = psutil.disk_io_counters()

        # converting valuest to get MB/s
        readBytes = round((disk_io_after.read_bytes - disk_io_before.read_bytes) / 1024 / 1024 *2, 2)
        writeBytes = round ( (disk_io_after.write_bytes - disk_io_before.write_bytes) / 1024 / 1024 * 2, 2)

        totalBytes = readBytes+writeBytes

        return readBytes, writeBytes, totalBytes


