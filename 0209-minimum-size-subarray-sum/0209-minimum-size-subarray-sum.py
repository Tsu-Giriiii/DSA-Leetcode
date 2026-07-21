class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = right = 0
        res= float('inf')
        prefix = 0
        '''while right < len(nums):
            prefix += nums[right]
            if prefix>= target and left <= right:
                res = min(res,right-left+1)
                prefix-= nums[left]
                left+=1
                if left>right:
                    right+=1
            else:
                right+=1
        return 0 if res == float('inf') else res'''

        while right < len(nums):
            prefix += nums[right]
            
            while prefix >= target:
                res = min(res,right-left+1)
                prefix -= nums[left]
                left+=1
            right+=1
        
        if res==float('inf'):
            return 0
        else:
            return res

        