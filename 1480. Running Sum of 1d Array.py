class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum = 0;
        result =[]
        for num in nums:
            sum = sum + num;
            result.append(sum);
            
        return result;