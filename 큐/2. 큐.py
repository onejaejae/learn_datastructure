#  LifoQueue()로 큐 만들기 (LIFO(Last-In, First-Out))

import queue
data_queue = queue.LifoQueue()

data_queue.put(10)
data_queue.put(20)

print(data_queue.qsize())
print(data_queue.get())

# PriorityQueue()로 큐 만들기
Queue = queue.PriorityQueue()

# tuple 형태로 첫번째 변수에는 우선순위, 두번째 변수에는 값을 넣는다
Queue.put((10, "korea"))
Queue.put((5,1))
Queue.put((15,"China"))

print(Queue.qsize())
print(Queue.get())

# 리스트 변수로 큐를 다루는 enqueue, dequeue 기능 구현해보기
queue_list = list()

def enqueue(data):
    queue_list.append(data)

def dequeue():
    data = queue_list[0]
    queue_list.pop(0)
    return data

for index in range(10):
    enqueue(index)

print(len(queue_list))
print(dequeue())
print(len(queue_list))