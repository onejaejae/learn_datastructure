import queue

data_queue = queue.Queue()
data_queue.put(10)
data_queue.put(20)

print(data_queue.qsize())
print(data_queue.get())
print(data_queue.get())