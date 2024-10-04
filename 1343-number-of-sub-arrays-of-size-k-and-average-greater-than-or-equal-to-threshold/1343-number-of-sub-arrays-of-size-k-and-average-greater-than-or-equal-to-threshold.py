class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sm, cnt = 0, 0
        
        # Initialize the first window sum
        for i in range(k):
            sm += arr[i]
        
        # Check the first window
        if sm / k >= threshold:
            cnt += 1
        
        # Slide the window
        for i in range(k, len(arr)):
            sm += arr[i] - arr[i - k]
            if sm / k >= threshold:
                cnt += 1
                
        return cnt