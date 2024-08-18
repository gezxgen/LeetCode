class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        solution = ""
        result = set()
        for word in words:
            for char in word:
                solution += morse[ord(char) - 97]
            result.add(solution)
            solution = ""
        return len(result)