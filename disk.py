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

    wmi_obj = wmi.WMI()

    @staticmethod
    def initiateMonitorDisk():
        df = pd.DataFrame()
        df["Disk read speed"] = None
        df["Disk write speed"] = None
        df["Disk total speed"] = None
        df["Disk wait time"] = None
        df["Disk queue"] = None
        df["Disk usage"] = None

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
    def diskInfo():
        wmi_obj = wmi.WMI()
        disks = wmi_obj.Win32_PerfFormattedData_PerfDisk_PhysicalDisk()[0]

        diskRead = round(int(disks.DiskReadBytesPersec)    / 1024/ 1024, 2)
        diskWrite = round(int(disks.DiskWriteBytesPersec)  / 1024/ 1024, 2)
        diskTotal = round(int(disks.DiskBytesPersec)       / 1024/ 1024,2)
        diskWatiTime = disks.AvgDiskSecPerTransfer * 1000
        diskQueue = disks.CurrentDiskQueueLength
        diskUsage = 100 - int(disks.PercentIdleTime)
        return diskRead, diskWrite, diskTotal, diskWatiTime, diskQueue, diskUsage

    @staticmethod
    def getDiskMany():
        disk_errors = Disk.wmi_obj.query("SELECT * FROM Win32_PerfFormattedData_PerfDisk_PhysicalDisk")

        for disk in disk_errors:
            return disk.PercentIdleTime

    @staticmethod
    def diskWaitTime():
        # Tworzenie obiektu WMI i pobieranie informacji o dysku
        wmi_obj = wmi.WMI()
        disk = wmi_obj.Win32_PerfFormattedData_PerfDisk_PhysicalDisk()[0]

        print(disk)
        # Obliczanie czasu oczekiwania na dane z dysku twardego
        waitTime = disk.AvgDiskSecPerTransfer * 1000

        return(waitTime)

        #print("Czas oczekiwania na dane z dysku twardego:", wait_time, "ms")


#print(Disk.disk_wait_time())

# while True:
#     start = time.time()
#     res = Disk.getDiskMany()
#
#     print(res)
#     print(time.time() - start)
#
#     time.sleep(1)

#print(Disk.diskInfo())