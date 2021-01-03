n = int(input())
s = input()
sm = "hackerearth"
count = n
for i in sm:
    time = s.count(i)
    if (i in "aerh"):
        time //= 2
    if time < count:
        count = time
print(count)
