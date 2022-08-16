import itertools

def solution(str1, str2):
    answer = 0
    str1 = list(str1)
    str2 = list(str2)

    c_str1 = list(itertools.combinations(str1,2))
    c_str2 = list(itertools.combinations(str2,2))

    c_str1 = [ x.upper() + y.upper() for x,y in c_str1 if x.isalpha() and y.isalpha()]
    c_str2 = [x.upper() + y.upper() for x,y in c_str2 if x.isalpha() and y.isalpha()]
    
    intersection = list(set(c_str1) & set(c_str2))
    union = list(set(c_str1) | set(c_str2))
    
    print(union, intersection)
    answer = len(intersection) / len(union)
    return answer

print(solution("FRANCE", "french"))