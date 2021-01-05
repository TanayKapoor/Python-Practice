for _ in range(int(input())):
    n = int(input())
    for i in range(1, n + 1):
        for j in range(1, 2 * n):
            if (n + 1 - i) <= j <= (n - 1 + i):
                print("*", end="")
            else:
                print(" ", end="")
        print("\n")
