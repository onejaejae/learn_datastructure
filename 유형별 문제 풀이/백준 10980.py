# 데이터의 개수가 최대 10,000,000 개이다.
# 시간 복잡도 O(N)의 정렬 알고리즘을 이용해야한다.
# 수의 범위가 1 ~ 10,000이므로 계수 정렬을 이용할 수 있다.
# 유의 사항: 데이터의 개수가 많을 때 파이썬에서는 sys.stdin.readline()을 사용해야 한다.

# 내 풀이 (메모리 초과)
# list의 중복이 들어가면 메모리 양이 커지므로 -> 계수 정렬 이용
n = int(input())
array = list()
for i in range(n):
    array.append(int(input()))

def qsort(data):
    if len(data) <= 1:
        return data
    
    pivot = data[0]
    left = [item for item in data[1:] if pivot > item]
    right = [item for item in data[1:] if pivot <= item]

    return qsort(left) + [pivot] + qsort(right)

array = qsort(array)
for j in array:
    print(j)

# 해설 풀이
import sys

n = int(sys.stdin.readline())
array = [0] * 10001

for i in range(n):
    data = int(sys.stdin.readline())
    array[data] += 1

for i in range(10001):
    if array[i] != 0:
        for j in range(array[i]):
            print(i)