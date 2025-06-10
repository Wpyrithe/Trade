import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import math
import statistics
from scipy import stats

# === PARAMETRES ===
TSEQ = 20
D75_THRESHOLD = 0
DIFF_THRESHOLDS = [0.1] #[0.05, 0.075, 0.1]
SYMBOLS = ["CVX", "XOM", "BTU", "AMR", "CNR", "PBR", "TTE.PA", "ENI.MI", "REP.MC", "RIGD.IL", "PSX", "SHEL", "VLO", 
"MPC", "COP", "HES", "PBF", "DINO", "DVN", "IEP", "EOG", "APA", "DK", "MUR", "CLMT", "BP.L", "TLW.L", "HBR.L", 
"DEC.L", "ENOG.L", "SHEL.L", "EXE", "VRN", "VET", "DNO.OL", "NESTE.HE", "IMO", "0386.HK", "0883.HK", 
"1088.HK", "1171.HK", "1898.HK", "0857.HK", "HESM", "NOG.L", "CNE.L", "VTS", "ALD.AX", "NHC.AX", "VEA.AX",
"BPT.AX", "CRN.AX", "MAU.PA", "ES.PA", "CVI", "SU", "PBR-A", "OXY", "FANG", "CTRA", "OVV", "AKRBP.OL", "EQNR.OL", "MTDR",
"SM", "CNX", "PR", "AR", "CNQ", "CRK", "CVE", "EC", "EQNR", "EQT", "CIVI", "CRC", "NOG", "YPF", "PARR", "HCC", "GPOR", 
"VIST", "NEXT", "CLB", "VNOM", "CRGY", "HPK", "METC", "HNRG", "KLXE", "GRNT", "REPX", "GPRK", "EGY", "AMPY", "EPM", "REI", 
"SMR.AX", "YAL.AX", "GFR", "METCB", "HE1.L", "GKP.L", "PANR.L", "ENQ.L", "SOU.L", "EME.L", "AET.L", "KIST.L", "CHAR.L", 
"GENL.L", "SEPL.L", "AXL.L", "RKH.L", "ORCP.L", "ECO.L", "FOG.L", "PXEN.L", "PHAR.L", "STAR.L", "BOR.L", "UJO.L",  
"ENW.L", "DR0.DE", "GALP.LS", "VAR.OL", "DOFG.OL", "BNOR.OL", "PEN.OL", "OKEA.OL", "REACH.OL", "BWO.OL", "QEC.OL", "IOX.OL", 
"PNOR.OL", "ALNG.OL", "SBX.OL", "HUNT.OL", "PSE.OL", "EC.PA"]


def get_normalized_close_prices(symbol, tseq):
    data = yf.Ticker(symbol)
    df = data.history(period="1mo")
    if df.empty or len(df) < tseq:
        return None
    closes = df['Close'][-tseq:].values
    norm = (closes - np.min(closes)) / (np.max(closes) - np.min(closes) + 1e-6)
    return norm


def analyze_series(seq):
    mean_val = statistics.mean(seq)
    dif = round(seq[-1] - seq[0], 3)
    days = np.arange(len(seq))
    slope, intercept, r_value, _, _ = stats.linregress(days, seq)
    coeff = round(slope, 3)
    disp = round(r_value, 3)
    t75 = math.floor(len(seq) * 3 / 4)
    dif75 = round((seq[-1] - seq[t75]) / mean_val, 3)
    dfinal = round(seq[-1] - seq[-2], 3)
    sconf = round(dif + coeff + disp - dif75 - dfinal, 3)
    return coeff, dif, dif75, disp, dfinal, sconf, (slope, intercept)


def select_symbols(symbols, diff_min):
    selection = []
    courbes = {}
    for sym in symbols:
        seq = get_normalized_close_prices(sym, TSEQ)
        if seq is None:
            continue
        coeff, dif, dif75, disp, dfinal, sconf, regression = analyze_series(seq)
        if dif >= diff_min and coeff >= 0 and disp >= 0.6 and dif75 >= D75_THRESHOLD:
            selection.append([sym, coeff, dif, dif75, disp, sconf])
            courbes[sym] = (seq, regression)
    selection.sort(key=lambda x: x[5], reverse=True)
    return selection, courbes


def plot_top5(selection, courbes):
    for entry in selection[:5]:
        sym = entry[0]
        seq, (slope, intercept) = courbes[sym]
        days = np.arange(len(seq))
        fit_line = slope * days + intercept

        plt.figure(figsize=(8, 4))
        plt.plot(seq, label="Cours normalisé")
        plt.plot(fit_line, '--', label="Régression linéaire")
        plt.title(f"{sym} - Score: {entry[5]}")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()


def main():
    for diff_min in DIFF_THRESHOLDS:
        print(f"\n=========== Seuil DiffMaxMin = {diff_min*100}% ===========")
        selection, courbes = select_symbols(SYMBOLS, diff_min)
        for s in selection:
            print(f"{s[0]} -- Coeff: {s[1]}, Dinit-fin: {s[2]}, D75: {s[3]}, Disp: {s[4]}, Sconf: {s[5]}")
        #print("\n--- PLOTS ---")
        #plot_top5(selection, courbes)


if __name__ == "__main__":
    main()
