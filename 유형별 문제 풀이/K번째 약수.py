# import sys
# sys.stdin = open("C:\workspaces\자료구조\유형별 문제 풀이\input.txt", "rt")

# 내 풀이
n, k = map(int, input().split())
array = list()

for i in range(1, n+1):
    if n % i == 0:
        array.append(i)

array.sort()
if len(array) < k:
    print(-1)
else:
    print(array[k-1])

# 해설 풀이
# for else 문
#