import matplotlib.pyplot as plt
from math import pi, cos, sin
from TraceDisque import trace_disque, trace_polygone_hyp, dicho_rayon, premiere_couronne, couronne_suivante, couronne_apres

trace_disque()

m = int(input("choisissez le nombre de côtés, strictement supérieur à 2 : "))
while not m > 2:
    m = int(input(
        "Ce n'est pas le bon nombre."
        " Choisissez le nombre de côtés, strictement supérieur à 2:"
        ))

alpha = 2*pi/m
# theta = 2*pi/n

angle_voulu = float(input("choisissez la taille de l'angle du polygone en degrés : "))

precision = float(input("choisissez la précision de r : "))

r = dicho_rayon(m, alpha, angle_voulu, precision)

print("r = ", r)

liste_points_premier_polygone = []

for k in range(m):
    liste_points_premier_polygone.append(
        complex(r*cos(k*alpha) + 1j*r*sin(k*alpha))
        )

trace_polygone_hyp(liste_points_premier_polygone)

liste_de_listes_pts_premiere_couronne = premiere_couronne(liste_points_premier_polygone)

a = couronne_suivante(liste_de_listes_pts_premiere_couronne)
b = couronne_apres(a)

plt.axis("equal")
plt.show()
