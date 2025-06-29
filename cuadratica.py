import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

#Cargar datos
file_path = "presidencia2024.xlsx"
df = pd.read_excel(file_path)
df['Fecha'] = pd.to_datetime(df['Fecha'])

#Variables
candidatos = ['XG', 'CS', 'JAM']
fecha_prediccion = pd.to_datetime('2024-06-02')
ordinal_prediccion = fecha_prediccion.toordinal()

#Resultados
predicciones = {}

plt.figure(figsize=(12, 7))
colors = {'XG': '#1f77b4', 'CS': '#ff7f0e', 'JAM': '#2ca02c'}

for candidato in candidatos:
    #Feature: fecha en días ordinales
    X = df['Fecha'].map(pd.Timestamp.toordinal).values.reshape(-1, 1)
    y = df[candidato].values

    #Generar features polinomiales grado 2
    poly = PolynomialFeatures(degree=2, include_bias=False)
    X_poly = poly.fit_transform(X)

    #Ajustar modelo
    model = LinearRegression().fit(X_poly, y)

    #Predicción para 2 de junio
    X_pred_poly = poly.transform(np.array([[ordinal_prediccion]]))
    pred = model.predict(X_pred_poly)[0]
    predicciones[candidato] = pred

    #Graficar puntos reales
    plt.scatter(df['Fecha'], df[candidato], color=colors[candidato], label=f'Datos {candidato}', s=40)

    #Graficar curva cuadrática
    fechas_futuras = pd.date_range(start=df['Fecha'].min(), end=fecha_prediccion + pd.Timedelta(days=5))
    fechas_ordinales = fechas_futuras.map(pd.Timestamp.toordinal).values.reshape(-1, 1)
    fechas_poly = poly.transform(fechas_ordinales)
    y_futuro = model.predict(fechas_poly)
    plt.plot(fechas_futuras, y_futuro, '--', color=colors[candidato], alpha=0.7, label=f'Tendencia {candidato}')

    #Burbuja de predicción
    plt.scatter(fecha_prediccion + pd.Timedelta(days=2), pred, s=300, alpha=0.6,
                color=colors[candidato], edgecolors='black')
    plt.text(fecha_prediccion + pd.Timedelta(days=2), pred,
             f"{pred:.1f}%", fontsize=10, ha='center', va='center', color='black')

#Gráfica general
plt.title('Tendencia de encuestas por candidato (Regresión Cuadrática)', fontsize=14)
plt.xlabel('Fecha')
plt.ylabel('Porcentaje estimado')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

#Imprimir predicciones ordenadas
print("\n📊 Predicciones para el 2 de junio de 2024 (Regresión Cuadrática):")
ordenado = sorted(predicciones.items(), key=lambda x: x[1], reverse=True)
for nombre, porcentaje in ordenado:
    print(f"{nombre}: {porcentaje:.2f}%")

ganador, porcentaje = ordenado[0]
print(f"\n🏆 Ganador previsto: {ganador} con {porcentaje:.2f}%")