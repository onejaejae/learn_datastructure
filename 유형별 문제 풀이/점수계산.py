import sys
sys.stdin = open("C:\workspaces\자료구조\유형별 문제 풀이\input.txt", "rt")

# 나의 풀이
# n = int(input())
# result = list(map(int, input().split()))
# score = [0] * n

# for i in range(n):
#     if i == 0 and result[i] == 1:
#         score[i] = 1  
#     elif result[i] == 1:
#         score[i] = score[i-1] + 1
#     else:
#         result[i] = 0


# sum = 0
# for x in score:
#     sum += x
# print(sum)

# 해설 풀이
n = int(input())
result = list(map(int, input().split()))
sum = 0
cnt = 0

for x in result:
    if x == 1:
        cnt += 1
        sum += cnt
    else:
        cnt = 0

print(sum)