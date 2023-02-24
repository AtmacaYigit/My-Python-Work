for i in range(101):
    if i % 3 == 0 and i % 5 == 0:
        print("fizbuz")
    elif i % 3 == 0:
        print("fiz")
    elif i % 5 == 0:
        print("buz")
    else:
        print(i)
