import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np

from utils.data_loader import load_data
from utils.configuracion import PAGE_CONFIG, COLORS

# Configuración de la página
st.set_page_config(**PAGE_CONFIG)


# Cargar datos
df = load_data()

# === NAVEGACIÓN ===
st.sidebar.header("🧭 Navegación")
page = st.sidebar.radio("Selecciona una página:", ["Inicio", "Análisis", "Resultados", "Conclusiones"])

# === PÁGINA HOME ===
if page == "Inicio":
    # Título principal con emoji
    st.title("🚢 Análisis de Supervivencia del Titanic")
    
    # Introducción del proyecto
    st.markdown("""
    ## 📋 Objetivo del Proyecto
    
    Este proyecto tiene como objetivo **analizar los factores que influyeron en la supervivencia de los pasajeros del Titanic** 
    mediante técnicas de análisis exploratorio de datos (EDA) y visualización interactiva.
    
    ### 🎯 Preguntas Clave a Responder:
    - ¿Qué factores fueron determinantes para la supervivencia?
    - ¿Cómo influyó la clase social en las posibilidades de supervivencia?
    - ¿Existieron diferencias significativas entre géneros y edades?
    - ¿El puerto de embarque tuvo algún impacto en la supervivencia?
    """)
    
    # Información sobre el dataset
    st.markdown("---")
    st.markdown("## 📊 Sobre el Dataset")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label="Total de Pasajeros",
            value=f"{df.shape[0]:,}",
            help="Número total de registros en el dataset"
        )
    
    with col2:
        supervivientes = df['Survived'].sum()
        st.metric(
            label="Supervivientes",
            value=f"{supervivientes:,}",
            delta=f"{(supervivientes/len(df)*100):.1f}%",
            help="Número y porcentaje de supervivientes"
        )
    
    with col3:
        st.metric(
            label="Variables Analizadas",
            value=f"{df.shape[1]}",
            help="Número de columnas/características en el dataset"
        )
    
    # Vista previa de los datos
    st.markdown("### 👀 Vista Previa de los Datos")
    with st.expander("Ver primeras filas del dataset", expanded=False):
        st.dataframe(df.head(10), use_container_width=True)
        st.caption(f"Mostrando las primeras 10 filas de {df.shape[0]} registros totales")
    
    # Información adicional
    st.markdown("---")
    st.markdown("""
    ### 🔍 Metodología del Análisis
    
    **1. Exploración Inicial:** Análisis descriptivo y limpieza de datos  
    **2. Análisis Univariado:** Distribución de variables individuales  
    **3. Análisis Bivariado:** Relaciones entre variables y supervivencia  
    **4. Visualizaciones:** Gráficos interactivos para insights clave  
    **5. Conclusiones:** Síntesis de hallazgos principales  
    
    ---
    
    💡 **Navega por las diferentes secciones** usando el menú lateral para explorar el análisis completo.
    """)

elif page == "Análisis":
    from Paginas.Analisis_datos import render_data_analysis_page
    render_data_analysis_page(df)

elif page == "Resultados":
    from Paginas.Resultados import render_results_page
    render_results_page(df)

elif page == "Conclusiones":
    from Paginas.Conclusiones import render_conclusions_page
    render_conclusions_page(df)

else:
    # Placeholder para otras páginas
    st.title(f"Página: {page}")
    st.write("Esta sección está en desarrollo. Pronto tendrás acceso al contenido completo.")    





