def letter_sum(a, b):
    start = 96
    value = (ord(a) + ord(b) - (2 * start)) % 26 + start
    if value == 96:
        return 'z'
    return chr(value)


t = int(input())
for _ in range(t):
    s = input()
    rev = s[::-1]
    val = ''
    for i in range(len(s)):
        val += letter_sum(s[i], rev[i])
    print(val)
