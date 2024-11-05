first_name = input("Prénom : ")
last_name = input("Nom : ")
x = ""
age = int(input("Âge : "))

while age <= 0:  # Vérifiez si l'âge est valide
    print("Veuillez ressaisir un âge valide.")
    age = int(input("Âge : "))  # Demande à l'utilisateur de ressaisir l'âge

# Vérification de l'âge pour déterminer si majeur ou mineur
if age > 18:
    x = "majeur"
else:
    x = "mineur"

# Affichage du message
print(f"Hello {first_name} {last_name}, {age} years old, vous êtes {x}.")
