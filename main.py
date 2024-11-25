from Fraction_implementer import Fraction


def main():
    try:
        # Création de fractions
        f1 = Fraction(3, 4)  # Fraction normale
        f2 = Fraction(5, 8)  # Une autre fraction
        f3 = Fraction(6, 3)  # Fraction qui devrait être simplifiée en un entier
        f4 = Fraction(0, 1)  # Fraction avec numérateur 0
        print(f"Fraction 1 : {f1}")
        print(f"Fraction 2 : {f2}")
        print(f"Fraction 3 (simplifiée) : {f3}")
        print(f"Fraction 4 : {f4}")

        # Utilisation de la méthode `as_mixed_number`
        print(f"Fraction 1 comme nombre mixte : {f1.as_mixed_number()}")

        # Opérations arithmétiques
        sum_result = f1 + f2
        print(f"Addition : {f1} + {f2} = {sum_result}")

        sub_result = f1 - f2
        print(f"Soustraction : {f1} - {f2} = {sub_result}")

        mul_result = f1 * f2
        print(f"Multiplication : {f1} * {f2} = {mul_result}")

        div_result = f1 / f2
        print(f"Division : {f1} / {f2} = {div_result}")

        power_result = f1 ** 2
        print(f"Puissance : {f1} ** 2 = {power_result}")

        # Comparaison
        print(f"Égalité entre {f1} et {f3} : {f1 == f3}")

        # Vérifications des propriétés
        print(f"{f1} est zéro ? {f1.is_zero()}")
        print(f"{f1} est un entier ? {f1.is_integer()}")
        print(f"{f1} est une fraction propre ? {f1.is_proper()}")
        print(f"{f1} est une fraction unité ? {f1.is_unit()}")
        print(f"{f1} est adjacent à {f2} ? {f1.is_adjacent_to(f2)}")

    except ValueError as ve:
        print(f"Erreur de valeur : {ve}")
    except ZeroDivisionError as zde:
        print(f"Erreur : Division par zéro détectée ! {zde}")
    except TypeError as te:
        print(f"Erreur de type : {te}")
    except Exception as e:
        print(f"Erreur inattendue : {e}")


if __name__ == "__main__":
    main()
