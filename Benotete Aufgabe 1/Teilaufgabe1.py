import CrudOperationen


def landkreiseAufklärung():
    read = CrudOperationen.read()
    for i in read:

    return


def summeStraftaten():
    return


def sortiertSummeStraftaten():
    return


while True:
    user_auswahl = input(
            "Bitte geben Sie Ziffer einer der nachfolgenden Optionen ein: \n1. Landkreise mit Aufklärungsquote < 50%, \n2. Summe aller erfassten Fälle je Straftat, \n3. Sortierte Summe aller erfassten Fälle je Straftat \n")
    if user_auswahl.isnumeric():
        auswahl_index = int(user_auswahl)
        if auswahl_index > 0 < 8:
            if auswahl_index == 1:
                landkreiseAufklärung()
            elif auswahl_index == 2:
                summeStraftaten()
            elif auswahl_index == 3:
                sortiertSummeStraftaten()
        else:
            print("Bitte geben Sie eine gültige Ziffer aus der Liste ein!")
    else:
        print("Bitte geben Sie eine gültige Ziffer aus der Liste ein!")
