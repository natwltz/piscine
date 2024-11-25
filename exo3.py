maximum_tableau = [98,12,104,23,131,9]
#fonction pour trouver le maximum du tableau
max = maximum_tableau[0]
for elt in maximum_tableau:
    if elt > max:
        max = elt
print("maximum",max)
#fonction pour trouver le minimum du tableau
min = maximum_tableau[0]
for elt in maximum_tableau:
    if elt < min:
        min = elt
print("minimum",min)
#fonction pour faire la somme de tous les elts positifs d'un tableau
somme_tableau = [5,-3,2,2,-1]
somme = 0
for elt in somme_tableau:
    if elt > 0:
        somme += elt
print("somme",somme)
