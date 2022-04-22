# 파이썬 리스트 기능에서 제공하는 메서드로 스택 사용해보기
data_stack = list()

data_stack.append(1)
data_stack.append(2)

print(data_stack)
print(data_stack.pop())
print(data_stack.pop())

# 리스트 변수로 스택을 다루는 pop, push 기능 구현해보기 (pop, push 함수 사용하지 않고 구현해보기)
stack_list = list()

def push(data):
    stack_list.append(data)

def pop():
    # 맨 끝의 값은 -1로 나타낼 수 있다
    data = stack_list[-1]
    del stack_list[-1]
    return data

for index in range(10):
    push(index)

print(stack_list)
print(pop())
print(pop())
print(stack_list)


