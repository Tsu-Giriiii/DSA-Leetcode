class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Brute force (Time Limit Exceeds (O(n^2)) if nums not in unique)
        '''if not nums:
            return 0
        unique = []
        for i in range(len(nums)):
            if nums[i] not in unique:
                unique.append(nums[i])
        maxcount = 1
        unique.sort()
        count = 1
        for i in range(len(unique)-1):
            if unique[i+1]==(unique[i]+1):
                count+=1
            else:
                maxcount = max(maxcount,count)
                count = 1
        maxcount = max(maxcount,count)
        return maxcount'''
        #it can be optimized by using a set(nums), however
        # due to sorting the above method would still be, O(nlog(n))

        # O(n) approach
        s = set(nums)
        longest = 0

        for num in s:
            if num-1 not in s:
                length = 1
                while num+length in  s:
                    length +=1
                
                longest = max(longest,length)
        
        return longest

        