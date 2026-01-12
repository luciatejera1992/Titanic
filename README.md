# Titanic — App de EDA interactiva (Streamlit)

Resumen del proyecto
--------------------

Aplicación interactiva para el análisis exploratorio del dataset del Titanic. La aplicación está
construida con Streamlit y contiene páginas para exploración de datos, visualizaciones y
conclusiones. Está pensada como una demo educativa de EDA con visualizaciones interactivas (Plotly)
y manipulación de datos con Pandas.

Estado
------

- Implementación principal en `Titanic:Streamlit/app.py` (interfaz y navegación).
- Páginas modulares en `Titanic:Streamlit/Paginas/` (Inicio, Análisis, Resultados, Conclusiones).
- Configuración centralizada en `Titanic:Streamlit/utils/configuracion.py`.
- Carga de datos en `Titanic:Streamlit/utils/data_loader.py` (usa `@st.cache_data`).

Estructura importante
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

- Las páginas son modulares: `app.py` importa y llama a funciones `render_*_page(df)` desde `Paginas/*` según la selección del sidebar.
- `utils/configuracion.py` contiene la paleta de colores (`COLORS`) y mapeo de nombres de columnas (`COLUMN_DISPLAY_NAMES`). Cualquier cambio de estilo o traducción debe hacerse ahí para que afecte a toda la app.
- `utils/data_loader.py` usa `Path(__file__).parent.parent / 'data/titanic_combined.csv'` y está decorado con `@st.cache_data` para evitar recargas de I/O en cada refresh.
- Las visualizaciones usan Plotly (px y graph_objects). Para mantener consistencia de color, usa `COLORS` definido en configuración.
- Las transformaciones derivadas (p. ej. `FamilySize`, `FamilyCategory`, extracción de `TITLE`) se realizan en las páginas antes de las visualizaciones; mantener esas transformaciones idempotentes ayuda con el cacheado y la reproducibilidad.

Buenas prácticas específicas
---------------------------

- Modifica `COLUMN_DISPLAY_NAMES` para cambiar etiquetas en tablas y captions — evita reemplazos directos en cada página.
- Si añades nuevos datasets, actualiza `utils/data_loader.py` con rutas y, de ser necesario, una opción para seleccionar dataset desde la UI.
- Mantén las importaciones de Streamlit (`st`) dentro de módulos de UI; las funciones utilitarias deben evitar efectos secundarios de UI para facilitar tests.

Contribuir
----------

Si quieres proponer cambios:

1. Haz un fork/branch y realiza cambios.
2. Asegúrate de que la app arranca con `streamlit run "Titanic:Streamlit/app.py"`.
3. Abre un pull request y describe el cambio y la página afectada.

Limitaciones conocidas
----------------------

- No hay tests automatizados en el repo actualmente.
- La estructura de nombres (`Titanic:Streamlit`) puede dar problemas en scripts que no citen la ruta entre comillas.

Contacto y feedback
-------------------

Si quieres que adapte el README (ej.: añadir un `requirements.txt`, scripts de dockerización o tests), dímelo y lo añado.


