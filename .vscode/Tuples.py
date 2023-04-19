# Tuple definiëren en afdrukken
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

# Een specifiek item uit de tuple ophalen
print(my_tuple[2])   # geeft 3 terug

# Tuple-items kunnen niet worden gewijzigd, maar je kunt wel een nieuwe tuple maken met een gewijzigd item
my_new_tuple = my_tuple[:2] + (10, 20, 30) + my_tuple[3:]
print(my_new_tuple)

# Door de tuple heen loopen met een for-loop
for item in my_tuple:
    print(item)

# Controleren of een bepaald item in de tuple zit
if 3 in my_tuple:
    print("Ja, 3 zit in de tuple")
    
# Tuple-items sorteren
my_tuple_sorted = tuple(sorted(my_tuple))
print(my_tuple_sorted)
