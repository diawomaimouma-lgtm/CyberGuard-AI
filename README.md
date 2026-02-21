# CyberGuard AI - Assistant Expert en Cybersécurité
Un chatbot spécialisé, rapide et sécurisé conçu pour les professionnels de la cybersécurité. Propulsé par l'API Groq (Llama-3.3-70b), cet outil fournit des analyses rigoureuses et techniques sur les menaces de sécurité.

## Fonctionnalités
- Personnalité Experte : Configuré par défaut comme un expert sérieux en cybersécurité.

- Réponses Ultra-Rapides : Utilise la technologie LPU de Groq pour une analyse instantanée.

- Interface Améliorée : Interface terminal en couleur pour une meilleure lisibilité (Bleu pour le Bot, jaune  pour l'Utilisateur).

- Horodatage : Chaque interaction est enregistrée avec l'heure précise.

- Mémoire Persistante : Sauvegarde l'historique de la conversation dans chat_history.json.

- Sécurité Avant Tout : Utilise des fichiers .env pour protéger vos clés API sensibles.

## Installation
1 **Cloner le project**:

  cd cyberguard- chatbot 

2 installer les  dependences:
pip install  groq python-dotenv colorama

3 Configuration de l API
-Créez un fichier nommé .env à la racine du dossier.

-Ajoutez votre clé API Groq à l'intérieur comme ceci :
 GROQ_API_KEY=gsk_votre_cle_secrete_ici

## utlisation (usage) et commandes
lancer l application: python main.py

- exit / quit	Ferme l'application de manière sécurisée.

- clear	Efface tout l'historique de la discussion actuelle.

- personality Remplace le rôle d'expert par une instruction personnalisée (ex: "Tu es un pirate").

## Structure du Projet
- main.py : L'interface du terminal et la boucle de gestion utilisateur.

- chatbot.py : La logique principale et la connexion à l'API Groq.

- chat_history.json : Stockage local pour la mémoire de la conversation.

- gitignore : Empêche les fichiers sensibles (comme .env) d'être publiés sur GitHub.

## Prérequis
- Python 3.8+ : Une version récente de Python est nécessaire pour assurer la compatibilité.

- Clé API Groq : Indispensable pour le fonctionnement de l'IA (Disponible gratuitement sur console.groq.com).

## Développé par [MAIMOUNA DIAWO]

*Restez en sécurité dans le monde numérique.*
