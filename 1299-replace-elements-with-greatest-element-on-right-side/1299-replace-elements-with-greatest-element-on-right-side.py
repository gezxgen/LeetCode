class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        x: int = -1
        c: int = 0
        for i in range(len(arr)-1, -1, -1):
            c = arr[i]
            arr[i] = x
            x = max(x, c)
        return arr