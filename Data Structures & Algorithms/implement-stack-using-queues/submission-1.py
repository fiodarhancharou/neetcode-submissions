from queue import Queue
class MyStack:

    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()
    def push(self, x: int) -> None:
        self.queue1.put(x)

    def pop(self) -> int:
        size = self.queue1.qsize()
        for _ in range(size-1):
            self.queue1.put(self.queue1.get())
        res = self.queue1.get()
        return res

    def top(self) -> int:
        res = self.pop()
        self.queue1.put(res)
        return res

    def empty(self) -> bool:
        return self.queue1.empty()  


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()