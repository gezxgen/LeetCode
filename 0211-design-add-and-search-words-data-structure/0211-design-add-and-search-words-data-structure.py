class TrieNode():
    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.word = True

    def search(self, word: str, root=None) -> bool:
        curr = root if root else self.root
        for i in range(len(word)):
            if word[i] == ".":
                return any(self.search(word[i + 1:], curr.children[child]) for child in curr.children)
            
            if word[i] not in curr.children:
                return False
            curr = curr.children[word[i]]
        return curr.word


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)