try:

    nb1 = float(input("Entrez le premier nombre : "))
    nb2 = float(input("Entrez le deuxième nombre : "))
    
    print("\nMenu d'opérations : +, -, *, /")
    op = input("Choisissez l'opérateur : ")

    if op == '+':
        res = nb1 + nb2
    elif op == '-':
        res = nb1 - nb2
    elif op == '*':
        res = nb1 * nb2
    elif op == '/':
        if nb2 == 0:
            res = "Erreur (division par zéro)"
        else:
            res = nb1 / nb2
    else:
        res = "Opérateur invalide"

    if isinstance(res, (int, float)):
        print(f"\nRésultat : {nb1} {op} {nb2} = {res}")
    else:
        print(f"\n{res}")

except ValueError:
    print("Erreur : Veuillez entrer des nombres valides.")