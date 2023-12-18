class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1
        i = 2
        maxVal = max(nums)
        if maxVal == nums[0]:
            return 0
        if maxVal == nums[-1]:
            return (len(nums) - 1)
        while i < len(nums):
            if nums[i - 1] == maxVal:
                return i - 1
            i+=1

        
solution = Solution()
print(solution.findPeakElement([6,5,4,3,2,3,2]))