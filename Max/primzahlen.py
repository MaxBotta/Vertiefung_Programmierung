

def set_line(text):
    with open("list.txt", "a") as f:
        f.write(str(text) + "\n")


def delete_line(i):
    lines = []
    with open("list.txt", "r") as file:

        # Text in Array speichern
        text = file.readlines()
        for v in text:
            v = v.rstrip()
            lines.append(v)

    with open("list.txt", "w") as file:
        # Zeile aus Array löschen und file überschreiben
        del lines[i]
        for v in lines:
            file.write(v + "\n")


def get_line(i):
    lines = []
    with open("list.txt", "r") as file:
        text = file.readlines()
        for v in text:
            v = v.rstrip()
            lines.append(v)

    return lines[i-1]


def check_if_prime_number(n):
    i = 2
    while i < n:
        if n % i == 0:
            return False
        elif n % i != 0:
            if i == n - 1:
                return True
            i += 1


def print_numbers():
    i = 1
    while i <= 100:
        write_number_check_prime(i)
        i += 1


def write_number_check_prime(n):
    with open("list.txt", "a") as f:
        prime = check_if_prime_number(n)
        f.write(str(n) + " " + str(prime) + "\n")


print_numbers()

