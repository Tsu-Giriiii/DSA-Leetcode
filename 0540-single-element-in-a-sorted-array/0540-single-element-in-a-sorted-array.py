class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        hi = len(nums)-1
        lo = 0

        while lo <= hi:
            mid = lo + (hi-lo)//2
            state = True if mid%2==0 else False

            if lo == hi or (nums[mid-1] < nums[mid] <nums[mid+1]):
                return nums[mid]

            elif state:
                if nums[mid]!=nums[mid+1]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid]!=nums[mid+1]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return nums[lo]