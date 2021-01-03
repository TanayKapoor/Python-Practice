t = int(input())
for i in range(t):
    c0, c1, c2, c3 = tuple(map(int, input().split()))


    def binary(a, b):
        if a == 0:
            if b == 0:
                return c0
            else:
                return c1
        else:
            if b == 0:
                return c2
            else:
                return c3


    ID = 1
    for a in range(2):
        for b in range(2):
            for c in range(3):
                if binary(binary(a, b), c) != binary(a, binary(b, c)):
                    ID = 0
                    break
    if ID == 1:
        print("Yes")
    else:
        print("No")
