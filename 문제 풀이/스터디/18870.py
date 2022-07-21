from collections import deque
import copy
from queue import PriorityQueue
import sys

# n = int(input())
# size = [i for i in range(n)]
# arr = list(map(int, input().split()))
# arr_c= set(arr)
# arr_c = sorted(arr_c)
# data = tuple(zip( arr_c,size))

# data = dict(data)

# for i in arr:
#     print(data[i],end=" ")


# def func(arr):
#     last = arr[-1]

#     sum=0
#     for i,data in enumerate(arr[:-1]):
#         sum+=data
#         if sum == last:
#             return i
#         pass
    
#     pass

def compressword(word, k):
    # 10^5
    word = list(word)
    check = False
    while True:
        i=0
        while i <len(word):
            #print("ok")
            size = word[i:i+k]
            if len(set(size))==1 and len(size)==k :
                check = True
                #print("in",i," ",word[i:i+k])
                del word[i:i+k]
                i-=1
            i+=1
        
        # print(word)
        if check == False:
            break
        else:
            check = False
        

    return str(word)

def textQueries(sentences, queries):
    arr=[]

    for check in queries:
        tmp=[]
        for i,data in enumerate(sentences):
            # print(type(check),check)
            str = (check).split(" ")

            size = len(str)
            cnt = 0

            for c in str:
                if c in data:
                    cnt+=1

            if size == cnt:
                tmp.append(i)
        
        if tmp:
            arr.append(tmp)
        else:
            arr.append([-1])
    return  arr        
    # Write your code here
#print(compressword("aabcbbbdeee",3))

def func(pos,even,odd):
    i = len(pos)-1

    while i>=0:
        
        for idx in reversed(pos[:i+1]): # 거꾸로
            # print("p",idx)
            if idx==0:#even
                pos[i] = even.get()   
            else:
                break
            i-=1
        
        for idx in reversed(pos[:i+1]): # 거꾸로
            # print(i, idx)
            if idx==0:#even
                break
            else:
                pos[i] = odd.get()
            i-=1
    print(pos)
        
def bubbleSort_DESC(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1, i, -1):
            if arr[j] > arr[j-1] and arr[j]%2==0 and arr[j-1%2]==0: #짝
                arr[j], arr[j-1] = arr[j-1], arr[j]
            elif arr[j] > arr[j-1] and arr[j]%2!=0 and arr[j-1%2]!=0: #홀
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr

def largest(num):
    num = list(num)
    print(num)
    odd = PriorityQueue() #odd 홀수
    pos=[]

    even = PriorityQueue() # even
    # 작은 순서로 정렬되어서 들어감
    for i, data in enumerate(num):
        tmp = data
        
        if int(tmp)%2==0: # even
            func(pos,even,odd)
            even.put(tmp)
            pos.append(0)
        else:
            func(pos,even,odd)
            odd.put(tmp)
            pos.append(1)
    
    
    
    
        print(i,pos)
    
    return "".join(pos)
    
        

# s = ['how it was done',
# 'are you how'
# ,'it goes to',
# 'goes done are it']

# q =['done it','it']


# # s= ['it go will away'
# # ,'go do art'
# # ,'what to will east']

# # q =['it will',
# # 'go east will',
# # 'will']
# print('it' in 'what to will east')
# print(textQueries(s,q))
a="1806579"#("0082663"

print(largest(a)) #8662003