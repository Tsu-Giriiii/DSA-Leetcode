class Solution:
    def longestSubsequence(self, nums):
        total_xor = 0
        has_non_zero = False
        
        for num in nums:
            total_xor ^= num
            if num != 0:
                has_non_zero = True
                
        # If all elements are 0, no non-zero XOR subsequence exists
        if not has_non_zero:
            return 0
            
        # If the total XOR of the entire array is non-zero
        if total_xor != 0:
            return len(nums)
            
        # If total XOR is 0 but there is at least one non-zero element
        return len(nums) - 1