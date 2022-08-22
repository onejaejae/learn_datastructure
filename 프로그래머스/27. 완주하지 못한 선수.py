from collections import defaultdict
def solution(participant, completion):
    answer = ""
    dic = defaultdict(int)
    for p in participant:
        dic[p] += 1
    
    for c in completion:
        dic[c] -= 1
    
    for key, value in dic.items():
        if value != 0:
            answer = key
            break
    return answer

print(solution(	["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))