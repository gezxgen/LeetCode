class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        HashMap, n = {}, len(nums)
        if n == 1:
            return ["Gold Medal"]
        if n == 2:
            return ["Gold Medal", "Silver Medal"] if nums[0] > nums[1] else ["Silver Medal", "Gold Medal"]
        
        # create a hashmap with number: index
        for i in range(n):
            HashMap[nums[i]] = i
        
        # sort by number
        HashMap, res = dict(sorted(HashMap.items(), reverse=True)), [""] * n
        
        # set the numbers as strings in a result array at index
        values = list(HashMap.values())
        res[values[0]], res[values[1]], res[values[2]] = "Gold Medal", "Silver Medal", "Bronze Medal"
        
        for i in range(3, n):
            res[values[i]] = str(i + 1)
        
        return res