from math import gcd  # Utilisé pour calculer le PGCD (plus grand commun diviseur)


class Fraction:
    """Classe représentant une fraction et les opérations qui peuvent être effectuées sur celle-ci"""

    def __init__(self, num=0, den=1):
        """Construit une fraction à partir d'un numérateur et d'un dénominateur.

        PRÉ : 'den' doit être différent de zéro.
        POST : Crée une fraction avec le numérateur `num` et le dénominateur `den`,
               stockée sous forme réduite.
        """
        if den == 0:
            raise ValueError("Le dénominateur ne peut pas être zéro.")
        self.num = num
        self.den = den
        self._reduce()

    def _reduce(self):
        """Simplifie la fraction pour qu'elle soit sous forme réduite."""
        common_divisor = gcd(self.num, self.den)
        self.num //= common_divisor
        self.den //= common_divisor
        if self.den < 0:  # Assure que le dénominateur est toujours positif
            self.num = -self.num
            self.den = -self.den

    @property
    def numerator(self):
        """Retourne le numérateur de la fraction."""
        return self.num

    @property
    def denominator(self):
        """Retourne le dénominateur de la fraction."""
        return self.den

    def __str__(self):
        """Retourne une représentation textuelle de la fraction sous forme réduite."""
        if self.den == 1:
            return str(self.num)
        return f"{self.num}/{self.den}"

    def as_mixed_number(self):
        """Retourne une représentation textuelle de la fraction sous forme de nombre mixte."""
        whole = self.num // self.den
        remainder = abs(self.num % self.den)
        if remainder == 0:
            return str(whole)
        return f"{whole} {remainder}/{self.den}" if whole != 0 else f"{remainder}/{self.den}"

    def __add__(self, other):
        """Surcharge de l'opérateur + pour les fractions."""
        if not isinstance(other, Fraction):
            raise TypeError("L'opérande doit être une instance de Fraction.")
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        """Surcharge de l'opérateur - pour les fractions."""
        if not isinstance(other, Fraction):
            raise TypeError("L'opérande doit être une instance de Fraction.")
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        """Surcharge de l'opérateur * pour les fractions."""
        if not isinstance(other, Fraction):
            raise TypeError("L'opérande doit être une instance de Fraction.")
        return Fraction(self.num * other.num, self.den * other.den)

    def __truediv__(self, other):
        """Surcharge de l'opérateur / pour les fractions."""
        if not isinstance(other, Fraction):
            raise TypeError("L'opérande doit être une instance de Fraction.")
        if other.num == 0:
            raise ZeroDivisionError("Impossible de diviser par une fraction avec un numérateur de 0.")
        return Fraction(self.num * other.den, self.den * other.num)

    def __pow__(self, other):
        """Surcharge de l'opérateur ** pour les fractions."""
        if not isinstance(other, int):
            raise TypeError("L'exposant doit être un entier.")
        return Fraction(self.num**other, self.den**other)

    def __eq__(self, other):
        """Surcharge de l'opérateur == pour les fractions."""
        if not isinstance(other, Fraction):
            raise TypeError("L'opérande doit être une instance de Fraction.")
        return self.num == other.num and self.den == other.den

    def __float__(self):
        """Retourne la valeur décimale de la fraction."""
        return self.num / self.den

    def is_zero(self):
        """Vérifie si la valeur de la fraction est 0."""
        return self.num == 0

    def is_integer(self):
        """Vérifie si une fraction est entière."""
        return self.num % self.den == 0

    def is_proper(self):
        """Vérifie si la valeur absolue de la fraction est < 1."""
        return abs(self.num) < self.den

    def is_unit(self):
        """Vérifie si le numérateur de la fraction est 1 dans sa forme réduite."""
        return abs(self.num) == 1 and self.den == 1

    def is_adjacent_to(self, other):
        """Vérifie si deux fractions diffèrent par une fraction unité."""
        if not isinstance(other, Fraction):
            raise TypeError("L'opérande doit être une instance de Fraction.")
        diff = abs(self - other)
        return diff.num == 1 and diff.den > 1
