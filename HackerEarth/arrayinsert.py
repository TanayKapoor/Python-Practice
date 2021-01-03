(n, query) = map(int, input().split())
# print(n,query)
arr = list(map(int, input().split()))
# print(arr)

for i in range(query):
    q = list(map(int, input().split()))
    # print(q)
    if q[0] == 1:
        arr[q[1]] = q[2]
    if q[0] == 2:
        sum = 0
        for j in range(q[1], q[2] + 1):
            sum += arr[j]
        print(sum)
