class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        strChar = (str(x))[::-1]
        temp = 1
        if len(strChar) == 1:
            return int(strChar)
        while strChar[-1] == '-' or strChar[-1] == '0':
            if strChar[-1] == '-':
                temp = -1
            strChar = strChar[:-1]
        print(int(strChar) * temp)
        

solution = Solution()
print(solution.reverse(1534236469))