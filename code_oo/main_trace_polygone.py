import matplotlib.pyplot as plt
from disque import Disque
from polygone_hyp import PolygoneHyp

disque = Disque()

disque.trace_contour()

m = int(input("choisissez le nombre de côtés, strictement supérieur à 2 : "))
while not m > 2:
    m = int(input(
        "Ce n'est pas le bon nombre."
        " Choisissez le nombre de côtés, strictement supérieur à 2 :"
        ))

if m == 3:
    angle_voulu = float(input(
        "Choisissez l'angle du polygone, en degrés, inférieur à 60° : "
        ))
    while not angle_voulu < 60:
        print("3")
        angle_voulu = int(input(
            "Ce n'est pas le bon nombre."
            "Choisissez l'angle du polygone, en degrés, inférieur à 60° :"
            ))
elif m == 4 or m == 5:
    angle_voulu = float(input(
        "Choisissez l'angle du polygone, en degrés, inférieur à 90° : "
        ))
    while not angle_voulu < 90:
        print("4 ou 5")
        angle_voulu = int(input(
            "Ce n'est pas le bon nombre."
            "Choisissez l'angle du polygone, en degrés, inférieur à 90° :"
            ))
elif m == 6:
    angle_voulu = float(input(
        "Choisissez l'angle du polygone, en degrés, inférieur à 120° : "
        ))
    while not angle_voulu < 120:
        print("6")
        angle_voulu = int(input(
            "Ce n'est pas le bon nombre."
            "Choisissez l'angle du polygone, en degrés, inférieur à 120° :"
            ))
else:
    angle_voulu = float(input("choisissez l'angle du polygone, en degrés : "))

precision = float(input("choisissez la précision de r : "))

polygone_hyp = PolygoneHyp(m, angle_voulu, precision)

r = polygone_hyp.r

print("r = ", r)

polygone_hyp.trace_polygone_hyp()

liste_points_premier_polygone = polygone_hyp.sommets


def premiere_couronne(liste_pts_sommets):
    zA = 0
    zB = 0
    liste_de_listes_pts_premiere_couronne = []
    liste_sym = []
    for i in range(len(liste_pts_sommets)):
        zA = liste_pts_sommets[i - 1]
        zB = liste_pts_sommets[i]
        liste_sym = polygone_hyp.points_symetrie_hyp_polygone(zA, zB)
        new_polygon = PolygoneHyp(m, angle_voulu, precision, liste_sym)
        new_polygon.trace_polygone_hyp()
        liste_de_listes_pts_premiere_couronne.append(liste_sym)
    return liste_de_listes_pts_premiere_couronne


a = premiere_couronne(liste_points_premier_polygone)

plt.axis("equal")
plt.show()
