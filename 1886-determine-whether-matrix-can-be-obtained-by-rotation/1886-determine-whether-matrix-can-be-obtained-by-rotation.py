class Solution(object):
    def findRotation(self, mat, target):
        def rotate(matrix):
            n = len(matrix)
            
            for i in range(n):
                for j in range(i, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
            for row in matrix:
                row.reverse()
        
        def is_equal(a, b):
            for i in range(len(a)):
                for j in range(len(a)):
                    if a[i][j] != b[i][j]:
                        return False
            return True
        
        for _ in range(4):
            if is_equal(mat, target):
                return True
            rotate(mat)
        
        return False