class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        nums = arr[:]
        arr.sort()
        d= {}
        rank = 1
        for i in range(len(arr)):
            if arr[i] not in d:
                d[arr[i]]=rank
                rank+=1
        return [d[num] for num in nums]