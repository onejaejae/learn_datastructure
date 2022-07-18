import sys
sys.stdin = open("C:\workspaces\자료구조\자료구조 활용 (스택, 큐, 해쉬, 힙)\input.txt", "rt")

n,k = map(int,input().split())
array = [i for i in range(1,n+1)]
cnt = 0

while len(array) > 1:
    cnt += 1
        
    if cnt == k:
        cnt = 0
        array.pop(0)
    else:
        array.append(array.pop(0))

print(array[0])

# 해설 풀이
from collections import deque
dq = list(range(1, n+1))
dq = deque(dq)

while dq:
    for _ in range(k-1):
        dq.append(dq.popleft())
    dq.popleft()

    if len(dq) == 1:
        print(dq[0])
        dq.popleft()