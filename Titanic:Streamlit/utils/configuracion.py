PAGE_CONFIG = {
    "page_title": "Titanic",  # Título en la pestaña del navegador
    "page_icon": "🚢",  # Emoji que aparece en la pestaña del navegador
    "layout": "wide",  # Layout ancho (usa todo el ancho de la pantalla) vs "centered"
    "initial_sidebar_state": "expanded"  # Sidebar visible por defecto ("collapsed" = oculto)
}


# PALETA DE COLORES
# =====================================
# Colores consistentes en toda la aplicación para mejor UX
# Códigos hexadecimales de colores (#RRGGBB)
COLORS = {
    # Colores generales para elementos de UI
    'primary': '#1f77b4',    # Azul principal (para gráficos y elementos destacados)
    'success': '#2ecc71',    # Verde (para indicadores positivos/éxito)
    'danger': '#e74c3c',     # Rojo (para alertas/errores)
    'warning': '#f39c12',    # Naranja (para advertencias)
    'info': '#3498db',       # Azul claro (para información)
    
    # Colores específicos por región (consistentes en todas las visualizaciones)
    'na': '#3498db',         # Norteamérica - Azul
    'eu': '#2ecc71',         # Europa - Verde
    'jp': '#e74c3c',         # Japón - Rojo
    'other': '#f39c12'       # Otros - Naranja
}


# =====================================
# MAPEO DE NOMBRES DE COLUMNAS
# =====================================
# Traduce nombres técnicos de columnas a nombres amigables para el usuario
# Se usa en tablas y visualizaciones para mejor comprensión


COLUMN_DISPLAY_NAMES = {
    'PassengerId': 'Numero de pasajero',     # Posición en el ranking                                        # Nombre del juego
    'Survived': 'Sobrevivió',               # Consola/plataforma
    'Pclass': 'Clase',            # Pasajeros en clase económica, ejecutiva o primera
    'Name': 'Nombre',                        # nombre del pasajero
    'Sex': 'Sexo',                      # Sexo del pasajero
    'Age': 'Edad',               # Edad del pasajero
    'SibSp': 'Hermanos/esposas a bordo',       # Hermanos/esposas a bordo
    'Parch': 'Padres/hijos a bordo',          # Padres/hijos a bordo
    'Ticket': 'Número de ticket',           # Número de ticket
    'Fare': 'Tarifa',                     # Tarifa del ticket
    'Deck': 'Cabina',                  # Cabina
    'Embarked': 'Embarque',           # Puerto de embarque (C = Cherbourg, Q = Queenstown, S = Southampton)
    'Embark_Town': 'Ciudad de embarque',  # Ciudad de embarque (Cherbourg, Queenstown, Southampton)
    'TITLE': 'Título'  # Título extraído del nombre (Sr., Sra., etc.)

}
