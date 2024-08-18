class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        m = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        s = ""
        r = set()
        for w in words:
            for c in w:
                s += m[ord(c) - 97]
            r.add(s)
            s = ""
        return len(r)