# https://dongdongfather.tistory.com/69
from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    user = defaultdict(set)
    cnt = defaultdict(int)

    for r in report:
        a,b = r.split()
        
        # user의 기본 값은 set
        # set은 add를 사용해서 항목 추가, list는 append를 사용해서 항목 추가(defaultdict에서 제공)
        user[a].add(b)
        cnt[b] += 1

    for id in id_list:
        result = 0
        for u in user[id]:
            if cnt[u] >= k:
                result += 1
        answer.append(result)

    return answer


print(solution(	["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))