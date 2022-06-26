# (x 좌표, y 좌표)를 입력 받은 뒤, x 좌표, y 좌표 순서대로 차례대로 오름차순 정렬.
# 파이썬의 기본 정렬 라이브러리는 기본적으로 튜플의 인덱스 순서대로 오름차순 정렬
# 따라서 단순히 기본 정렬 라이브러리를 이용하면 된다 (key 속성 설정 없이)

# 내 풀이
n = int(input())
array = list()

for _ in range(n):
    input_data = input().split()
    array.append((int(input_data[0]), int(input_data[1])))

array.sort(key=lambda x: (x[0], x[1]))
for i in array:
    print(i[0], i[1])

# 해설 풀이
n = int(input())
array = list()

for _ in range(n):
    x, y = input().split()
    array.append((x, y))

array = sorted(array)
for i in array:
    print(i[0], i[1])