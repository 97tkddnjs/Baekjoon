# 내풀이 <- 50 점 짜리...

from collections import deque

def bfs(port):
    
    queue = deque()
    queue.append("ICN")
    
    data = ["ICN"]
    
    while queue:
        x = queue.popleft()
        
        port[x] = sorted(port[x])

        if port[x]:
            tmp = port[x].pop(0)
            data.append(tmp)
            queue.append(tmp)
        
    return data
        
        
    
    pass


def solution(tickets):
    answer = []
    port={}
    for ticket in tickets:
        
        if port.get(ticket[0])==None:
            port[ticket[0]]=[ticket[1]]

            if port.get(ticket[1])==None:
                port[ticket[1]] = []

        else:
            port[ticket[0]].append(ticket[1])

    print(port)       
    
    return bfs(port)
    

    