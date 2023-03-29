class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_val = prices[0]
        outputs = 0
        for data in prices[1:]:
            if min_val >= data:
                min_val = data
            else:
                outputs = max(outputs, data - min_val)
        return outputs