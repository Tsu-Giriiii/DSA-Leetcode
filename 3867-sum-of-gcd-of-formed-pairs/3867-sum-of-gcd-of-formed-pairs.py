import math
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixGCD = []
        mx = nums[0]
        for i in range(len(nums)):
            if nums[i]>mx:
                mx=nums[i]
            prefixGCD.append(math.gcd(nums[i],mx))
        prefixGCD.sort()
        total = 0
        left = 0
        right = len(prefixGCD)-1
        while left<right:
            pair = math.gcd(prefixGCD[left],prefixGCD[right])
            total+=pair
            left +=1
            right-=1
        return total
