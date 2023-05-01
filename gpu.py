import GPUtil
#GPUtil.showUtilization()

class Gpu:

    GPUs = GPUtil.getGPUs()

    @staticmethod
    def getGpuLoad():
        return Gpu.GPUs[0].load * 100

    @staticmethod
    def getGpuMemoryUsed():
        return round(Gpu.GPUs[0].memoryUtil * 100,1)

    @staticmethod
    def getGpuName():
        return Gpu.GPUs[0].name

    @staticmethod
    def getGpuTemp():
        return Gpu.GPUs[0].temperature



print(Gpu.getGpuLoad())
print(Gpu.getGpuMemoryUsed())

print(Gpu.getGpuName())
print(Gpu.getGpuTemp())