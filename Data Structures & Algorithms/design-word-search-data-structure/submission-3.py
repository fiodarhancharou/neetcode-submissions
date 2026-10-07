class Node():
    def __init__(self, val=None):
        self.val = val
        self.childs = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.head = Node()

    def addWord(self, word: str) -> None:
        p = 0
        cur = self.head
        while p < len(word):
            if word[p] not in cur.childs:
                cur.childs[word[p]] = Node(word[p])
            cur = cur.childs[word[p]]
            if p == len(word) - 1:
                cur.is_end = True
            p += 1

    def dfs(self, head, p):
        if p == len(self.word):
            if head.is_end:
                return True
            return False
        if not self.word[p] == ".":
            if self.word[p] in head.childs:
                if self.dfs(head.childs[self.word[p]], p+1):
                    return True
            else:
                return False
        else:
            for child in head.childs:
                if self.dfs(head.childs[child], p+1):
                    return True
        return False

    def search(self, word: str) -> bool:
        self.word = word
        self.dfs(self.head, 0)
        return self.dfs(self.head, 0)
