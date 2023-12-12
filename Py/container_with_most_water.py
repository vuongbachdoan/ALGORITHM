class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result = 0
        start, end = 0, len(height) - 1
        while start - end != 0:
            col = end - start
            area = col * min(height[start], height[end])
            if area > result:
                result = area
            if(height[start] > height[end]):
                end -= 1
            else:
                start += 1
        return result

solution = Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7]))