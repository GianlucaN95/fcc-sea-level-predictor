import pandas as pd
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # 1. Carica il database dei dati storici del livello del mare
    df = pd.read_csv('epa-sea-level.csv')

    # 2. Prima linea di regressione (Tutti i dati storici dal 1880 al 2050)
    # Calcola la pendenza (slope) e l'intercetta (intercept) per fare la previsione
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Crea la sequenza di anni dal 1880 fino al 2050
    years_all = np.arange(df['Year'].min(), 2051)
    # Calcola i valori previsti per la linea del mare
    line_all = res_all.slope * years_all + res_all.intercept

    # 3. Seconda linea di regressione (Solo i dati recenti dal 2000 al 2050)
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    # Crea la sequenza di anni dal 2000 fino al 2050
    years_recent = np.arange(2000, 2051)
    # Calcola i valori previsti basati solo sull'andamento accelerato degli ultimi anni
    line_recent = res_recent.slope * years_recent + res_recent.intercept

    # Confeziona i risultati in un dizionario per i controlli automatici
    return {
        'years_all': years_all.tolist(),
        'line_all': line_all.tolist(),
        'years_recent': years_recent.tolist(),
        'line_recent': line_recent.tolist()
    }
