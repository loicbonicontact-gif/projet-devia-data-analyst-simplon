import plotly.express as px
import pandas as pd

# Données extraites des requêtes SQL (Produit A, B et C)
data = {
    'Produit': ['Produit A', 'Produit B', 'Produit C'],
    'Quantite': [1750, 1055, 575],
    'Chiffre_Affaires': [17500, 15825, 11500]
}
df = pd.DataFrame(data)
# --- Les ventes par produit (Volume) ---
fig_ventes = px.bar(
    df, 
    x='Produit', 
    y='Quantite', 
    title="6.a - Volume des ventes par produit",
    labels={'Quantite': 'Unités vendues'},
    text_auto=True
)
fig_ventes.write_html("ventes-par-produit.html")
# --- Le chiffre d'affaires par produit (Valeur) ---
fig_ca = px.bar(
    df, 
    x='Produit', 
    y='Chiffre_Affaires', 
    title="6.b - Chiffre d'affaires par produit (€)",
    labels={'Chiffre_Affaires': 'Chiffre d\'affaires (€)'},
    text_auto='.2f',
    color='Chiffre_Affaires'
)
fig_ca.write_html("ca-par-produit.html")
print("Succès : Les graphiques ont été générés dans ton dossier !")