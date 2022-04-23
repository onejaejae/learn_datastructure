# 링크드리스트 데이터 사이에 데이터를 추가
class Node:
    def __init__(self,data,next=None):
            self.data =data
            self.next = next

def add(data):
    node = head
    # 마지막 노드를 찾는 반복문
    while node.next:
        node = node.next
    # 마지막 노드에 새로운 노드의 주소값을 가리키도록 함
    node.next = Node(data)

node1 = Node(1)
node2 = Node(2)
node1.next = node2
head = node1

for index in range(3, 11):
    add(index)

node3 = Node(1.5)

node = head
search = True
while search:
    if node.data == 1:
        search = False
    else:
        node = node.next 

node_next = node.next
node.next = node3
node3.next = node_next

node = head
while node.next:
    print(node.data)
    node = node.next
