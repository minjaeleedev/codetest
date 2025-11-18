import sys
import re

N = int(sys.stdin.readline().strip())
histories = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

result = None
table = []
for i in range(6):
    ls = []
    for j in range(10):
        ls.append(set())

    table.append(ls)

for i, history in enumerate(histories):
    for grade, cl in enumerate(history):
        table[grade + 1][cl].add(i + 1)

same = [0] * (N + 1)
for i, history in enumerate(histories):
    student = set()
    for grade, cl in enumerate(history):
        sames = table[grade + 1][cl] - set([i + 1])
        student = student | sames

    same[i + 1] = len(student)

mx = 0
result = 0
for i in range(N):
    if mx < same[i]:
        result = i
        mx = same[i]

print(result)
