from flask import Flask, request, jsonify, render_template, redirect, url_for
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
        
        try:
            value = float(data[field])
            if value <= 0:
                return False, f"Le champ '{field}' doit être un nombre positif"
        except ValueError:
            return False, f"Le champ '{field}' doit être un nombre"
    
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
    try:
        age = float(data['age'])
        if age <= 0:
            return False, "L'âge doit être un nombre positif"
    except ValueError:
        return False, "L'âge doit être un nombre"
    
    if 'gender' not in data:
        return False, "Le champ 'gender' est manquant"
    if data['gender'] not in ['M', 'F']:
        return False, "Le genre doit être 'M' ou 'F'"
    
    return True, ""

@app.route("/")
def home():
    return render_template('home.html')

@app.route('/health/bmi', methods=['GET', 'POST'])
def bmi():
    if request.method == 'POST':
        data = request.form
        is_valid, error_message = validate_basic_data(data)
        
        if not is_valid:
            return render_template('bmi.html', error=error_message)
        
        bmi = calculate_bmi(
            height=float(data['height']),
            weight=float(data['weight'])
        )
        
        result = {
            'bmi': round(bmi, 2),
            'category': get_bmi_category(bmi)
        }
        return render_template('bmi.html', result=result)
    
    return render_template('bmi.html')

@app.route('/health/bmr', methods=['GET', 'POST'])
def bmr():
    if request.method == 'POST':
        data = request.form
        is_valid, error_message = validate_bmr_data(data)
        
        if not is_valid:
            return render_template('bmr.html', error=error_message)
        
        bmr = calculate_bmr(
            height=float(data['height']),
            weight=float(data['weight']),
            age=float(data['age']),
            gender=data['gender']
        )
        
        result = {
            'bmr': round(bmr, 2),
            'daily_calories': get_daily_calories(bmr)
        }
        return render_template('bmr.html', result=result)
    
    return render_template('bmr.html')

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