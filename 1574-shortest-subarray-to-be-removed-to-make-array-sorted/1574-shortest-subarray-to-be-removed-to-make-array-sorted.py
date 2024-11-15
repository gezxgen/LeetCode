from typing import List

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        
        # Step 1: Find the first rule breaker from the left
        s = 0
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                s = i
                break
        else:
            # If we never break, array is already sorted
            return 0
        
        # Step 2: Find the first rule breaker from the right
        e = n - 1
        for i in range(n - 1, 0, -1):
            if arr[i] < arr[i - 1]:
                e = i
                break
        
        # Step 3: Initial removal length (whole segment between s and e)
        res = min(n - s - 1, e)
        
        # Step 4: Sliding window for the minimal middle subarray to remove
        i, j = 0, e
        while i <= s and j < n:
            if arr[i] <= arr[j]:
                res = min(res, j - i - 1)
                i += 1
            else:
                j += 1
        
        return res
