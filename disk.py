import psutil
import time
import pandas as pd
import wmi



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
        df["Disk wait time"] = None

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

    @staticmethod
    def diskWaitTime():
        # Tworzenie obiektu WMI i pobieranie informacji o dysku
        wmi_obj = wmi.WMI()
        disk = wmi_obj.Win32_PerfFormattedData_PerfDisk_PhysicalDisk()[0]

        # Obliczanie czasu oczekiwania na dane z dysku twardego
        waitTime = disk.AvgDiskSecPerTransfer * 1000

        return(waitTime)

        #print("Czas oczekiwania na dane z dysku twardego:", wait_time, "ms")

#print(Disk.disk_wait_time())


