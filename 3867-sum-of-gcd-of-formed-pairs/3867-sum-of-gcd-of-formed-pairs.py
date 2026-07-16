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
        for i in range(int(len(prefixGCD)/2)):
            pair = math.gcd(prefixGCD[i],prefixGCD[len(prefixGCD)-1-i])
            total+=pair
        return total
