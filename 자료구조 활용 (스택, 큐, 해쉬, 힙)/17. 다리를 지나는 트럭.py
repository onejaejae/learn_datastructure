def solution(bridge_length, weight, truck_weights):
    
    answer = 0
    
    # 길이 제한 + 경과시간 구현 가능
    bridge = [0 for _ in range(bridge_length)]

    while bridge:
        answer += 1

        bridge.pop()
        
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                t = truck_weights.pop(0)
                bridge.append(t)
            else:
                bridge.append(0)

    return answer

print(solution(2,10,[7,4,5,6]))