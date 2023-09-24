class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        if self.isEmpty():
            print("데이터 없음")
        else:
            data_pop = self.data.pop(0)
            return data_pop

    def isEmpty(self):
        if len(self.data) == 0:
            return True
        else:
            return False

    def front(self):
        if self.isEmpty():
            print("데이터 없음")
        else:
            return self.data[0]

    def back(self):
        if self.isEmpty():
            print("데이터 없음")
        else:
            return self.data[-1] 

    def print(self):
        print(self.data)

queue = Queue() 
queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue())