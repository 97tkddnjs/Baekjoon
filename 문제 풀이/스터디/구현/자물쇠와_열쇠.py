# 2차원 배열일 시 적용 가능! 90 도 회전 함수!

def rotate90(list_data):
    n = len(list_data) # 원래 행 -> 열로~~
    m = len(list_data[0]) # 원래 열 -> 행으로
    
    tmp = [([0]*n)for _ in range(m)]
    

    for i in range(n): 
        for j in range(m):
            tmp[j][n-1-i] = list_data[i][j]
    
    return tmp
    

def solution(key, lock):
    
    answer = True
    
    n = len(key)
    m = len(lock)
    size = 3*m
    
    # 새로운 lock을 만들고 마치 딥러닝 커널 하듯이...
    new_lock = [[0]*(size)for _ in range(size)]
    
    # lock 데이터 넣기~
    for i in range(m):
        for j in range(m):
            new_lock[size//3+i][size//3+j] = lock[i][j]
            
    
    print(new_lock)
    # 360 도 돌아야 하니까 4번은 돌고 돌아~~ 가야 하지 않나~~~~
    for i in range(4):
        
        pass
    
    return answer