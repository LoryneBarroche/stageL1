from math import sqrt, cos, sin, acos, ceil
import numpy as np


def points_segment_eucli(zA, zB, precision=0.0001):
    """
    Renvoie une liste d'abscisses et une liste d'ordonnées des points
    d'un segment euclidien entre ``zA`` et ``zB``
    """
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
    return liste_abscisses, liste_ordonnees


def symetrie_axiale(theta_sur_2, zA):
    """
    Effectue la symétrie axiale d'un point zA par rapport à un axe passant par
    l'origine de notre repère (ici, le centre du disque de Poincaré) et
    formant un angle ``theta_sur_2`` avec l'axe des abscisses.

    L'angle entre zA et son symétrique est alors theta.
    La fonction rend les coordonées complexes du symétrique de zA.
    """
    theta = 2*theta_sur_2
    vect_zA = np.array([zA.real, zA.imag])
    S = np.array([[cos(theta), sin(theta)],
                  [sin(theta), -cos(theta)]])
    mul = np.matmul(S, vect_zA)
    return mul[0] + 1j*mul[1]


def mesure_angle_complexes(zA, zB, sommet):
    """
    Rend la valeur de l'angle (zA, sommet, zB), sachant que zA, zB et sommet
    sont tous trois des points du plan complexe
    """
    AB = sqrt((zB.real - zA.real) ** 2 + (zB.imag - zA.imag) ** 2)
    BSommet = sqrt((sommet.real - zB.real) ** 2 + (sommet.imag - zB.imag) ** 2)
    ASommet = sqrt((sommet.real - zA.real) ** 2 + (sommet.imag - zA.imag) ** 2)
    frac = (AB ** 2 - ASommet ** 2 - BSommet ** 2)/(- 2 * ASommet * BSommet)
    return acos(frac)
