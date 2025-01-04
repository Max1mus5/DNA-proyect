-- start
## Instalación

### Paso 1: Clona el Repositorio

```bash
git clone <https://github.com/Max1mus5/DNA-proyect.git>
cd DNA proyect
cd .\Backend\
```

### Paso 2: Crea un Entorno Virtual

Es recomendable crear un entorno virtual para manejar las dependencias del proyecto sin afectar tu sistema global.

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### Paso 3: Instala las Dependencias

Ejecuta el siguiente comando para instalar las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

### Paso 4: Inicia Jupyter Notebook

Para ejecutar el modelo de predicción fenotípica en Jupyter Notebook:

```bash
jupyter notebook
```

### Paso 5: Ejecuta el Servidor FastAPI

Para poner en marcha la API que se conectará con el frontend, usa:

```bash
python runserver.py
```
