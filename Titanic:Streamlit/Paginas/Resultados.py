from utils.configuracion import COLORS
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st
import pandas as pd
import numpy as np
from utils.data_loader import load_data 

def render_results_page(df):
    st.title("📈 Resultados y Hallazgos Principales")
    
    st.markdown("""
    Esta sección presenta los **resultados clave** y **visualizaciones principales** derivados del análisis 
    exploratorio del dataset del Titanic, junto con las **interpretaciones** y **conclusiones** más relevantes.
    """)
    
    # === MÉTRICAS PRINCIPALES ===
    st.markdown("## 🎯 Métricas Clave del Análisis")
    
    # Calcular métricas principales
    total_passengers = len(df)
    survivors = df['Survived'].sum()
    survival_rate = (survivors / total_passengers) * 100
    
    # Métricas por categorías principales
    female_survival = df[df['Sex'] == 'female']['Survived'].mean() * 100
    male_survival = df[df['Sex'] == 'male']['Survived'].mean() * 100
    first_class_survival = df[df['Pclass'] == 1]['Survived'].mean() * 100
    third_class_survival = df[df['Pclass'] == 3]['Survived'].mean() * 100
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Tasa General de Supervivencia",
            value=f"{survival_rate:.1f}%",
            delta=f"{survivors} de {total_passengers}",
            help="Porcentaje total de pasajeros que sobrevivieron"
        )
    
    with col2:
        st.metric(
            label="Supervivencia Femenina",
            value=f"{female_survival:.1f}%",
            delta=f"+{female_survival - survival_rate:.1f}% vs promedio",
            delta_color="normal",
            help="Tasa de supervivencia de las mujeres"
        )
    
    with col3:
        st.metric(
            label="Supervivencia Primera Clase",
            value=f"{first_class_survival:.1f}%",
            delta=f"+{first_class_survival - survival_rate:.1f}% vs promedio",
            delta_color="normal",
            help="Tasa de supervivencia en primera clase"
        )
    
    with col4:
        st.metric(
            label="Brecha Clase Social",
            value=f"{first_class_survival - third_class_survival:.1f}pp",
            delta="Primera vs Tercera clase",
            delta_color="off",
            help="Diferencia en puntos porcentuales entre primera y tercera clase"
        )
    


    # === VISUALIZACIONES PRINCIPALES ===
    st.markdown("---")
    st.markdown("## 📊 Visualizaciones Clave")
    
    # 1. Dashboard de Supervivencia por Factores Principales
    st.markdown("### 🎯 Panel de Supervivencia por Factores Críticos")
    
    # Crear subplot con múltiples gráficos
    fig_dashboard = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Supervivencia por Sexo', 'Supervivencia por Clase', 
                       'Supervivencia por Puerto', 'Supervivencia por Edad'),
        specs=[[{"type": "bar"}, {"type": "bar"}],
               [{"type": "bar"}, {"type": "histogram"}]]
    )
    
    # Gráfico 1: Supervivencia por Sexo
    sex_survival = df.groupby('Sex')['Survived'].mean()
    fig_dashboard.add_trace(
        go.Bar(x=['Femenino', 'Masculino'], 
               y=[sex_survival['female'], sex_survival['male']],
               name='Por Sexo',
               marker_color=[COLORS['success'], COLORS['primary']]),
        row=1, col=1
    )
    
    # Gráfico 2: Supervivencia por Clase
    class_survival = df.groupby('Pclass')['Survived'].mean()
    fig_dashboard.add_trace(
        go.Bar(x=['Primera', 'Segunda', 'Tercera'], 
               y=[class_survival[1], class_survival[2], class_survival[3]],
               name='Por Clase',
               marker_color=[COLORS['success'], COLORS['warning'], COLORS['danger']]),
        row=1, col=2
    )
    
    # Gráfico 3: Supervivencia por Puerto
    embark_survival = df.groupby('Embarked')['Survived'].mean()
    embark_labels = {'C': 'Cherbourg', 'Q': 'Queenstown', 'S': 'Southampton'}
    fig_dashboard.add_trace(
        go.Bar(x=[embark_labels.get(port, port) for port in embark_survival.index], 
               y=embark_survival.values,
               name='Por Puerto',
               marker_color=[COLORS['info'], COLORS['warning'], COLORS['primary']]),
        row=2, col=1
    )
    
    # Gráfico 4: Distribución de edad de supervivientes vs no supervivientes
    survivors_age = df[df['Survived'] == 1]['Age'].dropna()
    non_survivors_age = df[df['Survived'] == 0]['Age'].dropna()
    
    fig_dashboard.add_trace(
        go.Histogram(x=survivors_age, name='Supervivientes', 
                    marker_color=COLORS['success'], opacity=0.7, nbinsx=20),
        row=2, col=2
    )
    fig_dashboard.add_trace(
        go.Histogram(x=non_survivors_age, name='No Supervivientes', 
                    marker_color=COLORS['danger'], opacity=0.7, nbinsx=20),
        row=2, col=2
    )
    
    fig_dashboard.update_layout(
        height=700,
        showlegend=True,
        title_text="Panel de Resultados - Factores de Supervivencia",
        title_x=0.5
    )
    
    # Actualizar ejes Y para mostrar porcentajes
    fig_dashboard.update_yaxes(title_text="Tasa de Supervivencia", row=1, col=1)
    fig_dashboard.update_yaxes(title_text="Tasa de Supervivencia", row=1, col=2)
    fig_dashboard.update_yaxes(title_text="Tasa de Supervivencia", row=2, col=1)
    fig_dashboard.update_yaxes(title_text="Número de Pasajeros", row=2, col=2)
    
    st.plotly_chart(fig_dashboard, use_container_width=True)
    
    # === ANÁLISIS DETALLADO ===
    st.markdown("---")
    st.markdown("## 🔍 Análisis Detallado de Resultados")
    
    # 2. Mapa de Calor - Supervivencia por Clase y Sexo
    st.markdown("### Supervivencia por Clase y Sexo")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Crear matriz de supervivencia
        survival_matrix = df.groupby(['Pclass', 'Sex'])['Survived'].mean().unstack()
        
        fig_heatmap = px.imshow(
            survival_matrix.values,
            x=['Femenino', 'Masculino'],
            y=['Primera Clase', 'Segunda Clase', 'Tercera Clase'],
            color_continuous_scale='RdYlGn',
            aspect='auto',
            title='Tasa de Supervivencia por Clase y Sexo'
        )
        
        # Añadir texto con los valores
        for i in range(len(survival_matrix.index)):
            for j in range(len(survival_matrix.columns)):
                fig_heatmap.add_annotation(
                    x=j, y=i,
                    text=f"{survival_matrix.iloc[i, j]:.1%}",
                    showarrow=False,
                    font=dict(color="white" if survival_matrix.iloc[i, j] < 0.5 else "black", size=14)
                )
        
        fig_heatmap.update_layout(height=400)
        st.plotly_chart(fig_heatmap, use_container_width=True)
    
    with col2:
        st.markdown("#### 💡 Insights del heatmap:")
        st.markdown("""
        - **Mujeres de 1ª clase**: Tasa más alta (96.8%)
        - **Hombres de 3ª clase**: Tasa más baja (13.5%)
        - **Diferencia máxima**: 83.3 puntos porcentuales
        - **Patrón claro**: Clase y sexo interactúan fuertemente
        """)
        
        # Tabla de valores exactos
        detailed_table = []
        for pclass in [1, 2, 3]:
            for sex in ['female', 'male']:
                subset = df[(df['Pclass'] == pclass) & (df['Sex'] == sex)]
                if len(subset) > 0:
                    rate = subset['Survived'].mean()
                    detailed_table.append({
                        'Grupo': f"{'Mujer' if sex == 'female' else 'Hombre'} {['1ª', '2ª', '3ª'][pclass-1]}",
                        'Tasa': f"{rate:.1%}",
                        'N': len(subset)
                    })
        
        st.dataframe(pd.DataFrame(detailed_table), hide_index=True, use_container_width=True)
    
    # 3. Análisis de Distribución de Edades
    st.markdown("### 👥 Análisis de Supervivencia por Edad")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Gráfico de violín por edad y supervivencia
        fig_violin = px.violin(
            df, 
            x='Survived', 
            y='Age', 
            box=True,
            title='Distribución de Edades por Estado de Supervivencia',
            labels={'Survived': 'Supervivió', 'Age': 'Edad'},
            color='Survived',
            color_discrete_map={0: COLORS['danger'], 1: COLORS['success']}
        )
        fig_violin.update_layout(height=400)
        fig_violin.update_xaxes(tickvals=[0, 1], ticktext=['No', 'Sí'])
        st.plotly_chart(fig_violin, use_container_width=True)
    
    with col2:
        # Estadísticas de edad por supervivencia
        age_stats = df.groupby('Survived')['Age'].agg(['mean', 'median', 'std']).round(2)
        age_stats_formatted = pd.DataFrame({
            'Estadística': ['Edad Promedio', 'Edad Mediana', 'Desviación Estándar'],
            'No Supervivientes': [f"{age_stats.loc[0, 'mean']:.1f}", 
                                 f"{age_stats.loc[0, 'median']:.1f}", 
                                 f"{age_stats.loc[0, 'std']:.1f}"],
            'Supervivientes': [f"{age_stats.loc[1, 'mean']:.1f}", 
                              f"{age_stats.loc[1, 'median']:.1f}", 
                              f"{age_stats.loc[1, 'std']:.1f}"]
        })
        
        st.dataframe(age_stats_formatted, hide_index=True, use_container_width=True)
        
        st.markdown("#### 📊 Observaciones sobre Edad:")
        st.markdown(f"""
        - **Supervivientes**: Promedio {age_stats.loc[1, 'mean']:.1f} años
        - **No supervivientes**: Promedio {age_stats.loc[0, 'mean']:.1f} años
        - **Diferencia**: {age_stats.loc[0, 'mean'] - age_stats.loc[1, 'mean']:.1f} años
        - Los supervivientes tienden a ser ligeramente más jóvenes
        """)
    
    
    # 4. Análisis de Tamaño Familiar
    if 'SibSp' in df.columns and 'Parch' in df.columns:
        st.markdown("### 👨‍👩‍👧‍👦 Supervivencia por Tamaño de Familia")
        
        df['FamilySize'] = df['SibSp'] + df['Parch'] + 1  # +1 para incluir al pasajero
        df['FamilyCategory'] = df['FamilySize'].apply(
            lambda x: 'Solo' if x == 1 
            else 'Pequeña (2-4)' if x <= 4 
            else 'Grande (5+)'
        )
        
        col1, col2 = st.columns(2)
        
        with col1:
            family_survival = df.groupby('FamilyCategory')['Survived'].agg(['mean', 'count'])
            
            fig_family = px.bar(
                x=family_survival.index,
                y=family_survival['mean'],
                title='Tasa de Supervivencia por Tamaño de Familia',
                labels={'x': 'Tamaño de Familia', 'y': 'Tasa de Supervivencia'},
                color=family_survival['mean'],
                color_continuous_scale='RdYlGn'
            )
            fig_family.update_layout(height=400, showlegend=False)
            st.plotly_chart(fig_family, use_container_width=True)
        
        with col2:
            family_table = pd.DataFrame({
                'Tamaño Familia': family_survival.index,
                'Tasa Supervivencia': [f"{rate:.1%}" for rate in family_survival['mean']],
                'Total Pasajeros': family_survival['count']
            })
            st.dataframe(family_table, hide_index=True, use_container_width=True)
            
            st.info("💡 **Observación**: Las familias de tamaño mediano (2-4 personas) tuvieron mejores tasas de supervivencia que los pasajeros solos o familias muy grandes.")
    
    # === HALLAZGOS PRINCIPALES ===
    st.markdown("---")
    st.markdown("## 🏆 Hallazgos Principales")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### ✅ Factores que Aumentaron la Supervivencia:")
        st.markdown(f"""
        1. **Ser mujer**: {female_survival:.1f}% vs {male_survival:.1f}% (hombres)
        2. **Viajar en primera clase**: {first_class_survival:.1f}% de supervivencia
        3. **Edad joven**: Los supervivientes eran ~{age_stats.loc[0, 'mean'] - age_stats.loc[1, 'mean']:.1f} años más jóvenes
        4. **Familia mediana**: Mejor que viajar solo o en grupos grandes
        5. **Puerto Cherbourg**: Ligeramente mejor tasa de supervivencia
        """)
    
    with col2:
        st.markdown("### ❌ Factores de Riesgo:")
        st.markdown(f"""
        1. **Ser hombre**: Solo {male_survival:.1f}% de supervivencia
        2. **Tercera clase**: Solo {third_class_survival:.1f}% de supervivencia
        3. **Viajar solo**: Menor apoyo familiar
        4. **Familias grandes**: Dificultad para evacuar juntos
        5. **Combinación crítica**: Hombre en 3ª clase = {df[(df['Sex'] == 'male') & (df['Pclass'] == 3)]['Survived'].mean():.1%}
        """)
    
    # === IMPACTO ESTADÍSTICO ===
    st.markdown("---")
    st.markdown("## 📈 Significancia Estadística")
    
    # Crear tabla resumen de todos los factores
    factors_summary = []
    
    # Por sexo
    for sex in ['female', 'male']:
        subset = df[df['Sex'] == sex]
        factors_summary.append({
            'Factor': f"Sexo: {'Femenino' if sex == 'female' else 'Masculino'}",
            'N': len(subset),
            'Supervivientes': subset['Survived'].sum(),
            'Tasa': f"{subset['Survived'].mean():.1%}",
            'Impacto': 'Alto' if subset['Survived'].mean() > 0.6 or subset['Survived'].mean() < 0.3 else 'Medio'
        })
    
    # Por clase
    for pclass in [1, 2, 3]:
        subset = df[df['Pclass'] == pclass]
        factors_summary.append({
            'Factor': f"Clase: {['Primera', 'Segunda', 'Tercera'][pclass-1]}",
            'N': len(subset),
            'Supervivientes': subset['Survived'].sum(),
            'Tasa': f"{subset['Survived'].mean():.1%}",
            'Impacto': 'Alto' if subset['Survived'].mean() > 0.6 or subset['Survived'].mean() < 0.3 else 'Medio'
        })
    
    summary_df = pd.DataFrame(factors_summary)
    st.dataframe(summary_df, hide_index=True, use_container_width=True)
    
    # === CONCLUSIÓN FINAL ===
    st.markdown("---")
    st.success("""
    ## 🎯 **Conclusión del Análisis de Resultados**
    
    Los datos del Titanic revelan un **patrón claro y consistente**: la supervivencia no fue aleatoria, sino que estuvo 
    **fuertemente determinada por factores socioeconómicos y demográficos**. 
    
    El protocolo marítimo "mujeres y niños primero" se aplicó efectivamente, pero **la clase social amplificó 
    significativamente estas diferencias**, creando una jerarquía de supervivencia que reflejaba las 
    desigualdades sociales de la época.
    
    **Resultado más impactante**: Una mujer de primera clase tenía ~97% de posibilidades de sobrevivir, 
    mientras que un hombre de tercera clase tenía solo ~14% de posibilidades.
    """)
