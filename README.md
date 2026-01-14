# 🚢 Titanic — Aplicación interactiva de análisis de datos (Streamlit)

Aplicación web interactiva desarrollada con **Streamlit** para realizar un **Análisis Exploratorio de Datos (EDA)** del dataset del Titanic.  
El proyecto combina **Python, Pandas y Plotly** para explorar patrones de supervivencia, generar visualizaciones dinámicas y presentar conclusiones de forma clara y estructurada.

Este repositorio forma parte de mi portfolio como **Analista de Datos Junior**, con foco en análisis, visualización y comunicación de insights mediante aplicaciones interactivas.

---

## 📌 Resumen del proyecto

- Aplicación web multipágina construida con Streamlit.
- Análisis exploratorio del dataset del Titanic.
- Visualizaciones interactivas orientadas a la interpretación de resultados.
- Arquitectura modular y reutilizable.
- Uso de buenas prácticas: cacheo de datos, separación de lógica y configuración centralizada.

---

## 🎯 Objetivos

- Explorar los factores que influyen en la supervivencia de los pasajeros.
- Analizar variables demográficas y socioeconómicas.
- Crear visualizaciones interactivas para facilitar la comprensión de los datos.
- Presentar conclusiones claras y reproducibles.
- Demostrar el uso de Streamlit como herramienta de análisis y storytelling con datos.

---

## 🧰 Tecnologías y herramientas

- **Python 3.10+**
- **Streamlit** — interfaz web interactiva
- **pandas** — manipulación y transformación de datos
- **numpy** — cálculos numéricos
- **plotly** — visualizaciones interactivas
- **Git / GitHub** — control de versiones y documentación

---

## 📁 Estructura del proyecto


---------------------

Rutas clave (desde la raíz del repo):

- `Titanic:Streamlit/app.py` — punto de entrada Streamlit.
- `Titanic:Streamlit/Paginas/` — páginas renderizadas dinámicamente: `Analisis_datos.py`, `Resultados.py`, `Conclusiones.py`, `Inicio.py`.
- `Titanic:Streamlit/utils/configuracion.py` — constantes como `PAGE_CONFIG`, `COLORS`, y `COLUMN_DISPLAY_NAMES` usadas por las páginas.
- `Titanic:Streamlit/utils/data_loader.py` — función `load_data()` que lee `data/titanic_combined.csv`.
- `Titanic:Streamlit/data/` — datasets CSV usados por la app (`titanic_combined.csv`, `titanic.csv`, `Titanic-Dataset.csv`).

Dependencias
-------------

La app requiere al menos:

- Python 3.10+ (se recomienda usar un virtualenv o venv)
- streamlit
- pandas
- plotly
- numpy

Instalación (ejemplo rápido)
----------------------------

1. Crear/activar entorno virtual (zsh/macOS):

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Instalar dependencias:

```bash
pip install streamlit pandas plotly numpy
```

Ejecutar la aplicación
----------------------

Desde la raíz del repositorio puedes ejecutar la app Streamlit con:

```bash
streamlit run "Titanic:Streamlit/app.py"
```

Nota: la carpeta del proyecto de la app contiene dos puntos (`Titanic:Streamlit`) — si tu shell interpreta el carácter `:`, pon la ruta entre comillas como en el ejemplo.

Detalles y convenciones del proyecto
----------------------------------

Arquitectura multipágina:
app.py gestiona la navegación y llama a funciones render_*_page(df) definidas en cada archivo de Paginas/.

Configuración centralizada:
utils/configuracion.py contiene constantes globales como:
PAGE_CONFIG
COLORS
COLUMN_DISPLAY_NAMES
Esto permite mantener consistencia visual y facilitar cambios globales.
Carga eficiente de datos:
utils/data_loader.py utiliza @st.cache_data para evitar recargas innecesarias del dataset y mejorar el rendimiento.

Visualizaciones:
Implementadas con Plotly (plotly.express y graph_objects).
La paleta de colores se mantiene consistente usando las constantes definidas en configuración.

Transformaciones de datos:
Variables derivadas (por ejemplo, FamilySize, FamilyCategory, extracción de Title) se calculan dentro de las páginas antes de las visualizaciones, manteniendo transformaciones idempotentes y reproducibles.

📊 Análisis Realizado

Distribución de supervivencia por sexo y clase.

Análisis de edad y tarifas.

Impacto del tamaño del grupo familiar.

Comparativa entre variables categóricas y numéricas.

Visualización de patrones relevantes para la supervivencia.

📈 Conclusiones

La clase social y el sexo influyen significativamente en la probabilidad de supervivencia.

Existen diferencias claras en supervivencia según rangos de edad.

El tamaño del grupo familiar presenta patrones interesantes en los resultados.

Las conclusiones completas están documentadas dentro de la aplicación y sus visualizaciones interactivas.


---

Lucía Tejera

Analista de Datos Junior

LinkedIn: https://linkedin.com/in/tu-perfil


