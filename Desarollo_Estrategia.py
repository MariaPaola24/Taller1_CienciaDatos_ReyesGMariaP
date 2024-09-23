# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 20:23:48 2024

@author: USUARIO
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el dataset de Bruselas, Bélgica
file_path = 'C:/Users/USUARIO/Downloads/listings1.csv'  
df = pd.read_csv(file_path)

#Transformar el precio a formato numérico (quitar símbolos como "$" y ",")
df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)

#Manejo de valores faltantes (imputar la media o eliminar filas con valores faltantes importantes)
df['review_scores_rating'].fillna(df['review_scores_rating'].mean(), inplace=True)  # Imputamos la media en las calificaciones
df.dropna(subset=['price', 'neighbourhood_cleansed', 'bedrooms'], inplace=True)  # Eliminamos filas con valores faltantes clave

#Convertir columnas categóricas (por ejemplo, vecindario)
df['neighbourhood_cleansed'] = df['neighbourhood_cleansed'].astype('category')

#Calcular estadísticos básicos
descriptive_stats = df[['price', 'number_of_reviews', 'review_scores_rating', 'bedrooms']].describe()

# Mostrar las estadísticas calculadas
print(descriptive_stats)

#Agrupar por vecindario para obtener estadísticas agregadas
grouped_neighborhood = df.groupby('neighbourhood_cleansed').agg(
    avg_price=('price', 'mean'),
    avg_rating=('review_scores_rating', 'mean'),
    total_reviews=('number_of_reviews', 'sum'),
    total_listings=('id', 'count')
).reset_index()

#Mostrar los vecindarios más caros y más asequibles
top_expensive_neighborhoods = grouped_neighborhood.sort_values(by='avg_price', ascending=False).head(10)
top_affordable_neighborhoods = grouped_neighborhood.sort_values(by='avg_price').head(10)

print("Vecindarios más caros:")
print(top_expensive_neighborhoods)

print("Vecindarios más asequibles:")
print(top_affordable_neighborhoods)

#Mapa de calor de precios promedio por vecindario
plt.figure(figsize=(12, 8))
sns.barplot(data=grouped_neighborhood, x='avg_price', y='neighbourhood_cleansed', palette='coolwarm')
plt.title('Precios promedio por vecindario')
plt.xlabel('Precio Promedio ($)')
plt.ylabel('Vecindario')
plt.show()

#Gráfico de dispersión: Precio vs Calificación
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='price', y='review_scores_rating', hue='neighbourhood_cleansed', palette='coolwarm', alpha=0.7)
plt.title('Precio vs Calificación de Propiedades')
plt.xlabel('Precio ($)')
plt.ylabel('Calificación')
plt.show()

#Boxplot de precios por vecindario para detectar outliers
plt.figure(figsize=(12, 8))
sns.boxplot(data=df, x='neighbourhood_cleansed', y='price', palette='coolwarm')
plt.xticks(rotation=90)
plt.title('Distribución de Precios por Vecindario')
plt.xlabel('Vecindario')
plt.ylabel('Precio ($)')
plt.show()

#Gráfico de densidad de precios
plt.figure(figsize=(10, 6))
sns.kdeplot(df['price'], shade=True, color="r")
plt.title('Distribución de Densidad de Precios')
plt.xlabel('Precio ($)')
plt.ylabel('Densidad')
plt.show()
