import matplotlib.pyplot as plt
from isometrie import Isometrie
from point import Point
from fonctions_independantes import points_segment_eucli


class SegmentHyp:

    def __init__(self, zA, zB):
        """
        Segment hyperbolique entre deux points ``zA`` et ``zB``
        dans le disque de Poincaré
        """
        self.zA = zA
        self.zB = zB

    def points_segment_hyp(self, precis=1e-4):
        """
        Renvoie une liste de points du segment hyperbolique
        entre ``zA`` et ``zB``
        """
        pointA = Point(self.zA)
        coeff1, coeff2 = pointA.coeffs_isometrie_vers_zero()

        f = Isometrie(coeff1, coeff2)

        zAA = f(self.zA)
        zBB = f(self.zB)
        liste_abs_tmp, liste_ord_tmp = points_segment_eucli(zAA, zBB, precis)

        liste_points = []

        z_tmp = self.zA

        for k in range(len(liste_abs_tmp)):
            z_tmp = liste_abs_tmp[k] + 1j * liste_ord_tmp[k]
            z_tmp = f.inverse(z_tmp)
            liste_points.append(z_tmp)

        return liste_points

    def trace_segment_hyp(self):
        """
        Trace le segment hyperbolique entre les deux points ``zA`` et ``zB``
        """
        liste_points = self.points_segment_hyp()
        liste_abscisses = []
        liste_ordonnees = []
        for z in liste_points:
            liste_abscisses.append(z.real)
            liste_ordonnees.append(z.imag)
        plt.plot(liste_abscisses, liste_ordonnees)
