for i in range(int(input())):
    x = input()
    if x == x[::-1]:
        print(-1)
    else:
        print(''.join(sorted(x)))
