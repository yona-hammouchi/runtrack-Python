N = int(input("Entrez un entier supérieur à zéro pour afficher les tables de multiplication : "))


if N <= 0:
    print("Veuillez entrer un nombre supérieur à zéro.")
else:
   
    for i in range(1, N+1):  
        print(f"\nTable de {i}:")
        for j in range(1, 11):  
            print(f"{i} x {j} = {i*j}")