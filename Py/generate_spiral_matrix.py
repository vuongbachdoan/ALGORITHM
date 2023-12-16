class Solution(object):
    def generateMatrix(self, n):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        for i in range(n):
            result.append([0] * n)
        result[0][0] = 1

        startCol = 0
        startRow = 0
        endCol = n
        endRow = n
        isIncr = True
        num = 1
        while True:
            if isIncr == True:
                for i in range(startCol, endCol):
                    result[startRow][i] = num
                    num += 1
                startRow += 1
                
                for i in range(startRow, endRow):
                    result[i][endCol - 1] = num
                    num += 1
                endCol -= 1

                isIncr = False
                if num > n ** 2:
                    break

            if isIncr == False:
                for i in range(endCol - 1, startCol - 1, -1):
                    result[endRow - 1][i] = num
                    num += 1
                endRow -= 1
                for i in range(endRow - 1, startRow - 1, -1):
                    result[i][startCol] = num
                    num += 1
                startCol += 1

                isIncr = True
                if num > n ** 2:
                    break
        return result
        

solution = Solution()
print(solution.generateMatrix(3))