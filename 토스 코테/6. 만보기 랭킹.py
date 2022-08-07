def solution(steps_one, names_one, steps_two, names_two, steps_three, names_three):
    dic =dict()
    answer = []
    for i in range(len(names_one)):
        dic[names_one[i]] = dic.get(names_one[i], 0) + steps_one[i]

    for j in range(len(names_two)):
          dic[names_two[j]] = dic.get(names_two[j], 0) + steps_two[j]

    for k in range(len(names_three)):
        dic[names_three[k]] = dic.get(names_three[k], 0) + steps_three[k]
    
    dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
    for x in dic:
        answer.append(x[0])
        
    return answer

print(solution([1, 2, 3], ["james", "bob", "alice"], [10, 20, 30], ["james", "alice", "bob"], [1000, 1, 1], ["bob", "alice", "james"]))