liste = [("Nathan","Crawl",20),("Jacque","Dos",10),("Paul","Brasse",4)]
cmd = ""

def cmd_ajout(l):
    a = input("qui? :")
    b = input("quelle nage? :")
    c = input("combien de longueur ? :")
    t = (a,b,c)
    liste.append(t)

def cmd_liste(l):
    print("Prénom     |  Nage       |  Longueur")
    print("---------------------------------")
    for elt in l:
        print(f"{elt[0]:11}|  {elt[1]:8}|  {elt[2]}")

def cmd_exit():
    tmp = input("En êtes-vous sûr ? (o)oui / (n) non :")
    if tmp == "o":
        return False
    else:
        return True

     
exit = True
while exit:
    cmd = input("que faut t-il faire ?(ajout,liste ou exit)")
    if cmd == "ajout":
        cmd_ajout(liste)
        continue
    if cmd == "liste":
            cmd_liste(liste)
            continue
    if cmd == "exit":
        exit = cmd_exit()
        continue
    else:
        print(f"Commande {cmd} inconnue")
