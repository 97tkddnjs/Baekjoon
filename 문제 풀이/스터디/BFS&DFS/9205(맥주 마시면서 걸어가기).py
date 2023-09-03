import sys
from collections import deque

input =sys.stdin.readline

t= int(input())


def cal_func(val):
    return int(val)//50


def bfs(start , graph):


    queue = deque(start)
    

    
for _ in range(t):
    convinenet_cnt = int(input())
    sang =  list(map(cal_func, input().rsplit()))
    
    convinenet_pos=[]
    for i in range(convinenet_cnt):
        
        convinenet_pos.append(list(map(cal_func, input().rsplit())))


    rock_pos =  list(map(cal_func, input().rsplit()))
    
    graph = [ [0]*rock_pos[0] for _ in range( rock_pos[1] )  ]



