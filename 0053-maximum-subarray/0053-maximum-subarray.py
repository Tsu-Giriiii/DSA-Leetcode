class Solution(object):
    def maxSubArray(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_sum = arr[0]
        maxsum = arr[0]

        for i in range(1,len(arr)):
            current_sum = max(current_sum+arr[i],arr[i])
            maxsum = max(maxsum,current_sum)
        return maxsum

        
        