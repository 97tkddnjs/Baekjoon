n=int(input())

stack=[]
for i in range(n):
    data =int(input())
    stack.append(data)

    # if data==0:
    #     stack.pop()
    # else:
    #     stack.append(data)

for i in sorted(stack):
    print(i)




