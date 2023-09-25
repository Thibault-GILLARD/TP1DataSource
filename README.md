# TP1DataSource

Thibault Gillard

## Resultat du TP1

Analitics image 

![Image Description](https://github.com/Thibault-GILLARD/TP1DataSource/blob/master/source/Capture%20d%E2%80%99%C3%A9cran%202023-09-25%20%C3%A0%2008.42.08.png?raw=true)

Dashboard image

![Image Description](https://github.com/Thibault-GILLARD/TP1DataSource/blob/master/source/Capture%20d%E2%80%99%C3%A9cran%202023-09-19%20%C3%A0%2016.34.28.png?raw=true)

![Image Description](https://github.com/Thibault-GILLARD/TP1DataSource/blob/master/source/Capture%20d%E2%80%99%C3%A9cran%202023-09-25%20%C3%A0%2008.45.24.png?raw=true)

Bonus :

```html
# This is the button that we will be displayed on the page
    button_html = """
    <button onclick="sendEventToGA()">Click Me</button>"""
    
    # This is the code that will be executed when the button is clicked
    button_click_tracking = """ 
    <script>
        function sendEventToGA() {
            gtag('event', 'button_click', {
                'event_category': 'Custom Event Category',
                'event_label': 'Button Clicked'
            });
        }
    </script>
    """
  
    return prefix_google + "Hello from Space!" + button_html + button_click_tracking
```
![Image Description](https://github.com/Thibault-GILLARD/TP1DataSource/blob/master/source/Capture%20d%E2%80%99%C3%A9cran%202023-09-25%20%C3%A0%2008.45.24.png?raw=true)

# TP1 Résumé

## Objectif

- Créer une application Python avec Flask.
- Versionner le code avec GitHub.
- Déployer l'application avec Deta.
- Intégrer Google Analytics pour le suivi des utilisateurs.
- Préparer un rapport récapitulatif.

## Réalisations

### Application Python avec Deta

- Inscription/connexion à Deta.
- Déploiement avec Deta Micro.
- Accès au tableau de bord Deta.

### Versionnage avec GitHub

- Connexion à GitHub.
- Création d'un dépôt GitHub.
- Initialisation de Git.
- Création de fichiers essentiels (README, .gitignore, requirements.txt).

### Google Analytics

- Connexion à Google Analytics.
- Création d'un compte et d'une propriété.
- Intégration du code de suivi Google Analytics.
- Test d'installation.
- Consultation du tableau de bord Google Analytics.

### Rapport

- Création d'un rapport PDF incluant nom, URL de l'application, capture d'écran du tableau de bord Google Analytics, et URL du projet GitHub.

## Options Supplémentaires

- Ajout d'un bouton d'événement Google Analytics.

Félicitations pour avoir accompli le TP1, incluant la création, le versionnage, le déploiement, et le suivi de votre application Python.
