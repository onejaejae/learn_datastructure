# import sys
# sys.stdin = open("C:\workspaces\자료구조\유형별 문제 풀이\input.txt", "rt")

n = int(input())
array = [list(map(int ,input().split())) for _ in range(n)]
cnt = 0

array.append([0]*n)
array.insert(0, [0]*n)

for i in range(n):
    array[i].insert(0,0)
    array[i].append(0)


# 나의 풀이
for i in range(1,n+1):
    for j in range(1,n+1):
        if array[i][j] > array[i-1][j] and array[i][j] > array[i+1][j] and array[i][j] > array[i][j-1] and array[i][j] > array[i][j+1]:
            cnt += 1

print(cnt)

# 해설 풀이
dx = [-1, 0, 1, 0]
dy = [0, 1, 0,-1]
for i in range(1, n+1):
    for j in range(1, n+1):
        # 모든 경우가 참일 때, all은 True를 반환
        if all(array[i][j] > array[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt += 1

    