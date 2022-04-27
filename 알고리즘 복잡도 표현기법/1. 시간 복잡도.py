# 1부터 n까지의 합을 구하는 알고리즘 1
# 입력 n에 따라 덧셈을 n번 해야 함
# 시간 복잡도 : n, 빅 오 표기법으로는 O(n)

def sum_all(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum

print(sum_all(5))


# 1부터 n까지의 합을 구하는 알고리즘 2
# 입력 n이 어떻든 간에, 곱셈/덧셈/나눗셈 하면 됨(반복문이 없음)
# 시간 복잡도 : 1, 빅 오 표기법으로는 O(1)
def sum_all2(n):
    return int(n * (n+1) /2)
print(sum_all(5))