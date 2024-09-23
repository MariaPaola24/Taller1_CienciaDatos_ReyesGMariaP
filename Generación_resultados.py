# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 21:40:45 2024

@author: USUARIO
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json

# Cargar el dataset
file_path = "ruta_a_tu_archivo/listings.csv"  # Cambia a la ruta donde tienes el archivo CSV
df = pd.read_csv(file_path)

#Dimensiones del dataset
n_rows, n_columns = df.shape

#Tipos de datos
data_types = df.dtypes.astype(str)

#Selección de los 5 atributos más importantes
important_columns = ['price', 'bedrooms', 'number_of_reviews', 'review_scores_rating', 'neighbourhood_cleansed']

#Análisis univariado de los atributos seleccionados

# 4.1 Precio
df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)  # Convertir a formato numérico
price_stats = df['price'].describe()

#Gráfico de la distribución de precios
plt.figure(figsize=(8, 6))
sns.histplot(df['price'], kde=True, color='blue')
plt.title('Distribución del Precio')
plt.xlabel('Precio ($)')
plt.ylabel('Frecuencia')
plt.savefig('distribucion_precio.png')
plt.close()

#Número de habitaciones
bedrooms_stats = df['bedrooms'].describe()

# Gráfico de la distribución del número de habitaciones
plt.figure(figsize=(8, 6))
sns.countplot(df['bedrooms'], palette='coolwarm')
plt.title('Distribución del Número de Habitaciones')
plt.xlabel('Número de Habitaciones')
plt.ylabel('Frecuencia')
plt.savefig('distribucion_habitaciones.png')
plt.close()

#Número de reseñas
reviews_stats = df['number_of_reviews'].describe()

# Gráfico de la distribución del número de reseñas
plt.figure(figsize=(8, 6))
sns.histplot(df['number_of_reviews'], kde=True, color='green')
plt.title('Distribución del Número de Reseñas')
plt.xlabel('Número de Reseñas')
plt.ylabel('Frecuencia')
plt.savefig('distribucion_resenas.png')
plt.close()

#Calificación de las reseñas
rating_stats = df['review_scores_rating'].describe()

# Gráfico de la distribución de calificaciones
plt.figure(figsize=(8, 6))
sns.histplot(df['review_scores_rating'], kde=True, color='orange')
plt.title('Distribución de las Calificaciones')
plt.xlabel('Calificación')
plt.ylabel('Frecuencia')
plt.savefig('distribucion_calificaciones.png')
plt.close()

#Vecindario
neighbourhood_stats = df['neighbourhood_cleansed'].value_counts().head(10)

# Gráfico de los 10 vecindarios con más propiedades
plt.figure(figsize=(10, 6))
sns.barplot(x=neighbourhood_stats.values, y=neighbourhood_stats.index, palette='viridis')
plt.title('Top 10 Vecindarios con más Propiedades')
plt.xlabel('Número de Propiedades')
plt.ylabel('Vecindario')
plt.savefig('top_10_vecindarios.png')
plt.close()

# Generar el resumen
initial_report = {
    "Dimensiones del dataset": f"{n_rows} filas y {n_columns} columnas",
    "Tipos de datos": data_types.to_dict(),
    "Estadísticas del precio": price_stats.to_dict(),
    "Estadísticas del número de habitaciones": bedrooms_stats.to_dict(),
    "Estadísticas del número de reseñas": reviews_stats.to_dict(),
    "Estadísticas de calificaciones": rating_stats.to_dict(),
    "Top 10 vecindarios con más propiedades": neighbourhood_stats.to_dict(),
}

# Guardar el reporte en formato JSON
with open("reporte_entendimiento_inicial.json", "w") as outfile:
    json.dump(initial_report, outfile)

# Imprimir un mensaje indicando que los gráficos y el informe han sido generados correctamente
print("El reporte y los gráficos se han generado correctamente.")
