class Node:
    def __init__(self, v):
        self.data = v
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertFirst(self, value):
        new_node = Node(value)
        if self.head == None:
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.head.prev
            self.head.prev.next = new_node
            self.head.prev = new_node
            self.head = new_node

    def insertLast(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.head.prev
            self.head.prev.next = new_node
            self.head.prev = new_node

    def deleteFirst(self):
        if self.head == None:
            print("데이터가 없습니다")
        else:
            self.head.prev.next = self.head.next
            self.head.next.prev = self.head.prev
            # self.head.next = None
            # self.head.prev = None
            self.head = self.head.next

    def deleteLast(self):
        if self.head == None:
            print("데이터가 없습니다")
        else:
            self.head.prev.prev.next = self.head
            self.head.prev = self.head.prev.prev
            # self.head.prev.next = None
            # self.head.prev.prev = None

    def insertAt(self, pos, value):
        if self.getLength() <= pos:
            print("out of index")
            return
        
        new_node = Node(value)
        # 첫번째에 추가
        if pos == 0:    
            new_node.next = self.head
            new_node.prev = self.head.prev
            self.head.prev.next = new_node
            self.head.prev = new_node
            self.head = new_node
        else:
            # new_node.prev 찾기
            curr = self.head
            for _ in range(pos - 1):
                curr = curr.next
                
            new_node.next = curr.next
            new_node.prev = curr
            curr.next.prev = new_node
            curr.next = new_node

    def deleteAt(self, pos):
        if self.getLength() <= pos:
            print("out of index")
            return
        # 리스트가 비었을시
        if self.head == None:
            print("데이터가 없습니다")
        # 리스트가 안 비었을시
        else:
            # 첫번째 노드 삭제
            if pos == 0:
                self.head.prev.next = self.head.next
                self.head.next.prev = self.head.prev
                self.head = self.head.next
            else:
                # 지우려는 노드 앞 노드 찾기
                curr = self.head
                for _ in range(pos - 1):
                    curr = curr.next

                self.head.prev.prev = curr
                curr.next = curr.next.next

    def showList(self):
        if self.head == None:
            print("데이터가 없습니다.")
        else:
            curr = self.head
            for _ in range(self.getLength()):
                print(curr.data, end = " ")
                if curr.next != self.head:
                    print("<->", end = " ")
                else:
                    print()
                curr = curr.next

    def getLength(self):
        if self.head == None:
            return 0
        else:
            curr = self.head
            len = 1
            while curr.next != self.head:
                curr = curr.next
                len += 1
            return len
        
    def reverse(self):
        prev = self.head
        curr = self.head.prev
        next = curr.prev
        for _ in range(self.getLength()):
            curr.next = next
            curr.prev = prev
            curr = next
            prev = prev.prev
            next = next.prev
        self.head = curr

dll = DoublyLinkedList()
dll.insertFirst(2)
dll.insertFirst(1)
dll.insertLast(3)
dll.insertAt(0, 0)
dll.showList()
dll.insertAt(5, 4)
dll.showList()
dll.deleteAt(0)
dll.showList()
dll.deleteAt(4)
dll.showList()
dll.reverse()
dll.showList()