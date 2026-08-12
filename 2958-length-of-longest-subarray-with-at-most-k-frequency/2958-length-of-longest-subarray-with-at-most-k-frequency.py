class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
        d = {}
        left = 0
        longest = 0
        for right in range(len(nums)):
            if nums[right] not in d:
                d[nums[right]] = []
            d[nums[right]].append(right)

            if len(d[nums[right]]) >k:
                left = max(left,d[nums[right]][-k-1]+1)
            longest = max(longest,right-left+1)
        return longest