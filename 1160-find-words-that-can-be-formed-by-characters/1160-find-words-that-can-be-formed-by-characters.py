class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        mp = {char: 0 for char in ascii_lowercase}
        flag: bool = True
        done: set = set()
        cnt: int = 0

        for char in chars:
            if char in mp:
                mp[char] += 1
        
        for word in words:
            flag = True
            done = set()
            for char in word:
                if (char not in done) and (mp[char] < word.count(char)):
                    flag = False
                    break
                done.add(char)
            if flag:
                cnt += len(word)
        return cnt