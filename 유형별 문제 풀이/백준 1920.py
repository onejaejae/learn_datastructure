# 특정 정수의 등장 여부만을 간단히 체크하면 된다.
# Python에서는 dictionary 자료형을 해시처럼 사용할 수 있습니다.
# 본 문제는 set 자료형을 이용해 더욱 간단히 풀 수 있습니다.

# dictionary를 이용한 풀이
n = int(input())
n_list = list(map(int, input().split()))

n_hash = dict()
for i in range(n):
    n_hash[hash(n_list[i])] = n_list[i]

m = int(input())
m_list = list(map(int, input().split()))

for j in range(m):
    if(hash(m_list[j]) in n_hash):
        print(1)
    else:
        print(0)

# set을 이용한 풀이
# set은 중복을 제거하므로
n = int(input())
array = set(map(int, input().split()))
m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i not in array:
        print(0)
    else:
        print(1)
