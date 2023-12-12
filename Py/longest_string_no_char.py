class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = ''
        for index in range(len(s)):
            check_string = ''
            count = index
            while count < len(s):
                if s[count] in check_string:
                    break
                check_string += s[count]
                count += 1

            if len(check_string) > len(result):
                result = check_string
        return len(result)
        
solution = Solution()
print(solution.lengthOfLongestSubstring('pwwkew'))