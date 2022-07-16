def solution(N):
    result = 0
    N = list(str(N))
    N.sort(reverse=True)
    
    for x in N:
        result = result * 10 + int(x)
    print(result) 
    

solution(553)
