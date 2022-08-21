def solution(survey, choices):
    total_score = {'RT' : {'R':0, 'T':0}, 'CF' : {'C':0, 'F':0}, 'JM' : {'J':0, 'M':0}, 'AN' : {'A':0, 'N':0}}
    score = {1: 3, 2:2,3:1,4:0,5:1,6:2,7:3}

    answer = ''
    i = 0
    for s in survey:
        if 1 <= choices[i] <= 3:
            total_score[''.join(sorted(s))][s[0]] += score[choices[i]]
        elif 5 <= choices[i] <= 7:
            total_score[''.join(sorted(s))][s[1]] += score[choices[i]]
        i += 1
    
    for value in total_score.values():
        new_dict = sorted(value.items(), key=lambda x:(-x[1], x[0]))
        answer += new_dict[0][0]
    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))