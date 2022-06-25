# 데이터의 개수가 1,000개 이하이므로 기본적인 정렬 알고리즘으로 해결할 수 있다

# 파이썬의 기본 정렬 알고리즘을 이용해 문제 해결하기
n = int(input())

array = list()
for i in range(n):
    array.append(int(input()))

array.sort()
for data in array:
    print(data)

# 선택 정렬 알고리즘으로 문제 해결하기
n = int(input())
array = list()

for _ in range(n):
    array.append(int(input()))

for j in range(n):
    lowest = j
    
    for k in range(lowest+1, len(array)):
        if array[lowest] > array[k]:
            lowest = k
    
    array[j], array[lowest] = array[lowest], array[j]

for i in array:
    print(i)