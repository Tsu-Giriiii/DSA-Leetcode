class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Brute Force
        '''d = {}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        return min(d,key=d.get)'''

        #using XOR operator
        result = 0
        for i in nums:
            result^=i
        return result

        