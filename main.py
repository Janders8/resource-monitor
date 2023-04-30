from ram import Ram
from cpu import Cpu

df = Cpu.initiateMonitor()

while True:


    df.loc[len(df)] = Cpu.getThreadUsage()

    print(df)