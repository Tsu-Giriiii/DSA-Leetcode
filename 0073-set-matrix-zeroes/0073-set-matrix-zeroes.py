class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        s = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    s.add((i,j))
        
        for (i,j) in s:
            matrix[i]=[0]*len(matrix[0])
            for k in range(len(matrix)):
                matrix[k][j]=0
