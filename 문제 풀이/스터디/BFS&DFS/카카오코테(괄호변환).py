'''
균형잡힌 문자열 먼저 하나 잡아야 되고
올바른으로 되는 지 체크~
'''
def ok(come):
    cnt =0
    for i in come:
        if cnt<0:
            return False
        
        if i =='(':
            cnt+=1
        elif i==')':
            cnt-=1
    if cnt !=0:
        return False
    
    return True

def balance(come):
    cnt=0
    for i in come:
        if i =='(':
            cnt+=1
        elif i==')':
            cnt-=1
    
    if cnt !=0:
        return False
    
    return True

def func(s):
    
    length = len(s)
    
    if ok(s):
        return s
    
    if s=="":
        return ""
    
    for i in range(2,length+2,2):
        if balance(s[:i]) and balance(s[i:]):
            u = s[:i]
            v = s[i:]
            break
    print("u ",u, "v ",v)
    if ok(u):
        return u + func(v)
    else:
        tmp=u[1:-1]
        here ='('+func( v)+')'+tmp[::-1]
        print(here)
        return here
        

def solution(p):
    answer = func(p)    
    
    return answer

# 52% 흐음...
p ="(()())()"
print(solution(p))