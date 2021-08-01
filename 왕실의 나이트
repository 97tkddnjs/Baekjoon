a = input()

def func(val):
  ch ={'a' : 1, 'b': 2, 'c':3, 'd':4, 'e':5, 'f':6,'g':7 , 'h':8}
  x =ch.get(val[0])
  y = int(val[1])
  print(x,y)
  # 동 서 남 북
  dx = [-2, 2, 0, 0]
  dy = [0, 0, 2, -2]

  temp =[]

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    
    print(nx, ny)

    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
      temp.append(0)
    else:
      if i == 0 or i ==1:
        if (ny+1) < 8 and (ny -1) >0:
          temp.append(2)
        else:
          temp.append(1)
      else:
        if (nx+1) < 8 and (nx -1) >0:
          temp.append(2)
        else:
          temp.append(1) 
    
  return sum(temp)

print(func(a))


