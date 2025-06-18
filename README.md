<h1>Predicción de la Elección Presidencial de México 2024 mediante Regresión Lineal con Machine Learning en Python</h1>
<p>Este proyecto utiliza un modelo de regresión lineal desarrollado con técnicas de aprendizaje automático supervizado en Python para predecir al candidato ganador de la elección 
  presidencial de México, celebrada el 2 de junio de 2024. La predicción se basa en datos de encuestas recopiladas desde julio de 2023 hasta mayo de 2024. Además, se realiza una 
  comparación entre los resultados estimados por el modelo y los resultados oficiales obtenidos el día de la elección.</p>

<h3>Predicciones para el 2 de junio de 2024:</h3>
<p>Claudia Sheinbaum Pardo: 58.30%</p>
<p>Bertha Xóchitl Gálvez Ruíz: 32.94%</p>
<p>Jorge Álvarez Máynez: 8.56%</p>

<h3>Ganador previsto: Claudia Sheinbaum Pardo con 58.30%</h3>

<img src="Figure_1.png" alt="Predicción 2024" width="1000"/>

<h3>Porcentaje de votos de los valores reales y los valores predichos</h3>

<h4>Reales</h4>
<p>Claudia Sheinbaum Pardo: 59.3577%</p>
<p>Bertha Xóchitl Gálvez Ruiz: 27.9056%</p>
<p>Jorge Álvarez Máynez: 10.4187%</p>

<h4>Predichos</h4>
<p>Claudia Sheinbaum Pardo: 58.30%</p>
<p>Bertha Xóchitl Gálvez Ruiz: 32.94%</p>
<p>Jorge Álvarez Máynez: 8.56%</p>

<h3>Utilicé la métrica de Error Absoluto Medio para evaluar el rendimiento del modelo, y sus resultados fueron estos:</h3>
<p>Xóchitl Gálvez MAE de 3.92 </br> Claudia Sheinbaum MAE de 4.77 </br> Jorge Máynez MAE de 2.36</p>

<p>El MAE es una métrica que calcula el promedio de la diferencia absoluta entre los valores reales y los valores predichos, sin importar si fueron sobrestimados o subestimados. Cuanto menor es el MAE, mejor es la precisión del modelo.</p>

<p>En este caso, el modelo tuvo su menor error al predecir a Jorge Máynez, seguido de Xóchitl Gálvez, y con un mayor error en el caso de Claudia Sheinbaum. Aunque los valores predichos de Sheinbaum se aproximan bastante a su resultado real, el MAE refleja una mayor variabilidad en las encuestas, lo cual impacta el ajuste del modelo.</p>

<h3>Observaciones</h3>

<p>El modelo sobrestimó significativamente a Xóchitl Gálvez, lo que pudo haber sido resultado de una tendencia inflada en las encuestas previas a mayo de 2024, posiblemente debido a sesgos de respuesta o encuestadoras afiliadas.</p>
<p>Se observa una tendencia a la baja en los porcentajes de Xóchitl en los últimos meses, lo cual sugiere que votantes indecisos migraron a otras opciones, en especial a Jorge Máynez, quien mostró un crecimiento constante y estable hacia el final del periodo.</p>
<p>Aunque el MAE indica que la predicción de Máynez fue la más precisa, esto también puede explicarse por la menor varianza en las encuestas sobre su candidatura, lo cual facilitó el aprendizaje del modelo.</p>
<p>En el caso de Claudia Sheinbaum, el modelo predijo correctamente su victoria con un margen pequeño de error. Aunque el MAE es mayor en su caso, esto se debe en parte a la alta dispersión de datos en las encuestas, no necesariamente a una mala predicción general.</p>

<h3>Conclusión</h3>
<p>Tomando en cuenta el análisis del gráfico y la evaluación cuantitativa, se concluye que el modelo de regresión lineal aplicado fue capaz de capturar con buena precisión las tendencias generales de los candidatos, especialmente con Máynez y Sheinbaum. La sobrestimación de Xóchitl Gálvez revela una limitación común en modelos predictivos basados en encuestas: el posible sesgo en los datos de entrada.</p>

<p>Ademas, este modelo no contempló explícitamente a los votantes indecisos, cuya decisión final probablemente influyó en el ajuste de las proporciones, especialmente en el descenso de Xóchitl y el crecimiento de Máynez. No se detectan anomalías significativas entre los resultados reales y predichos que sugieran fraude electoral. Por lo tanto, los resultados predichos reflejan adecuadamente la realidad, y cualquier diferencia puede atribuirse a cambios legítimos en la intención de voto durante los últimos meses antes de la elección.</p>
