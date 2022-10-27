import sys
input = sys.stdin.readline

# 답지 참조할 것!
def tree(tree_data):
    length = len(tree_data)

    try:    
        print(tree_data[length//2])
    except:
        return
    tree(tree_data[:length//2])
    tree(tree_data[length//2:])
    pass

n= int(input())

data = list(map(int,input().split()))

tree(data)


