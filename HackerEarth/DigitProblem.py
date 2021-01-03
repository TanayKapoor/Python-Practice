x, k = map(int, input().split(" "))
x = list(str((x)))
# print(x)
cnt = 0
while k != 0:
    for i in x:
        if x[x.index(i)] != '9':
            x[x.index(i)] = '9'
            k -= 1
            if k == 0:
                break
            # print("k: ",k)
        else:
            cnt += 1
            # print("cnt: ",cnt)
# print(cnt)
'''while cnt!=0:
    for i in x:
        if i!='9':
            x[x.index(i)]='9'
            cnt-=1'''
print("".join(x))
