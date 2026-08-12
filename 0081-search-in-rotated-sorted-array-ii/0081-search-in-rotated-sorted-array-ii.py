class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        hi = len(nums)-1
        lo = 0
        while lo<=hi:
            mid = lo+(hi-lo)//2
            
            if nums[mid]==target:
                return True
            while lo < mid and nums[lo]==nums[mid]:
                lo+=1
            if nums[lo]<=nums[mid]:
                if nums[lo]<=target<nums[mid]:
                    hi = mid-1
                else:
                    lo = lo+1
            else:
                if nums[mid]<target<=nums[hi]:
                    lo = mid+1
                else:
                    hi = mid-1
        return False