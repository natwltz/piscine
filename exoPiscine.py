liste = [("Nathan","Crawl",20),("Jacque","Dos",10),("Paul","Brasse",4)]
cmd = ""
exit = True
while exit:
    cmd = input("que faut t-il faire ?(ajout,liste ou exit)")
    if cmd == "ajout":
        a = input("qui? :")
        b = input("quelle nage? :")
        c = input("combien de longueur ? :")
        t = (a,b,c)
        liste.append(t)
        continue
    if cmd == "liste":
        for elt in liste:
            print("nom :",elt[0])
            print("nage : ",elt[1])
            print("longueur : ",elt[2])
            continue
    if cmd == "exit":
        exit = False
        continue
    print(f"Commande {cmd} inconnue")
