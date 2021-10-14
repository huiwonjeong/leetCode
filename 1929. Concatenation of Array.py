class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [];
        for x in range(0,2):
            for num in nums:
                result.append(num);
                
        return result;