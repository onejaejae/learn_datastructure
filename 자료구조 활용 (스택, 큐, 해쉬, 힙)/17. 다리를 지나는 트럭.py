def solution(bridge_length, weight, truck_weights):
    
    answer = 0
    bridge = [0 for _ in range(bridge_length)]

    while truck_weights:
        answer += 1

        bridge.pop()
        if sum(bridge) + truck_weights[0] <= weight:
            t = truck_weights.pop(0)
            bridge.append(t)
        else:
            bridge.append(0)
    return answer

print(solution(2,10,[7,4,5,6]))