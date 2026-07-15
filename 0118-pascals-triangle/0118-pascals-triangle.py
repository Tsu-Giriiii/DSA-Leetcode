class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascal = [[1],[1,1]]
        if numRows==1:
            return [[1]]
        if numRows==2:
            return[[1],[1,1]]
        
        while len(pascal)<numRows:
            prev = pascal[-1]
            element = [1]
            for i in range(1,len(prev)):
                element.append(prev[i-1]+prev[i])
            element.append(1)
            pascal.append(element)

        return pascal

            
