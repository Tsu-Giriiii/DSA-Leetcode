class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        maxcount = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                left = right + 1
            else:
                maxcount = max(maxcount, right - left + 1)

        return maxcount


        