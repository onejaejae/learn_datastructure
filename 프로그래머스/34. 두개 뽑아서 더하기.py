# def solution(numbers):
#     answer = set()
#     res = [0] * 2
#     def DFS(L,S):
#         if L==2:
#             answer.add(sum(res))
#         else:
#             for i in range(S, len(numbers)):
#                 res[L] = numbers[i]
#                 DFS(L+1, i+1)
#     DFS(0,0)
#     return sorted(list(answer))

from itertools import combinations
def solution(numbers):
    answer = set()
    for i in combinations(numbers, 2):
        answer.add(sum(i))

    return sorted(list(answer))

print(solution([2, 1, 3, 4, 1]))