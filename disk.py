import psutil
import time


class Disk:
    @staticmethod
    def disk_activity():
        disk_io_counters1 = psutil.disk_io_counters()
        disk_io_counters2 = psutil.disk_io_counters()

        read_count1 = disk_io_counters1.read_count
        write_count1 = disk_io_counters1.write_count
        read_bytes1 = disk_io_counters1.read_bytes
        write_bytes1 = disk_io_counters1.write_bytes

        # Wait for some time
        time.sleep(1)

        disk_io_counters2 = psutil.disk_io_counters()

        read_count2 = disk_io_counters2.read_count
        write_count2 = disk_io_counters2.write_count
        read_bytes2 = disk_io_counters2.read_bytes
        write_bytes2 = disk_io_counters2.write_bytes

        # Calculate the number of read and write operations and bytes transferred
        read_ops = read_count2 - read_count1
        write_ops = write_count2 - write_count1
        read_bytes = read_bytes2 - read_bytes1
        write_bytes = write_bytes2 - write_bytes1

        # Calculate the total number of operations and bytes transferred
        total_ops = read_ops + write_ops
        total_bytes = read_bytes + write_bytes

        # Calculate the percentage of disk activity
        disk_activity_percent = (total_ops / psutil.cpu_count() / psutil.cpu_freq().current) * 100

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