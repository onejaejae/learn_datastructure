from array import array
from ntpath import join
import sys
sys.stdin = open("C:\workspaces\자료구조\자료구조 활용 (스택, 큐, 해쉬, 힙)\input.txt", "rt")

num, m = map(int ,input().split())
# str로 바꿔야 map이 하나하나 접근 가능
num = list(map(int, str(num)))
stack = []

for x in num:
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m-=1
    stack.append(x)

if m != 0:
    stack = stack[:-m]

res= "".join(map(str, stack))
print(res)