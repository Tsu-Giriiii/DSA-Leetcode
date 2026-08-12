class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(nums)-1
        min_element = float("inf")
        while lo < hi:
            mid = lo + (hi-lo)//2

            if nums[mid]> nums[hi]:
                lo = mid+1
            else:
                hi = mid
            
        return nums[lo]

        