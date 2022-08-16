from collections import defaultdict
def solution(n,words):
    dict = defaultdict(int)
    dict[0] = 1
    res = 0

    for i in range(1, n):
        dict[i]

    for index in range(1,len(words)):
        dict[(index) % n] += 1
        if words[index][0] != words[index-1][-1]:
            print(dict)
            res = (index) % n
            break
        if words[index] in words[:index]:
            res = (index) % n
            break
    else:
        return [0,0]
    
    return [res+1, dict[res]]

print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))