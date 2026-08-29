class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        hi = len(nums)-1
        lo = 0 

        while lo <= hi:

            mid = lo + (hi-lo)//2

            if lo == hi or (nums[mid-1] <nums[mid]>nums[mid+1]):
                return mid
            
            elif nums[mid]>nums[mid+1]:
                hi = mid -1
            
            else:
                lo = mid+1

        return mid