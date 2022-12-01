from itertools import groupby; from stopwatch import Stopwatch
s = Stopwatch(1); s.start()
groups = [list(group) for empty, group in groupby([line.strip("\n") for line in open("2022/22DEC01/22DEC01.txt")], lambda line: not line.strip()) if not empty]
for x in range(len(groups)): groups[x] = sum([int(y) for y in groups[x]])
groups.sort(reverse=True)
print(f"Answer I  = {groups[0]}" + f", Answer II = {(groups[0] + groups[1] + groups[2])}")
s.stop()
print(s)