class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        maj = []
        for num in nums:
            if num not in d:
                d[num]=1
            else:
                d[num]+=1

        for num in d:
            if d[num]>len(nums)/3:
                maj.append(num)
        return maj
        