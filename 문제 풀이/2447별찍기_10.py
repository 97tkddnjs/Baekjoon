import sys

sys.setrecursionlimit(10 ** 7)


def draw(arr, x, y, size):
    # print(x,y, size)

    if size == 1:
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                arr[x + i * size][y + j * size] = '*'
                #print(arr[x + i * size][y + j * size])
                return
    tmp =size//3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            draw(arr, x + i * (tmp), y + j * (tmp), tmp)



# print(matrix)

val = int(input())
matrix = [[" " for i in range(val)] for j in range(val)]
draw(matrix, 0, 0, val)

for i in range(val):
    for j in range(val):
        print(matrix[i][j], end='')
    print()
