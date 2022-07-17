import sys
sys.stdin = open("C:\workspaces\자료구조\자료구조 활용 (스택, 큐, 해쉬, 힙)\input.txt", "rt")

s = input()
stack = []
cnt = 0

for i in range(len(s)):
    if s[i] == "(":
        stack.append(s[i])
    else:
        stack.pop()
        if s[i-1] == "(":
            cnt += len(stack)
        else:
            cnt += 1

print(cnt)
