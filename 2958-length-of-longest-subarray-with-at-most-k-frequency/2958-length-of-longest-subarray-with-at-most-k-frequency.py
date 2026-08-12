class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #Naive Approach
        '''if not nums:
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
        return longest'''

        #better approach
        if not nums:
            return 0
        longest = 0
        left = 0
        count = {}

        for right in range(len(nums)):
            curr = nums[right]
            if curr in count:
                count[curr]+=1
            else:
                count[curr]=1
            
            while count[curr]>k:
                left_slide = nums[left]
                count[left_slide]-=1
                left+=1
            longest = max(longest,right-left+1)
        return longest


