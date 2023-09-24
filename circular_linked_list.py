class Node:
    def __init__(self, v):
        self.data = v
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None # 연결리스트의 첫번째 노드

    def getLength(self):
        if self.head == None:
            return 0
        else:
            len = 1
            curr = self.head
            while curr.next != self.head:
                len += 1
                curr = curr.next
            return len

    def insertFirst(self, value):
        new_node = Node(value)
        # 리스트가 비었을시
        if self.head == None:
            self.head = new_node
            new_node.next = self.head
        # 리스트가 안 비었을시
        else:
            # 마지막 노드 찾기
            curr = self.head
            while curr.next != self.head: # while curr != None:
                curr = curr.next

            new_node.next = self.head
            curr.next = new_node
            self.head = new_node

    def insertLast(self, value):
        new_node = Node(value)
        # 리스트가 비었을시
        if self.head == None:
            self.head = new_node
            new_node.next = new_node
        # 리스트가 안 비었을시
        else:
            curr = self.head
            while curr.next != self.head: 
                curr = curr.next
            curr.next = new_node
            new_node.next = self.head

    def insertAt(self, pos, value):
        if self.getLength() <= pos:
            print("out of index")
            return
        if self.head == None:
            print("데이터 없음")
        else:
            new_node = Node(value)
            # 첫번째에 추가
            if pos == 0:
                # 마지막 노드 찾기
                curr = self.head
                while curr.next != self.head:
                    curr = curr.next

                curr.next = new_node
                new_node.next = self.head
                self.head = new_node
            else:
                # new_node 앞노드 찾기
                curr = self.head
                for _ in range(pos - 1):
                    curr = curr.next

                new_node.next = curr.next
                curr.next = new_node

    def deleteAt(self, pos):
        if self.head == None:
            print("데이터 없음")
            return
        if self.getLength() <= pos:
            print("out of indext")
            return
        # 첫번째 노드 삭제
        if pos == 0:
            # 마지막 노드 찾기
            curr = self.head
            while curr.next != self.head:
                curr = curr.next

            curr.next = self.head.next
            self.head = self.head.next
        else:
            # 지우려는 노드 앞노드 찾기
            curr = self.head
            for _ in range(pos - 1):
                curr = curr.next

            remove = curr.next
            curr.next = remove.next

    def deleteFirst(self):
        if self.head == None:
            print("데이터가 없습니다.")
        # 노드가 한개만 있을때
        elif self.head == self.head.next:
            self.head = None
        # 노드가 두개 이상일때
        else:
            # 마지막 노드 찾기
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
        
            curr.next = self.head.next
            self.head = self.head.next

    def deleteLast(self):
        if self.head == None:
            print("데이터가 없습니다.")
        # 노드가 한개만 있을때
        elif self.head == self.head.next:
            self.head = None
        # 노드가 두개 이상일때
        else:
            # 마지막에서 앞에 노드 찾기
            prev = self.head
            while prev.next.next != self.head:
                prev = prev.next

            prev.next = self.head

    def showList(self):
        if self.head == None:
            print("데이터 없음")
        else:
            curr = self.head
            for _ in range(self.getLength()):
                print(curr.data, end = " ")
                if curr.next != self.head:
                    print("->", end = " ")  
                else:
                    print()
                curr = curr.next 

cll = CircularLinkedList()
cll.insertFirst(2)
cll.insertFirst(1)
cll.insertLast(3)
cll.insertAt(0, 0)
cll.showList()
cll.insertAt(3, 3.5)
cll.showList()
cll.deleteAt(3)
cll.showList()