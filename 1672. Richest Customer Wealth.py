class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        sum = 0;
        
        for account in accounts:
            sum_buf = 0;
            for a in account:
                sum_buf = sum_buf + a;
            if sum_buf > sum:
                sum = sum_buf;
                
                
        return sum;
        