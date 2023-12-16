class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return nums.index(target)
        
        

solution = Solution()
print(solution.searchInsert([1,3,5,6], 2))
        