import DEC01.DEC01 as first
import DEC02.DEC02 as second
import DEC03.DEC03 as third
import time
from math import pow
times = []
days = [first, second, third]
for day in days:
    for x in range(10000):
        start = time.perf_counter() * 1000000
        day.main(pri=False)
        end = time.perf_counter() * 1000000
        times.append(end-start)
    print(f"{sum(times)/len(times)}µs")
    times.clear()