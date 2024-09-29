class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(nums, L, M, R):
            left, right = nums[L:M+1], nums[M+1:R+1]
            i, j, k = L, 0, 0
            
            while (j <= len(left)-1) and (k <= len(right)-1):
                if left[j] <= right[k]:
                    nums[i] = left[j]
                    j += 1
                else:
                    nums[i] = right[k]
                    k += 1
                i += 1
            if j <= len(left)-1:
                nums[i:R+1] = left[j:len(left)]
            else:
                nums[i:R+1] = right[k:len(right)]
            return nums
        
        def mergeSort(nums, l, r):
            if l == r:
                return nums
            
            m = (r + l) // 2
            mergeSort(nums, l, m)
            mergeSort(nums, m+1, r)
            merge(nums, l, m, r)
            return nums
            
        return mergeSort(nums, 0, len(nums)-1)