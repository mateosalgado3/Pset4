
import pandas as pd
import numpy as np

def build_conversion_cohort(visits, orders):
    """
    Crea cohortes de conversión basadas en el primer día de visita.
    """
    # Fecha de primera visita por usuario
    first_visit = visits.groupby('uid')['start_ts'].min().reset_index()
    first_visit.columns = ['uid', 'first_visit_date']

    # Fecha de primera compra por usuario
    first_order = orders.groupby('uid')['buy_ts'].min().reset_index()
    first_order.columns = ['uid', 'first_order_date']

    # Unir visitas y órdenes
    cohort = pd.merge(first_visit, first_order, on='uid', how='left')

    # Calcular días desde la primera visita hasta la primera compra
    cohort['days_to_conversion'] = (cohort['first_order_date'] - cohort['first_visit_date']).dt.days

    return cohort

def build_ltv_cohort(visits, orders):
    """
    Calcula el Lifetime Value (LTV) agrupado por cohorte de primer visita.
    """
    # Primera visita de cada usuario
    visits['first_visit_date'] = visits.groupby('uid')['start_ts'].transform('min')
    visits['cohort_month'] = visits['first_visit_date'].dt.to_period('M')

    # Unir compras con la cohorte
    orders = orders.copy()
    orders = orders.merge(visits[['uid', 'cohort_month']], on='uid', how='left')

    # Calcular ingresos por cohorte
    ltv = orders.groupby('cohort_month').agg({
        'uid': 'nunique',
        'revenue': 'sum'
    }).rename(columns={'uid': 'n_users', 'revenue': 'total_revenue'}).reset_index()

    # LTV promedio
    ltv['ltv'] = ltv['total_revenue'] / ltv['n_users']

    return ltv

def build_conversion_cohort(visits, orders):
    """
    Crea cohortes de conversión basadas en el primer día de visita.
    Añade categorización de Conversion 0d, 1d, etc.
    """
    # Fecha de primera visita por usuario
    first_visit = visits.groupby('uid')['start_ts'].min().reset_index()
    first_visit.columns = ['uid', 'first_visit_date']

    # Fecha de primera compra por usuario
    first_order = orders.groupby('uid')['buy_ts'].min().reset_index()
    first_order.columns = ['uid', 'first_order_date']

    # Unir visitas y órdenes
    cohort = pd.merge(first_visit, first_order, on='uid', how='left')

    # Calcular días desde la primera visita hasta la primera compra
    cohort['days_to_conversion'] = (cohort['first_order_date'] - cohort['first_visit_date']).dt.days

    # Categorización de conversiones
    cohort['conversion_category'] = cohort['days_to_conversion'].apply(
        lambda x: f"Conversion {x}d" if pd.notnull(x) else 'No Conversion'
    )

    return cohort


def calculate_cac(costs, conversion_cohort, visits):
    """
    Calcula el Customer Acquisition Cost (CAC) por fuente de tráfico.
    """
    # Contar nuevos clientes por fuente
    new_clients_by_source = conversion_cohort.dropna(subset=['days_to_conversion']).merge(
        visits[['uid', 'source_id']], on='uid', how='left'
    ).groupby('source_id').uid.nunique().reset_index().rename(columns={'uid': 'new_customers'})

    # Sumar costos por fuente
    total_costs_by_source = costs.groupby('source_id').costs.sum().reset_index()

    # Unir costos y nuevos clientes
    cac = pd.merge(total_costs_by_source, new_clients_by_source, on='source_id', how='left')

    # Calcular CAC
    cac['cac'] = cac['costs'] / cac['new_customers']

    return cac


def calculate_romi(costs, orders, visits):
    """
    Calcula el Return on Marketing Investment (ROMI) por fuente.
    """
    # Traer source_id al nivel de compras
    orders_sources = orders.merge(visits[['uid', 'source_id']], on='uid', how='left')

    # Ingresos por fuente
    revenue_by_source = orders_sources.groupby('source_id').revenue.sum().reset_index()

    # Costos por fuente
    costs_by_source = costs.groupby('source_id').costs.sum().reset_index()

    # Unir
    romi = pd.merge(revenue_by_source, costs_by_source, on='source_id', how='left')

    # Calcular ROMI
    romi['romi'] = (romi['revenue'] - romi['costs']) / romi['costs']

    return romi

