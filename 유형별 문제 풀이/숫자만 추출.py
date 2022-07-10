# import sys
# sys.stdin = open("C:\workspaces\자료구조\유형별 문제 풀이\input.txt", "rt")

s = input()
res = 0
cnt = 0
for x in s:
    if 48 <= ord(x) <= 57:
        x = int(x)
        res = res * 10 + x

for i in range(1, res+1):
    if res % i == 0:
        cnt += 1

print(res)
print(cnt)

