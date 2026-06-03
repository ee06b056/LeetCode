class Trie:

    def __init__(self, is_end=False):
        self.children = {}
        self.is_end = is_end

    def insert(self, word: str) -> None:
        char = word[0]
        if char not in self.children:
            self.children[char] = Trie()
        if len(word) == 1:
            self.children[char].is_end = True
        else:
            self.children[char].insert(word[1:])

    def search(self, word: str) -> bool:
        char = word[0]
        if char not in self.children:
            return False
        if len(word) == 1:
            return self.children[char].is_end
        else:
            return self.children[char].search(word[1:])

    def startsWith(self, prefix: str) -> bool:
        if len(prefix) == 0:
            return True
        char = prefix[0]
        return char in self.children and self.children[char].startsWith(prefix[1:])
        

class TrieFaster:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['#'] = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return '#' in node

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True
    
class TrieNode:
    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.is_end: bool = False

class TrieGeneric:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)