from point import Point


class Isometrie:

    def __init__(self, a, b):
        """
        Isométries du disque de Poincaré, c'est-à-dire celles selon la matrice:
        [[a             b]
        [b barre      a barre]]

        le "barre" étant le conjugué complexe
        """
        self.a = a
        self.b = b

    def __call__(self, z):
        """
        Création de la fonction d'isométrie

        L'utilistaion de __call__ permet d'écrire : "f(z)"
        à la place de : "f.__call__(z)"
        lorsque l'on veut l'utiliser
        """
        a_conjugue = Point(self.a).conjugue()
        b_conjugue = Point(self.b).conjugue()
        return (self.a * z + self.b) / (b_conjugue*z + a_conjugue)

    def inverse(self, z):
        """
        Renvoie l'isométrie inverse
        """
        a_conjugue = Point(self.a).conjugue()
        b_conjugue = Point(self.b).conjugue()
        return (a_conjugue * z - self.b) / (-b_conjugue * z + self.a)
