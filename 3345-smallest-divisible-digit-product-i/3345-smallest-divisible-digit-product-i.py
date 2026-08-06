class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        ans =n
        while ans<=100:
            temp = ans
            prod =1
            while temp>0:
                d = temp%10
                temp = temp//10
                prod = prod*d
            if prod%t==0:
                return ans
            else:
                ans = ans+1