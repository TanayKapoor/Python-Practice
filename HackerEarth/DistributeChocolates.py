for _ in range(int(input())):

    c, n = [int(y) for y in input().split()]

    a = n * (n - 1) // 2

    b = (c - a) // n

    if b < 1:

        print(c)

    else:

        left = c - (b * n + a)

        print(left)
