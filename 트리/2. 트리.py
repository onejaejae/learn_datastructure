# 이진 탐색 트리 삭제 코드 구현과 분석

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class NodeMgmt:
    def __init__(self, head):
        self.head = head
    
    def insert(self, value):
        self.current_node = self.head
        while True:
            if self.current_node.value > value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    def search(self, value):
        self.current_node = self.head
        
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif self.current_node.value > value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False

    def delete(self, value):
        searched = False
        self.current_node = self.head
        self.parent = self.head

        # 삭제 할 Node가 존재하는지 탐색
        while self.current_node:
            if self.current_node.value == value:
                searched = True
                break
            elif self.current_node > value:
                self.parent =  self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent =  self.current_node
                self.current_node = self.current_node.right

        if searched == False:
            return False
        
        # CASE 1: 삭제할 Node가 Leaf Node인 경우
        if self.current_node.left == None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None
            del self.current_node
        
        # CASE 2: 삭제할 Node가 Child Node를 한 개 가지고 있는 경우
        # 왼쪽 Child Node를 가지고 있는 경우
        elif self.current_node.left != None and self.current_node.right ==None:
            if value < self.parent.value:
                self.parent.left = self.current_node.left
            else:
                self.parent.right = self.current_node.left 
         # 오른쪽 Child Node를 가지고 있는 경우
        elif self.current_node.left == None and self.current_node.right != None:
            if value < self.parent.value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right

        # 삭제 할 Node가 Child Node를 두 개 가지고 있을 경우(삭제 할 Node가 Parent Node 왼쪽에 있을 때)
            # 전략 - 삭제 할 Node의 오른쪽 자식 중, 가장 작은 값을 삭제 할 Node의 Parent Node가 가리키도록 한다.
        elif self.current_node.left != None and self.current_node.right != None:
            if value < self.parent.value:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right

                while self.change_node.left != None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                
                # 삭제 할 Node가 Parent Node의 왼쪽에 있고, 삭제 할 Node의 오른쪽 자식 중, 가장 작은 값을 가진 Node의 오른쪽에 Child Node가 있을 때
                # 가장 작은 값을 가진 Node의 Child Node가 왼쪽에 있을 경우는 없음, 왜냐하면 왼쪽 Node가 있다는 것은 해당 Node보다 더 작은 값을 가진 Node가 있다는 뜻이기 때문
                if self.change_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                # 삭제 할 Node가 Parent Node의 왼쪽에 있고, 삭제 할 Node의 오른쪽 자식 중, 가장 작은 값을 가진 Node의 Child Node가 없을 때
                else:
                    self.change_node_parent.left = None

                self.parent.left = self.change_node
                self.change_node.left = self.current_node.left
                self.change_node_right = self.change_node.right

            # 삭제 할 Node가 Child Node를 두 개 가지고 있을 경우(삭제 할 Node가 Parent Node 오른쪽에 있을 때)
            else:
                self.change_node = self.change_node.right
                self.change_node_parent = self.change_node.right

                while self.change_node.left != None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                
                if self.change_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None
                
                self.parent.right = self.change_node
                self.change_node.left = self.current_node.left
                self.change_node.right = self.current_node.right

        return True

