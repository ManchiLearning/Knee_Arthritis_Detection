# Configuración del Entorno de Desarrollo

## Fecha: [25/06/2024]

### Instalación de Anaconda
- **Descripción:** Instalación de Anaconda para gestionar el entorno de desarrollo.
- **Estado:** Completado
- **Pasos Realizados:**
  1. Visité el sitio web de Anaconda en [anaconda.com](https://www.anaconda.com/products/individual).
  2. Descargué el instalador adecuado para mi sistema operativo.
  3. Ejecuté el instalador y seguí las instrucciones en pantalla:
     - Acepté los términos y condiciones.
     - Elegí la instalación para "Just Me" (solo para mí).
     - Seleccioné la ubicación de instalación predeterminada.
     - Permití que el instalador agregue Anaconda a mi PATH.
  4. Verifiqué la instalación abriendo el terminal y ejecutando `conda --version`.
- **Resultado:** La instalación de Anaconda se completó exitosamente y `conda --version` muestra la versión de conda instalada.
- **Notas Adicionales:** Ninguna.

### Creación del Entorno Virtual
- **Descripción:** Creación del entorno virtual `knee_arthritis_env` con Python 3.12.4.
- **Estado:** Completado
- **Pasos Realizados:**
  1. Abrí Anaconda Navigator.
  2. Hice clic en "Environments" y luego en "Create".
  3. Nombré el entorno como `knee_arthritis_env` y seleccioné Python 3.12.4.
  4. Hice clic en "Create" para crear el entorno.
  5. Activé el entorno ejecutando `conda activate knee_arthritis_env` en la terminal.
- **Resultado:** El entorno `knee_arthritis_env` se creó y se activó exitosamente.
- **Notas Adicionales:** Ninguna.

### Instalación de Jupyter Notebook y Librerías Básicas
- **Descripción:** Instalación de Jupyter Notebook y librerías básicas para el proyecto.
- **Estado:** Completado
- **Comandos Utilizados:**
  ```sh
  conda install jupyter pandas numpy scikit-learn matplotlib seaborn
```

### Instalación de Librerías para Deep Learning y Procesamiento de Imágenes
- **Descripción:** Instalación de TensorFlow, Keras y Pillow para el procesamiento de imágenes y deep learning.
- **Estado:** Completado
- **Comandos Utilizados:**
  ```sh
  pip install tensorflow keras pillow
```

### Instalación de Librerías Adicionales
- **Descripción:** Instalación de librerías adicionales como OpenCV, SciPy, tqdm y albumentations..
- **Estado:** Completado
- **Comandos Utilizados:**
  ```sh
  pip install opencv-python scipy tqdm albumentations
```

### Verificación de la Instalación
- **Descripción:** Verificación de la instalación de todas las librerías necesarias.
- **Estado:** Completado
- **Notas:** Todas las librerías se instalaron correctamente y el entorno está listo para su uso.

## Próximas Tareas
- Organización de carpetas para el proyecto.
- Descarga de datos desde Kaggle.
- Verificación de la calidad de los datos.

## Notas y Comentarios
- Revisar las librerias instaladas, si se considera alguna otra, agregarla.