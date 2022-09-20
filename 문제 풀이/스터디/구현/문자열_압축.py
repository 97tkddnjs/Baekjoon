
# 프로그래머스에서 풀이할 것!
# 카카오 2020 기출 문제 lv2
# 문자열 슬라이싱 하는 것 외우기
# 삼항 연산자 외우기!!
def solution(s):
    length = len(s)
    
    answer = len(s)
    
    # 절반까지만 하면 된다. 
    for step in range(1, length//2+1):
        init = s[:step]
        tmp=""
        cnt = 1 # 최소는 1이기 때문에
        
        # step 만큼 움직일 것이므로 
        # < - 초기가 step인것은 이것 부터 비교하려고 하는 것이다
        for cmp in range(step ,length+step, step ):
            
            # [ : ] null 을 반환해버리니까 
            if init == s[cmp : cmp+step]:
                cnt+=1
            else:
                tmp += init if cnt == 1  else str(cnt)+init 
                # 바꾸기 로직
                init = s[cmp : cmp+step]
                cnt=1
        
        #print(tmp)        
        answer = min(len(tmp), answer)
            
    
    return answer