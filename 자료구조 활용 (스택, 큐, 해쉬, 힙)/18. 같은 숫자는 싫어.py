def solution(arr):
    answer = []
    i = 0
    while i < len(arr)-1:
       
        if arr[i] == arr[i+1]:
            if arr[i] not in answer:
                answer.append(arr[i])
                
        i+=1
    
    return answer

print(solution([1,1,3,3,0,1,1]))