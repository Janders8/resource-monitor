import psutil

class Disc:

    @staticmethod
    def getDiscUsage():
        return psutil.disk_usage('/')


