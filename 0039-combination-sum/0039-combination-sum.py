class Solution:
    def combinationSum(self, can, t):
        res, cur = [], []
        
        def b(nums, l, n, i, tot, cur, sm):
            # append if target is found
            if sm == n:
                tot.append(cur.copy())
                return
            
            # return if sum is too big
            if sm > n or i == l:
                return
            
            # if it is smaller, include and not include the value
            cur.append(nums[i])
            b(nums, l, n, i, tot, cur, sm + nums[i])
            cur.pop()
            
            b(nums, l, n, i + 1, tot, cur, sm)
            

        b(can, len(can), t, 0, res, cur, 0)
        return res