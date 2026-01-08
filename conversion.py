print("1. Celsius vers Fahrenheit/Kelvin")
print("2. Fahrenheit vers Celsius/Kelvin")
choix = input("Votre choix (1 ou 2) : ")

try:
    if choix == "1":
        c = float(input("Température en Celsius : "))
        f = c * 9/5 + 32
        k = c + 273.15
        print(f"\n{c}°C = {f}°F = {k}K")
    elif choix == "2":
        f = float(input("Température en Fahrenheit : "))
        c = (f - 32) * 5/9
        k = c + 273.15
        print(f"\n{f}°F = {c:.2f}°C = {k:.2f}K")
    else:
        print("Choix invalide.")
except ValueError:
    print("Erreur : Entrez une valeur numérique.")