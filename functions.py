import pandas as pd
import requests
import re
import time
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def explorar_df(df):
    print(df.info())

    print('Primeras filas')
    print(df.head())

    print('Describe()')
    print(df.describe(include='all').T)

    print('Nulos')
    nulos = df.isnull().sum()
    print(nulos[nulos > 0] if nulos.any() else 'Notnnull')

    print('Duplicados')
    print(df.duplicated().sum())
    
    print('Tamaño')
    print(f"Filas: {df.shape[0]} | Columnas: {df.shape[1]}")

def limpiar_dataset(df):
    df_clean = df.copy()
    df_clean.columns = (df_clean.columns
                        .str.strip()
                        .str.lower()
                        .str.replace(' ', '_')
                        .str.replace('.', '', regex=False))
    df_clean.duplicated().sum()
    df_clean = df_clean.drop_duplicates()
    df_clean = df_clean.dropna(how='all') 
    return df_clean

def categorico(df,col):
    """Realiza un análisis descriptivo de una columna categórica."""
    print(df[col].value_counts())
    print(df[col].unique())
    print(df[col].nunique())
    

def numerico(df,col):
    """Realiza un análisis descriptivo de una columna numérica."""
    print(df[col].describe())
    print(df[col].isnull().sum())
    print(df[col].nunique())
    

def filtrar_fila(df,col,lista):
    return df[df[col].isin(lista)]

def completar_nulos(df,col,valor):
    df[col] = df[col].fillna(valor)
    return df

def estadisticos(df):
    print(df.describe())
    print(df.select_dtypes(include=["number"]).describe())
    

def ver_nulos(df):
    df_con_nulos = df[df.isnull().any(axis=1)]
    display(df_con_nulos)


def ver_duplicados(df):
    df_duplicados = df[df.duplicated()]
    display(df_duplicados)
    return df_duplicados

def rango_edad(df,col):
    """Crea rangos de edad a partir de una columna numérica."""
    df=df.copy()
    bins = [0, 18, 35, 50, 65, 120]
    labels = ['Niños(0-18)', 'Jóvenes(19-35)', 'Adultos(36-50)', 'Adultos maduros(51-65)', 'Adultos mayores(66+)']
    
    df['grupo_edad'] = pd.cut(df[col], bins=bins, labels=labels, include_lowest=True)
    
    return df


def separa_fecha_hora (df,col):
    df[col] = pd.to_datetime(df[col].str.extract(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})')[0])
    df['fecha'] = df[col].dt.date
    df['hora'] = df[col].dt.time
    return df

def agrupar_hora(df,col):
    """Crea grupos a partir de las horas."""
    bins = [0, 6, 12, 18, 24]
    labels = ['Noche(0-6)', 'Mañana(6-12)', 'Tarde(12-18)', 'Noche(18-24)']
    
    horas_extraidas = pd.to_datetime(df[col], format='%H:%M:%S', errors='coerce').dt.hour
    
    df['fecha_y_hora'] = pd.cut(horas_extraidas, bins=bins, labels=labels, include_lowest=True)
    
    return df


def iso8601_to_seconds(duration):
    """Convierte formatos tipo PT10M30S a segundos totales."""
    patron = re.compile(r'PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?')
    match = patron.match(duration)
    if not match: return 0
    horas, minutos, segundos = match.groups(default=0)
    return int(horas) * 3600 + int(minutos) * 60 + int(segundos)