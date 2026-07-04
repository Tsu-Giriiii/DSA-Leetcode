class Solution(object):
    def maxFrequency(self, nums, k):
        nums = sorted(nums)
        
        left = 0
        maxfreq = 0
        windsum = 0

        for right in range(len(nums)):
            windsum += nums[right]

            while nums[right]*(right-left+1)-windsum>k:
                windsum -= nums[left]
                left+=1
            maxfreq = max(maxfreq,right-left+1)
        return maxfreq


            
    

            
            

        
      



        