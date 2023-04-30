import psutil
import time


class Disk:
    @staticmethod
    def disk_activity():

        start = time.time()
        disk_before = psutil.disk_io_counters()
        time.sleep(1)
        end = time.time()
        disk_after = psutil.disk_io_counters()


        read_bytes = disk_after.read_bytes - disk_before.read_bytes
        write_bytes = disk_after.write_bytes - disk_before.write_bytes

        disk_time = end - start

        print(psutil.disk_io_counters().read_time/ 1000000000)
        print(psutil.disk_io_counters())



        disk_activity_percent = (disk_before.read_time/1000000000 + disk_before.read_time/1000000000) / disk_time


        return disk_activity_percent

    @staticmethod
    def disk_activityV2():
        disk_io_before = psutil.disk_io_counters()
        time.sleep(1)  # Wait for 1 second
        disk_io_after = psutil.disk_io_counters()

        read_bytes_diff = disk_io_after.read_bytes - disk_io_before.read_bytes
        write_bytes_diff = disk_io_after.write_bytes - disk_io_before.write_bytes
        bytes_diff = read_bytes_diff + write_bytes_diff
        total_bytes = disk_io_after.read_bytes + disk_io_after.write_bytes
        return bytes_diff / total_bytes * 100

    @staticmethod
    def getDiscUsage():
        n_c = tuple(psutil.disk_io_counters())
        n_c = [(100.0 * n_c[i + 1]) / n_c[i] for i in range(0, len(n_c), 2)]
        return n_c

    @staticmethod
    def getDisKPercent():
        p = psutil.Process()
        io_counters = p.io_counters()
        disk_usage_process = io_counters[2] + io_counters[3]  # read_bytes + write_bytes
        disk_io_counter = psutil.disk_io_counters()
        disk_total = disk_io_counter[2] + disk_io_counter[3]  # read_bytes + write_bytes

        return(disk_usage_process / disk_total * 100)


print(Disk.disk_activity())