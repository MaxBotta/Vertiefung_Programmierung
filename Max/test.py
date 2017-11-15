
repeat = True
while repeat:
    print("1. Schleife")
    answer = input("1. y/n")
    if answer == "y":
        break
    while repeat:
        print("2. Schleife")
        answer = input("2. y/n")
        if answer == "y":
            break


