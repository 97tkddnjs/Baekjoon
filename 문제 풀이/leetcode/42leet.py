# 못풀겠어서 답안지 체크해봄
from typing import List

class Solution:
    '''
    문제는 투포인터 관점으로 생각해볼 것 
    <- 브루트 포스로 생각하면 구간합의 느낌이 온다. 
    안올 수도 있긴 함...
    각 max_val을 비교해서 작은 값을 가진 쪽이 큰 쪽으로 움직이게 만들어 준다.
    volume : 문제의 핵심 각 포인터의 max_val에서 해당 idx를 빼게 되면 그것이 volume이다.
    '''

    def trap(self, height: List[int]) -> int:
        

        volume = 0

        #######
        # 시작은 각각 같은 자리에서 시작하게 됨
        # 투포인터의 기준이 되는 것 왼쪽, 오른쪽을 가리키는 value
        left, right = 0 , len(height)-1

        # 초기 각각의 최대값 중 가장 큰 값은 각 포인터의 위치로 한다.
        left_max_val , right_max_val= height[left], height[right]
        #######
        while left < right: # <- 이쪽도 핵심 기능임
            left_max_val , right_max_val = max(left_max_val, height[left]) , max(right_max_val, height[right])

            # 이 부분이 문제의 핵심 같은 데 잘 이해가 안됨
            #  <- 이해가 필요한 데...
            if left_max_val <= right_max_val:
                volume += left_max_val -height[left] 
                left+=1
            else:
                volume += right_max_val - height[right]
                right-=1
            
        
        return volume