n, x, y = input().split()
l = [int(i) for i in input().split()]
temp = 1
for i in range(len(l)):
    if l[i] < int(x) or l[i] > int(y):
        print('NO')
        temp = 0
        break
if temp == 1:
    print("YES")
