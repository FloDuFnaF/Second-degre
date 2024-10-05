import math

# Définir une propriété pour mentionner la fin du programme

fin="Fin du programme, veuillez le relancer pour le réexecuter"

def choix():
    print("Quel genre de calcul voulez-vous faire ? ('racines' ou 'canonique')")
    choix=input()
    if choix=="racines":
        # Demander pour le(s) racine(s) à l'utilisateur quelles seront les valeurs A, B et C.
        a=float(input("Combien sera a ? : "))
        b=float(input("Combien sera b ? : "))
        c=float(input("Combien sera c ? : "))
        # Le code va calculer tout seul delta et dire à l'utilisateur le nombre précis.
        delta=b*b-4*a*c
        def racines():

            # Démontrer à l'utilisateur comment le calcul de Delta se fait.
            print("Pour calculer Delta, il faut faire : b*b-4*a*c, et avec le cas actual, le calcul ressemble à : ", b ," x ", b ," - ", 4 ," x ", a ," x ", c)
            print("donc Delta est égal à : ", delta)

            if delta > 0:
                # Alors il y a deux racines
                # Demander à l'utilisateur s'il veut savoir les racines
                voulez1=(input("Voulez-vous savoir les racines ? (oui / non) : "))
                if voulez1 == "oui":
                    x1=-b-math.sqrt(delta)/(2*a)
                    print("La racine 'x1' est égal à : ", x1)
                    x2=-b+math.sqrt(delta)/(2*a)
                    print("La racine 'x2' est égal à : ", x2)
                    print(fin)
                elif voulez1 == "non":
                    print(fin)
                else:
                    print("La réponse n'est pas reconnu")
                    print(fin)
                
            elif delta == 0:
                # Alors il n'y a qu'une seule racine
                # Demander à l'utilisateur s'il veut savoir les racines
                voulez2=(input("Voulez-vous savoir la racine ? (oui / non) : "))
                if voulez2 == "oui":
                    x=-b/(2*a)
                    print("La racine 'x' est égal à : ", x)
                    print(fin)
                elif voulez2 == "non":
                    print(fin)
                else:
                    print("La réponse n'est pas reconnu")
                    print(fin)

            else:
                # Alors il n'y a aucune racine
                print("Delta est égal à : ", delta ,", étant donné que Delta est négatif, nous n'avons pas de racine(s).")
                print(fin)

    elif choix=="canonique":
        # Demander pour la forme canonique, à l'utilisateur quelles seront les valeurs A, B et C.
        a=float(input("Combien sera a ? : "))
        b=float(input("Combien sera b ? : "))
        c=float(input("Combien sera c ? : "))
        # Le code va calculer tout seul delta et dire à l'utilisateur le nombre précis.
        delta=b*b-4*a*c
        h = -b / (2 * a)  # Le terme h dans (x - h)^2
        k = delta / (4 * a)  # Le terme k ajouté ou soustrait à la fin
        h_sign = f"- {abs(h)}" if h >= 0 else f"+ {abs(h)}"
        k_sign = f"+ {abs(k)}" if k < 0 else f"- {abs(k)}"

        def canonique():
            # La partie juste ici est encore en développement, de ce fait, je n'ai pas trop d'idée(s), et j'improvise légèrement ce que je fais. Mais voici ce que je peux apporter :
            print("Pour calculer la forme canonique, nous devons transformer l'équation (Le programme n'est pas forcément pertinent)")
            print("La forme canonique d'un trinôme du second degré est : ax² +- bx +- c = a[(x + b / 2a)² - delta / 4a²]")
            print(f"La forme canonique du trinôme est : {a}[(x {h_sign})² {k_sign}]")
    if choix == "racines":
        racines() 
    elif choix == "canonique":
        canonique()
    else:
        print("Commande non reconnues.")
        print(fin)       
choix()
