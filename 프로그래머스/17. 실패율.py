# 나의 풀이
# def solution(N, stages):
#     answer = []
#     res = []
   
#     for i in range(1, N+1):
#         tot = 0
#         same = 0
#         for s in stages:
#             if i <= s :
#                 tot += 1
#         same = stages.count(i)
#         if tot == 0:
#             answer.append((0,i))
#         else:
#             answer.append((same/tot, i))

#     answer = sorted(answer, key=lambda a : (-a[0], a[1]))
#     for a,b in answer:
#         res.append(b)
#     return res

def solution(n, stages):
    result = {}
    denominator = len(stages)
    
    for stage in range(1, n+1):
        if denominator != 0:
            cnt = stages.count(stage)
            result[stage] = cnt / denominator
            denominator -= cnt
        else:
            result[stage] = 0
    return sorted(result, key=lambda x: result[x], reverse=True)

print(solution(7, [2, 1, 2, 6, 2, 4, 3, 3]))