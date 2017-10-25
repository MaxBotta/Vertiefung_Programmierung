list = [5, 6, 7, 8, 9]
print(list)


def change_list(l):
    del l[2]
    print(l)


change_list(list)
print(list)
print(list[:])
