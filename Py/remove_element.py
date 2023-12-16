class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        arr = []
        for item in nums:
            if item != val:
                arr.append(item)
        return arr + list('_' * (str(nums).count(str(val))))
        
solution = Solution()
print(solution.removeElement([3,2,2,3], 3))