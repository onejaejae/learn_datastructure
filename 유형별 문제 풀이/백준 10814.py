# (나이, 이름)의 정보를 입력 받은 뒤에 나이를 기준으로 정렬합니다.
# 파이썬의 기본 정렬 라이브러리를 사용합니다.
# 나이가 동일한 경우, 먼저 입력된 이름 순서를 따르도록 key 속성을 설정해야 합니다.
# https://somjang.tistory.com/entry/Python-%EB%82%B4%EA%B0%80-%EC%9B%90%ED%95%98%EB%8A%94-%EC%88%9C%EC%84%9C%EB%8C%80%EB%A1%9C-%EB%A6%AC%EC%8A%A4%ED%8A%B8%EB%A5%BC-%EC%A0%95%EB%A0%AC%ED%95%98%EB%8A%94-%EB%8B%A4%EC%96%91%ED%95%9C-%EB%B0%A9%EB%B2%95

# 내 풀이
n = int(input())
array = list()

for _ in range(n):
    array.append(input().split())

array = [[i, int(data[0]), data[1]] for i, data in enumerate(array)]
array.sort(key=lambda x: (x[1], x[0]))

for data in array:
    print(data[1], data[2])

# 해설 풀이
n = int(input())
array = list()

for _ in range(n):
    input_data = input().split()
    array.append((int(input_data[0]), input_data[1]))

# python 정렬 라이브러리 특성 => stable한 속성
# 기본적으로 원래 앞에 있던 원소가 정렬된 이후에도 앞에 들어가도록 된다. (파이썬 기본 정렬 라이브러리 특성)
array = sorted(array, key=lambda x: x[0])

for i in array:
    print(i[0], i[1])