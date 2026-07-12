class Solution(object):
    def getConcatenation(self, nums):
        ans = []
        ans[:] = nums+nums
        return ans