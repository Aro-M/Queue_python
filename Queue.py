class Queue:
    def __init__(self):
        self.value = []
    def enqueue(self,val):
        self.value.insert(0,val)
    def dequeue(self):
        self.value.pop(-1)
    def size(self):
        return len(self.value)
    def isEmpty(self):
        if len(self.value) == 0:
            return  True
        else:
            return False
    def clear(self):
        self.value = []
    def show(self):
       for x  in self.value:
            print(x ,  end ="  \n")


qt = Queue()
qt.enqueue(4)
qt.enqueue("sdadsxz")
qt.enqueue(55.5)
qt.enqueue(26)
qt.enqueue("aES")
qt.dequeue()
qt.dequeue()
print(qt.size())
print(qt.isEmpty())
qt.show()
