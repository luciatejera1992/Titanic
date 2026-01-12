
from utils.configuracion import COLORS
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from utils.data_loader import load_data

def render_conclusions_page(df):
    st.title("🎯 Conclusiones del Análisis del Titanic")
    
    st.markdown("""
    Esta sección presenta las **conclusiones finales** del análisis exploratorio de datos del Titanic, 
    sintetizando los hallazgos principales y sus **implicaciones** tanto históricas como metodológicas.
    """)
    
    # === RESUMEN EJECUTIVO ===
    
    st.markdown("""
    
    ### 📊 **Hallazgo Principal**
    
    **La supervivencia no fue aleatoria**, sino que estuvo **sistemáticamente influenciada** por:
    - **Factores demográficos**: Sexo y edad
    - **Factores socioeconómicos**: Clase del boleto
    - **Factores familiares**: Tamaño del grupo familiar
    - **Factores logísticos**: Puerto de embarque
    """)
    
    # Métricas de impacto visual
    col1, col2, col3 = st.columns(3)
    
    # Calcular métricas clave
    female_survival = df[df['Sex'] == 'female']['Survived'].mean()
    male_survival = df[df['Sex'] == 'male']['Survived'].mean()
    first_class_survival = df[df['Pclass'] == 1]['Survived'].mean()
    third_class_survival = df[df['Pclass'] == 3]['Survived'].mean()
    
    with col1:
        st.metric(
            label="🚺 Ventaja de Género",
            value=f"{female_survival/male_survival:.1f}x",
            delta="Las mujeres tuvieron 3.9x más probabilidades",
            help="Ratio de supervivencia femenina vs masculina"
        )
    
    with col2:
        st.metric(
            label="💎 Ventaja de Clase",
            value=f"{first_class_survival/third_class_survival:.1f}x",
            delta="Primera clase vs Tercera clase",
            help="Ratio de supervivencia entre primera y tercera clase"
        )
    
    with col3:
        st.metric(
            label="🎯 Precisión del Modelo Social",
            value="96.8%",
            delta="Mujeres de primera clase",
            help="La combinación más favorable de factores"
        )
    
    # === CONCLUSIONES POR FACTOR ===
    st.markdown("---")
    st.markdown("## 🔍 Conclusiones por Factor Analizado")
    
    # Factor 1: Género
    st.markdown("### 👥 Factor Género")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown(f"""
        **📊 Datos:**
        - Mujeres: **{female_survival:.1%}** supervivencia
        - Hombres: **{male_survival:.1%}** supervivencia
        - Diferencia: **{female_survival - male_survival:.1%}**
        
        **🎯 Conclusión:**
        El protocolo marítimo **"mujeres y niños primero"** 
        fue efectivamente aplicado durante la evacuación.
        """)
    
    with col2:
        # Gráfico comparativo de género
        gender_data = pd.DataFrame({
            'Género': ['Mujeres', 'Hombres'],
            'Supervivencia': [female_survival * 100, male_survival * 100],
            'Total': [len(df[df['Sex'] == 'female']), len(df[df['Sex'] == 'male'])]
        })
        
        fig_gender = px.bar(
            gender_data, 
            x='Género', 
            y='Supervivencia',
            title='Tasa de Supervivencia por Género',
            color='Supervivencia',
            color_continuous_scale='RdYlGn',
            text='Supervivencia'
        )
        fig_gender.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
        fig_gender.update_layout(height=350, showlegend=False)
        st.plotly_chart(fig_gender, use_container_width=True)
    
    # Factor 2: Clase Social
    st.markdown("### 🎫 Factor Clase Social")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Gráfico de supervivencia por clase
        class_survival = df.groupby('Pclass')['Survived'].mean()
        class_counts = df.groupby('Pclass').size()
        
        fig_class = go.Figure()
        
        fig_class.add_trace(go.Bar(
            name='Tasa de Supervivencia',
            x=['Primera Clase', 'Segunda Clase', 'Tercera Clase'],
            y=[class_survival[1] * 100, class_survival[2] * 100, class_survival[3] * 100],
            marker_color=[COLORS['success'], COLORS['warning'], COLORS['danger']],
            text=[f"{class_survival[1]:.1%}", f"{class_survival[2]:.1%}", f"{class_survival[3]:.1%}"],
            textposition='outside'
        ))
        
        fig_class.update_layout(
            title='Supervivencia por Clase Social',
            yaxis_title='Tasa de Supervivencia (%)',
            height=350,
            showlegend=False
        )
        st.plotly_chart(fig_class, use_container_width=True)
    
    with col2:
        st.markdown(f"""
        **📊 Datos:**
        - 1ª Clase: **{class_survival[1]:.1%}** ({class_counts[1]} pasajeros)
        - 2ª Clase: **{class_survival[2]:.1%}** ({class_counts[2]} pasajeros)
        - 3ª Clase: **{class_survival[3]:.1%}** ({class_counts[3]} pasajeros)
        
        **🎯 Conclusión:**
        La **posición socioeconómica** determinó 
        significativamente el acceso a los 
        **recursos de evacuación** (botes salvavidas, 
        ubicación de camarotes, información).
        """)
    
    # Factor 3: Interacción de Factores
    st.markdown("### 🔄 Interacción de Factores")
    
    # Crear matriz de supervivencia detallada
    interaction_data = []
    for pclass in [1, 2, 3]:
        for sex in ['female', 'male']:
            subset = df[(df['Pclass'] == pclass) & (df['Sex'] == sex)]
            if len(subset) > 0:
                interaction_data.append({
                    'Clase': f"{['Primera', 'Segunda', 'Tercera'][pclass-1]}",
                    'Sexo': 'Mujer' if sex == 'female' else 'Hombre',
                    'Tasa_Supervivencia': subset['Survived'].mean() * 100,
                    'Total': len(subset),
                    'Supervivientes': subset['Survived'].sum()
                })
    
    interaction_df = pd.DataFrame(interaction_data)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.dataframe(
            interaction_df[['Clase', 'Sexo', 'Tasa_Supervivencia', 'Total']].round(1),
            column_config={
                'Tasa_Supervivencia': st.column_config.ProgressColumn(
                    'Tasa Supervivencia (%)',
                    min_value=0,
                    max_value=100
                )
            },
            hide_index=True,
            use_container_width=True
        )
    
    with col2:
        st.markdown("""
        **💡 Insights Clave:**
        
        1. **Máxima supervivencia**: Mujeres de 1ª clase (96.8%)
        2. **Mínima supervivencia**: Hombres de 3ª clase (13.5%)
        3. **Brecha máxima**: 83.3 puntos porcentuales
        4. **Efecto multiplicativo**: Los factores se potencian mutuamente
        
        **🎯 Implicación**: La **intersección** de privilegios 
        sociales y protocolos de emergencia creó una 
        **jerarquía de supervivencia** muy marcada.
        """)
    
    # === IMPLICACIONES HISTÓRICAS ===
    st.markdown("---")
    st.markdown("## 🏛️ Implicaciones Históricas y Sociales")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📚 **Contexto Histórico (1912)**
        
        **🎭 Sociedad Eduardiana:**
        - Rígida estratificación social
        - Roles de género muy definidos
        - Diferencias de clase extremas
        
        **� Diseño del Titanic:**
        - Segregación física por clases
        - Acceso diferenciado a cubiertas
        - Ubicación estratégica de botes salvavidas
        
        **⚖️ Protocolos Marítimos:**
        - "Mujeres y niños primero" (protocolo Birkenhead)
        - Autoridad del capitán y oficiales
        - Jerarquía en situaciones de emergencia
        """)
    
    with col2:
        st.markdown("""
        ### 🔬 **Relevancia Contemporánea**
        
        **📊 Para Análisis de Datos:**
        - Importancia del contexto histórico
        - Sesgos sistemáticos en los datos
        - Interseccionalidad en el análisis
        
        **🚨 Para Gestión de Crisis:**
        - Planificación inclusiva de evacuación
        - Equidad en acceso a recursos de emergencia
        - Protocolos no discriminatorios
        
        **⚖️ Para Justicia Social:**
        - Impacto de desigualdades estructurales
        - Consecuencias de privilegios acumulados
        - Necesidad de políticas equitativas
        """)
    
    
    # === CONCLUSIÓN FINAL ===
    st.markdown("---")
    st.markdown("## 🎯 Conclusión Final")
    
    st.success("""
    ### 🏆 **Síntesis del Proyecto**
    
    Este análisis exploratorio del desastre del Titanic ha demostrado que **los datos pueden revelar 
    patrones profundos sobre desigualdad social y toma de decisiones en crisis**. 
    
    ### 🔬 **Valor del Análisis de Datos**
    
    - **📊 Cuantifica desigualdades** que podrían parecer anecdóticas
    - **🔍 Revela patrones sistemáticos** en lugar de eventos aleatorios  
    - **💡 Proporciona evidencia** para mejorar políticas y protocolos
    - **⚖️ Documenta injusticias** históricas con rigor científico
    """)
    
    # === AGRADECIMIENTOS Y FUENTES ===
    st.markdown("---")
    st.markdown("## 📚 Referencias y Metodología")
    
    with st.expander("📖 Fuentes de Datos y Metodología", expanded=False):
        st.markdown("""
        ### 📊 **Fuente de Datos:**
        - **Dataset**: Titanic - Machine Learning from Disaster (Kaggle)
        - **Registros**: 891 pasajeros con información completa
        - **Variables**: 12 características por pasajero
        - **Período**: Naufragio del RMS Titanic (15 de abril de 1912)
        
        ### 🔬 **Metodología Aplicada:**
        1. **Limpieza de datos**: Tratamiento de valores faltantes
        2. **Análisis exploratorio**: Estadística descriptiva e inferencial
        3. **Visualización**: Gráficos interactivos con Plotly
        4. **Análisis bivariado**: Correlaciones entre variables
        5. **Síntesis**: Interpretación contextual de resultados
        
        ### 🛠️ **Herramientas Utilizadas:**
        - **Python**: Lenguaje de programación principal
        - **Pandas**: Manipulación y análisis de datos
        - **Plotly**: Visualizaciones interactivas
        - **Streamlit**: Interfaz web interactiva
        - **NumPy**: Cálculos numéricos

""")
        

