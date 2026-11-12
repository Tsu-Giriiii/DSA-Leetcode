class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        left = 0
        max_count = 0
        flag = None    #flag 0 means increasing
        for right in range(len(nums)):
            
            if right+1 < len(nums) and (nums[right+1]> nums[right]):
                if flag == 1 or flag == None:
                    flag = 0
                    max_count = max(max_count,right - left+1)
                    left = right
                    continue
            elif right+1 < len(nums) and (nums[right+1]< nums[right]):
                if flag == 0 or flag == None:
                    flag = 1
                    max_count = max(max_count, right-left+1)
                    left = right
                    continue
            elif right+1 < len(nums) and nums[right+1] == nums[right]:
                max_count = max(max_count,right-left+1)
                left = right+1
                flag = None
                continue
            max_count = max(max_count,right-left+1)
            
                
            
        return max_count