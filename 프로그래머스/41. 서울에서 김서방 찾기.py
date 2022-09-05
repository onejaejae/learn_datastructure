def solution(seoul):
    answer = ""
    for index, value in enumerate(seoul):
        if value == 'Kim':
            answer = "김서방은 %d에 있다." %index
        
    return answer

print(solution(["Jane", "Kim"]))