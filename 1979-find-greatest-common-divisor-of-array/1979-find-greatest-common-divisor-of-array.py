class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a = max(nums)
        b = min(nums)
        GCD = 1
        for i in range(1,b+1):
            if a%i==0 and b%i==0:
                GCD=i
        return GCD

        