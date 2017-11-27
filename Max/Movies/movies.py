import xml.etree.ElementTree as ET
import operator


def print_list(list):
    print()
    for item in list:
        print(item)


# Hard gecoded! Anmerkung: Regisseur funktioniert nicht
def print_nodes(root):
    result_list = []
    for movie in root.findall("movie"):
        try:
            new_movie = {}
            new_movie["Titel"] = movie.find("title").text
            if not movie.find("producer/person/name").text:
                continue
            else:
                new_movie["Regisseur"] = movie.find("producer/person/name").text
            new_movie["Jahr"] = movie.find("year").text
            new_movie["Plot"] = movie.find("plot-outline").text
            result_list.append(new_movie)
        except IOError:
            print('An error occured trying to read the XML file.')
            continue

    print(result_list)


# Gibt mir alle Filme mit den Werten zurück, die ich als Parameter übergebe.
def get_tags(tags, root):
    result_list = []
    for movie in root.iter("movie"):
        new_movie = {}
        for tag in tags:
            try:
                new_movie[tag] = movie.find(tags[tag]).text

            except IOError:
                print('An error occured trying to read the XML file.')
                continue
        result_list.append(new_movie)

    return result_list


# Filme aus den Jahren 2000-2010
def get_movies_period(movies, start, end):
    result_list = []
    for movie in movies:
        if int(start) <= int(movie["Jahr"]) <= int(end):
            result_list.append(movie)

    return result_list


def get_genres(root):
    all_genres = []
    result = []
    # Alle Genres der Liste hinzufügen
    for node in root.findall(".//genres/item"):
        all_genres.append(node.text)

    # Doppelte Genres aussortieren
    for genre in all_genres:
        if genre in str(result):
            continue
        else:
            result.append(genre)

    return result


def get_directors(root):
    all_directors = []
    result = []
    # Alle Regisseure der Liste hinzufügen
    for node in root.findall(".//producer/person/name"):
        all_directors.append(node.text)

    # Anzahl der Vorkommnisse
    for director in all_directors:
        dict = {}
        occurrence = all_directors.count(director)
        dict["name"] = director
        dict["occurrence"] = occurrence
        result.append(dict)

    # Liste sortieren
    result.sort(key=operator.itemgetter('occurrence'), reverse=True)

    return result


def execute():
    tree = ET.parse("movies.xml")
    root = tree.getroot()

    while True:
        print("\nMENÜ")
        print("----------------------------------------------")
        print("1: Titel, Regisseur, Jahr und Plot")
        print("2: Filme zwischen 2000 und 2010")
        print("3: Alle Genres")
        print("4: Alle Regisseure sortiert nach Häufigkeit")
        answer = input("\nWählen Sie eine Funktion: ")
        if answer == "1":
            print_list(get_tags({"Titel": "title", "Jahr": "year", "Regisseur": "director/person/name", "Plot": "plot-outline"}, root))
        elif answer == "2":
            print_list(get_movies_period(get_tags({"Titel": "title", "Jahr": "year"}, root), 2000, 2010))
        elif answer == "3":
            print_list(get_genres(root))
        elif answer == "4":
            print_list(get_directors(root))
        else:
            print("Falsche Eingabe")


execute()
