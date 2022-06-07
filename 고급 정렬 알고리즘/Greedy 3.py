# 백준 11399
n = int(input())
s = list(map(int, input().split()))
s.sort()
minimum = 0

for index in range(n):
    for index2 in range(n+1):
        minimum += s[index2]

print(minimum)
