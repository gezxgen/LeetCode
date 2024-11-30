class TrieNode():
    def __init__(self):
        self.children = {}
        self.word = False


class Trie:
    def __init__(self, children={}):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:           
            if char not in curr.children:               # search what we have
                curr.children[char] = TrieNode()        # fill what we dont have
            curr = curr.children[char]
        curr.word = True                                # mark as word
        
    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)