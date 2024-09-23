# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 21:14:01 2024

@author: USUARIO
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset
file_path = "C:/Users/USUARIO/Downloads/listings1.csvv"  # Ruta al archivo proporcionado
df = pd.read_csv(file_path)

#Dimensiones del dataset
n_rows, n_columns = df.shape
print(f"Dimensiones del dataset: {n_rows} filas y {n_columns} columnas")

#Tipos de datos
print("\nTipos de datos de las columnas:")
print(df.dtypes)

#Selección de los 5 atributos más importantes
# Para un análisis inmobiliario, consideramos los siguientes atributos clave:
important_columns = ['price', 'bedrooms', 'number_of_reviews', 'review_scores_rating', 'neighbourhood_cleansed']

#Reporte del comportamiento de los atributos seleccionados (Análisis Univariado)

#Precio
print("\nAnálisis del atributo: Precio")
df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)  # Convertir a formato numérico
print(df['price'].describe())

#Gráfico de la distribución de precios
plt.figure(figsize=(8, 6))
sns.histplot(df['price'], kde=True, color='blue')
plt.title('Distribución del Precio')
plt.xlabel('Precio ($)')
plt.ylabel('Frecuencia')
plt.show()

#Número de habitaciones (bedrooms)
print("\nAnálisis del atributo: Número de habitaciones")
print(df['bedrooms'].describe())

#Gráfico de la distribución del número de habitaciones
plt.figure(figsize=(8, 6))
sns.countplot(df['bedrooms'], palette='coolwarm')
plt.title('Distribución del Número de Habitaciones')
plt.xlabel('Número de Habitaciones')
plt.ylabel('Frecuencia')
plt.show()

#Número de reseñas (number_of_reviews)
print("\nAnálisis del atributo: Número de reseñas")
print(df['number_of_reviews'].describe())

#Gráfico de la distribución del número de reseñas
plt.figure(figsize=(8, 6))
sns.histplot(df['number_of_reviews'], kde=True, color='green')
plt.title('Distribución del Número de Reseñas')
plt.xlabel('Número de Reseñas')
plt.ylabel('Frecuencia')
plt.show()

#Calificación de las reseñas (review_scores_rating)
print("\nAnálisis del atributo: Calificación de las reseñas")
print(df['review_scores_rating'].describe())

# Gráfico de la distribución de calificaciones
plt.figure(figsize=(8, 6))
sns.histplot(df['review_scores_rating'], kde=True, color='orange')
plt.title('Distribución de las Calificaciones de las Reseñas')
plt.xlabel('Calificación')
plt.ylabel('Frecuencia')
plt.show()

#Vecindario (neighbourhood_cleansed)
print("\nAnálisis del atributo: Vecindario")
print(df['neighbourhood_cleansed'].value_counts().head(10))

#Gráfico de los 10 vecindarios con más propiedades
plt.figure(figsize=(10, 6))
top_neighbourhoods = df['neighbourhood_cleansed'].value_counts().head(10)
sns.barplot(x=top_neighbourhoods.values, y=top_neighbourhoods.index, palette='viridis')
plt.title('Top 10 Vecindarios con más Propiedades')
plt.xlabel('Número de Propiedades')
plt.ylabel('Vecindario')
plt.show()

#Resumen final
print("\nResumen del análisis univariado:")
print(f"- Precio: Rango de precios desde ${df['price'].min()} hasta ${df['price'].max()}, con una media de ${df['price'].mean():.2f}.")
print(f"- Número de habitaciones: La mayoría de las propiedades tienen {df['bedrooms'].mode()[0]} habitaciones.")
print(f"- Número de reseñas: Las propiedades tienen entre {df['number_of_reviews'].min()} y {df['number_of_reviews'].max()} reseñas, con una media de {df['number_of_reviews'].mean():.2f}.")
print(f"- Calificación de las reseñas: Las calificaciones varían entre {df['review_scores_rating'].min()} y {df['review_scores_rating'].max()}, con una media de {df['review_scores_rating'].mean():.2f}.")
print(f"- Vecindarios: Los 10 vecindarios más comunes son {', '.join(top_neighbourhoods.index[:5])}.")
