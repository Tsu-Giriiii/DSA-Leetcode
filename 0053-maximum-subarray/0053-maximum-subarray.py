class Solution(object):
    def maxSubArray(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
    
        # Stores the result (maximum sum found so far)
        res = arr[0]
        
        # Maximum sum of subarray ending at current position
        maxEnding = arr[0]

        for i in range(1, len(arr)):
            
            # Either extend the previous subarray or start 
            # new from current element
            maxEnding = max(maxEnding + arr[i], arr[i])
            
            # Update result if the new subarray sum is larger
            res = max(res, maxEnding)
        
        return res
        