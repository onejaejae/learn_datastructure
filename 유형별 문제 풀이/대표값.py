#import sys
#sys.stdin = open("C:\workspaces\자료구조\유형별 문제 풀이\input.txt", "rt")

n = int(input())
score = list(map(int, input().split()))

math_avg = round(sum(score) / n)

for i, data in enumerate(score):
    score[i] = (i, data, abs(data-math_avg))
#https://gorokke.tistory.com/38
score = sorted(score, key=lambda x: (x[2], -x[1], x[0]))
print(math_avg, score[0][0] +1)