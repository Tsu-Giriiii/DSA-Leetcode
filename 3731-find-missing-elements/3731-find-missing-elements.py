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
        first = min(nums)
        last = max(nums)

        ans = []
        for num in range(first,last):
            if num not in nums:
                ans.append(num)
        
        return ans
