# import sys
# sys.stdin = open("C:\workspaces\자료구조\유형별 문제 풀이\input.txt", "rt")

array = [list(map(int, input().split())) for _ in range(9)]


result = [0] * 9
result2 = [0] * 9

for i in range(9):
    result = [0] * 9
    result2 = [0] * 9

    for j in range(9):
        result[array[i][j] -1] += 1
        result2[array[j][i] -1] += 1
    if 0 in result or 0 in result2:
        print("NO")
        exit()

result = [0] * 9
result2 = [0] * 9
result3 = [0] * 9
result4 = [0] * 9
result5 = [0] * 9

for i in range(3):
    for j in range(3):
        result[array[i][j]-1] +=1
        result2[array[i][(j*-1)-1]-1] +=1
        result3[array[(i*-1) -1][j]-1] +=1
        result4[array[(i*-1) -1][(-1*j)-1]-1] +=1
        result5[array[i+3][j+3]-1] +=1

if 0 in result or 0 in result2 or 0 in result3 or 0 in result4 or 0 in result5:
    print("NO")
    exit()

print("YES")
