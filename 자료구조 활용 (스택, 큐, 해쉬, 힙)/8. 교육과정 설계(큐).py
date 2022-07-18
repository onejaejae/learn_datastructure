# import sys
# sys.stdin = open("C:\workspaces\자료구조\자료구조 활용 (스택, 큐, 해쉬, 힙)\input.txt", "rt")
from collections import deque

essential = list(input())
dq = deque(essential)
n = int(input())

for i in range(n):
    class_design = input()
    class_design = deque(class_design)

    while class_design:
        if class_design[0] in dq:
            if class_design.popleft() != dq.popleft():
                print("#%d NO" %(i+1))
                break
        else:
            class_design.popleft()
    else:
        if dq:
            print("#%d NO" %(i+1))
        else:
            print("#%d YES" %(i+1))
    dq = deque(essential)

# 해설 풀이
need = input()

for i in range(n):
    plan = input()
    dq = deque(need)

    for x in plan:
        if x in dq:
            if x != dq.popleft():
                print("#%d NO" %(i+1))
                break
    else:
        if dq:
            print("#%d NO" %(i+1))
        else:
            print("#%d YES" %(i+1))
