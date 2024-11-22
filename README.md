# Application Santé : Calculateur de BMR et BMI

![Flask](https://img.shields.io/badge/Flask-2.2-blue) ![Python](https://img.shields.io/badge/Python-3.10-green) ![License](https://img.shields.io/badge/License-MIT-yellow)

## Description

Cette application Flask permet aux utilisateurs de calculer deux indicateurs clés pour leur santé :
- **IMC (Indice de Masse Corporelle)** : Permet de connaître si votre poids est adéquat en fonction de votre taille.
- **BMR (Métabolisme Basal)** : Calcule vos besoins caloriques quotidiens en fonction de votre taille, poids, âge, et niveau d'activité.

L'application est conçue pour être intuitive et stylée, afin d'offrir une expérience utilisateur optimale. Elle inclut des pages HTML interactives et responsives, facilitant l'entrée des données et l'affichage des résultats.

---

## Fonctionnalités

1. **Page d'accueil** :
   - Présentation de l'application.
   - Deux boutons pour accéder au calcul de l'IMC ou du BMR.

2. **Calcul de l'IMC** :
   - Formulaire permettant de saisir la taille et le poids.
   - Résultat affichant l'IMC, la catégorie correspondante (sous-poids, normal, surpoids, obésité) et des recommandations.

3. **Calcul du BMR** :
   - Formulaire pour saisir la taille, le poids, l'âge, et le genre.
   - Résultat affichant le BMR ainsi que des suggestions sur les besoins caloriques journaliers en fonction de différents niveaux d'activité.

4. **Navigation fluide** :
   - Boutons pour retourner à la page d'accueil ou choisir un autre calcul.

---

## Structure du Projet

### 📂 Dossiers et Fichiers

```plaintext
    health-calculator-service/
    ├── app.py
    ├── Dockerfile
    ├── health_utils.py
    ├── Makefile
    ├── README.md
    ├── requirements.txt
    ├── templates
    │   ├── base.html
    │   ├── bmi.html
    │   ├── bmr.html
    │   └── home.html
    └── tests
        └── test_health.py
```
- `app.py` : Le fichier principal de l'application Flask.
- `Dockerfile` : Définit l'image Docker pour l'application.
- `health_utils.py` : Contient les fonctions pour calculer l'IMC et le BMR.
- `Makefile` : Contient des commandes pour simplifier les tâches de développement
- `README.md` : Ce fichier.
- `requirements.txt` : Liste des dépendances Python nécessaires.
- `templates` : Dossier contenant les fichiers HTML pour les pages de l'application
- `tests` : Dossier pour les tests unitaires et d'intégration.
- `.github/workflow/ci-cd.yml` : Définit le workflow de CI/CD pour l'application sur Azure.

---

## Technologies Utilisées

- **Backend** : Flask (Python)
- **Frontend** : HTML5, CSS3
- **Tests** : `unittest` pour les tests unitaires
- **CI/CD** : GitHub Actions pour les déploiements automatisés

---

## Installation et Exécution

### 1. Prérequis

- `Python 3.10` ou version supérieure.
- `pip` pour gérer les dépendances.
- `Azure Web App` pour l'hébergement de l'application
- `GitHub Actions` pour la CI/CD
- `Azure credentials` pour l'authentifiaction sur azure

### 2. Installation et deéploiement de l'infra sur azure via github action

Clonez le dépôt et installez les dépendances :
```bash
    mkdir health-app
    cd health-app
    git clone https://github.com/fyls237/python-devops.git
    git push -uf origin main
```
Ou acceder directement à votre repository via github et cliquez sur le bouton "Actions" pour lancer
la CI/CD.

### 3. Exécution de l'application
- Accéder à l'application via le lien fourni par Azure Web App:
    [Application de calcul de la santé](https://health-calculator-service-f7eufqeff3hnh0ck.francecentral-01.azurewebsites.net/)



---

## Documentation 

- [Documentation Azure](https://docs.microsoft.com/fr-fr/azure)
- [Documentation Flask](https://flask.palletsprojects.com/en/2.0.x)
- [Documentation GitHub Actions](https://docs.github.com/en/actions)
- [Documentation Python](https://docs.python.org/3/)
- [Documentation unittest](https://docs.python.org/3/library/unittest.html)
- [Documentation Azure CLI](https://docs.microsoft.com/fr-fr/cli/azure/install-azure-cli)


---





