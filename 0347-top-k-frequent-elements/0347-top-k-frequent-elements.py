class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = {}               # Create HashMap (key: value)
        output = []

        if k == len(nums):
            return nums
        
        for num in nums:            # HashMap for number of frequent elements
            if num in num_freq.keys():
                num_freq[num] = num_freq.get(num) + 1
            else:
                num_freq[num] = 1

        for i in range(k):          # For amount of max numbers, add to output
            max_val = max(num_freq.values())
            for keys, value in num_freq.items():        # Get key from value
                if value == max_val:
                    key = keys
            output.append(key)      # Add key to return
            num_freq.pop(key)       # Delete the key
        
        return output
