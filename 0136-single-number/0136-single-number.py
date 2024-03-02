class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Create HashMap
        number_count = {}

        # Fill in the HashMap
        for num in nums:
            if num in number_count.keys():
                number_count[num] = number_count.get(num) + 1
            else:
                number_count[num] = 1

        # Find the one
        for key in number_count.keys():
            if number_count[key] != 2:
                return key
