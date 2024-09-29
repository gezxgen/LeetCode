class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # create variables and start mapping chars
        done, flag, cnt = True, set(), 0
        mp = {char: 0 for char in ascii_lowercase}
        for char in chars: mp[char] = mp.get(char, 0) + 1
        
        # check if the word can fit
        for word in words:
            done, flag = set(), True
            for char in word:
                if (char not in done) and (mp[char] < word.count(char)):
                    flag = False        # set false if it can't fit
                    break               # break out, no need to continue
                done.add(char)          # append char to the already checked
            if flag: cnt += len(word)   # append the length of word if it fits
        return cnt