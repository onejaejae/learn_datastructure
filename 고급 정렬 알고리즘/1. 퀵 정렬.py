import random

def qsort(data):
    if len(data) <= 1:
        return data
    
    left, right = list(), list()
    pivot = data[0]

    for i in range(1, len(data)):
        if pivot > data[i]:
            left.append(data[i])
        else:
            right.append(data[i])
    
    return qsort(left) + [pivot] + qsort(right)

data_list = random.sample(range(100), 10)
print(qsort(data_list))

# 위 퀵정렬 코드를 파이썬 list comprehension을 사용해서 더 깔끔하게 작성해보기
def qsort2(data):
    if len(data) <= 1:
        return data
    
    pivot = data[0]
    left = [item for item in data[1:] if pivot > item]
    right = [item for item in data[1:] if pivot <= item]

    return qsort(left) + [pivot] + qsort(right)

data_list = random.sample(range(100), 10)
print(qsort(data_list))
