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

    def move_down(self, poped_idx):
        left_child_poped_idx = poped_idx * 2
        right_child_poped_idx = (poped_idx * 2) + 1

        # CASE 1: 왼쪽 자식 노드가 없을 때
        if left_child_poped_idx >= len(self.heap_array):
            return False
        # CASE 2: 오른쪽 자식 노드만 없을 때
        elif right_child_poped_idx >= len(self.heap_array):
            if self.heap_array[poped_idx] < self.heap_array[right_child_poped_idx]:
                return True
            else:
                return False 
        # CASE 3: 왼쪽, 오른쪽 자식 노드 모두 있을 때
        else:
            if self.heap_array[left_child_poped_idx] > self.heap_array[right_child_poped_idx]:
                if self.heap_array[poped_idx] < self.heap_array[left_child_poped_idx]:
                    return True
                else:
                    return False
            else:
                if self.heap_array[poped_idx] < self.heap_array[right_child_poped_idx]:
                    return True
                else:
                    return False

    def pop(self):
        # 0번 index의 None 값이 들어가있으므로
        if len(self.heap_array) <= 1:
            return None

        returned_data = self.heap_array[1]
        # -1은 마지막 index
        self.heap_array[1] = self.heap_array[-1]
        del self.heap_array[-1]
        
        poped_idx = 1
        while self.move_down(poped_idx):
            left_child_poped_idx = poped_idx * 2
            right_child_poped_idx = (poped_idx * 2) + 1

            # CASE 1: 왼쪽 자식 노드가 없을 때
            if left_child_poped_idx >= len(self.heap_array):
                return False
            
            # CASE 2: 오른쪽 자식 노드만 없을 때
            elif right_child_poped_idx >= len(self.heap_array):
                if self.heap_array[poped_idx] < self.heap_array[left_child_poped_idx]:
                    self.heap_array[poped_idx], self.heap_array[left_child_poped_idx] = self.heap_array[left_child_poped_idx], self.heap_array[poped_idx] 
                    poped_idx = left_child_poped_idx
            
             # CASE 3: 왼쪽, 오른쪽 자식 노드 모두 있을 때
            else:
                if self.heap_array[left_child_poped_idx] > self.heap_array[right_child_poped_idx]:
                    if self.heap_array[poped_idx] < self.heap_array[left_child_poped_idx]:
                        self.heap_array[poped_idx], self.heap_array[left_child_poped_idx] = self.heap_array[left_child_poped_idx], self.heap_array[poped_idx]
                        poped_idx = left_child_poped_idx
                else:
                    if self.heap_array[poped_idx] < self.heap_array[right_child_poped_idx]:
                        self.heap_array[poped_idx], self.heap_array[right_child_poped_idx] = self.heap_array[right_child_poped_idx], self.heap_array[poped_idx]
                        poped_idx = right_child_poped_idx
                   
        return returned_data


heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
heap.pop()
print(heap.heap_array)

