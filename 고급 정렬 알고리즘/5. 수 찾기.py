# 백준 1920
N=5
N_list = [4,1,5,2,3]
M=5
M_list = [1,3,7,9,5]

#1) 시간 복잡도에서 실패
#for item in M_list:
#    if item in N_list:
#        print(1)
#    else:
#        print(0)

# 이진 탐색 사용
N_list.sort()

def binary_search(value, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2
    if N_list[mid] > value:
        end = mid - 1
        return binary_search(value, start , end)
    elif N_list[mid] < value:
        start = mid + 1
        return binary_search(value, start , end)
    else:
        return 1


for item in M_list:
    print(binary_search(item, 0, N - 1))