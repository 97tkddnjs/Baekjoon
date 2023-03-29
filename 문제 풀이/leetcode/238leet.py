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
    
    
# 맞춘 코드    
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        length = len(nums)-1

        left = []
        right = []
        print(nums)
        for i, data in enumerate(nums):
            # check
            left_idx = i -1
            right_idx = length -i +1

            if  left_idx < 0 or right_idx >= len(nums):
                left.append(1)
                right.append(1)
            else:
                left.append(left[i-1]*nums[left_idx])
                right.append(right[i-1]*nums[right_idx])
            
        outputs =[ left[i]*right[length-i] for i in range(len(nums))]    

        return outputs
