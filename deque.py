class Deque:
    def __init__(self):
        self.data = []

    def add_rear(self, value):
        self.data.append(value)

    def add_front(self, value):
        self.data.insert(0, value)

    def delete_rear(self):
        if self.isEmpty():
            print("데이터 없음")
        else:
            self.data.pop(-1)

    def delete_front(self):
        if self.isEmpty():
            print("데이터 없음")
        else:
            self.data.pop(0)

    def isEmpty(self):
        if len(self.data) == 0:
            return True
        else:
            return False
        
    def front(self):
        if self.isEmpty():
            print("데이터 없음")
        else:
            return(self.data[0])
        
    def back(self):
        if self.isEmpty():
            print("데이터 없음")
        else:
            return(self.data[-1])
        
    def print(self):
        print(self.data)

deque = Deque() 
deque.add_rear(1)
deque.add_rear(2)
deque.add_rear(3)
deque.add_front(0)
deque.delete_front()
deque.delete_rear()
deque.print() 