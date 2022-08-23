# 나의 풀이
# def solution(dartResult):
#     res = []
#     cnt = 0
#     start = 0

#     for i in range(start, len(dartResult)):
#         str = dartResult[i]
#         k = i+1
#         if str.isdigit():
#             if dartResult[i+1] == '0':
#                 res.append(int(str)*10)
#                 k = i+2
#             else:
#                 res.append(int(str))
#             for j in range(k, len(dartResult)):
#                 next_str = dartResult[j]
#                 if next_str.isdigit():
#                     break
#                 else:
#                     if next_str.isalpha():
#                         if next_str == "D":
#                             res[cnt] **= 2
#                         elif next_str == "T":
#                             res[cnt] **= 3
#                     else:
#                         if next_str == "*":
#                             if cnt == 0:
#                                 res[cnt] *= 2
#                             else:
#                                 res[cnt] *= 2
#                                 res[cnt-1] *= 2
#                         elif next_str == "#":
#                             res[cnt] *= -1
#             cnt+=1
    
#     return sum(res)

# 다른 풀이
def solution(dartResult):
    n = ''
    score = []
    for i in dartResult:
        if i.isnumeric():
            n += i
        elif i == 'S':
            n = int(n)**1
            score.append(n)
            n = ''
        elif i == 'D':
            n = int(n)**2
            score.append(n)
            n = ''
        elif i == 'T':
            n = int(n)**3
            score.append(n)
            n = ''
        elif i == '*':
            if len(score) > 1:
                score[-2] = score[-2] * 2
                score[-1] = score[-1] * 2
            else:
                score[-1] = score[-1] * 2
        elif i == '#':
            score[-1] = score[-1] * -1
        
    return sum(score)
    

print(solution("10D10S0D"))