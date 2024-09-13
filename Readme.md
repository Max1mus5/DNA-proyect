# Proyecto de Biotecnología para la Feria Tecnológica
![alt CRIsPR CRAFT](./assets//logo.png)

Crearemos una red neuronal perceptrón multicapa (MLP) con conexiones residuales para predecir fenotipos a partir de datos genotípicos. El modelo incorporará el mapeo genotipo-fenotipo, utilizando características de entrada como los polimorfismos de nucleótido único (SNP) y las posiciones de los cromosomas para inferir rasgos fenotípicos, incorporaremos estadísticas de resumen (si están disponibles) y nos centraremos en las leyes mendelianas de la herencia para predecir fenotipos simples.

## Conjunto de datos propuesto: genome.csv
Estructura:
- rsid: Identificador del SNP.
- cromosoma: Número de cromosoma.
- posición: Posición física del SNP en el cromosoma.
- genotipo: Información del alelo (por ejemplo, AA, AG, GG).
#### Modificaciones:
- Puede añadir etiquetas fenotípicas (por ejemplo, color de ojos, altura, susceptibilidad a enfermedades) para el aprendizaje supervisado.

## 1. Requerimientos del Proyecto

### Funcionales
- **Interfaz Interactiva**: Los estudiantes podrán introducir secuencias de ADN.
- **Modelos de Predicción Fenotípica**: Inferir características fenotípicas a partir de ADN. Los modelos pueden estar orientados a plantas, árboles o humanos.
- **Modelo de Edición Genética**: Implementar un modelo básico de edición genética inspirado en CRISPR.
- **Apartado Educativo**: Explicaciones sobre las predicciones y las ediciones genéticas.

### No Funcionales
- **Usabilidad**: Aplicación amigable e intuitiva para estudiantes de secundaria.
- **Tiempo de Respuesta**: Predicciones con tiempos de respuesta razonables.
- **Escalabilidad**: Enfocada en uso puntual para la feria.
- **Visualización**: Gráficos o animaciones para ilustrar modificaciones de ADN.

### Colores
![alt colores](.//assets/colores.png)

## 2. Fases del Proyecto

### [Backend](./Backend/Readme.md)

#### Semana 1 (7/09 - 13/09)
- **Definir el Flujo de Trabajo**: Configurar el entorno y tecnologías a utilizar (Python, Jupyter, FastAPI).
- **Implementación del Modelo de Predicción**: Crear un modelo básico de inferencia fenotípica utilizando librerías como `scikit-learn`, `numpy`, y `pandas`.
- **Modelo de Edición Genética**: Estudio e implementación de un modelo básico de edición genética (inspirado en CRISPR), utilizando librerías como `Biopython`.

#### Semana 2 (14/09 - 20/09)
- **Refinamiento y Entrenamiento**: Mejorar el modelo con más datos y entrenamiento adicional.
- **Implementación de la API**: Desarrollar una API con FastAPI para recibir secuencias de ADN y devolver resultados de predicción y edición.

#### Semana 3 (21/09 - 27/09)
- **Pruebas de Rendimiento**: Testear la performance del backend y realizar ajustes necesarios.
- **Base de Datos**: Integrar una base de datos SQLite para almacenar predicciones y permitir comparaciones.
- **Integración del Modelo de Edición Genética**: Completar la integración del modelo de edición genética.

#### Semana 4 (28/09 - 1/10)
- **Pruebas Finales**: Verificar estabilidad y corregir errores.
- **Documentación**: Crear documentación detallada del backend.
- **Preparación para la Presentación**: Asegurar que todo esté listo para la presentación.

### Frontend

#### Semana 1 (7/09 - 13/09)
- **Diseño Inicial**: Definir el flujo de usuario, interfaces y componentes.
- **Elección de Framework**: Seleccionar herramientas y tecnologías (React, posible uso de Astro).

#### Semana 2 (14/09 - 20/09)
- **Implementación de la Interfaz**: Crear la interfaz para ingresar cadenas de ADN y visualizar resultados.
- **Integración de la API**: Conectar la interfaz con la API del backend para mostrar predicciones.
- **Explicaciones Visuales**: Desarrollar gráficos para ilustrar los cambios de ADN y sus efectos fenotípicos.

#### Semana 3 (21/09 - 27/09)
- **Refinamiento de Interfaz**: Añadir animaciones y mejorar la usabilidad.
- **Pruebas de Usabilidad**: Realizar pruebas con usuarios para asegurar una experiencia intuitiva.

#### Semana 4 (28/09 - 1/10)
- **Testeo Completo**: Revisar y ajustar la aplicación final.
- **Ajustes Finales**: Preparar la aplicación para la presentación.

## 5. Fecha de Entrega
- **Fecha Final**: 1 de octubre, dejando días para pruebas y ajustes finales.

