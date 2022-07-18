import sys
sys.stdin = open("C:\workspaces\자료구조\자료구조 활용 (스택, 큐, 해쉬, 힙)\input.txt", "rt")
from collections import deque

n,m = map(int, input().split())
# cnt = 0
# dq = list(map(int, input().split()))
# dq = deque(dq)

# while True: 
#     if m == 0:
#         if max(dq) == dq[0]:
#             cnt += 1
#             print(cnt)
#             exit()
#         else:
#             m = len(dq) -1
#             dq.append(dq.popleft())
#     else:
#         if max(dq) == dq[0]:
#             cnt += 1
#             dq.popleft()
#             m -= 1
#         else:
#             dq.append(dq.popleft())
#             m -= 1

# 해설 풀이

Q = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
print(Q)

