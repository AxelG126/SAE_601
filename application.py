"""
📝 **Instructions** :
- Installez toutes les bibliothèques nécessaires en fonction des imports présents dans le code, utilisez la commande suivante :conda create -n projet python pandas numpy ..........
- Complétez les sections en écrivant votre code où c’est indiqué.
- Ajoutez des commentaires clairs pour expliquer vos choix.
- Utilisez des emoji avec windows + ;
- Interprétez les résultats de vos visualisations (quelques phrases).
"""

### 1. Importation des librairies et chargement des données
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px

# Chargement des données
url = 'https://github.com/AxelG126/SAE_601/blob/main/ds_salaries.csv?raw=true'
df = pd.read_csv(url)



### 2. Exploration visuelle des données
#Option pour afficher un aperçu des données
st.title("📊 Visualisation des Salaires en Data Science")
st.markdown("Explorez les tendances des salaires à travers différentes visualisations interactives.")

st.write("cocher cette case pour afficher les 5 premières lignes des données")
if st.checkbox("Afficher un aperçu des données"):
    st.write(df.head(5)) # Affiche les 5 premières lignes
    # Description des colonnes du DataFrame
    st.write("work_year : L'année au cours de laquelle le salaire a été versé.")
    st.write("experience_level : Le niveau d'expérience dans l'emploi au cours de l'année")
    st.write("employment_type : Le type d'emploi pour la fonction")
    st.write("job_title : La fonction exercée au cours de l'année.")
    st.write("salary (salaire) : Le montant total brut du salaire versé.")
    st.write("salary_currency : La devise du salaire versé sous la forme d'un code ISO 4217.")
    st.write("salary_in_usd : le salaire en USD")
    st.write("employee_residence : Pays de résidence principale de l'employé pendant l'année de travail, sous la forme d'un code pays ISO 3166.")
    st.write("remote_ratio : La quantité globale de travail effectué à distance")
    st.write("company_location : Le pays du bureau principal de l'employeur ou de la succursale contractante.")
    st.write("company_size : Nombre médian de personnes ayant travaillé pour l'entreprise au cours de l'année.")
#Ces détails de données ont été pris dans les explications du dataset sur kaggle
#Statistique générales avec describe pandas 

st.subheader("📌 Statistiques générales", anchor = "statistiques-generales")
st.write(df.describe())  # Affiche des statistiques descriptives
st.write("Voici une description des données, pour chaque variable quantitative on peut voir leur nombre, moyenne, mediane, quantil, minimum et maximum.")

### 3. Distribution des salaires en France par rôle et niveau d'expérience, uilisant px.box et st.plotly_chart
st.subheader("🌍 Distribution des salaires en France", anchor = "distribution-des-salaires-en-france")
df_france = df[df["company_location"] == "FR"] #garde uniquement la france pour la company-location
st.plotly_chart(px.box(df_france, x='experience_level', y='salary_in_usd', color='experience_level')) #box plot avec ce nouveau dataframe
st.write("Ce graphique montre la répartition des salaires selon le niveau d'expérience de la personne, on observe que les SE (senior) sont les mieux payés mais aussi ceux qui ont les plus grands écarts de salaire entre eux.")
st.write("Les 2 autres catégories sont bien plus proches les unes des autres et les salaires ont moins d'écarts entre eux que les seniors.")
st.write("Ce graphique montre la répartition des salaires selon le niveau d'expérience de l'employé.")
st.plotly_chart(px.box(df_france, x='job_title', y='salary_in_usd', color='experience_level')) #autre visualisation avec le job title cette fois



### 4. Analyse des tendances de salaires :
#### Salaire moyen par catégorie : en choisisant une des : ['experience_level', 'employment_type', 'job_title', 'company_location'], utilisant px.bar et st.selectbox 

var = st.selectbox('choisir un catégorie', options =['experience_level', 'employment_type', 'job_title', 'company_location']) #les colonnes sont selectionnable dans une selectbox
st.subheader(f"📅 Distribution des salaires par {var}", anchor = "distribution-des-salaires-par-variable") #affiche la titre pour la variable selectionnée
st.plotly_chart( px.bar(df.groupby(var,as_index = False)[['salary_in_usd']].mean().round(2).sort_values('salary_in_usd', ascending = False), x= var, y= 'salary_in_usd'))
#affiche la moyenne du salaire selon la catégorie sélectionnée, arrondis à 2 chiffres après la virgule, et trier dans l'ordre décroissant de moyenne de salaire.
st.write("Ce graphique permet de voir le salaire moyen selon la catégorie sélectionnée, les barres sont trier dans l'ordre décroissant de salaire moyen pour mieux observer quelle catégorie sont les mieux payées en moyenne.")
### 5. Corrélation entre variables
# Sélectionner uniquement les colonnes numériques pour la corrélation

numeric_df = df.select_dtypes(include=[np.number])
#garde uniquement les variables numériques

# Calcul de la matrice de corrélation
#votre code
correlation_matrix = numeric_df.corr()
#calcul de corrélation avec le nouveau df

# Affichage du heatmap avec sns.heatmap
fig, ax = plt.subplots()
st.subheader("🔬 Corrélations entre variables numériques", anchor = "correlations-entre-variables-numeriques")
st.write(correlation_matrix)
st.write("Sur cette matrice de corrélation on peut observer que les variables ne s'influence pas beaucoup entre elles, à l'exception de work_year qui influe légèrement sur toutes les variables, ce qui est logique car il y a es années covid dans les données qui ont donc influencé les salaires, la part de télétravail, etc.")
st.subheader("️🌡 Heatmap entre variables numériques",anchor = "heatmap-entre-variables-numeriques") #créer une heatmap à partir de la matrice de corrélation
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', ax = ax)
st.pyplot(fig)
st.write("Cette heatmap permet de représenter avec des couleurs la matrice de corrélation, pour y voir plus facilement les corrélations entre les variables.")


### 6. Analyse interactive des variations de salaire



# Une évolution des salaires pour les 10 postes les plus courants
# count of job titles pour selectionner les postes
# calcule du salaire moyen par an
#utilisez px.line 

top10 = df['job_title'].value_counts().nlargest(10).index #nouveau df avec les 10 métiers les plus représentés
salaire_moyen = df.groupby(["job_title","work_year"], as_index=False)[["salary_in_usd"]].mean() #salaire moyen par métier et par année
moyenne_salaire_top10 = salaire_moyen["job_title"].isin(top10) 
st.subheader("🏅 Salaire moyen des 10 métiers les plus représentés par année",anchor = "salaire-moyen-des-metiers")
st.write(salaire_moyen)
st.subheader("📈 Evolution du salaire moyen par année et par métier", anchor = "evolution-du-salaire")
st.plotly_chart(px.line(salaire_moyen[moyenne_salaire_top10],x="work_year",y="salary_in_usd",color='job_title')) 
st.write("On peut voir l'évolution des salaires par an selon les métiers, on peut observer des baisses drastiques en 2021 et des métiers qui se rajoute en graphique petit à petit en 2021 et 2022.")


# Créer le graphique


### 7. Salaire médian par expérience et taille d'entreprise
# utilisez median(), px.bar


salary_by_experience = df.groupby(["company_size", "experience_level"])[['salary_in_usd']].median().reset_index()#salaire médian par company_size et par experience_level


# Créer un graphique en barres avec des groupements de 4 barres
fig = px.bar(salary_by_experience, 
             x="company_size", 
             y="salary_in_usd", 
             color="experience_level", 
             barmode="group",  # Assurer que les barres sont groupées
             labels={"salary_in_usd": "Médiane du salaire en USD", "company_size": "Taille de l'entreprise"}
            )
st.subheader("🏢 Médiane des salaires par taille d'entreprise et niveau d'expérience",anchor = "mediane-salaires-taille")
# Afficher le graphique
st.plotly_chart(fig)
st.write("Ce graphique montre le salaire médian par taille d'entreprise (L / M / S) mais aussi en couleur le niveau d'expérience, on peut donc observer des choses intéressantes comme le fait que les seniors sont moins bien payés dans les petites entreprises en comparaison des autres salaires avec des plus grosses entreprises.")  

### 8. Ajout de filtres dynamiques
#Filtrer les données par salaire utilisant st.slider pour selectionner les plages  

st.subheader("🎚 Slider des salaires",anchor = "slider-des-salaires")
valeur_basse, valeur_haute = st.slider('label', min_value = df['salary_in_usd'].min(), max_value = df['salary_in_usd'].max(), value=(0,150000))#initialisation des paramètres du slider 
st.write("Nombre de valeurs: " + str(df.query(f"salary_in_usd >= {valeur_basse} and salary_in_usd <= {valeur_haute}").shape[0])) #affichage des données selon le slider
st.write(df.query(f"salary_in_usd >= {valeur_basse} and salary_in_usd <= {valeur_haute}"))


### 9.  Impact du télétravail sur le salaire selon le pays

salary_by_remote = df.groupby(["company_location", "remote_ratio"])[['salary_in_usd']].median().reset_index() #salaire median selon la company_size et le remote_ratio

# Créer un graphique en barres avec des groupements de 4 barres
fig3 = px.bar(salary_by_remote, 
             x="company_location", 
             y="salary_in_usd", 
             color="remote_ratio", 
             barmode="group",  # Assurer que les barres sont groupées
             labels={"salary_in_usd": "Médiane du salaire en USD", "company_size": "Taille de l'entreprise"}
            )
st.subheader("🏳 Médiane des salaires par pays de l'entreprise et niveau de télétravail",anchor = "salaire-pays-teletravail")
st.plotly_chart(fig3)
st.write("Ce graphique montre l'impact du télétravail sur les salaires par pays. En bleu foncé on a les salaires à 0% en télétravail, en bleu clair à 50 % en télétravail et en blanc à 100% en télétravail.")
st.write("On voit que les salaires sont globalement équilibrés selon le pourcentage de télétravail, à part en IE(Irlande) où les salaires en 0% télétravail sont bien supérieur aux salaires en télétravail dans les données que nous avons.") 
### 10. Filtrage avancé des données avec deux st.multiselect, un qui indique "Sélectionnez le niveau d'expérience" et l'autre "Sélectionnez la taille d'entreprise"
#votre code 

st.subheader("🎛 Filtres de données sur le niveau d'expérience et sur la taille de l'entreprise",anchor = "filtres")
experience_levels = df["experience_level"].unique()
company_sizes = df["company_size"].unique()

selected_experience = st.multiselect(
    "Sélectionnez le niveau d'expérience",
    options=experience_levels,
    default=experience_levels  # Sélectionne tout par défaut
)

selected_company_size = st.multiselect(
    "Sélectionnez la taille d'entreprise",
    options=company_sizes,
    default=company_sizes
)

# Application des filtres
filtered_df = df[
    (df["experience_level"].isin(selected_experience)) &
    (df["company_size"].isin(selected_company_size))
]

# Affichage du DataFrame filtré
st.write("Données filtrées :", filtered_df)


# Création de la barre de navigation statique
st.sidebar.header("Sommaire 📋")
st.sidebar.markdown("""
- [📌 Statistiques générales](#statistiques-generales)
- [🌍 Distribution des salaires en France](#distribution-des-salaires-en-france)
- [📅 Distribution des salaires par variable](#distribution-des-salaires-par-variable)
- [🔬 Corrélations entre variables numériques](#correlations-entre-variables-numeriques)
- [🌡️ Heatmap entre variables numériques](#heatmap-entre-variables-numeriques)
- [🏅 Salaire moyen des 10 métiers les plus représentés par année](#salaire-moyen-des-metiers)
- [📈 Evolution du salaire moyen par année des métiers les plus représentés](#evolution-du-salaire)
- [🏢 Médiane des salaires par taille d'entreprise et niveau d'expérience](#mediane-salaires-taille)
- [🎚️ Slider des salaires](#slider-des-salaires)
- [🏳️ Médiane des salaires par pays de l'entreprise et niveau de télétravail](#salaire-pays-teletravail)
- [🎛️ Filtres de données](#filtres)
""", unsafe_allow_html=True)

