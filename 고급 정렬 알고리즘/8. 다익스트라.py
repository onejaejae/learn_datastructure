# heapq 라이브러리 활용을 통해 우선순위 큐 사용하기
# 우선순위 큐 -> 최소 힙의 구조를 가지고 있는 우선 순위 큐
from collections import deque
import heapq
from turtle import distance

queue = []
heapq.heappush(queue, [2, 'A'])
heapq.heappush(queue, [5, 'B'])
heapq.heappush(queue, [1, 'C'])
heapq.heappush(queue, [7, 'D'])

for index in range(len(queue)):
    print(heapq.heappop(queue))

# 다익스트라 알고리즘
mygraph = {
    'A' : { 'B' : 8, 'C': 1, 'D': 2},
    'B' : {},
    'C' : { 'B' : 5, 'D': 2},
    'D' : { 'E' : 3, 'F': 5},
    'E' : {'F' : 1},
    'F' : {'A': 5}
}

def dijkstra(graph, start):
    # distances = { node: inf} 형태로 저장됨, node는 graph의 키 값
    distances = { node : float('inf') for node in graph}
    
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])
   
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        if distances[current_node] < current_distance:
            continue

        # 딕셔너리(dictionary)는 items()함수를 사용하면 딕셔너리에 있는 키와 값들의 쌍을 얻을 수 있습니다. 
        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])
    
    return distances

print(dijkstra(mygraph, 'A'))