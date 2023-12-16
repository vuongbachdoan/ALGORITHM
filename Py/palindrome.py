class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        arrChar = list(str(x))
        while len(arrChar) != 0:
            if arrChar[0] == arrChar[-1]:
                arrChar.pop()
                if len(arrChar) == 0:
                    break
                arrChar = arrChar[1:]
            else:
                break
        return bool(len(arrChar) == 0)
        
    
solution = Solution()
print(solution.isPalindrome(12))