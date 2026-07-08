class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        write_head = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[write_head],nums[i]=nums[i],nums[write_head]
                write_head+=1


        