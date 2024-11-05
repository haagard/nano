while True:
    langue = input("'fr'/'en' ? ")

    if langue == "fr":
        print("Coucou")
        break  # Sort de la boucle si la langue est correcte
    elif langue == "en":
        print("Hey")
        break  # Sort de la boucle si la langue est correcte
    else:
        print("'fr'/'en'.")
