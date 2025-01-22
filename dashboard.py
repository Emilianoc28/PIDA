import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from streamlit_folium import folium_static

# Configuración inicial
st.set_page_config(page_title="Dashboard EDA", layout="wide")

# Carga de datos
@st.cache_data
def cargar_datos():
    ruta_archivo = "D:\\Soy Henry\\Labs\\Data Analystic\\Dataset\\Internet.xlsx"
    hojas = {
        "Penetracion_hogares": pd.read_excel(ruta_archivo, sheet_name="Penetracion-hogares"),
        "Accesos_tecnologia": pd.read_excel(ruta_archivo, sheet_name="Accesos_tecnologia_localidad"),
        "Totales_velocidad": pd.read_excel(ruta_archivo, sheet_name="Totales Accesos Por Tecnología"),
        "Ingresos": pd.read_excel(ruta_archivo, sheet_name="Ingresos "),
        "Velocidad_prov": pd.read_excel(ruta_archivo, sheet_name="Velocidad % por prov"),
        "Mapa_Conectividad": pd.read_excel("D:\\Soy Henry\\Labs\\Data Analystic\\Dataset\\mapa_conectividad.xlsx", sheet_name="Hoja3"),  # Nueva hoja de conectividad
    }
    return hojas

datos = cargar_datos()
# Cargar datos de la hoja 'Penetracion-hogares'
df_penetracion = datos["Penetracion_hogares"]  # Hoja 'Penetracion-hogares'

# Definir manualmente todas las provincias de Argentina
provincias = [
    "Buenos Aires", "CABA", "Catamarca", "Chaco", "Chubut", "Córdoba", "Corrientes",
    "Entre Ríos", "Formosa", "Jujuy", "La Pampa", "La Rioja", "Mendoza", "Misiones",
    "Neuquén", "Río Negro", "Salta", "San Juan", "San Luis", "Santa Cruz", "Santa Fe",
    "Santiago del Estero", "Tierra del Fuego", "Tucumán"
]

# Barra lateral
st.sidebar.title("Opciones del Dashboard")
seccion = st.sidebar.selectbox(
    "Selecciona la sección a explorar:",
    [
        "Penetración por Hogares",
        "Accesos por Tecnología",
        "Totales de Accesos por Velocidad",
        "Ingresos",
        "Velocidades por Provincia",
        "Mapa de Conectividad",
        "KPIs y Resumen",
    ]
)
# Filtrar datos según las provincias seleccionadas manualmente
df_filtrado = df_penetracion

# Si no hay provincias seleccionadas, usa todo el DataFrame
if df_filtrado.empty:
    st.warning("No hay datos disponibles para las provincias seleccionadas.")

# Funciones de visualización
def mostrar_penetracion():
    df = datos.get("Penetracion_hogares")
    if df is not None:
        st.subheader("Penetración de Internet por Hogares")
        años = st.sidebar.multiselect("Años", df["Año"].unique(), default=df["Año"].unique())
        provincias = st.sidebar.multiselect("Provincias", df["Provincia"].unique(), default=df["Provincia"].unique())
        df_filtrado = df[(df["Año"].isin(años)) & (df["Provincia"].isin(provincias))]
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(
            data=df_filtrado,
            x="Año",
            y="Accesos por cada 100 hogares",
            hue="Provincia",
            ax=ax
        )
        ax.set_title("Penetración de Internet por Año y Provincia")
        st.pyplot(fig)
    else:
        st.error("Datos no disponibles para esta sección.")

def mostrar_accesos_tecnologia():
    df = datos.get("Accesos_tecnologia")
    if df is not None:
        st.subheader("Accesos por Tecnología")
        st.dataframe(df.head())
    else:
        st.error("Datos no disponibles para esta sección.")

def mostrar_totales_velocidad():
    df = datos.get("Totales_velocidad")
    if df is not None:
        st.subheader("Totales de Accesos por Velocidad")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.lineplot(data=df, x="Año", y="Total", hue="Trimestre", marker="o", ax=ax)
        ax.set_title("Evolución de Accesos Totales por Velocidad")
        st.pyplot(fig)
    else:
        st.error("Datos no disponibles para esta sección.")

# Función para mostrar los ingresos por tecnología
def mostrar_ingresos():
    df = datos["Ingresos"]
    st.subheader("Ingresos por Tecnología")

    # Filtro interactivo para seleccionar años
    años = st.sidebar.multiselect(
        "Selecciona el/los años:",
        options=df["Año"].unique(),
        default=df["Año"].unique(),
        key="multiselect_años"  # Asignar un identificador único para este widget
    )

    # Filtrar los datos según los años seleccionados
    df_filtrado = df[df["Año"].isin(años)]

    # Verificar si hay datos disponibles después del filtrado
    if not df_filtrado.empty:
        # Crear gráfico de barras para los ingresos
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(x="Año", y="Ingresos (miles de pesos)", data=df_filtrado, ax=ax, palette="viridis")

        # Ajustar título y etiquetas
        ax.set_title("Ingresos por Año", fontsize=16)
        ax.set_xlabel("Año", fontsize=12)
        ax.set_ylabel("Ingresos (miles de pesos)", fontsize=12)

        # Mostrar el gráfico en Streamlit
        st.pyplot(fig)
    else:
        st.warning("No hay datos disponibles para los años seleccionados.")

def mostrar_mapa_conectividad():
    df_conectividad = datos["Mapa_Conectividad"]
    st.subheader("Mapa de Conectividad por Localidad")

    if df_conectividad is not None:
        # Filtramos el DataFrame según las provincias seleccionadas
        provincias_seleccionadas = st.sidebar.multiselect("Selecciona las provincias", df_conectividad["Provincia"].unique())
        
        if provincias_seleccionadas:
            df_conectividad_filtrado = df_conectividad[df_conectividad["Provincia"].isin(provincias_seleccionadas)]
        else:
            df_conectividad_filtrado = df_conectividad

        if df_conectividad_filtrado.empty:
            st.warning("No hay datos disponibles para las provincias seleccionadas.")
        else:
            # Creación del mapa
            mapa = folium.Map(location=[-38.4161, -63.6167], zoom_start=5)

            # Definición de colores para cada provincia
            colores = ["blue", "green", "red", "purple", "orange", "pink", "darkblue", "gray", "lightblue"]
            color_provincias = {provincia: colores[i % len(colores)] for i, provincia in enumerate(provincias_seleccionadas)}

            # Añadir marcadores al mapa
            for _, row in df_conectividad_filtrado.iterrows():
                color = color_provincias.get(row["Provincia"], "blue")  # Color por provincia
                tecnologias = [tec for tec in ["ADSL", "Cablemódem", "Fibra óptica", "Satelital", "Wireless", "Telefonía Fija", "3G", "4G"]
                               if row[tec] == "SI"]
                folium.Marker(
                    location=[row["Latitud"], row["Longitud"]],
                    popup=f"{row['Localidad']} ({row['Provincia']})<br>Tecnologías: {', '.join(tecnologias)}",
                    tooltip=row["Localidad"],
                    icon=folium.Icon(color=color)
                ).add_to(mapa)

            # Mostrar el mapa
            folium_static(mapa)
    else:
        st.error("Datos de conectividad no disponibles.")


    # Filtrar datos en base a las selecciones
    df_filtrado = df[df["Año"].isin(años)]

    if df_filtrado.empty:
        st.warning("No hay datos para los años seleccionados. Por favor, elige otros filtros.")
    else:
        # Mostrar los datos filtrados
        st.write("Datos filtrados:")
        st.dataframe(df_filtrado)

        # Tabla dinámica: Suma de ingresos por año
        st.write("Ingresos Totales por Año:")
        tabla_ingresos = (
            df_filtrado.groupby("Año")["Ingresos (miles de pesos)"]
            .sum()
            .reset_index()
            .rename(columns={"Ingresos (miles de pesos)": "Ingresos Totales (miles de pesos)"})
        )
        st.dataframe(tabla_ingresos)

        # Gráfico de barras
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(data=tabla_ingresos, x="Año", y="Ingresos Totales (miles de pesos)", ax=ax, palette="Blues_d")
        ax.set_title("Ingresos Totales por Año")
        ax.set_xlabel("Año")
        ax.set_ylabel("Ingresos (miles de pesos)")
        st.pyplot(fig)

# Función para mostrar KPIs
# Función para mostrar KPIs y resumen
# Función para mostrar KPIs



# KPIs y Resumen sin usar la columna "Provincia" en el filtrado
def mostrar_kpi_ingresos(df_filtrado):
    # KPI 1: Total de Ingresos
    total_ingresos = df_filtrado["Ingresos (miles de pesos)"].sum()
    st.metric(label="Total de Ingresos (miles de pesos)", value=f"{total_ingresos:,.0f}")

    # KPI 2: Promedio de Ingresos por Año
    promedio_ingresos = df_filtrado["Ingresos (miles de pesos)"].mean()
    st.metric(label="Promedio de Ingresos por Año (miles de pesos)", value=f"{promedio_ingresos:,.0f}")

    # KPI 3: Número de registros de datos
    num_registros = df_filtrado.shape[0]
    st.metric(label="Número de Registros Filtrados", value=f"{num_registros}")

    # Resumen de los datos filtrados
    st.write("Resumen de los Datos Filtrados:")
    resumen = {
        "Año mínimo": df_filtrado["Año"].min(),
        "Año máximo": df_filtrado["Año"].max(),
        "Número total de registros": num_registros,
    }
    st.write(resumen)

def mostrar_kpi_penetracion(df_penetracion):
    provincias = [
        "Buenos Aires", "Catamarca", "Chaco", "Chubut", "CABA", "Córdoba", "Corrientes", "Entre Ríos", 
        "Formosa", "Jujuy", "La Pampa", "La Rioja", "Mendoza", "Misiones", "Neuquén", "Río Negro", 
        "Salta", "San Juan", "San Luis", "Santa Cruz", "Santa Fe", "Santiago del Estero", "Tierra del Fuego", 
        "Tucumán"
    ]  # Provincias definidas manualmente

    if df_penetracion is not None and not df_penetracion.empty:

        # KPI: Aumento del 2% en el acceso a Internet por cada 100 hogares por provincia
        st.subheader("KPI: Aumento del 2% en el acceso a Internet por cada 100 hogares por provincia")
        
        # Agrupamos por provincia para obtener los valores de acceso actual y nuevo acceso por cada 100 hogares
        df_kpi = df_penetracion.groupby(["Provincia"]).agg(
            acceso_actual=("Accesos por cada 100 hogares", "last"),  # Acceso actual en el último trimestre
            nuevo_acceso=("Accesos por cada 100 hogares", "first")  # Nuevo acceso en el siguiente trimestre
        ).reset_index()

        # Calcular el KPI (porcentaje de aumento)
        df_kpi["KPI (%)"] = ((df_kpi["nuevo_acceso"] - df_kpi["acceso_actual"]) / df_kpi["acceso_actual"]) * 100

        # Mostrar los resultados en el dashboard
        st.write(df_kpi)
        
        # Graficar el KPI si es necesario
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(x="Provincia", y="KPI (%)", data=df_kpi, ax=ax)
        ax.set_title("Aumento del Acceso a Internet por cada 100 Hogares")
        ax.set_ylabel("KPI (%)")
        ax.set_xlabel("Provincia")
        plt.xticks(rotation=90)# Rotar las etiquetas de las provincias en el eje X para que se vean verticalmente
        st.pyplot(fig)

    else:
        st.warning("No hay datos disponibles para los KPIs de penetración.")

def mostrar_velocidades():
    df = datos["Velocidad_prov"]
    st.subheader("Velocidades por Provincia")

    # Filtros interactivos
    años = st.sidebar.multiselect(
        "Selecciona el/los años:",
        options=df["Año"].unique(),
        default=df["Año"].unique()
    )
    provincias = st.sidebar.multiselect(
        "Selecciona la/las provincias:",
        options=df["Provincia"].unique(),
        default=df["Provincia"].unique()
    )

    # Filtrar datos en base a las selecciones
    df_filtrado = df[(df["Año"].isin(años)) & (df["Provincia"].isin(provincias))]

    if df_filtrado.empty:
        st.warning("No hay datos para las selecciones realizadas. Por favor, elige otros filtros.")
    else:
        # Crear la tabla pivotada
        df_agrupado = (
            df_filtrado.groupby(["Provincia", "Año"], as_index=False)["Mbps (Media de bajada)"]
            .mean()
        )
        df_pivot = df_agrupado.pivot(index="Provincia", columns="Año", values="Mbps (Media de bajada)")

        # Mostrar los datos filtrados
        st.write("Datos filtrados:")
        st.dataframe(df_filtrado)

        # Gráfico de calor
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(df_pivot, cmap="coolwarm", annot=True, fmt=".2f", ax=ax)
        ax.set_title("Distribución de Velocidades por Provincia y Año")
        st.pyplot(fig)

# Función principal para mostrar ambos KPIs
def mostrar_kpi_y_resumen():
    # Mostrar KPIs de Ingresos
    df_filtrado = datos["Ingresos"]  # El dataframe para KPIs debería estar relacionado con los ingresos
    mostrar_kpi_ingresos(df_filtrado)

    # Mostrar KPIs de Penetración
    df_penetracion=datos["Penetracion_hogares"]
    mostrar_kpi_penetracion(df_penetracion)

# Renderizar la sección seleccionada
if seccion == "Penetración por Hogares":
    mostrar_penetracion()
elif seccion == "Accesos por Tecnología":
    mostrar_accesos_tecnologia()
elif seccion == "Totales de Accesos por Velocidad":
    mostrar_totales_velocidad()
elif seccion == "Ingresos":
    mostrar_ingresos()
elif seccion == "Velocidades por Provincia":
    mostrar_velocidades()
elif seccion == "Mapa de Conectividad":
    mostrar_mapa_conectividad()
elif seccion == "KPIs y Resumen":
    mostrar_kpi_y_resumen()


# Footer
st.sidebar.info("Dashboard creado para explorar el EDA de telecomunicaciones.")
