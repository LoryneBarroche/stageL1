import matplotlib.pyplot as plt
from math import sqrt


class Disque:

    def __init__(self, centre=0+1j*0, rayon=1):
        """
        Disque dans le plan euclidien complexe de centre et rayon donnés.
        Par défaut, il s'agit du disque unité.
        Cela nous servira à tracer le contour du disque de Poincaré
        """
        self.centre = centre
        self.rayon = rayon

    # pas moi
    def _contour(self, nombre_points=10000):
        """
        Renvoie deux listes contenant les coordonnees selon x et y des points
        du cercle formant le contour du disque
        """
        abscisse_centre = self.centre.real
        ordonnee_centre = self.centre.imag
        liste_abscisses = [
            abscisse_centre - self.rayon + i * (2 * self.rayon) / nombre_points
            for i in range(nombre_points)
        ] + [abscisse_centre + self.rayon]
        liste_ordonnees = [
            sqrt(abs(self.rayon**2-(x-abscisse_centre)**2))+ordonnee_centre
            for x in liste_abscisses
        ]
        liste_ordonnees2 = [
            -sqrt(
                abs(self.rayon**2 - (x - abscisse_centre) ** 2)
                ) + ordonnee_centre
            for x in liste_abscisses
        ]
        liste_ordonnees2.reverse()
        liste_ordonnees.extend(liste_ordonnees2)
        liste_abscisses2 = [
            abscisse_centre - self.rayon + i * (2 * self.rayon) / nombre_points
            for i in range(nombre_points)
        ] + [abscisse_centre + self.rayon]
        liste_abscisses2.reverse()
        liste_abscisses.extend(liste_abscisses2)
        return liste_abscisses, liste_ordonnees

    # pas moi
    def trace_contour(self):
        """
        trace le contour du disque
        """
        liste_abscisses, liste_ordonnees = self._contour()
        plt.plot(liste_abscisses, liste_ordonnees, c="black")
