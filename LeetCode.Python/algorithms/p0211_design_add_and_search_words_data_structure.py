class TrieNode:
    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True

    def search(self, word: str) -> bool:
        return self._find_(word, 0, self.root)

    def _find_(self, word: str, i: int, node: TrieNode) -> bool:
        if i == len(word):
            return node.is_end
        char = word[i]
        if char == ".":
            return any(self._find_(word, i + 1, child) for child in node.children.values())
        if char not in node.children:
            return False
        return self._find_(word, i + 1, node.children[char])


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)