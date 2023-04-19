# Lijsten definiëren en afdrukken
my_list = ["appel", "banaan", "kers"]
print(my_list)

# Items aan een lijst toevoegen
my_list.append("druif")
print(my_list)

# Items uit een lijst verwijderen
my_list.remove("banaan")
print(my_list)

# Lijsten indexeren
print(my_list[0])    
print(my_list[-1])   
print(my_list[1:3])  

# Lijsten sorteren
my_list.sort()       
print(my_list)

# Lijsten doorlopen met een for-loop
for item in my_list:
    print(item)

# Lijsten combineren (concatenation)
list_1 = ["a", "b", "c"]
list_2 = [1, 2, 3]
combined_list = list_1 + list_2
print(combined_list)
