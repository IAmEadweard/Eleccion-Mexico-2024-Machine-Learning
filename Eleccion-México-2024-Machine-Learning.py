import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

#Cargar archivo
file_path = "presidencia2024.xlsx"
df = pd.read_excel(file_path)

#Convertir fechas
df['Fecha'] = pd.to_datetime(df['Fecha'])

#Crear variables de fecha
df['Año'] = df['Fecha'].dt.year
df['Mes'] = df['Fecha'].dt.month
df['Día'] = df['Fecha'].dt.day

#Candidatos en columnas
candidatos = ['XG', 'CS', 'JAM']

#Preparar features
X = df[['Año', 'Mes', 'Día']]
predicciones = {}
mae_scores = {}
coeficientes = {}
eleccion = pd.DataFrame({'Año': [2024], 'Mes': [6], 'Día': [2]})
fecha_prediccion = pd.to_datetime('2024-06-02')

#Entrenar un modelo para cada candidato
for candidato in candidatos:
    y = df[candidato]
    model = LinearRegression()
    model.fit(X, y)
    
    #Guardar coeficientes
    coeficientes[candidato] = model.coef_
    
    #Evaluar error (usando entrenamiento como aproximación)
    y_pred_train = model.predict(X)
    mae_scores[candidato] = mean_absolute_error(y, y_pred_train)

    #Predicción para el día de la elección
    pred = model.predict(eleccion)[0]
    predicciones[candidato] = pred

#Mostrar resultados
print("\n📊 Predicciones para el 2 de junio de 2024:")
ordenado = sorted(predicciones.items(), key=lambda x: x[1], reverse=True)
for nombre, porcentaje in ordenado:
    print(f"{nombre}: {porcentaje:.2f}%")

ganador, porcentaje = ordenado[0]
print(f"\n🏆 Ganador previsto: {ganador} con {porcentaje:.2f}%")

#Mostrar tabla resumen de métricas
print("\n📈 Resumen de modelos:")
resumen = pd.DataFrame({
    'Predicción (%)': predicciones,
    'MAE (error)': mae_scores,
    'Coef Año': {c: coef[0] for c, coef in coeficientes.items()},
    'Coef Mes': {c: coef[1] for c, coef in coeficientes.items()},
    'Coef Día': {c: coef[2] for c, coef in coeficientes.items()},
})
print(resumen.round(2))

#Visualizar tendencias
plt.figure(figsize=(12, 7))
colors = {'XG': '#1f77b4', 'CS': '#ff7f0e', 'JAM': '#2ca02c'}

for candidato in candidatos:
    plt.plot(df['Fecha'], df[candidato], label=candidato, color=colors[candidato])
    plt.scatter(df['Fecha'], df[candidato], color=colors[candidato], s=40)

    #Línea de regresión sobre el tiempo
    df_sorted = df.sort_values('Fecha')
    fechas_ordinal = df_sorted['Fecha'].map(pd.Timestamp.toordinal).values.reshape(-1, 1)
    model_fecha = LinearRegression().fit(fechas_ordinal, df_sorted[candidato])
    fechas_futuras = pd.date_range(start=df['Fecha'].min(), end=fecha_prediccion)
    pred_linea = model_fecha.predict(fechas_futuras.map(pd.Timestamp.toordinal).values.reshape(-1, 1))
    plt.plot(fechas_futuras, pred_linea, '--', color=colors[candidato], alpha=0.5)

    #Burbuja de predicción
    plt.scatter(fecha_prediccion + pd.Timedelta(days=3), predicciones[candidato],
                s=300, alpha=0.6, color=colors[candidato], edgecolors='black', label=f'Predicción {candidato}')
    plt.text(fecha_prediccion + pd.Timedelta(days=3), predicciones[candidato],
             f"{predicciones[candidato]:.1f}%", fontsize=10, ha='center', va='center', color='black')

plt.title('Tendencia de encuestas por candidato', fontsize=14)
plt.xlabel('Fecha')
plt.ylabel('Porcentaje estimado')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()