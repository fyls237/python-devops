from typing import Union
import math

def validate_health_inputs(
    height: Union[int, float], 
    weight: Union[int, float], 
    age: Union[int, float] = None, 
    gender: str = None
) -> None:
    """
    Valide les paramètres d'entrée pour les calculs de santé.
    
    Args:
        height (float): Taille en centimètres
        weight (float): Poids en kilogrammes
        age (float, optional): Âge en années
        gender (str, optional): Genre ('M' ou 'F')
    
    Raises:
        ValueError: Si les paramètres ne respectent pas les contraintes
    """
    # Validation de la taille
    if not isinstance(height, (int, float)) or height <= 0 or height > 300:
        raise ValueError("La taille doit être un nombre positif entre 0 et 300 cm")
    
    # Validation du poids
    if not isinstance(weight, (int, float)) or weight <= 0 or weight > 700:
        raise ValueError("Le poids doit être un nombre positif entre 0 et 700 kg")
    
    # Validation de l'âge (si fourni)
    if age is not None:
        if not isinstance(age, (int, float)) or age <= 0 or age > 120:
            raise ValueError("L'âge doit être un nombre positif entre 0 et 120 ans")
    
    # Validation du genre (si fourni)
    if gender is not None:
        if gender not in ['M', 'F']:
            raise ValueError("Le genre doit être 'M' ou 'F'")

def calculate_bmi(height: Union[int, float], weight: Union[int, float]) -> float:
    """
    Calcule l'Indice de Masse Corporelle (IMC).
    
    Args:
        height (float): Taille en centimètres
        weight (float): Poids en kilogrammes
    
    Returns:
        float: Valeur de l'IMC
    """
    # Validation des entrées
    validate_health_inputs(height, weight)
    
    # Conversion de la taille en mètres
    height_meters = height / 100
    
    # Calcul de l'IMC
    bmi = weight / (height_meters ** 2)
    
    return round(bmi, 2)

def calculate_bmr(
    height: Union[int, float], 
    weight: Union[int, float], 
    age: Union[int, float], 
    gender: str
) -> float:
    """
    Calcule le Métabolisme de Base (BMR) selon l'équation de Harris-Benedict.
    
    Args:
        height (float): Taille en centimètres
        weight (float): Poids en kilogrammes
        age (float): Âge en années
        gender (str): Genre ('M' ou 'F')
    
    Returns:
        float: Taux métabolique basal en calories
    """
    # Validation des entrées
    validate_health_inputs(height, weight, age, gender)
    
    # Calcul du BMR selon le genre
    if gender == 'M':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:  # gender == 'F'
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    
    return round(bmr, 2)

def get_bmi_health_risk(bmi: float) -> dict:
    """
    Évalue les risques de santé en fonction de l'IMC.
    
    Args:
        bmi (float): Indice de Masse Corporelle
    
    Returns:
        dict: Catégorie de risque et recommandations
    """
    risk_categories = {
        (float('-inf'), 18.5): {
            'category': 'Sous-poids',
            'risk_level': 'Élevé',
            'recommendation': 'Consultez un professionnel de santé. Vous pourriez avoir besoin de prendre du poids.'
        },
        (18.5, 25): {
            'category': 'Poids normal',
            'risk_level': 'Faible',
            'recommendation': 'Maintenez un mode de vie sain avec une alimentation équilibrée et de l\'exercice.'
        },
        (25, 30): {
            'category': 'Surpoids',
            'risk_level': 'Modéré',
            'recommendation': 'Envisagez de faire de l\'exercice et d\'ajuster votre alimentation.'
        },
        (30, float('inf')): {
            'category': 'Obésité',
            'risk_level': 'Élevé',
            'recommendation': 'Consultez un professionnel de santé pour un plan de gestion personnalisé.'
        }
    }
    
    for (lower, upper), category_info in risk_categories.items():
        if lower < bmi <= upper:
            return category_info
    
    raise ValueError("Impossible de déterminer la catégorie de risque")

# Exemple d'utilisation
if __name__ == "__main__":
    try:
        # Test BMI
        test_height = 175  # cm
        test_weight = 70   # kg
        bmi_result = calculate_bmi(test_height, test_weight)
        bmi_risk = get_bmi_health_risk(bmi_result)
        
        print(f"IMC: {bmi_result}")
        print(f"Catégorie: {bmi_risk['category']}")
        print(f"Niveau de risque: {bmi_risk['risk_level']}")
        print(f"Recommandation: {bmi_risk['recommendation']}")
        
        # Test BMR
        test_age = 30
        test_gender = 'M'
        bmr_result = calculate_bmr(test_height, test_weight, test_age, test_gender)
        print(f"BMR: {bmr_result} calories")
        
    except ValueError as e:
        print(f"Erreur : {e}")