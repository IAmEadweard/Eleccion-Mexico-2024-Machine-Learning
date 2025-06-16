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
<p>Xóchitl Gálvez MAE de 3.92 </br> Claudia Sheinbaum MAE de 4.77 </br> JAM de 2.36</p>

<p>Como verán, esta métrica (MAE) es el promedio de la diferencia absoluta entre el valor real y el valor predicho; da valores positivos, y mientras más pequeños sean los valores, es mejor. Para empezar, esta métrica de evaluación indica que la candidata con peor predicción fue Claudia Sheinbaum, que a Jorge Máynez fue al que mejor predijo, y que el valor de Xóchitl Gálvez es un poco elevado, pero representa una buena predicción.</p>

<h3>Conclusión</h3>
<p>Analizando las respuestas del modelo con MAE, aparentemente sin sentido, nos damos cuenta de que el modelo predijo muy bien a Claudia Sheinbaum, aunque el algoritmo no opina lo mismo; que el modelo sobrestimó mucho a Xóchitl Gálvez, aunque el algoritmo tampoco lo interpreta así; y que la predicción de Jorge Máynez fue buena, aunque no mejor que la de Claudia Sheinbaum, pero el algoritmo considera que la de Máynez fue la mejor.</p>

<p>Entonces, solo me queda recalcar que algo debió haber pasado en los últimos meses antes de las elecciones, recordando que las encuestas de esta base de datos fueron realizadas entre julio de 2023 y mayo de 2024. Algo debió haber ocurrido antes del 2 de junio o en los ultimos meses de encuestas para que se beneficiara un poco a Jorge Máynez y se perjudicara a Xóchitl Gálvez. De Claudia Sheinbaum no hay mucho que decir, pues la diferencia entre sus valores reales y los predichos no es mucha.</p>

<p>Aunque el algoritmo no tiene mucha certeza sobre lo que pasó con ella, con los otros dos sí. Por lo tanto, debo concluir que los resultados no son muy diferentes a los reales, y muy probablemente sí ocurrió algo. Tomando en cuenta que esta base de datos utilizada no contempla las encuestas de personas que no sabían por qué candidato querían votar, llego ahora a la conclusión de que el conteo de los votos fue transparente y no hubo fraude.</p>
