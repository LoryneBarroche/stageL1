from math import pi, cos, sin, atan, degrees
from segment_hyp import SegmentHyp
from fonctions_independantes import mesure_angle_complexes, symetrie_axiale
from point import Point
from isometrie import Isometrie
import matplotlib.pyplot as plt


class PolygoneHyp:

    def __init__(self, m, angle_voulu, precision=1e-5, sommets=[0]):
        # def __init__(self, m, angle_voulu, rayon=None, precision=1e-5):
        """
        Polygone régulier à ``m`` côtés d'angle ``angle_voulu``
        dans le disque de Poincaré.

        Ce polygone est centré à l'origine, la longueur euclidienne du
        rayon ``self.r`` est calculée avec ``precision``.

        Un polygone possède une liste de sommets: ``self.sommets``,
        chaque sommet est un nombre complexe du disque unité. On
        peut soit les générer soit les donner en paramètres.

        Le "_" avant une méthode signifie qu'elle ne sera pas utilisée
        à l'extérieur de la classe.
        """

        self.m = m
        self.angle_voulu = angle_voulu
        self.precision = precision
        self.alpha = 2*pi/self.m
        self.r = self._calcule_rayon()
        if sommets == [0]:
            # print("1")
            self.sommets = self._genere_sommets(self.r)
        else:
            # print("2")
            self.sommets = sommets
        # print(self.sommets)

    def _genere_sommets(self, r):
        """
        Génère la liste des sommets de ``self``.
        """

        liste_points_premier_polygone = []

        for k in range(self.m):
            liste_points_premier_polygone.append(
                complex(r*cos(k*self.alpha) + 1j*r*sin(k*self.alpha))
                )
        return liste_points_premier_polygone

    def _calcule_angle_polygone(self, r):
        """
        Calcule l'angle d'un polygone en fonction du rayon donné et
        des sommets du polygone. Tous les sommets ont le même angle,
        donc pour optimiser : on ne génère que 3 sommets et pas tout
        le polygone...
        Factuellement on ne pourrait en générer que 2 mais arrive une
        division par zéro dont je ne parviens pas à trouver la cause.
        """
        sommets = self._genere_sommets(r)

        liste_points_lignes = []

        for i in range(len(sommets)):
            segment = SegmentHyp(sommets[i - 1], sommets[i])
            points_segment = segment.points_segment_hyp()
            liste_points_lignes.append(points_segment)

        pt1 = liste_points_lignes[1][len(liste_points_lignes[0]) - 11]
        pt2 = liste_points_lignes[2][10]
        sommet = sommets[1]

        return degrees(mesure_angle_complexes(pt1, pt2, sommet))

    def _calcule_rayon(self):
        """
        Calcule le rayon par dichotomie en fonction du nombre de côtés et
        de l'angle voulu en respectant la précision.
        """
        r_min = 0
        r_max = 1
        while r_max - r_min > self.precision:
            milieu = (r_min + r_max)/2
            angle_calcule = self._calcule_angle_polygone(milieu)
            if self.angle_voulu < angle_calcule:
                r_min = milieu
            else:
                r_max = milieu
        return r_min

    def trace_polygone_hyp(self):
        """
        Trace le polygone étant donnée une liste de points de ses sommets
        """
        # print(self.sommets)
        for i in range(len(self.sommets)):
            segment_hyp = SegmentHyp(self.sommets[i-1], self.sommets[i])
            segment_hyp.trace_segment_hyp()

    def points_symetrie_hyp_polygone(self, zA, zB):
        """
        Réalise l'inversion d'un polygone par rapport à deux points, zA et zB.
        On procède en trois étapes, notées au fur et à mesure du code.

        Les bouts de code en commentaire dessinent les points
        à chaque étape de construction.
        """

        # 1 : isométrie envoie A vers 0 et appliquée à tous les points

        liste_pts_sommets_homographie = []
        pointA = Point(zA)
        a, b = pointA.coeffs_isometrie_vers_zero()
        f = Isometrie(a, b)
        for z in self.sommets:
            liste_pts_sommets_homographie.append(f(z))
        zA_homographie = f(zA)
        zB_homographie = f(zB)

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

        # 3 : isométrie inverse appliquée à tous ces points symétrisés

        liste_pts_sommets_homographie_inverse = []
        for z in liste_pts_sommets_symetrie:
            liste_pts_sommets_homographie_inverse.append(
                f.inverse(z)
                )

        """liste_abscisses = []
        liste_ordonnees = []
        for z in liste_pts_sommets_homographie_inverse:
            liste_abscisses.append(z.real)
            liste_ordonnees.append(z.imag)
        plt.scatter(liste_abscisses, liste_ordonnees, color="black")"""

        return liste_pts_sommets_homographie_inverse
