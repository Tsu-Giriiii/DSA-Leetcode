from typing import List
import bisect
class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        #brute force
        '''gcdPairs = []
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                pairs = math.gcd(nums[i],nums[j])
                gcdPairs.append(pairs)
        gcdPairs.sort()
        ans = []
        for i in range(len(queries)):
            ans.append(gcdPairs[queries[i]])
        return ans'''

        max_val = max(nums)
        
        # Count frequencies of each number
        count = [0] * (max_val + 1)
        for num in nums:
            count[num] += 1
            
        # exact_gcd[i] will store the number of pairs with GCD exactly equal to i
        exact_gcd = [0] * (max_val + 1)
        
        # Iterate backwards to compute exact GCD pairs using sieve-like method
        for i in range(max_val, 0, -1):
            multiples = 0
            # Count how many numbers in nums are multiples of i
            for j in range(i, max_val + 1, i):
                multiples += count[j]
                
            # Total pairs where both elements are multiples of i
            total_pairs = (multiples * (multiples - 1)) // 2
            
            # Subtract pairs that have a strictly larger GCD (multiples of i)
            for j in range(2 * i, max_val + 1, i):
                total_pairs -= exact_gcd[j]
                
            exact_gcd[i] = total_pairs
            
        # Build prefix sums of the exact GCD counts
        prefix_sums = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            prefix_sums[i] = prefix_sums[i - 1] + exact_gcd[i]
            
        # Answer each query using binary search
        ans = []
        for q in queries:
            # bisect_right finds the first index where prefix_sums[idx] > q
            idx = bisect.bisect_right(prefix_sums, q)
            ans.append(idx)
            
        return ans
        