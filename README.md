# Knee_Arthritis_Detection
Proyecto de Detección y Clasificación de Artritis de Rodilla

## Setup del proyecto
**Requerimientos:** python 3.8 - 3.11

- Clonar repositorio

- En directorio del repositorio:

  - **Crear ambiente virtual:**
    `python3.x venv venv` (**Nota:** asegúrese de reemplazar x con la versión de python. Por ejemplo, en caso de tener python 3.9: `python3.9 venv venv`)

  - **Activar ambiente virtual:**
  
    En windows (terminal):  `./venv/Scripts/activate`
    
  - **Instalar requirements.txt:**
  
    En un terminal con el venv activado: `pip install -R requirements.txt`

## Carga del dataset

En donde se desee cargar el dataset de imágenes se debe realizar lo siguiente:
  
- Para trabajar con **sklearn**:
  - Importar la función `load_dataset` del archivo `utils.py`. Esta función recibe como parámetro el directorio de las imágenes (por defecto "data/raw/images") y retorna una tupla de 3 elementos:
      - **imgs:** Imágenes cargadas como array de NumPy de dimensiones (#imagenes, dim1, dim2) donde dim1 y dim2 es largo y ancho de las imágenes.
      - **labels:** Labels numéricos de las imágenes como array de NumPy (únicamente número según categorías).
      - **names:** Labels con clasificación de las imágenes como lista de python (por ejemplo, 0doubtful)

- Para trabajar con **tensorflow**:
  - Importar la función `load_dataset_tensorflow` del archivo `utils.py`. Esta función recibe como parámetro el directorio de las imágenes (por defecto "data/raw/images") y el subset que se desea cargar según lo siguiente:
      - **train:** Carga el dataset y lo configura como dataset de entrenamiento.
      - **valid:** Carga el dataset y lo configura como dataset de validación.
      - **both:** Carga una tupla con dos datasets, uno de entrenamiento y otro de validación.
  **NOTA:** En caso de usar **both**, se debe suministrar el parámetro **validation_split** como decimal entre 0 y 1 indicando el porcentaje del dataset usado para validación.
  
## Actualizar archivo requirements.txt

- Con el virtual environment activado ejecutar en consola: `pip freeze > requirements.txt`
- Realizar commit en repositorio y push.
