class Solution(object):
    def removeDuplicates(self, nums):
        write_index = 1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[write_index]=nums[i]
                write_index +=1
            
        return write_index
        
        