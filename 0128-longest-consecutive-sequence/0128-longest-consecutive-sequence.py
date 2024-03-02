class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        HashSet = set(nums)     # Create HashSet
        longest = 0

        for num in HashSet:                 # Look for every number if it is a sequence (no left neighbor)
            if (num - 1) not in HashSet:    # if it is a start of a sequence
                length = 0                  # reset start value
                while (num + length) in HashSet:    # while sequence is still going
                    length += 1
                longest = max(longest, length)      # continue which ever is longer

        return longest          # return longest sequence of nums