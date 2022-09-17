import sys
input = sys.stdin.readline

n = input()

length = len(n)

l_c=0
r_c =0

for i in range(length//2):
    l_c +=int(n[i])
    r_c+=int(n[length-i-2])
    pass

if l_c == r_c:
    print("LUCKY")
else:
    print("READY")


