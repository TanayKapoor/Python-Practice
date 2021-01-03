try:
    N = int(input())
    i, j, p = [int(i) for i in input().split()]
    for r in range(N):
        for c in range(N):
            print(max(0, min(p - abs(i - r), p - abs(j - c))), end=' ')
        print()
except Exception as exception:
    print('-' * 22)
    print(exception)