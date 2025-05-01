# src/data_prep.py

import pandas as pd
import os

# Definimos rutas relativas
RAW_DATA_PATH = 'data/raw/'
INTERIM_DATA_PATH = 'data/interim/'

def load_data():
    """
    Carga los archivos CSV originales desde data/raw/.
    """
    visits = pd.read_csv(os.path.join(RAW_DATA_PATH, 'visits_log_us.csv'))
    orders = pd.read_csv(os.path.join(RAW_DATA_PATH, 'orders_log_us.csv'))
    costs = pd.read_csv(os.path.join(RAW_DATA_PATH, 'costs_us.csv'))
    return visits, orders, costs

def clean_visits(visits):
    """
    Limpia y transforma el dataset de visitas.
    - Ajusta tipos de datos.
    - Convierte columnas a snake_case.
    - Elimina duplicados.
    """
    visits.columns = visits.columns.str.lower().str.strip().str.replace(' ', '_')
    
    visits['start_ts'] = pd.to_datetime(visits['start_ts'])
    visits['end_ts'] = pd.to_datetime(visits['end_ts'])
    visits['uid'] = visits['uid'].astype(str)
    visits['source_id'] = visits['source_id'].astype(int)

    visits = visits.drop_duplicates()
    visits = visits.dropna()

    return visits

def clean_orders(orders):
    """
    Limpia y transforma el dataset de órdenes.
    - Ajusta tipos de datos.
    - Convierte columnas a snake_case.
    - Elimina duplicados.
    """
    orders.columns = orders.columns.str.lower().str.strip().str.replace(' ', '_')
    
    orders['buy_ts'] = pd.to_datetime(orders['buy_ts'])
    orders['uid'] = orders['uid'].astype(str)
    orders['revenue'] = orders['revenue'].astype(float)

    orders = orders.drop_duplicates()
    orders = orders.dropna()

    return orders

def clean_costs(costs):
    """
    Limpia y transforma el dataset de costos de marketing.
    - Ajusta tipos de datos.
    - Convierte columnas a snake_case.
    - Elimina duplicados.
    """
    costs.columns = costs.columns.str.lower().str.strip().str.replace(' ', '_')
    
    costs['dt'] = pd.to_datetime(costs['dt'])
    costs['source_id'] = costs['source_id'].astype(int)
    costs['costs'] = costs['costs'].astype(float)

    costs = costs.drop_duplicates()
    costs = costs.dropna()

    return costs

def save_clean_data(visits, orders, costs):
    """
    Guarda los datasets limpios en data/interim/.
    """
    visits.to_csv(os.path.join(INTERIM_DATA_PATH, 'visits_clean.csv'), index=False)
    orders.to_csv(os.path.join(INTERIM_DATA_PATH, 'orders_clean.csv'), index=False)
    costs.to_csv(os.path.join(INTERIM_DATA_PATH, 'costs_clean.csv'), index=False)

def prepare_data():
    """
    Función principal para cargar, limpiar y guardar datasets.
    """
    visits, orders, costs = load_data()
    visits_clean = clean_visits(visits)
    orders_clean = clean_orders(orders)
    costs_clean = clean_costs(costs)
    save_clean_data(visits_clean, orders_clean, costs_clean)

    print("Datasets cargados, limpiados y guardados en 'data/interim/'.")

if __name__ == "__main__":
    prepare_data()
