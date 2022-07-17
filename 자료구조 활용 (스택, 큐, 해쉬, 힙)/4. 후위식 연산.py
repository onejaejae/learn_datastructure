import sys
sys.stdin = open("C:\workspaces\자료구조\자료구조 활용 (스택, 큐, 해쉬, 힙)\input.txt", "rt")

str = input()
stack = []
result = 0

for x in str:
    if x.isdecimal():
        stack.append(int(x))
    else:
        p1 = stack.pop()
        p2 = stack.pop()

        if x == "+":
            result = p2 + p1
            stack.append(result)
        elif x == "-":
            result = p2 - p1
            stack.append(result)
        elif x == "*":
            result = p2 * p1
            stack.append(result)
        elif x == "/":
            result = p2 // p1
            stack.append(result)

print(stack[0])