import unittest
from Fraction_implementer import Fraction


class TestFraction(unittest.TestCase):

    def test_constructor(self):
        """Test du constructeur avec différents cas"""
        # Cas normaux
        f1 = Fraction(3, 4)
        self.assertEqual(f1.numerator, 3)
        self.assertEqual(f1.denominator, 4)

        # Simplification automatique
        f2 = Fraction(6, 8)
        self.assertEqual(f2.numerator, 3)
        self.assertEqual(f2.denominator, 4)

        # Fraction négative
        f3 = Fraction(-3, 4)
        self.assertEqual(f3.numerator, -3)
        self.assertEqual(f3.denominator, 4)

        # Dénominateur négatif
        f4 = Fraction(3, -4)
        self.assertEqual(f4.numerator, -3)
        self.assertEqual(f4.denominator, 4)

        # Gestion des erreurs
        with self.assertRaises(ValueError):
            Fraction(1, 0)  # Dénominateur nul

    def test_addition(self):
        """Tests de l'addition avec différents cas"""
        # Addition de fractions positives
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        result = f1 + f2
        self.assertEqual(result.numerator, 5)
        self.assertEqual(result.denominator, 6)

        # Addition avec une fraction négative
        f3 = Fraction(-1, 3)
        result = f1 + f3
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 6)

        # Addition de fractions nulles
        f4 = Fraction(0, 1)
        result = f1 + f4
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 2)

    def test_subtraction(self):
        """Tests de la soustraction avec différents cas"""
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        result = f1 - f2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 6)

        # Soustraction avec une fraction négative
        f3 = Fraction(-1, 3)
        result = f1 - f3
        self.assertEqual(result.numerator, 5)
        self.assertEqual(result.denominator, 6)

    def test_multiplication(self):
        """Test de la multiplication"""
        f1 = Fraction(2, 3)
        f2 = Fraction(3, 4)
        result = f1 * f2
        # Résultat simplifié : 6/12 devient 1/2
        self.assertEqual(result.numerator, 1)  # Numérateur attendu
        self.assertEqual(result.denominator, 2)  # Dénominateur attendu

        # Ajouter un cas supplémentaire pour une multiplication sans simplification immédiate
        f3 = Fraction(1, 2)
        f4 = Fraction(2, 3)
        result2 = f3 * f4
        # Résultat simplifié : 1/3
        self.assertEqual(result2.numerator, 1)
        self.assertEqual(result2.denominator, 3)

    def test_division(self):
        """Tests de la division"""
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 4)
        result = f1 / f2
        self.assertEqual(result.numerator, 2)
        self.assertEqual(result.denominator, 1)

        # Division par zéro
        with self.assertRaises(ZeroDivisionError):
            f1 / Fraction(0, 1)

    def test_equality(self):
        """Tests de l'égalité"""
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 4)
        self.assertTrue(f1 == f2)

        f3 = Fraction(3, 4)
        self.assertFalse(f1 == f3)

    def test_is_proper(self):
        """Tests de la méthode is_proper"""
        f1 = Fraction(1, 2)
        self.assertTrue(f1.is_proper())

        f2 = Fraction(3, 2)
        self.assertFalse(f2.is_proper())

        f3 = Fraction(-1, 2)
        self.assertTrue(f3.is_proper())

    def test_is_zero(self):
        """Tests de la méthode is_zero"""
        f1 = Fraction(0, 1)
        self.assertTrue(f1.is_zero())

        f2 = Fraction(1, 2)
        self.assertFalse(f2.is_zero())

    def test_as_mixed_number(self):
        """Tests de la méthode as_mixed_number"""
        f1 = Fraction(7, 3)
        self.assertEqual(f1.as_mixed_number(), "2 1/3")

        f2 = Fraction(4, 2)
        self.assertEqual(f2.as_mixed_number(), "2")

        f3 = Fraction(1, 3)
        self.assertEqual(f3.as_mixed_number(), "1/3")


if __name__ == "__main__":
    unittest.main()
