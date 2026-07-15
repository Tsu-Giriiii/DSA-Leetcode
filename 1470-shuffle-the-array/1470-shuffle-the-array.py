class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        final = []
        for i in range(n):
            final.append(nums[i])
            final.append(nums[n+i])
        return final