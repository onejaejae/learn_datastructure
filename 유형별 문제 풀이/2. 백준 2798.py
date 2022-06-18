N, M = map(int, input().split())
data = list(map(int, input().split()))

result = 0
length = len(data)
count = 0
print(length)
for i in range(0, length):
    for j in range(i+1, length):
        for k in range(j+1, length):
            print(i)
            sum_value = data[i] + data[j] + data[k]
            if sum_value <= M:
                result = max(result, sum_value)

print(result)

for i in range(9,8):
    print("asd")