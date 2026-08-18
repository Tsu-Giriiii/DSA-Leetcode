class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        ans = -1
        if k > len(nums):
            return ans
        d = dict()
        left = 0
        for right in range(k-1,len(nums)):
            for num in set(nums[left:right+1]):
                d[num] = d.get(num,0)+1
            left+=1
        
        ans = max((key for key,val in d.items() if val==1),default=-1)
        print(d)
        return ans
        
        