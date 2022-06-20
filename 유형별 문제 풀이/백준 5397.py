test_case = int(input())

for _ in range(test_case):
    left_stack = []
    right_stack = []
    data = input()
    for i in data:
        if i == '-':
            if left_stack:
                left_stack.pop()
        elif i == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        elif i == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        else:
            left_stack.append(i)
    # list의 append로 구현하였으므로 뒤집어줘야함
    left_stack.extend(reversed(right_stack))
    # python join
    # https://blockdmask.tistory.com/468
    print(''.join(left_stack))