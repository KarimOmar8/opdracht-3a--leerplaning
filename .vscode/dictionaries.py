# Dictionary definiëren en afdrukken
my_dict = {"naam": "John", "leeftijd": 30, "adres": "Hoofdstraat 1"}
print(my_dict)

# Een specifiek item uit de dictionary ophalen
print(my_dict["naam"])   # geeft "John" terug

# Items aan een dictionary toevoegen
my_dict["telefoonnummer"] = "06-12345678"
print(my_dict)

# Items uit een dictionary verwijderen
del my_dict["leeftijd"]
print(my_dict)

# Door de dictionary heen loopen met een for-loop
for key in my_dict:
    print(key, ":", my_dict[key])

# Controleren of een bepaald item in de dictionary zit
if "naam" in my_dict:
    print("Ja, 'naam' is een key in de dictionary")

# Dictionary-items sorteren
sorted_dict = dict(sorted(my_dict.items()))
print(sorted_dict)
