# Análisis y Predicción de Acceso a Internet en Argentina

Este proyecto se centra en el análisis de datos de acceso a Internet en Argentina, con el objetivo de proporcionar información valiosa sobre el acceso a Internet por cada 100 hogares, la penetración de servicios de telecomunicaciones y otros KPIs relevantes. A través del uso de metodologías de análisis exploratorio de datos (EDA), creación de KPIs e informes visuales, este trabajo permite extraer conclusiones sobre las tendencias actuales del acceso a Internet en las provincias de Argentina.

## Descripción del Proyecto

En este proyecto, se aborda un conjunto de datos que contiene información sobre la penetración de Internet en diferentes provincias de Argentina, recopilada por ENACOM. Se analizan métricas clave relacionadas con el acceso a Internet, como la penetración por cada 100 hogares, los ingresos de los proveedores de servicios de Internet, y la evolución de las conexiones de acuerdo con el tipo de tecnología disponible en cada provincia.

El proyecto tiene como objetivo identificar patrones significativos en el acceso a Internet, proponer KPIs (Indicadores Clave de Desempeño) y generar visualizaciones que ayuden a comprender cómo mejorar el acceso al servicio en el futuro.

## Tecnologías y Herramientas Utilizadas

Este proyecto hace uso de una serie de herramientas y tecnologías de vanguardia en análisis de datos y desarrollo de aplicaciones web interactivas:

- **Python**: Lenguaje de programación principal para análisis de datos y visualización.
- **Pandas**: Librería principal utilizada para la manipulación de datos y análisis estadístico.
- **Matplotlib / Seaborn**: Librerías de visualización para gráficos y análisis exploratorio de datos (EDA).
- **Streamlit**: Framework para construir aplicaciones web interactivas de manera sencilla.
- **Folium**: Para generar mapas interactivos y análisis geoespaciales.
- **Jupyter Notebook**: Herramienta de desarrollo interactivo utilizada para realizar análisis previos y visualizaciones.

## Metodología Aplicada

### 1. Análisis Exploratorio de Datos (EDA)

El proceso de EDA comienza con la carga de los datos desde múltiples hojas de Excel que contienen información relevante sobre el acceso a Internet en Argentina, tales como:

- **Penetración por hogares**: Muestra el acceso por cada 100 hogares.
- **Accesos por tecnología**: Información sobre la distribución de acceso a Internet por tecnologías como ADSL, fibra óptica, entre otras.
- **Ingresos**: Datos sobre los ingresos generados por el acceso a Internet en diversas provincias.

El análisis de los datos se realizó con los siguientes pasos:

- **Revisión de los datos**: Inspección inicial de las estructuras y valores presentes en los datasets.
- **Limpieza de los datos**: Se eliminaron filas y columnas irrelevantes, se gestionaron los valores faltantes y se corrigieron inconsistencias.
- **Transformación**: Los datos fueron transformados para facilitar su análisis, generando nuevas variables derivadas y calculando métricas de interés.

### 2. Creación de KPIs

Los KPIs fundamentales fueron calculados para medir el éxito de las estrategias de acceso a Internet en Argentina. Entre ellos, se incluyó un KPI clave que establece la meta de aumentar el acceso a Internet en un 2% por cada 100 hogares, por provincia. La fórmula utilizada fue:
KPI = ((Nuevo_acceso - Acceso_actual) / Acceso_actual) * 100
Este KPI permite evaluar el progreso hacia la mejora del acceso al servicio de Internet en cada provincia.

### 3. Visualización de Datos y Resultados

Se crearon múltiples visualizaciones interactivas usando Streamlit y Matplotlib/Seaborn para representar tanto los datos como los KPIs calculados. Algunas de las visualizaciones clave incluyen:

- Gráfico de barras para mostrar el KPI de aumento en el acceso a Internet por provincia.
- Mapas interactivos para representar geográficamente la penetración de Internet en las provincias argentinas.

### 4. Desarrollo del Dashboard Interactivo

Un dashboard interactivo fue creado utilizando Streamlit, lo que permite a los usuarios explorar los KPIs, filtrar los datos por provincia, año o trimestre, y visualizar las métricas clave de acceso a Internet en tiempo real.

## Conclusiones y Resultados

### KPIs Relevantes

Durante el análisis de los datos, se identificaron varios KPIs clave que ofrecen un panorama detallado del acceso a Internet en las provincias de Argentina. Entre estos se incluyen:

- **KPI de acceso por cada 100 hogares**: Calculado para cada provincia, permite visualizar el acceso al servicio de Internet y su evolución trimestre a trimestre.
- **KPI de incremento en el acceso**: Permite medir el objetivo de aumentar en un 2% el acceso al servicio de Internet para el siguiente trimestre.
- **Ingreso promedio por provincia**: Calcula el ingreso generado por los proveedores de Internet por cada provincia, dando una idea del impacto económico del acceso a Internet.

### Hallazgos

- Se observó que algunas provincias tienen un mayor crecimiento en la penetración de Internet, mientras que otras permanecen estancadas. Esto podría indicar la necesidad de políticas públicas específicas para mejorar la infraestructura en zonas menos desarrolladas.
- Los ingresos generados por los proveedores de Internet están correlacionados con la cobertura geográfica de los servicios, lo que sugiere que mejorar la cobertura también podría aumentar los ingresos.

### Siguientes Pasos

- **Recomendaciones**: Las provincias con menor crecimiento en la penetración de Internet podrían beneficiarse de subsidios gubernamentales o incentivos para mejorar la infraestructura de telecomunicaciones.
- **Proyectos de expansión**: Utilizar los resultados de los KPIs para diseñar proyectos de expansión del acceso a Internet en áreas rurales y remotas.

## Cómo Ejecutar el Proyecto

Para ejecutar este proyecto en tu máquina local, sigue los siguientes pasos:

### Clonar el repositorio:

```bash
git clone https://github.com/tu_usuario/tu_proyecto.git

cd tu_proyecto

pip install -r requirements.txt

streamlit run dashboard.py