phrase = input("Entrez un mot ou une phrase : ")

# Transformations
longueur = len(phrase)
majuscules = phrase.upper()
minuscules = phrase.lower()
inverse = phrase[::-1]

# Vérification du palindrome (en ignorant la casse et les espaces)
propre = phrase.replace(" ", "").lower()
est_palindrome = propre == propre[::-1]

print(f"\n--- Analyse de '{phrase}' ---")
print(f"Longueur    : {longueur}")
print(f"Majuscules  : {majuscules}")
print(f"Minuscules  : {minuscules}")
print(f"Inversion   : {inverse}")
print(f"Palindrome  : {'Oui' if est_palindrome else 'Non'}")

print("\nNote : La variable 'phrase' contient toujours l'originale car les strings sont immuables.")