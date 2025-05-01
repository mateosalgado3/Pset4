
# Showz Marketing Optimization - Análisis y Recomendaciones

## Descripción del Proyecto

Este proyecto tiene como objetivo **optimizar los gastos de marketing** de Showz, una plataforma de venta de entradas para eventos, utilizando análisis de datos para identificar las fuentes de marketing más efectivas, calcular el **Customer Acquisition Cost (CAC)**, el **Lifetime Value (LTV)** de los usuarios, y la rentabilidad de las inversiones a través del **Return on Marketing Investment (ROMI)**.

El análisis se centra en tres áreas clave:
1. **Visitas**: Se analiza el comportamiento de los usuarios en el sitio web.
2. **Ventas**: Se estudian las conversiones, el ticket promedio y el LTV por cohorte.
3. **Marketing**: Se examinan los costos de marketing, el CAC y el ROMI para cada fuente.

## Instrucciones de Ejecución

### 1. Clonación del Repositorio

Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/tu_usuario/showz_marketing_optimization.git
cd showz_marketing_optimization
2. Configuración del Entorno
Asegúrate de tener Python 3.7+ instalado en tu sistema. Puedes crear un entorno virtual para evitar conflictos con otras dependencias:

bash
Copiar
python3 -m venv env
source env/bin/activate  
3. Instalación de Dependencias
Instala las dependencias necesarias desde el archivo requirements.txt:

bash
Copiar
pip install -r requirements.txt
Las librerías principales utilizadas son:

pandas (análisis de datos)

numpy (operaciones numéricas)

matplotlib (visualización de datos)

seaborn (visualización avanzada)

4. Preparación de los Datos
Los datos originales deben ser colocados en la carpeta data/raw/ en formato CSV:

visits_log_us.csv: Registro de visitas al sitio web.

orders_log_us.csv: Información sobre las compras realizadas.

costs_us.csv: Detalle de los gastos en marketing.

Para limpiar y preparar los datos, ejecuta el siguiente comando para correr el script de preparación:

bash
Copiar
python src/data_prep.py
Este script:

Carga los datos.

Limpia los datos (elimina duplicados, valores nulos y convierte las columnas de fecha a datetime).

Guarda los datos limpios en la carpeta data/interim/.

5. Análisis en el Jupyter Notebook
Abre el notebook principal para realizar todo el análisis y visualizar los resultados:

bash
Copiar
jupyter notebook notebooks/PSet4_Showz_Marketing.ipynb
El notebook está dividido en tres secciones clave:

5.1 Análisis de Visitas
DAU, WAU, MAU: Calculamos usuarios activos diarios, semanales y mensuales.

Sesiones: Calculamos cuántas sesiones ocurren por día y la duración de las mismas.

Frecuencia de Regreso: Medimos la recurrencia de los usuarios en el sitio.

5.2 Análisis de Ventas
Conversiones: Calculamos el tiempo hasta la conversión (0d, 1d, 2d, etc.) y comparamos cohortes.

Ticket Promedio: Calculamos el tamaño promedio de compra.

Lifetime Value (LTV): Calculamos el LTV por cohorte de primer visita.

5.3 Análisis de Marketing
Gastos de Marketing: Visualizamos los gastos totales por fuente.

CAC: Calculamos el Costo de Adquisición de Clientes por cada fuente de marketing.

ROMI: Calculamos el Retorno sobre la Inversión en Marketing por fuente y temporal.

6. Resultados y Conclusiones
Al final del notebook, encontrarás las conclusiones clave de cada análisis:

Fuentes/Plataformas ganadoras: Identificamos qué fuentes de marketing son más efectivas.

Presupuesto óptimo: Proponemos cómo distribuir la inversión en marketing.

Supuestos y limitaciones: Discutimos los supuestos detrás del análisis y las limitaciones del mismo.

7. Guardado de Resultados
Las cohortes y resultados procesados pueden ser guardados en la carpeta data/processed/:

python
Copiar
# Guardar resultados de cohortes de conversiones y LTV
conversion_cohort.to_csv('../data/processed/conversion_cohort.csv', index=False)
ltv_cohort.to_csv('../data/processed/ltv_cohort.csv', index=False)
Esto es útil para mantener los datos organizados y listos para análisis posteriores o modelado.

Estructura del Proyecto
La estructura del proyecto es la siguiente:

bash
Copiar
showz_marketing_optimization/
│
├── data/
│   ├── raw/            # Archivos CSV originales
│   ├── interim/        # Archivos CSV limpios
│   ├── processed/      # Archivos CSV procesados
│
├── notebooks/          # Notebooks de análisis
│   └── PSet4_Showz_Marketing.ipynb  # Análisis completo de marketing
│
├── src/                # Scripts fuente
│   ├── data_prep.py    # Preparación y limpieza de datos
│   ├── metrics.py      # Funciones de cálculo de métricas (CAC, ROMI, LTV)
│   └── viz.py          # Funciones para visualización (opcional)
│
├── reports/            # Resultados gráficos y reportes
│   └── figures/        # Gráficos generados
│
├── requirements.txt    # Librerías necesarias
├── README.md           # Este archivo
└── .gitignore          # Archivos a ignorar en el repositorio
8. Consideraciones Finales
Este análisis proporciona una base sólida para optimizar la inversión en marketing de Showz, identificando las plataformas más rentables y proponiendo un presupuesto óptimo basado en LTV, CAC y ROMI. Las recomendaciones de inversión se basan en un enfoque científico y datos concretos.
