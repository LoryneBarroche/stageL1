from math import sqrt, cos, acos, sin, atan, ceil, degrees
# from math import pi
import matplotlib.pyplot as plt
import numpy as np


# pas moi

# 1

def points_cercle_disque(
        zI, rayon, nombre_points=10000
        ):
    """
    Renvoie deux listes contenant les coordonnees selon x et y des points
    d'un cercle de centre et de rayon donnés
    """
    abscisse_centre = zI.real
    ordonnee_centre = zI.imag
    liste_abscisses = [
        abscisse_centre - rayon + i * (2 * rayon) / nombre_points
        for i in range(nombre_points)
    ] + [abscisse_centre + rayon]
    liste_ordonnees = [
        sqrt(abs(rayon**2 - (x - abscisse_centre) ** 2)) + ordonnee_centre
        for x in liste_abscisses
    ]
    liste_ordonnees2 = [
        -sqrt(
            abs(rayon**2 - (x - abscisse_centre) ** 2)
            ) + ordonnee_centre
        for x in liste_abscisses
    ]
    liste_ordonnees2.reverse()
    liste_ordonnees.extend(liste_ordonnees2)
    liste_abscisses2 = [
        abscisse_centre - rayon + i * (2 * rayon) / nombre_points
        for i in range(nombre_points)
    ] + [abscisse_centre + rayon]
    liste_abscisses2.reverse()
    liste_abscisses.extend(liste_abscisses2)
    return liste_abscisses, liste_ordonnees


# moi

# 2

def conjugue_complexe(z):
    return z.real - 1j*z.imag


# moi

# 3

def isometrie_disque(a, b, z):
    return (a * z + b) / (conjugue_complexe(b)*z + conjugue_complexe(a))


# moi

# 4

def isometrie_disque_inverse(a, b, z):
    return (conjugue_complexe(a) * z - b) / (-conjugue_complexe(b) * z + a)


# moi

# 5

def coeffs_isometrie_vers_zero(z):
    coeff1 = 1/sqrt(1 - (z.real ** 2 + z.imag ** 2))
    coeff2 = -z/sqrt(1 - (z.real ** 2 + z.imag ** 2))
    return coeff1, coeff2


# moi

# 6

def points_segment_eucli(zA, zB, precision=0.0001):

    inv = False

    if zB.real < zA.real:
        zB, zA = zA, zB
        inv = True

    z_mouvant = zA
    pas = ceil(abs(zB - zA)/precision)
    # math.ceil() prend l'entier supérieur

    liste_abscisses = []
    liste_ordonnees = []

    for k in range(pas):
        z_mouvant = zA + (k/pas) * (zB - zA)
        liste_abscisses.append(z_mouvant.real)
        liste_ordonnees.append(z_mouvant.imag)

    if inv:
        liste_abscisses.reverse()
        liste_ordonnees.reverse()

    # plt.plot(liste_abscisses, liste_ordonnees)

    return liste_abscisses, liste_ordonnees


# moi

# 7

def points_segment_hyp(zA, zB):
    coeff1, coeff2 = coeffs_isometrie_vers_zero(zA)

    zAA = isometrie_disque(coeff1, coeff2, zA)
    zBB = isometrie_disque(coeff1, coeff2, zB)

    liste_abscisses_tmp, liste_ordonnees_tmp = points_segment_eucli(zAA, zBB)

    liste_points = []

    z_tmp = zA

    for k in range(len(liste_abscisses_tmp)):
        z_tmp = liste_abscisses_tmp[k] + 1j * liste_ordonnees_tmp[k]
        z_tmp = isometrie_disque_inverse(coeff1, coeff2, z_tmp)
        liste_points.append(z_tmp)

    return liste_points


# moi

# 8

def trace_segment_hyp(zA, zB):
    liste_points = points_segment_hyp(zA, zB)
    liste_abscisses = []
    liste_ordonnees = []
    for z in liste_points:
        liste_abscisses.append(z.real)
        liste_ordonnees.append(z.imag)
    plt.plot(liste_abscisses, liste_ordonnees)


# pas moi

# 9

def trace_disque():
    """
    trace le disque de rayon unité
    """
    liste_abscisses, liste_ordonnees = points_cercle_disque(0 + 1j*0, 1)
    plt.plot(liste_abscisses, liste_ordonnees, c="black")


# moi

# 10

def mesure_angle_complexes(zA, zB, sommet):
    AB = sqrt((zB.real - zA.real) ** 2 + (zB.imag - zA.imag) ** 2)
    BSommet = sqrt((sommet.real - zB.real) ** 2 + (sommet.imag - zB.imag) ** 2)
    ASommet = sqrt((sommet.real - zA.real) ** 2 + (sommet.imag - zA.imag) ** 2)
    frac = (AB ** 2 - ASommet ** 2 - BSommet ** 2)/(- 2 * ASommet * BSommet)
    return acos(frac)


# moi

# 11

def calcule_angle_polygone(m, alpha, r):

    liste_points_premier_polygone = []

    for k in range(m):
        liste_points_premier_polygone.append(
            complex(r*cos(k*alpha) + 1j*r*sin(k*alpha))
            )

    liste_points_lignes = []

    for i in range(len(liste_points_premier_polygone)):
        liste_points_lignes.append(
            points_segment_hyp(liste_points_premier_polygone[i-1],
                               liste_points_premier_polygone[i])
                              )

    pt1 = liste_points_lignes[1][len(liste_points_lignes[0]) - 11]
    pt2 = liste_points_lignes[2][10]
    sommet = liste_points_premier_polygone[1]
    return degrees(mesure_angle_complexes(pt1, pt2, sommet))


# moi

# 12

def symetrie_axiale(theta_sur_2, zA):
    theta = 2*theta_sur_2
    vect_zA = np.array([zA.real, zA.imag])
    S = np.array([[cos(theta), sin(theta)],
                 [sin(theta), -cos(theta)]])
    print(S, vect_zA, np.matmul(S, vect_zA))
    mul = np.matmul(S, vect_zA)
    return mul[0] + 1j*mul[1]


# moi

# 13

def dicho_rayon(nb_cotes, alpha, angle_voulu, precision):
    r_min = 0
    r_max = 1
    while r_max - r_min > precision:
        milieu = (r_min + r_max)/2
        angle_calcule = calcule_angle_polygone(nb_cotes, alpha, milieu)
        if angle_voulu < angle_calcule:
            r_min = milieu
        else:
            r_max = milieu
    return r_min


# moi

# 14

def points_symetrie_hyp_polygone(liste_pts_sommets, zA, zB):

    # 1 : homographie envoie A vers 0 et appliquée à tous les points

    liste_pts_sommets_homographie = []
    a, b = coeffs_isometrie_vers_zero(zA)
    for z in liste_pts_sommets:
        liste_pts_sommets_homographie.append(isometrie_disque(a, b, z))
    zA_homographie = isometrie_disque(a, b, zA)
    zB_homographie = isometrie_disque(a, b, zB)

    """liste_abscisses1 = []
    liste_ordonnees1 = []
    for z in liste_pts_sommets_homographie:
        liste_abscisses1.append(z.real)
        liste_ordonnees1.append(z.imag)
    plt.scatter(liste_abscisses1, liste_ordonnees1, color="blue")"""
    
    """l = liste_pts_sommets_homographie
    plt.scatter(l[0].real, l[0].imag, color="blue")"""

    # 2 : symétrie axiale par rapport à A'B'

    coeff_dir = (
        zB_homographie.imag - zA_homographie.imag)/(
            zB_homographie.real - zA_homographie.imag
            )

    liste_pts_sommets_symetrie = []
    theta_sur_2 = atan(coeff_dir)
    for z in liste_pts_sommets_homographie:
        liste_pts_sommets_symetrie.append(symetrie_axiale(theta_sur_2, z))

    """liste_abscisses2 = []
    liste_ordonnees2 = []
    for z in liste_pts_sommets_symetrie:
        liste_abscisses2.append(z.real)
        liste_ordonnees2.append(z.imag)
    plt.scatter(liste_abscisses2, liste_ordonnees2, color="red")"""

    # 3 : homographie inverse appliquée à tous ces points symétrisés

    liste_pts_sommets_homographie_inverse = []
    for z in liste_pts_sommets_symetrie:
        liste_pts_sommets_homographie_inverse.append(
            isometrie_disque_inverse(a, b, z)
            )

    """liste_abscisses = []
    liste_ordonnees = []
    for z in liste_pts_sommets_homographie_inverse:
        liste_abscisses.append(z.real)
        liste_ordonnees.append(z.imag)
    plt.scatter(liste_abscisses, liste_ordonnees, color="black")"""

    return liste_pts_sommets_homographie_inverse


# moi

# 15

def trace_polygone_hyp(liste_pts_sommets):
    for i in range(len(liste_pts_sommets)):
        trace_segment_hyp(
            liste_pts_sommets[i-1],
            liste_pts_sommets[i]
        )
    return


# moi

# 16

def premiere_couronne(liste_pts_sommets):
    zA = 0
    zB = 0
    liste_de_listes_pts_premiere_couronne = []
    liste_sym = []
    for i in range(len(liste_pts_sommets)):
        zA = liste_pts_sommets[i - 1]
        zB = liste_pts_sommets[i]
        liste_sym = points_symetrie_hyp_polygone(liste_pts_sommets, zA, zB)
        trace_polygone_hyp(liste_sym)
        liste_de_listes_pts_premiere_couronne.append(liste_sym)
    return liste_de_listes_pts_premiere_couronne


# moi
# reprendre entièrement les 2 prochaines fonctions car
# elles n'ont pas du tout été réfléchies !!!
# Je trace trop de fois chaque polygone

def couronne_suivante(liste_de_listes_pts_premiere_couronne):
    lst_de_lst_de_lst = []
    for i in range(len(liste_de_listes_pts_premiere_couronne)):
        lst_de_lst_de_lst.append(premiere_couronne(liste_de_listes_pts_premiere_couronne[i]))
    return lst_de_lst_de_lst


def couronne_apres(lst_de_lst_de_lst):
    lst_de_lst_de_lst_de_lst = []
    for i in range(len(lst_de_lst_de_lst)):
        for k in range(len(lst_de_lst_de_lst)):
            lst_de_lst_de_lst_de_lst.append(premiere_couronne(lst_de_lst_de_lst[i][k]))
    return lst_de_lst_de_lst_de_lst


"""A = 0.4 + -0.6j
B = 0.2 + 0.2j
plt.scatter(0, 0)
plt.scatter(A.real, A.imag)
plt.scatter(B.real, B.imag)
# plt.plot([A.real, B.real], [A.imag, B.imag])

trace_disque()
trace_segment_hyp(A, B)
symA = symetrie_axiale(pi/2, A)
print(symA)
plt.scatter(symA.real, symA.imag)
symB = symetrie_axiale(pi/2, B)
print(symB)
plt.scatter(symB.real, symB.imag)
axes = plt.gca()
plt.axis("equal")
plt.plot()
plt.show()"""
