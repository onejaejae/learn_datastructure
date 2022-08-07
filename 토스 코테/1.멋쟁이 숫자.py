def solution(s):
    i = 0
    max = -216000
   

    while i < len(s) -2:
        if s[i] == s[i+1] and s[i+1] == s[i+2] and s[i] == s[i+2]:
            if max < int(s[i:i+3]):
                max = int(s[i:i+3])
        i+=1
    
    if max == -216000:
        return -1
    elif max == 000:
        return 0
    else:
        return max
   

print(solution("111999333"))