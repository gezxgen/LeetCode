class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        biggest: int = -1
        current: int = 0
        
        for i in range(len(arr)-1, -1, -1):
            current = arr[i]
            arr[i] = biggest
            biggest = max(biggest, current)
            
        
        return arr
    