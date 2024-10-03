# Procesamiento de una Cadena de ADN mediante Redes Neuronales: Predicción de Enfermedades a través de SNPs

## Introducción

El análisis de SNPs (polimorfismos de nucleótido único) en el ADN nos permite comprender cómo variaciones genéticas pueden influir en la predisposición a ciertas enfermedades. Las redes neuronales son herramientas poderosas que pueden aprender a partir de estas variaciones para predecir fenotipos, como la presencia o ausencia de enfermedades. En esta exposición, desglosaremos el procesamiento de una cadena de ADN a través de un modelo de red neuronal.



## Estructura del ADN:
<div align="center">
  <img src="../../assets/DNA.png" alt="ADN structure" width="400"/>
</div>

## Entendiendo los [SNPs](https://learn.genetics.utah.edu/content/precision/snips/)
![SNPsDiagram](../../assets/SNPs.svg)

## 1. Capa de Entrada

Comprendiendo ahora la estructura del ADN, y cuando se identifica un SNP, vamos a ver los puntos clave de la capa de entrada de nuestro modelo de red neuronal:

- **[Cromosoma](https://www.chromosomewalk.ch/en/list-of-chromosomes/) (numérico)**: Representa el cromosoma donde se encuentra el SNP. Por ejemplo, el cromosoma 12 se representaría simplemente como el número 1.

- **Posición**: Indica la ubicación exacta del SNP en el cromosoma. Por ejemplo, si el SNP está en la posición 72017, se codifica como 72017.

- **Genotipo**: Este es el tipo de alelo presente en la posición específica. Utilizamos codificación one-hot para representar los genotipos. Por ejemplo, para el genotipo AA, el vector sería [0, 0, 1] (donde [1, 0, 0] representa AA y [0, 1, 0] representa AG).

Así, un vector de entrada para un SNP específico podría verse así:

```
[1, 72017, 1, 0, 0]
```
<div align="center">
  <img src="../../assets/SNP-dataset.svg" alt="One-hot encoding" width="500"/>
</div>

## 2. Capas Ocultas

Las capas ocultas son donde ocurre la mayor parte del procesamiento en la red neuronal. En este modelo, empleamos:

- **Capas Densas con activación ReLU**: Cada capa densa aplica transformaciones lineales a la entrada y luego utiliza la función de activación ReLU (Rectified Linear Unit). Esto es importante porque permite que el modelo capture relaciones no lineales entre los diferentes SNPs y su relación con el fenotipo. La activación ReLU ayuda a resolver el problema del desvanecimiento del gradiente, permitiendo que los modelos profundos se entrenen de manera más efectiva.

- **Conexiones Residuales**: Estas conexiones permiten que la información de la capa anterior se incorpore directamente a la siguiente, facilitando que el modelo aprenda tanto los efectos lineales directos de los SNPs como las interacciones no lineales entre ellos. Este enfoque es similar al utilizado en arquitecturas avanzadas como ResNet, y mejora la capacidad del modelo para capturar relaciones complejas que afectan el riesgo de enfermedades.

## 3. Capa de Salida

La capa de salida produce la predicción final del modelo. Dependiendo del tipo de tarea, se elige la función de activación adecuada:

- **Clasificación binaria**: Para problemas que implican una predicción de sí/no (por ejemplo, presencia o ausencia de una enfermedad), utilizamos una función de activación sigmoide. Esta función devuelve un valor entre 0 y 1, que se interpreta como la probabilidad de que la enfermedad esté presente.

- **Clasificación multiclase**: Si el objetivo es predecir entre varias categorías (por ejemplo, diferentes tipos de color de ojos), se utiliza la función de activación softmax. Esto produce un vector de probabilidades para cada clase, donde la clase con la mayor probabilidad es la predicción final.

## 4. Técnicas Clave

Para asegurar que el modelo sea robusto y generalice bien, implementamos varias técnicas clave:

- **Regularización**: Utilizamos técnicas como la regularización L2, que penaliza los pesos grandes para evitar el sobreajuste, y el dropout, que desconecta aleatoriamente algunas neuronas durante el entrenamiento. Esto ayuda a prevenir que el modelo dependa demasiado de ciertas características.

- **Optimización**: Empleamos el optimizador Adam, que ajusta los pesos de la red de manera eficiente utilizando una tasa de aprendizaje adaptativa. Esto permite que el modelo converja más rápidamente a un buen mínimo en la función de pérdida.

## 5. Predicción de Fenotipos

El modelo se basa en los principios de la herencia mendeliana y las técnicas de aprendizaje automático para inferir fenotipos a partir del genotipo. En esencia, el modelo aprende a identificar patrones en las variaciones genéticas que están asociadas con el riesgo de enfermedad. Esto se traduce en una capacidad predictiva que puede tener implicaciones significativas para la medicina personalizada.

## Resumen

En resumen, el proceso de transformación de información genética en predicciones fenotípicas a través de redes neuronales implica:

1. **Codificación de datos genéticos** en un formato numérico comprensible.
2. **Aplicación de transformaciones no lineales** para capturar relaciones complejas entre SNPs y fenotipo.
3. **Uso de técnicas de regularización y optimización** para mejorar la generalización y la eficacia del modelo.

Con estas herramientas, podemos utilizar el poder del aprendizaje automático para predecir riesgos de enfermedades a partir de la genética, abriendo nuevas posibilidades en la atención médica y la investigación biomédica.

## Ejemplo de Predicción de Fenotipos a partir de SNPs

Para ilustrar cómo funciona nuestro modelo de red neuronal en la predicción de enfermedades, consideremos un conjunto de datos genéticos que contiene información sobre varios SNPs.

### Datos de Entrada

Supongamos que tenemos el siguiente conjunto de datos:

| rsid | Chromosome | Position | Genotype |
|------|------------|----------|----------|
| rs1  | 12         | 345678   | GG       |
| rs2  | 5          | 123456   | AG       |
| rs3  | 3          | 987654   | AA       |
| rs4  | 1          | 123456   | GG       |

### Transformación a Vectores de Entrada

Transformamos cada SNP en un vector numérico que nuestro modelo puede procesar:

- **Para el SNP rs1**: `Chromosome = 12`, `Position = 345678`, `Genotype = GG`  
  **Vector**: `[12, 345678, 0, 0, 1]`

- **Para el SNP rs2**: `Chromosome = 5`, `Position = 123456`, `Genotype = AG`  
  **Vector**: `[5, 123456, 0, 1, 0]`

- **Para el SNP rs3**: `Chromosome = 3`, `Position = 987654`, `Genotype = AA`  
  **Vector**: `[3, 987654, 1, 0, 0]`

- **Para el SNP rs4**: `Chromosome = 1`, `Position = 123456`, `Genotype = GG`  
  **Vector**: `[1, 123456, 0, 0, 1]`

### Preparación de los Datos para el Modelo

Ahora, podemos combinar estos vectores en un solo conjunto de datos de entrada para alimentar nuestro modelo. Esto puede verse como una matriz donde cada fila representa un SNP:

```
Inputs = [
    [12, 345678, 0, 0, 1],
    [5, 123456, 0, 1, 0],
    [3, 987654, 1, 0, 0],
    [1, 123456, 0, 0, 1]
]
```

### Proceso a través del Modelo

1. **Capa de Entrada**: Cada vector se alimenta a la red neuronal.

2. **Capas Ocultas**: A través de varias capas densas con activación ReLU, el modelo aprenderá las interacciones entre SNPs. Las conexiones residuales permitirán que la información fluya eficientemente entre las capas, facilitando el aprendizaje de relaciones complejas.

3. **Capa de Salida**: Para un problema de clasificación binaria (por ejemplo, predecir la presencia o ausencia de una enfermedad), la red neuronal generará una salida que será un valor entre 0 y 1.

### Output Esperado

Supongamos que, tras entrenar el modelo con suficientes datos, obtenemos una predicción de la probabilidad de que una enfermedad esté presente. El output del modelo podría ser:

- **Probabilidad de enfermedad**: `0.87`

Este valor indica que hay un 87% de probabilidad de que el paciente presente la enfermedad asociada a la combinación de SNPs analizados.

### Interpretación del Output

Con un output de `0.87`, podríamos interpretar que el modelo sugiere una alta predisposición a la enfermedad. Esto podría llevar a:

- **Recomendaciones para el paciente**: Realizar pruebas adicionales o implementar un seguimiento médico.
- **Investigación adicional**: Estudiar más sobre la relación entre los SNPs identificados y la enfermedad en cuestión, contribuyendo así a la ciencia médica.


