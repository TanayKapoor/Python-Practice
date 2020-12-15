def main():
    cost = input("Enter the cost: ")
    tend = input("Enter the tendered amount: ")
    change = float(tend) - float(cost)

    fiveD = int(change / 5)
    oneD = int(change - fiveD * 5)
    a = change - fiveD * 5 - oneD
    fifty = int(a / 0.5)
    b = a - fifty * 0.5
    quarter = int(b / 0.25)
    c = a - fifty * 0.5 - quarter * 0.25
    dime = int(c / 0.10)
    d = a - fifty * 0.5 - quarter * 0.25 - dime * 0.10
    nickel = int(d / 0.05)
    e = a - fifty * 0.5 - quarter * 0.25 - dime * 0.10 - nickel * 0.05
    penny = int(e / 0.01)

    print(fiveD, oneD, fifty, quarter, dime, nickel, penny)
    print("Your change is $%.02f" % change)
    print("$5 dollar    :", fiveD)
    print("$1 dollar    :", oneD)
    print("$0.50 cents  :", fifty)
    print("$0.25 cents  :", quarter)
    print("$0.10 cents  :", dime)
    print("$0.05 cents  :", nickel)
    print("$0.01 cents  :", penny)


main()
