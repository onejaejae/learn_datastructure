# import sys
import heapq as hq
# sys.stdin = open("C:\workspaces\자료구조\자료구조 활용 (스택, 큐, 해쉬, 힙)\input.txt", "rt")

arr = []

while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(arr) == 0:
            print(-1)
        else:
            print(-hq.heappop(arr))
    else:
        hq.heappush(arr, -n)