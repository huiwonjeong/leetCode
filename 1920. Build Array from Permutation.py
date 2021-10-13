class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [];
        for x in nums:
            result.append(nums[x]);
            
        return result;