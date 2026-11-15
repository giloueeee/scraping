import streamlit as st

# Configuration générale
st.set_page_config(page_title="My Streamlit Dashboard", layout="wide")

# Titre principal
st.title("My Streamlit Dashboard")
st.write("Bienvenue dans votre tableau de bord interactif construit avec Streamlit.")

# Séparateur
st.markdown("---")

# Présentation de l'application
st.header("Navigation")
st.write("""
Cette application est organisée en plusieurs pages accessibles via le menu situé
dans la barre latérale gauche.
Vous y trouverez :
- **textes** : contenu textuel, exemples de mise en forme, markdown, textes bruts
- **widgets** : démonstration interactive des widgets Streamlit (checkbox, sliders, etc.)
- **dashboard** : le tableau de bord avec deux colonnes
- **chargement** : barre de progression, message temporaire et spinner
""")

st.markdown("### Vous pouvez commencer en sélectionnant une page dans la sidebar.")

# Message d'info
st.info("Utilisez le menu dans la barre latérale gauche.")

# Pied de page
st.markdown("---")
st.caption("2025 – Dashboard Streamlit multi-page Exemple")
