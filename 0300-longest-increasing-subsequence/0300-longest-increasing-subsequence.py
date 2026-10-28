class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        
        t = [1]*(n)
        t[0] = 1


        for i in range(1,n):
            for j in range(i):
                if nums[j]<nums[i]:
                    t[i] = max(1+t[j], t[i])
        return max(t)
