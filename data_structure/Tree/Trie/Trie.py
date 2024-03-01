from collections import defaultdict
from collections import deque


class Node:
    def __init__(self, val=""):
        self.isWord = False
        self.next = defaultdict(Node)
        self.val = val


class Trie:
    def __init__(self):
        self.root = Node()
        self.count = 0

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.next:
                cur.next[c] = Node(cur.val + c)
            cur = cur.next[c]

        if not cur.isWord:
            cur.isWord = True
            self.count += 1

    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur.next:
                return False
            cur = cur.next[c]
        return cur.isWord
    
    def startWith(self, prefix):
        cur = self.root
        for c in prefix:
            if c not in cur.next:
                return False
            cur = cur.next[c]
        return True


if __name__ == "__main__":
    insert_list = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    trie = Trie()
    
    for word in insert_list:
        trie.insert(word)

    print(trie.count)
    print(trie.startWith("mo"))
    print(trie.startWith("mout"))
    print(trie.search("mobil"))
    print(trie.search("moneypot"))

    levels = [[]]
    q = deque([trie.root])

    while q:
        cur_level = []
        for _ in range(len(q)):
            node = q.popleft()
            for next_node in node.next.values():
                cur_level.append(next_node.val)
                q.append(next_node)
        if cur_level:
            levels.append(cur_level)

    print(levels)
