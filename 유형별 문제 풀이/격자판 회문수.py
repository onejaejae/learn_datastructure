# import sys
# sys.stdin = open("C:\workspaces\자료구조\유형별 문제 풀이\input.txt", "rt")

# 나의 풀이
cnt = 0
array = [list(map(int, input().split())) for _ in range(7)]

for i in range(7):
    for j in range(3):
        for k in range(2):
            if array[i][j+k] != array[i][4+j-k]:
                break
        else:
            cnt += 1

for i in range(7):
    for j in range(3):
        for k in range(2):
            if array[j+k][i] != array[4+j-k][i]:
                break
        else:
            cnt += 1

print(cnt)

# 해설 풀이
for i in range(3):
    for j in range(7):
        tmp = array[j][i:i+5]
        if tmp == tmp[::-1]:
            cnt += 1