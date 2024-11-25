liste = [("Nathan","Crawl",20),("Nathan","Brasse",12),("Jacque","Dos",10),("Paul","Brasse",4)]
cmd = ""

def cmd_ajout(liste):
    a = input("qui? :")
    b = input("quelle nage? :")
    c = input("combien de longueur ? :")
    t = (a,b,c)
    liste.append(t)
def cmd_liste(liste):
    print("Prénom     |  Nage    |  Longueur")
    print("---------------------------------")
    for elt in liste:
        print(f"{elt[0]:11}|  {elt[1]:8}|  {elt[2]}")
def cmd_exit():
    tmp = input("En êtes-vous sûr ? (o)oui / (n) non :")
    if tmp == "o":
        return False
    else:
        return True
def cmd_nageur(liste):
    nageur = input("Qui ? :")
    print("Nages de ",nageur, ":")
    print("----------------------")
    for elt in liste:
        if elt[0] == nageur:
            print(f"{elt[1]:8}|  {elt[2]}")
def cmd_nage(liste):
    nage = input("Quel nage ? :")
    print(nage, ":")
    print("Prénom     |  Longueur")
    print("----------------------")
    for elt in liste:
         if elt[1] == nage:
            print(f"{elt[0]:11}|  {elt[2]}")
     
exit = True
while exit:
    cmd = input("que faut t-il faire ?(ajout,liste,nageur,nage ou exit) :")
    if cmd == "ajout":
        cmd_ajout(liste)
        continue
    if cmd == "liste":
            cmd_liste(liste)
            continue
    if cmd == "nageur":
            cmd_nageur(liste)
            continue
    if cmd == "nage":
            cmd_nage(liste)
            continue
    if cmd == "exit":
        exit = cmd_exit()
        continue
    else:
        print(f"Commande {cmd} inconnue")
