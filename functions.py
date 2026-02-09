import pandas as pd
import requests
import re
import time
import functions

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


def get_api(indicador):
    url = f"https://ghoapi.azureedge.net/api/{indicador}"
    respuesta = re.get(url)
    datos_json = respuesta.json()
    
    # 3. Convertir la lista que hay en la llave 'value' a un DataFrame
    df = pd.DataFrame(datos_json['value'])
    return df

def iso8601_to_seconds(duration):
    """Convierte formatos tipo PT10M30S a segundos totales."""
    patron = re.compile(r'PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?')
    match = patron.match(duration)
    if not match: return 0
    horas, minutos, segundos = match.groups(default=0)
    return int(horas) * 3600 + int(minutos) * 60 + int(segundos)