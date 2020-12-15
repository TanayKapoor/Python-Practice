print("Enter number of inputs:")
n = int(input())
phonebook = dict()
for i in range(n):
    print("Enter data:")
    line = input()
    line = line.split()
    phonebook[line[0]] = phonebook.get(line[0], line[1])

while 1:
    try:
        print("Enter name to fetch data:")
        q = input()
        if q in phonebook:
            print(str(q) + "=" + str(phonebook[q]))
        else:
            print("Not found")
    except:
        break