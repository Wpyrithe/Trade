import numpy as np
import pandas as pd
import yfinance as yf
import statistics
import math
from scipy import stats
import datetime
import random



# === PARAMETRES ===
TSEQ = 20  # taille de la fenetre d'analyse
HOLD_DAYS = 2  # temps de conservation des actions
STEP = 2  # fréquence de trading
NB_SELECTION = 8  # nombre de titres à sélectionner
LEVERAGE = 1  # effet de levier appliqué sur chaque trade
SYMBOLS = ["HPK", "METC", "HNRG", "KLXE", "GRNT", "REPX", "GPRK", "EGY", "AMPY", "EPM", "REI", 
"SMR.AX", "YAL.AX", "GFR", "METCB", "HE1.L", "GKP.L"]  # exemple réduit
START_DATE = "2024-01-01"
END_DATE = "2024-04-30"

# === FILTRES ===
DIFF_MIN = 0.1
DISP_MIN = 0.6
DIF75_MIN = 0
COEFF_MIN = 0


def download_data(symbols, start, end):
    data = yf.download(symbols, start=start, end=end, group_by='ticker', auto_adjust=True)
    return data


def analyze_series(prices):
    seq = (prices - np.min(prices)) / (np.max(prices) - np.min(prices) + 1e-6)
    mean_val = statistics.mean(seq)
    dif = round(seq[-1] - seq[0], 3)
    days = np.arange(len(seq))
    slope, intercept, r_value, _, _ = stats.linregress(days, seq)
    coeff = round(slope, 3)
    disp = round(r_value, 3)
    t75 = math.floor(len(seq) * 3 / 4)
    dif75 = round((seq[-1] - seq[t75]) / mean_val, 3)
    dfinal = round(seq[-1] - seq[-2], 3)

    # Filtres comme dans le code original
    if dif < DIFF_MIN or coeff < COEFF_MIN or disp < DISP_MIN or dif75 < DIF75_MIN:
        return None

    sconf = round(dif + coeff + disp - dif75 - dfinal, 3)
    return sconf


def backtest(data, symbols):
    returns = []
    dates = data.index

    for start_idx in range(0, len(dates) - TSEQ - HOLD_DAYS, STEP):
        start_date = dates[start_idx]
        end_date = dates[start_idx + TSEQ - 1]
        sell_date = dates[start_idx + TSEQ + HOLD_DAYS - 1]

        scores = []
        for sym in symbols:
            try:
                sym_data = data[sym]['Close'] if isinstance(data.columns, pd.MultiIndex) else data[f'{sym}']
                window = sym_data.loc[start_date:end_date]
                if len(window) < TSEQ:
                    continue
                score = analyze_series(window.values)
                if score is not None:
                    scores.append((sym, score))
            except:
                continue

        scores.sort(key=lambda x: x[1], reverse=True)
        selected = [s[0] for s in scores[:NB_SELECTION]]

        for sym in selected:
            try:
                price_start = data[sym]['Close'].loc[end_date]
                price_end = data[sym]['Close'].loc[sell_date]
                if pd.isna(price_start) or pd.isna(price_end):
                    continue
                ret = (price_end - price_start) / price_start
                leveraged_ret = ret * LEVERAGE
                returns.append(leveraged_ret)
            except:
                continue

    avg_return = np.mean(returns)
    cum_return = np.prod([1 + r for r in returns]) - 1
    print(f"Backtest terminé sur {len(returns)} trades")
    print(f"Effet de levier appliqué : x{LEVERAGE}")
    print(f"Rendement moyen par trade: {round(avg_return*100, 2)}%")
    print(f"Rendement cumulé approximatif: {round(cum_return*100, 2)}%")


if __name__ == "__main__":
    print("Téléchargement des données...")
    data = download_data(SYMBOLS, START_DATE, END_DATE)
    print("Lancement du backtest...")
    backtest(data, SYMBOLS)

