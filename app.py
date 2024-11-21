from flask import Flask, request, jsonify
from http import HTTPStatus
from typing import Dict, Any
from health_utils import calculate_bmi, calculate_bmr

app = Flask(__name__)

def validate_basic_data(data: Dict[str, Any]) -> tuple[bool, str]:
    """
    Valide les données de base (taille et poids).
    """
    if not data:
        return False, "Aucune donnée fournie"
    
    required_fields = ['height', 'weight']
    for field in required_fields:
        if field not in data:
            return False, f"Le champ '{field}' est manquant"
        
        if not isinstance(data[field], (int, float)) or data[field] <= 0:
            return False, f"Le champ '{field}' doit être un nombre positif"
    
    return True, ""

def validate_bmr_data(data: Dict[str, Any]) -> tuple[bool, str]:
    """
    Valide les données spécifiques au calcul du BMR.
    """
    is_valid, message = validate_basic_data(data)
    if not is_valid:
        return False, message
    
    if 'age' not in data:
        return False, "Le champ 'age' est manquant"
    if not isinstance(data['age'], (int, float)) or data['age'] <= 0:
        return False, "L'âge doit être un nombre positif"
    
    if 'gender' not in data:
        return False, "Le champ 'gender' est manquant"
    if data['gender'] not in ['M', 'F']:
        return False, "Le genre doit être 'M' ou 'F'"
    
    return True, ""

@app.route('/health/bmi', methods=['POST'])
def calculate_body_mass_index():
    """
    Calcule l'Indice de Masse Corporelle (IMC).
    """
    try:
        data = request.get_json()
        is_valid, error_message = validate_basic_data(data)
        
        if not is_valid:
            return jsonify({
                'error': error_message
            }), HTTPStatus.BAD_REQUEST
        
        bmi = calculate_bmi(
            height=data['height'],
            weight=data['weight']
        )
        
        return jsonify({
            'bmi': round(bmi, 2),
            'message': get_bmi_category(bmi)
        })
        
    except Exception as e:
        return jsonify({
            'error': f"Une erreur s'est produite: {str(e)}"
        }), HTTPStatus.INTERNAL_SERVER_ERROR

@app.route('/health/bmr', methods=['POST'])
def calculate_basal_metabolic_rate():
    """
    Calcule le Métabolisme de Base (BMR).
    """
    try:
        data = request.get_json()
        is_valid, error_message = validate_bmr_data(data)
        
        if not is_valid:
            return jsonify({
                'error': error_message
            }), HTTPStatus.BAD_REQUEST
        
        bmr = calculate_bmr(
            height=data['height'],
            weight=data['weight'],
            age=data['age'],
            gender=data['gender']
        )
        
        return jsonify({
            'bmr': round(bmr, 2),
            'daily_calories': get_daily_calories(bmr)
        })
        
    except Exception as e:
        return jsonify({
            'error': f"Une erreur s'est produite: {str(e)}"
        }), HTTPStatus.INTERNAL_SERVER_ERROR

def get_bmi_category(bmi: float) -> str:
    """
    Retourne la catégorie d'IMC correspondante.
    """
    if bmi < 18.5:
        return "Sous-poids"
    elif bmi < 25:
        return "Poids normal"
    elif bmi < 30:
        return "Surpoids"
    else:
        return "Obésité"

def get_daily_calories(bmr: float) -> Dict[str, float]:
    """
    Calcule les besoins caloriques quotidiens selon le niveau d'activité.
    """
    return {
        'sédentaire': round(bmr * 1.2, 2),
        'légèrement_actif': round(bmr * 1.375, 2),
        'modérément_actif': round(bmr * 1.55, 2),
        'très_actif': round(bmr * 1.725, 2),
        'extrêmement_actif': round(bmr * 1.9, 2)
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)