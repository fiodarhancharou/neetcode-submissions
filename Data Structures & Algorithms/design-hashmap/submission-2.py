class MyHashMap:

    def __init__(self):
        self.store = [False]*1000001

    def put(self, key: int, value: int) -> None:
        self.store[key] = value

    def get(self, key: int) -> int:
        if self.store[key] is not False:
            return self.store[key]
        return -1

    def remove(self, key: int) -> None:
        if self.store[key] is not False:
            self.store[key] = False


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)