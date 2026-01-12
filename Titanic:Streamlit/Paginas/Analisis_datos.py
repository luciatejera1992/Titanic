from utils.configuracion import COLORS
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import pandas as pd
import numpy as np
from utils.data_loader import load_data 

def render_data_analysis_page(df):
    st.title("🔍 Análisis Exploratorio de Datos")
    
    st.markdown("""
    En esta sección exploraremos los datos del Titanic en profundidad, aplicando técnicas de análisis exploratorio 
    para identificar patrones y tendencias que nos ayuden a entender los factores de supervivencia.
    """)
    
    # === INFORMACIÓN GENERAL DEL DATASET ===
    st.markdown("## 📊 Información General del Dataset")


    # Vista rápida y métricas principales

    st.markdown("""----""")

    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        st.metric("Filas", f"{df.shape[0]:,}")
    with col2:
        st.metric("Columnas", f"{df.shape[1]:,}")
    with col3:
        st.metric("Duplicados", f"{df.duplicated().sum():,}")

    st.markdown("""----""")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Modificaciones Realizadas")
        
        st.info("- Se han eliminado dos columnas [Cabin] y [Deck].")

        st.info("- La columna [Embarked] ha sido completada con la moda debido " \
                "a la poca cantidad de valores faltantes.")

        st.info("- Se han creado tres nuevas columnas, [Titulo], [Grupo Familiar], [Menor de edad].")

    with col2:
        st.markdown("### 📋 Resumen de Datos")
        info_data = {
            'Característica': ['Total de Pasajeros', 'Supervivientes', 'Tasa de Supervivencia', 'Variables Numéricas', 'Variables Categóricas'],
            'Valor': [
                f"{len(df):,}",
                f"{df['Survived'].sum():,}",
                f"{(df['Survived'].mean()*100):.1f}%",
                f"{df.select_dtypes(include=[np.number]).shape[1]}",
                f"{df.select_dtypes(include=['object']).shape[1]}"
            ]
        }
        st.dataframe(pd.DataFrame(info_data), hide_index=True, use_container_width=True)

    st.markdown("""----""")


# === ANÁLISIS UNIVARIADO ===

    st.markdown("## 📈 Análisis Univariado")
    
    # Distribución por Clase
    st.markdown("### 🎫 Distribución por Clase de Pasajero")

    col1, col2 = st.columns(2)

    with col1:
        # Gráfico de barras por clase
        class_counts = df['Pclass'].value_counts().sort_index()
        fig_class = px.bar(
            x=class_counts.index,
            y=class_counts.values,
            labels={'x': 'Clase', 'y': 'Número de Pasajeros'},
            title='Distribución de Pasajeros por Clase',
            color=class_counts.values,
            color_continuous_scale='Blues'
        )
        fig_class.update_layout(showlegend=False, height=400)
        st.plotly_chart(fig_class, use_container_width=True)
    
    with col2:
        # Tabla de distribución
        class_df = pd.DataFrame({
            'Clase': ['Primera', 'Segunda', 'Tercera'],
            'Cantidad': [
                len(df[df['Pclass'] == 1]),
                len(df[df['Pclass'] == 2]),
                len(df[df['Pclass'] == 3])
            ],
            'Porcentaje': [
                f"{len(df[df['Pclass'] == 1])/len(df)*100:.1f}%",
                f"{len(df[df['Pclass'] == 2])/len(df)*100:.1f}%",
                f"{len(df[df['Pclass'] == 3])/len(df)*100:.1f}%"
            ]
        })
        st.dataframe(class_df, hide_index=True, use_container_width=True)
        
        st.info("💡 La mayoría de pasajeros viajaban en tercera clase, seguido por primera y segunda clase.")
    
    # Distribución por Sexo
    st.markdown("### 👥 Distribución por Sexo")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Gráfico de pie por sexo
        sex_counts = df['Sex'].value_counts()
        fig_sex = px.pie(
            values=sex_counts.values,
            names=sex_counts.index,
            title='Distribución por Sexo',
            color_discrete_map={'male': COLORS['primary'], 'female': COLORS['success']}
        )
        fig_sex.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig_sex, use_container_width=True)
    
    with col2:
        # Distribución por puerto de embarque
        embark_counts = df['Embarked'].value_counts()
        fig_embark = px.bar(
            x=embark_counts.index,
            y=embark_counts.values,
            labels={'x': 'Puerto de Embarque', 'y': 'Número de Pasajeros'},
            title='Distribución por Puerto de Embarque',
            color=embark_counts.values,
            color_continuous_scale='Greens'
        )
        fig_embark.update_layout(showlegend=False, height=400)
        st.plotly_chart(fig_embark, use_container_width=True)
        st.markdown("La mayoría de pasajeros embarcó en **Southampton**, seguido por **Cherbourg** y **Queenstown**.")



# === DISTRIBUCION POR TITULO  ===


    st.markdown("### Distribución por Título")
    title_counts = df['TITLE'].value_counts()
    fig_title = px.bar(
        x=title_counts.index,
        y=title_counts.values,
        title='Distribución por Título',
        labels={'x': 'Título', 'y': 'Número de Pasajeros'},
        color=title_counts.values,
        color_continuous_scale='Blues'
    )
    fig_title.update_layout(showlegend=False, height=400)
    st.plotly_chart(fig_title, use_container_width=True)
    st.markdown("Los títulos más comunes son **Mr.**, **Miss.**, y **Mrs.**, reflejando las convenciones sociales de la época.") 
    