import unittest
from typing import Union

from health_utils import (
    calculate_bmi, 
    calculate_bmr, 
    validate_health_inputs, 
    get_bmi_health_risk
)

class TestHealthUtils(unittest.TestCase):
    def test_validate_health_inputs(self):
        """Test la validation des entrées pour les calculs de santé."""
        # Cas valides
        try:
            validate_health_inputs(height=175, weight=70)
            validate_health_inputs(height=175, weight=70, age=30, gender='M')
        except ValueError:
            self.fail("Validation incorrecte pour des entrées valides")
        
        # Cas invalides
        with self.assertRaises(ValueError, msg="Doit rejeter une taille négative"):
            validate_health_inputs(height=-175, weight=70)
        
        with self.assertRaises(ValueError, msg="Doit rejeter un poids excessif"):
            validate_health_inputs(height=175, weight=1000)
        
        with self.assertRaises(ValueError, msg="Doit rejeter un genre invalide"):
            validate_health_inputs(height=175, weight=70, age=30, gender='X')
    
    def test_calculate_bmi(self):
        """Test le calcul de l'Indice de Masse Corporelle (IMC)."""
        test_cases = [
            # (height, weight, expected_bmi)
            (175, 70, 22.86),    # Poids normal
            (160, 50, 19.53),    # Limite sous-poids
            (190, 100, 27.70)    # Surpoids
        ]
        
        for height, weight, expected_bmi in test_cases:
            with self.subTest(height=height, weight=weight):
                calculated_bmi = calculate_bmi(height, weight)
                self.assertAlmostEqual(
                    calculated_bmi, 
                    expected_bmi, 
                    places=2, 
                    msg=f"IMC incorrect pour taille {height}cm et poids {weight}kg"
                )
    
    def test_calculate_bmr(self):
        """Test le calcul du Métabolisme de Base (BMR)."""
        test_cases = [
            # (height, weight, age, gender, expected_bmr)
            (175, 70, 25, 'M', 1706.69),   # Homme
            (160, 60, 30, 'F', 1384.14),   # Femme
            (180, 80, 35, 'M', 1813.61),   # Homme différent
            (165, 55, 40, 'F', 1336.31)    # Femme différente
        ]
        
        for height, weight, age, gender, expected_bmr in test_cases:
            with self.subTest(height=height, weight=weight, age=age, gender=gender):
                calculated_bmr = calculate_bmr(height, weight, age, gender)
                self.assertAlmostEqual(
                    calculated_bmr, 
                    expected_bmr, 
                    places=2, 
                    msg=f"BMR incorrect pour {gender}, {height}cm, {weight}kg, {age} ans"
                )
    
    def test_get_bmi_health_risk(self):
        """Test l'évaluation des risques de santé selon l'IMC."""
        test_cases = [
            # (bmi, expected_category, expected_risk_level)
            (16.5, 'Sous-poids', 'Élevé'),
            (22.0, 'Poids normal', 'Faible'),
            (27.5, 'Surpoids', 'Modéré'),
            (32.5, 'Obésité', 'Élevé')
        ]
        
        for bmi, expected_category, expected_risk_level in test_cases:
            with self.subTest(bmi=bmi):
                risk_info = get_bmi_health_risk(bmi)
                self.assertEqual(
                    risk_info['category'], 
                    expected_category, 
                    f"Catégorie incorrecte pour IMC {bmi}"
                )
                self.assertEqual(
                    risk_info['risk_level'], 
                    expected_risk_level, 
                    f"Niveau de risque incorrect pour IMC {bmi}"
                )
    
    def test_invalid_inputs(self):
        """Test la gestion des entrées invalides."""
        # Test IMC
        with self.assertRaises(ValueError, msg="Doit rejeter une taille invalide pour IMC"):
            calculate_bmi(-175, 70)
        
        # Test BMR
        with self.assertRaises(ValueError, msg="Doit rejeter un genre invalide pour BMR"):
            calculate_bmr(175, 70, 30, 'invalid')

def calculate_example_metrics():
    """
    Fonction de démonstration pour afficher des exemples de calculs.
    Utile pour les logs ou la documentation.
    """
    example_profiles = [
        {"height": 175, "weight": 70, "age": 30, "gender": 'M'},
        {"height": 160, "weight": 55, "age": 25, "gender": 'F'}
    ]
    
    print("=== Exemples de métriques santé ===")
    for profile in example_profiles:
        print(f"\nProfil : {profile}")
        
        bmi = calculate_bmi(profile['height'], profile['weight'])
        bmi_risk = get_bmi_health_risk(bmi)
        bmr = calculate_bmr(
            profile['height'], 
            profile['weight'], 
            profile['age'], 
            profile['gender']
        )
        
        print(f"IMC : {bmi}")
        print(f"Catégorie IMC : {bmi_risk['category']}")
        print(f"Niveau de risque : {bmi_risk['risk_level']}")
        print(f"Recommandation : {bmi_risk['recommendation']}")
        print(f"BMR : {bmr} calories")

if __name__ == '__main__':
    # Option 1 : Exécuter les tests unitaires
    unittest.main(verbosity=2)
    
    # Option 2 : Afficher des exemples de calculs
    # calculate_example_metrics()