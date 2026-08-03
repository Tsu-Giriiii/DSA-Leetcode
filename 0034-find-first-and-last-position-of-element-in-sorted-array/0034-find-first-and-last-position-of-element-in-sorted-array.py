class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first = -1
        last = -1
        high = len(nums)-1
        low = 0
        while low<=high:
            mid = low+(high-low)/2
            if nums[mid]==target:
                first = mid
                high = mid-1
            elif nums[mid]>target:
                high = mid-1
            else:
                low = mid+1

        high = len(nums)-1
        low = 0
        while low<=high:
            mid = low+(high-low)/2
            if nums[mid]==target:
                last = mid
                low = mid+1
            elif nums[mid]>target:
                high = mid-1
            else:
                low = mid+1

        return [first,last] 