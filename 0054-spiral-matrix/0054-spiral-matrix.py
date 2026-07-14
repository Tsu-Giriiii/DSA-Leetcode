class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)-1
        n = len(matrix[0])-1
        spiral = []
        s = set()
        Up = 0
        Right = n
        Down = m
        Left = 0

        while len(s)!=(m+1)*(n+1):
            for j in range(Left,Right+1):
                if (Up,j) not in s:
                    spiral.append(matrix[Up][j])
                    s.add((Up,j))
                else:
                    return spiral
            Up+=1
            
            for i in range(Up,Down+1):
                if (i,Right) not in s:
                    spiral.append(matrix[i][Right])
                    s.add((i,Right))
                else:
                    return spiral
            Right-=1

            for j in range(Right,Left-1,-1):
                if (Down,j) not in s:
                    spiral.append(matrix[Down][j])
                    s.add((Down,j))
                else:
                    return spiral
            Down-=1
            for j in range(Down,Up-1,-1):
                if (j,Left) not in s:
                    spiral.append(matrix[j][Left])
                    s.add((j,Left))
                else:
                    return spiral
            Left+=1
        else:
            return spiral



            