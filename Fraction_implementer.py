"""
Nom : Zebiri Saad

Classe : 2TM2

"""
from math import gcd  # Utilisé pour calculer le PGCD (plus grand commun diviseur)

class Fraction:
    """Classe représentant une fraction et les opérations qui peuvent être effectuées sur celle-ci."""

    def __init__(self, num=0, den=1):
        """Construit une fraction à partir d'un numérateur et d'un dénominateur.

        PRÉ : 'den' doit être différent de zéro.
        POST : Crée une fraction avec le numérateur `num` et le dénominateur `den`,
               stockée sous forme réduite.
        EXCEPTIONS : Lève une ValueError si `den` est égal à zéro.
        """
        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError("Les numérateur et dénominateur doivent être des entiers.")
        if den == 0:
            raise ValueError("Le dénominateur ne peut pas être zéro.")
        self._num = num
        self._den = den
        self._reduce()



    @property
    def numerator(self):
        """Retourne le numérateur de la fraction."""
        return self._num

    @property
    def denominator(self):
        """Retourne le dénominateur de la fraction."""
        return self._den

    def __str__(self):
        """Retourne une représentation textuelle de la fraction sous forme réduite."""
        if self._den == 1:
            return str(self._num)
        return f"{self._num}/{self._den}"

    def as_mixed_number(self):
        if self._num == 0:
            return "0"
        whole = self._num // self._den
        remainder = abs(self._num % self._den)
        if remainder == 0:
            return str(whole)
        return f"{whole if whole != 0 else ''} {remainder}/{self._den}".strip()

    def __add__(self, other):
        """Surcharge de l'opérateur + pour les fractions."""
        if not isinstance(other, Fraction):
            raise TypeError("L'opérande doit être une instance de Fraction.")
        new_num = self._num * other._den + other._num * self._den
        new_den = self._den * other._den
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        """Surcharge de l'opérateur - pour les fractions."""
        if not isinstance(other, Fraction):
            raise TypeError("L'opérande doit être une instance de Fraction.")
        new_num = self._num * other._den - other._num * self._den
        new_den = self._den * other._den
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        """Surcharge de l'opérateur * pour les fractions."""
        if not isinstance(other, Fraction):
            raise TypeError("L'opérande doit être une instance de Fraction.")
        return Fraction(self._num * other._num, self._den * other._den)

    def __truediv__(self, other):
        """Surcharge de l'opérateur / pour les fractions."""
        if not isinstance(other, Fraction):
            raise TypeError("L'opérande doit être une instance de Fraction.")
        if other._num == 0:
            raise ZeroDivisionError("Impossible de diviser par une fraction avec un numérateur de 0.")
        return Fraction(self._num * other._den, self._den * other._num)

    def __pow__(self, exponent):
        if not isinstance(exponent, int):
            raise TypeError("L'exposant doit être un entier.")
        if exponent < 0:
            # Inverser la fraction pour la puissance négative
            if self._num == 0:
                raise ZeroDivisionError("Division par zéro.")
            return Fraction(self._den, self._num) ** -exponent
        elif exponent == 0:
            return Fraction(1, 1)  # Tout nombre à la puissance de zéro est 1
        else:
            return Fraction(self._num ** exponent, self._den ** exponent)

    def __eq__(self, other):
        """Surcharge de l'opérateur == pour les fractions."""
        if not isinstance(other, Fraction):
            raise TypeError("L'opérande doit être une instance de Fraction.")
        return self._num == other._num and self._den == other._den

    def __float__(self):
        """Retourne la valeur décimale de la fraction."""
        return self._num / self._den

    def is_zero(self):
        """Vérifie si la valeur de la fraction est 0."""
        return self._num == 0

    def is_integer(self):
        """Vérifie si une fraction est entière."""
        return self._num % self._den == 0

    def _reduce(self):
        """Simplifie la fraction pour qu'elle soit sous forme réduite."""
        initial_num, initial_den = self._num, self._den
        common_divisor = gcd(self._num, self._den)
        self._num //= common_divisor
        self._den //= common_divisor
        if self._den < 0:  # Assure que le dénominateur est toujours positif
            self._num = -self._num
            self._den = -self._den


    def is_proper(self):
        """Vérifie si la valeur absolue de la fraction est < 1."""
        result = abs(self._num) < self._den
        return result

    def is_unit(self):
        """Vérifie si le numérateur de la fraction est 1 dans sa forme réduite."""
        return abs(self._num) == 1 and self._den == 1

    def is_adjacent_to(self, other):
        """Vérifie si deux fractions diffèrent par une fraction unité."""
        if not isinstance(other, Fraction):
            raise TypeError("L'opérande doit être une instance de Fraction.")
        diff = abs(self - other)
        return diff._num == 1 and diff._den > 1
