from queue import Queue
class MyStack:

    def __init__(self):
        self.queue = Queue()
    def push(self, x: int) -> None:
        self.queue.put(x)

    def pop(self) -> int:
        size = self.queue.qsize()

        for _ in range(size-1):
            self.queue.put(self.queue.get())
        res = self.queue.get()
        return res

    def top(self) -> int:
        res = self.pop()
        self.queue.put(res)
        return res

    def empty(self) -> bool:
        return self.queue.empty()  


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()