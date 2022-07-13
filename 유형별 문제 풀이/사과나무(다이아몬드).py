# import sys
# sys.stdin = open("C:\workspaces\자료구조\유형별 문제 풀이\input.txt", "rt")

# 나의 풀이
# n = int(input())
# array = [list(map(int, input().split())) for _ in range(n)]
# p1 = p2 = n // 2
# total = array[0][p1]

# for i in range(1, n):
#     if i > n // 2:
#         p1 += 1
#         p2 -= 1
#         for a in range(p1, p2+1):
#             total += array[i][a]
#     else:
#         p1 -= 1
#         p2 += 1
#         for b in range(p1, p2+1):
#             total += array[i][b]
# print(total)

for i in range(n):
    for j in range(p1, p2+1):
        total += array[i][j]
    if i//2 > i:
        p1 -= 1
        p2 += 1
    else:
        p1+=1
        p2-=1