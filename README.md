# README: Visualisation Interactive des Salaires en Data Science

## Description du Projet
Ce projet permet d'explorer les salaires en Data Science à travers des visualisations interactives avec Streamlit et Plotly. Vous pouvez explorer les tendances par métier, niveau d'expérience, et emplacement tout en utilisant des filtres dynamiques pour affiner les résultats.

## Prérequis

### Installation des Bibliothèques
Vous devez créer un environnement conda et installer les bibliothèques nécessaires avec la commande suivante :
conda create -n projet python pandas numpy matplotlib jupyterlab kagglehub seaborn streamlit plotly
conda activate projet


### Chargement des Données
Les données sont chargées depuis une URL GitHub :

https://github.com/AxelG126/SAE_601/blob/main/ds_salaries.csv?raw=true


## Instructions
1. **Lancez l'application Streamlit** :

    streamlit run chemin_de_application.py

2. **Explorez les visualisations** en utilisant les différents filtres et options disponibles.
3. **Ajoutez des commentaires** clairs à votre code pour expliquer vos choix.

## Fonctionnalités Clés

### 1. Importation et chargement des données
Les données sont chargées depuis une source distante et affichées sous forme de tableau interactif.

### 2. Exploration des Données
Un bouton permet d’afficher un aperçu des premières lignes du jeu de données avec des descriptions explicatives des colonnes.

### 3. Distribution des Salaires en France
Un graphique box plot montre la répartition des salaires par niveau d’expérience et par fonction.

### 4. Salaire Moyen par Catégorie
Visualisez la moyenne des salaires par niveau d’expérience, fonction, type d’emploi ou localisation d’entreprise.

### 5. Corrélation entre Variables
Une matrice de corrélation et une heatmap permettent d'identifier les relations entre les variables numériques.

### 6. Évolution des Salaires par Métier
Affichez l’évolution des salaires des 10 métiers les plus réprésentés au fil des années.

### 7. Salaire Médian par Expérience et Taille d'Entreprise
Une visualisation permet de comparer les salaires médians par niveau d’expérience et taille d’entreprise.

### 8. Filtres Dynamiques
Un slider permet de filtrer les données par plages de salaires.

### 9. Impact du Télétravail
Un graphique montre la médiane des salaires par pays en fonction du pourcentage de télétravail.

### 10. Filtrage Avancé
Des filtres interactifs permettent de sélectionner les données selon le niveau d’expérience et la taille de l’entreprise.

## Navigation
Une barre de navigation latérale permet d’accéder rapidement aux différentes sections de l’application.
