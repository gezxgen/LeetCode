class Solution:
    def largestGoodInteger(self, num: str) -> str:
        mx: int = -1
            
        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                mx = max(mx, int(num[i]))
        
        return "" if mx == -1 else str(mx)*3