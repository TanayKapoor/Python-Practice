from math import ceil

S, X, N = map(int, input().split())

TY = []
for i in range(N):
    A, B = map(int, input().split())

    TY.append([A, B])

TY.sort()
day = 0

i = 0
while i < S:
    if len(TY) > 0:
        if X * (TY[0][0] - day - 1) > S:
            day += ceil((S - i) / X)
            i += X * ceil((S - i) / X)
        else:
            i += X * (TY[0][0] - day - 1)
            day = TY[0][0] - 1
    else:
        day += ceil((S - i) / X)
        i += X * ceil((S - i) / X)
    if i < S:
        if len(TY) > 0:
            i += TY[0][1]
            day += 1
    else:
        break
    del TY[0]

print(day)
