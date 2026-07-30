class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) ==1:
            return nums[0]
        if len(nums) == 0:
            return 0
        
        
        new_max = nums[0]
        new_min = nums[0]

        ans = nums[0]

        for i in range(1,len(nums)):
            prev_max = new_max
            prev_min = new_min

            new_max = max(prev_min*nums[i], nums[i],prev_max*nums[i])
            new_min = min(prev_max*nums[i],nums[i],prev_min*nums[i])

            ans = max(ans,new_max)

        return ans

        