# 힙에 데이터 삽입 구현 (Max Heap 예)
from operator import truediv


class Heap:
    def __init__(self,data):
        self.heap_array = list() 
        # 힙 구현의 편의를 위해, root node index 번호를 1로 지정
        self.heap_array.append(None)
        self.heap_array.append(data)    
    
    def move_up(self, inserted_idx):
        if inserted_idx <= 1:
            return False
        
        parent_idx = inserted_idx // 2
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:
            return True
        else:
            return False


    def insert(self, data):
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True
        
        self.heap_array.append(data)
        # 0번 index의 None 값이 들어가있으므로
        inserted_idx = len(self.heap_array) -1

        # 자식 node가 부모 node 값보다 크다면 swap
        while self.move_up(inserted_idx):
            parent_idx = inserted_idx // 2
            # swap
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx] ,self.heap_array[inserted_idx]
            inserted_idx = parent_idx



        return True

heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
print(heap.heap_array)

