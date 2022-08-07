from collections import deque

def solution(prices):
    dq = deque(prices)
    answer = []
    
    while dq:
        sec = 0
        price = dq.popleft()
        
        for x in dq:
            sec += 1
            if x < price:
                break
        answer.append(sec)

    return answer


print(solution([1, 2, 3, 2, 3]))