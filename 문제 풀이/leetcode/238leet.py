class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        2<=nums. length <=10**5
        브루트 포스를 생각하면 절대 불가
        """
        pro = 1

        for num in nums:
            pro*=num
        
        output = [ pro//data if data !=0 else 0 for data in nums]
        # case 0에선 안됨 
        # 닫시 생각...
        return output
