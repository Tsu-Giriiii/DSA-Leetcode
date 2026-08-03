class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==1 and nums[0]==target:
            return 0
        high = len(nums)-1
        low = 0
        while low<=high:
            mid = low + (high-low)/2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                high = mid-1
            else:
                low = mid+1
        return -1