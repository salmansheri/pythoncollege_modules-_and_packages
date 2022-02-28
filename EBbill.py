def bill(name, unit):
    if unit in range(100, 201):
        print("{},You need to pay {} Rs".format(name, unit * 3))
    elif unit in range(201, 501):
        print("{},You need to pay {} Rs".format(name, unit * 4))
    elif unit > 501:
        print("{},You need to pay {} Rs".format(name, unit * 6))
    else:
        print("You need not to pay the bill")
