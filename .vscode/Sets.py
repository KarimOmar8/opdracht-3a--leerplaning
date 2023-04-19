# Set definiëren en afdrukken
my_set = {1, 2, 3, 4, 5}
print(my_set)

# Een specifiek item uit de set ophalen 
if 3 in my_set:
    print("Ja, 3 zit in de set")

# Set-items toevoegen
my_set.add(6)
print(my_set)

# Set-items verwijderen
my_set.remove(3)
print(my_set)

# Door de set heen loopen met een for-loop
for item in my_set:
    print(item)

# Set-items samenvoegen met een andere set
my_new_set = {4, 5, 6, 7, 8}
my_merged_set = my_set.union(my_new_set)
print(my_merged_set)

# Set-items overlappen met een andere set
my_common_set = my_set.intersection(my_new_set)
print(my_common_set)
