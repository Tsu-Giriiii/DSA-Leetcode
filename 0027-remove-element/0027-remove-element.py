class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        n = len(nums)
        count = 0
        while val in nums:
            nums.remove(val)
            count+=1
        for i in range(count):
            nums.append('_')
        return n - count