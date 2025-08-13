from math import sqrt


class Point:

    def __init__(self, z):
        """
        point du plan hyperbolique
        """
        self.z = z

    def conjugue(self):
        """
        renvoie le conjugué de z
        """
        return self.z.real - 1j*self.z.imag

    def coeffs_isometrie_vers_zero(self):
        """
        calcule des coefficients de l'isométrie du disque de Poincaré,
        c'est-à-dire selon la matrice:
        [[a             b]
        [b barre      a barre]]
        qui envoie z sur 0 (avec a = coeff1 et b = boeff2)
        """
        coeff1 = 1/sqrt(1 - (self.z.real ** 2 + self.z.imag ** 2))
        coeff2 = -self.z/sqrt(1 - (self.z.real ** 2 + self.z.imag ** 2))
        return coeff1, coeff2
