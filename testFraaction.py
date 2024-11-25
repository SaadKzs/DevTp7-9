import unittest
from Fraction_implementer import Fraction  # Remplacez par le nom de votre fichier Python contenant la classe Fraction


class TestFraction(unittest.TestCase):

    def test_constructor(self):
        """Test du constructeur"""
        # Cas normaux
        f1 = Fraction(3, 4)
        self.assertEqual(f1.numerator, 3)
        self.assertEqual(f1.denominator, 4)

        # Simplification automatique
        f2 = Fraction(6, 8)
        self.assertEqual(f2.numerator, 3)
        self.assertEqual(f2.denominator, 4)

        # Gestion des erreurs
        with self.assertRaises(ValueError):
            Fraction(1, 0)  # Denominateur nul

    def test_str(self):
        """Test de la méthode __str__"""
        f1 = Fraction(3, 4)
        self.assertEqual(str(f1), "3/4")

        f2 = Fraction(2, 1)
        self.assertEqual(str(f2), "2")

    def test_as_mixed_number(self):
        """Test de la méthode as_mixed_number"""
        f1 = Fraction(7, 3)
        self.assertEqual(f1.as_mixed_number(), "2 1/3")

        f2 = Fraction(4, 2)
        self.assertEqual(f2.as_mixed_number(), "2")

        f3 = Fraction(1, 3)
        self.assertEqual(f3.as_mixed_number(), "1/3")

    def test_addition(self):
        """Test de l'addition"""
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        result = f1 + f2
        self.assertEqual(result.numerator, 5)
        self.assertEqual(result.denominator, 6)

    def test_division(self):
        """Test de la division"""
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 4)
        result = f1 / f2
        self.assertEqual(result.numerator, 2)
        self.assertEqual(result.denominator, 1)

        # Division par zéro
        f3 = Fraction(0, 1)
        with self.assertRaises(ZeroDivisionError):
            f1 / f3

    def test_equality(self):
        """Test de l'égalité"""
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 4)
        f3 = Fraction(3, 4)
        self.assertTrue(f1 == f2)
        self.assertFalse(f1 == f3)

    def test_is_integer(self):
        """Test de la méthode is_integer"""
        f1 = Fraction(4, 2)
        self.assertTrue(f1.is_integer())

        f2 = Fraction(3, 2)
        self.assertFalse(f2.is_integer())

    def test_is_proper(self):
        """Test de la méthode is_proper"""
        f1 = Fraction(1, 2)
        self.assertTrue(f1.is_proper())

        f2 = Fraction(3, 2)
        self.assertFalse(f2.is_proper())

    def is_adjacent_to(self, other):
        """Vérifie si deux fractions diffèrent par une fraction unité."""
        if not isinstance(other, Fraction):
            raise TypeError("L'opérande doit être une instance de Fraction.")

        # Calcul de la différence
        diff = self - other

        # Assurez-vous que la fraction est bien simplifiée
        if diff.numerator < 0:
            diff = Fraction(-diff.numerator, diff.denominator)

        # Vérifie si la différence est exactement une fraction unité
        return diff.numerator == 1 and diff.denominator > 1


if __name__ == "__main__":
    unittest.main()
