nombre_1 = input("Entrez un nombre : ")
nombre_2 = input("Entrez un nombre : ")

if not nombre_1.isnumeric() or not nombre_2.isnumeric():
    print("Veuillez entrer uniquement des nombres.")
    raise SystemError("Fin du programme")


nombre_1 = int(nombre_1)
nombre_2 = int(nombre_2)

operation = input("Choisier une operation ['+', '-', '*' ou '/']: ")

if operation not in ["+", "-", "*" ,"/"]:
    print("Veuillez entrer une operation valide.")
    raise SystemError("Fin du programme")

if operation == "+":
    resultat = nombre_1 + nombre_2
elif operation == "-":
    resultat = nombre_1 - nombre_2
elif operation == "*":
    resultat = nombre_1 * nombre_2
elif operation == "/":
    if nombre_2 == 0:
        print("Division par zero impossible.")
        raise SystemError("Fin du programme")
    resultat = round(nombre_1 / nombre_2)
    
print(f"Le resultat de l'operation est: {round(resultat, 2)}")# Ecrivez votre code ici !
