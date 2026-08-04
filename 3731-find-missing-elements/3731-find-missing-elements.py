class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #Brute Force
        '''nums.sort()
        first = nums[0]
        last = nums[-1]
        next_num = first
        ans = []
        while next_num<=last:
            if next_num not in nums:
                ans.append(next_num)
            next_num+= 1

        return ans'''

        #Better Approach
        f = min(nums)
        l = max(nums)

        s = set(nums)
        ans = []
        for i in range(f,l):
            if i not in s:
                ans.append(i)
        
        return ans
