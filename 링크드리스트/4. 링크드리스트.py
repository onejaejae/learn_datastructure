# 링크드리스트의 복잡한 기능 2 (특정 노드를 삭제)
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def search_node(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next

    def delete(self, data):
        if self.head == '':
            print("해당 값을 가진 노드가 없습니다.")
            return
        
        # head를 삭제 할 경우
        if self.head.data == data:
            temp = self.head
            self.head = temp.next
            del temp
        # 마지막 노드, 중간 노드를 삭제 할 경우
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                else:
                    node = node.next

linkedList1 = NodeMgmt(0)

linkedList1.delete(0)
print(linkedList1.head)
            
linkedList1 = NodeMgmt(0)
for data in range(1, 10):
    linkedList1.add(data)


linkedList1.delete(4)
print(linkedList1.search_node(4))