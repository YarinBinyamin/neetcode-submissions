class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        n = len(matrix) 
        m = len(matrix[0])
        left, right = 0 , (n*m) -1
        while left <= right:
            mid = (left + right) // 2
            row, col = mid // m , mid % m
            value = matrix[row][col]
            
            # Check if target is at mid
            if value == target:
                return True
            elif value > target:
                right = mid -1
            else:
                left = mid +1 
                
        return False