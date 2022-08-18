# 내 풀이
# def solution(lottos, win_nums):
#     rank = {
#         6 : 1,
#         5 : 2,
#         4 : 3,
#         3 : 4,
#         2 : 5,
#     }
#     zero_cnt = 0
#     same_cnt = 0

#     while 0 in lottos:
#         lottos.remove(0)
#         zero_cnt += 1

#     for l in lottos:
#         if l in win_nums:
#             same_cnt += 1
    
#     return [rank.get(zero_cnt + same_cnt, 6), rank.get(same_cnt,6)]

# 프로그래머스 풀이법
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)    # lottos 안의 0의 개수를 반환
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
            
    return rank[cnt_0 + ans],rank[ans]

print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))