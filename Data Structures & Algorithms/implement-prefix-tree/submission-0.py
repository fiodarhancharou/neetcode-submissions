class Trie():
    def __init__(self, val=None, childs=None, end=False):
        self.val = val
        self.childs = childs
        self.end = end

class PrefixTree:

    def __init__(self):
        self.head = Trie(childs={})

    def dfs(self, head):
        if not head:
            return
        self.dfs(head.childs[""])

    def insert(self, word: str) -> None:
        cur = self.head
        for l in word:
            if l not in cur.childs:
                cur.childs[l] = Trie(l,{})
            cur = cur.childs[l]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.head
        for l in word:
            if l not in cur.childs:
                return False
            cur = cur.childs[l]
        return cur.end

    def startsWith(self, prefix: str) -> bool:
        cur = self.head
        for l in prefix:
            if l not in cur.childs:
                return False
            cur = cur.childs[l]
        return True
        