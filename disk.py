import psutil
import time
import pandas as pd
import wmi


class Disk:

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
    def disk_info():
        wmi_obj = wmi.WMI()
        disks = wmi_obj.Win32_PerfFormattedData_PerfDisk_PhysicalDisk()[0]

        disk_read = round(int(disks.DiskReadBytesPersec) / 1024 / 1024, 2)
        disk_write = round(int(disks.DiskWriteBytesPersec) / 1024 / 1024, 2)
        disk_total = round(int(disks.DiskBytesPersec) / 1024 / 1024, 2)
        disk_wait_time = disks.AvgDiskSecPerTransfer * 1000
        disk_queue = disks.CurrentDiskQueueLength
        disk_usage = 100 - int(disks.PercentIdleTime)
        return disk_read, disk_write, disk_total, disk_wait_time, disk_queue, disk_usage

    @staticmethod
    def get_disk_many():
        disk_errors = Disk.wmi_obj.query("SELECT * FROM Win32_PerfFormattedData_PerfDisk_PhysicalDisk")

        for disk in disk_errors:
            return disk.PercentIdleTime

    @staticmethod
    def disk_wait_time():
        wmi_obj = wmi.WMI()
        disk = wmi_obj.Win32_PerfFormattedData_PerfDisk_PhysicalDisk()[0]
        wait_time = disk.AvgDiskSecPerTransfer * 1000

        return wait_time

    @staticmethod
    def get_hard_drive_model():
        c = wmi.WMI()
        for drive in c.Win32_DiskDrive():
            return drive.Model

        return "No disc detected"
