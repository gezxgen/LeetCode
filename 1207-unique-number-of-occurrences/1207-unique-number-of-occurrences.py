class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        HashMap = {}
        HashSet = set()
        # Save all values with occurences in HashMap
        for num in arr:
            if num in HashMap:
                HashMap[num] += 1
            else:
                HashMap[num] = 1
        
        # Add each accurance to HashSet
        for val in HashMap:
            if HashMap[val] in HashSet:
                return False
            else:
                HashSet.add(HashMap[val])

        return True