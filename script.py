import random
import string

lengte = int(input("Hoe lang moet het wachtwoord zijn? "))

letters = string.ascii_letters
cijfers = string.digits
symbolen = string.punctuation

print("Welke tekens moeten in het wachtwoord worden opgenomen?")
inclusies = []
if input("Letters (ja/nee)? ").lower() == "ja":
    inclusies.extend(letters)
if input("Cijfers (ja/nee)? ").lower() == "ja":
    inclusies.extend(cijfers)
if input("Symbolen (ja/nee)? ").lower() == "ja":
    inclusies.extend(symbolen)

wachtwoord = "".join(random.choice(inclusies) for i in range(lengte))

print("Het gegenereerde wachtwoord is:", wachtwoord)
