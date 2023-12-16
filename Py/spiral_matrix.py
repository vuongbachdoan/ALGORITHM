class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        startCol = 0
        startRow = 0
        endCol = len(matrix[0])
        endRow = len(matrix)
        isIncr = True
        while True:
            if isIncr == True:
                for i in range(startCol, endCol):
                    result.append(matrix[startRow][i])
                startRow += 1
                
                for i in range(startRow, endRow):
                    print(i)
                    result.append(matrix[i][endCol - 1])
                endCol -= 1

                isIncr = False
                if len(result) == len(matrix) * len(matrix[0]):
                    break

            if isIncr == False:
                for i in range(endCol - 1, startCol - 1, -1):
                    result.append(matrix[endRow - 1][i])
                endRow -= 1
                for i in range(endRow - 1, startRow - 1, -1):
                    result.append(matrix[i][startCol])
                startCol += 1

                isIncr = True
                if len(result) == len(matrix) * len(matrix[0]):
                    break
        
        return result
        

solution = Solution()
print(solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))