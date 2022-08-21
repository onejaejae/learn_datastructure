# import math
# def DFS(L,S):
#     global cnt
#     if L == 3:
#         for i in range(2, int(math.sqrt(sum(res))) + 1):
#             if sum(res) % i == 0:
#                 break
#         else:
#             cnt+=1
#     else:
#         for i in range(S, n):
#             res[L] = arr[i]
#             DFS(L+1, i+1)
            

# if __name__ == "__main__":
#     cnt = 0
#     arr = list(map(int, input().split()))
#     n = len(arr)
#     res = [0] * 3
#     check = [0] * n

#     DFS(0,0)
#     print(cnt)

from itertools import combinations
import math
def solution(nums):
    answer = 0
    nums = list(combinations(nums, 3))
    for num in nums:
        for i in range(2, int(math.sqrt(sum(num)) +1)):
            if sum(num) % i == 0:
                break
        else:
            answer+=1
    return answer

print(solution([1,2,7,6,4]))