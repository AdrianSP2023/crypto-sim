# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 02:41 UTC · vueltas 103 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 901.48 € (-2.46%) | 102 | 28 | 27% | -0.234% | -0.990% | -1.114% | -23.14 € |
| reversion_bb | 921.48 € (-0.30%) | 13 | 5 | 38% | +0.127% | -0.973% | -1.092% | -2.92 € |
| ruptura_volumen | 891.32 € (-3.56%) | 131 | 16 | 18% | -0.398% | -1.097% | -1.212% | -32.79 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 903.30 € (-2.27%) | 82 | 2 | 16% | -0.314% | -1.136% | -1.257% | -21.34 € |
| macd_momentum | 897.25 € (-2.92%) | 176 | 17 | 20% | -0.047% | -0.696% | -0.804% | -27.95 € |
| estocastico_rebote | 902.37 € (-2.37%) | 146 | 17 | 37% | +0.021% | -0.658% | -0.781% | -22.09 € |
| ruptura_estricta | 898.53 € (-2.78%) | 62 | 17 | 16% | -0.874% | -1.800% | -1.939% | -25.67 € |
| macd_sin_salida | 902.19 € (-2.39%) | 120 | 27 | 35% | -0.070% | -0.787% | -0.905% | -21.71 € |
| c_banda_atr_tope | 917.55 € (-0.72%) | 24 | 5 | 25% | -0.150% | -1.250% | -1.378% | -6.92 € |
| ruptura_volumen_tope | 915.24 € (-0.97%) | 37 | 5 | 22% | +0.042% | -1.058% | -1.151% | -9.02 € |
| c_banda_atr_regimen | 906.98 € (-1.87%) | 52 | 18 | 25% | -0.420% | -1.422% | -1.575% | -17.01 € |
| macd_momentum_regimen | 905.06 € (-2.07%) | 94 | 13 | 20% | -0.104% | -0.882% | -0.998% | -19.03 € |
| ruptura_volumen_regimen | 892.16 € (-3.47%) | 104 | 16 | 13% | -0.575% | -1.326% | -1.446% | -31.50 € |
| c_banda_atr_evento | 907.48 € (-1.81%) | 69 | 28 | 26% | -0.198% | -1.080% | -1.187% | -17.14 € |
| macd_momentum_evento | 902.22 € (-2.38%) | 129 | 17 | 15% | -0.075% | -0.780% | -0.876% | -22.99 € |
| ruptura_volumen_evento | 904.00 € (-2.19%) | 81 | 16 | 17% | -0.257% | -1.082% | -1.176% | -20.10 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 02:40 | macd_momentum_evento | NIGHT | momentum perdido | -0.36% | -0.86% | -0.20 |
| 2026-10-01 02:40 | macd_momentum | NIGHT | momentum perdido | -0.36% | -0.86% | -0.19 |
| 2026-10-01 02:40 | pullback_tendencia | ETH | rotura de tendencia | -0.07% | -0.57% | -0.13 |
| 2026-10-01 02:35 | macd_momentum_evento | ETH | momentum perdido | +0.21% | -0.29% | -0.07 |
| 2026-10-01 02:35 | c_banda_atr_evento | TRUMP | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 02:35 | c_banda_atr_evento | KSM | timeout | +0.66% | +0.16% | +0.04 |
| 2026-10-01 02:35 | macd_momentum_regimen | ETH | momentum perdido | +0.21% | -0.29% | -0.07 |
| 2026-10-01 02:35 | c_banda_atr_regimen | TRUMP | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 02:35 | c_banda_atr_regimen | KSM | timeout | +0.66% | +0.16% | +0.04 |
| 2026-10-01 02:35 | c_banda_atr_regimen | PEPE | timeout | -0.24% | -0.74% | -0.17 |
| 2026-10-01 02:35 | c_banda_atr_regimen | LINK | timeout | +0.30% | -0.20% | -0.05 |
| 2026-10-01 02:35 | ruptura_volumen_tope | TRUMP | take-profit | +2.50% | +1.40% | +0.32 |
| 2026-10-01 02:35 | macd_sin_salida | TRUMP | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 02:35 | macd_sin_salida | XDC | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 02:35 | ruptura_estricta | TRUMP | take-profit | +3.00% | +2.50% | +0.56 |

## Eventos de la última vuelta

- 2026-10-01 02:40 [pullback_tendencia] CIERRE ETH rotura de tendencia bruto -0.07% neto -0.57%
- 2026-10-01 02:35 [macd_momentum] ENTRADA SOL @ 104.24 (22.41 €, apertura)
- 2026-10-01 02:35 [macd_sin_salida] ENTRADA SOL @ 104.24 (22.56 €, apertura)
- 2026-10-01 02:35 [macd_momentum_regimen] ENTRADA SOL @ 104.24 (22.63 €, apertura)
- 2026-10-01 02:35 [macd_momentum_evento] ENTRADA SOL @ 104.24 (22.54 €, apertura)
- 2026-10-01 02:35 [c_banda_atr] ENTRADA LINK @ 12.7466 (22.53 €, apertura)
- 2026-10-01 02:35 [ruptura_volumen] ENTRADA LINK @ 12.7466 (22.29 €, apertura)
- 2026-10-01 02:35 [macd_momentum] ENTRADA LINK @ 12.7466 (22.41 €, apertura)
- 2026-10-01 02:35 [ruptura_estricta] ENTRADA LINK @ 12.7466 (22.46 €, apertura)
- 2026-10-01 02:35 [ruptura_volumen_tope] ENTRADA LINK @ 12.7466 (22.88 €, apertura)
- 2026-10-01 02:35 [macd_momentum_regimen] ENTRADA LINK @ 12.7466 (22.63 €, apertura)
- 2026-10-01 02:35 [ruptura_volumen_regimen] ENTRADA LINK @ 12.7466 (22.32 €, apertura)
- 2026-10-01 02:35 [c_banda_atr_evento] ENTRADA LINK @ 12.7466 (22.68 €, apertura)
- 2026-10-01 02:35 [macd_momentum_evento] ENTRADA LINK @ 12.7466 (22.54 €, apertura)
- 2026-10-01 02:35 [ruptura_volumen_evento] ENTRADA LINK @ 12.7466 (22.60 €, apertura)
- 2026-10-01 02:35 [c_banda_atr] ENTRADA ADA @ 0.219246 (22.53 €, apertura)
- 2026-10-01 02:35 [c_banda_atr_regimen] ENTRADA ADA @ 0.219246 (22.68 €, apertura)
- 2026-10-01 02:35 [c_banda_atr_evento] ENTRADA ADA @ 0.219246 (22.68 €, apertura)
- 2026-10-01 02:35 [ruptura_volumen] ENTRADA AVAX @ 9.725 (22.29 €, apertura)
- 2026-10-01 02:35 [ruptura_estricta] ENTRADA AVAX @ 9.725 (22.46 €, apertura)
- 2026-10-01 02:35 [ruptura_volumen_tope] ENTRADA AVAX @ 9.725 (22.88 €, apertura)
- 2026-10-01 02:35 [ruptura_volumen_regimen] ENTRADA AVAX @ 9.725 (22.32 €, apertura)
- 2026-10-01 02:35 [ruptura_volumen_evento] ENTRADA AVAX @ 9.725 (22.60 €, apertura)
- 2026-10-01 02:35 [c_banda_atr] ENTRADA AAVE @ 143.64 (22.53 €, apertura)
- 2026-10-01 02:35 [macd_sin_salida] ENTRADA AAVE @ 143.64 (22.56 €, apertura)
- 2026-10-01 02:35 [c_banda_atr_regimen] ENTRADA AAVE @ 143.64 (22.68 €, apertura)
- 2026-10-01 02:35 [macd_momentum_regimen] ENTRADA AAVE @ 143.64 (22.63 €, apertura)
- 2026-10-01 02:35 [c_banda_atr_evento] ENTRADA AAVE @ 143.64 (22.68 €, apertura)
- 2026-10-01 02:35 [estocastico_rebote] ENTRADA HYPE @ 78.99 (22.55 €, apertura)
- 2026-10-01 02:35 [macd_momentum] ENTRADA TAO @ 266.864 (22.41 €, apertura)
- 2026-10-01 02:35 [c_banda_atr_regimen] ENTRADA TAO @ 266.864 (22.68 €, apertura)
- 2026-10-01 02:35 [macd_momentum_regimen] ENTRADA TAO @ 266.864 (22.63 €, apertura)
- 2026-10-01 02:35 [macd_momentum_evento] ENTRADA TAO @ 266.864 (22.54 €, apertura)
- 2026-10-01 02:35 [macd_momentum] ENTRADA ARB @ 0.1802 (22.41 €, apertura)
- 2026-10-01 02:35 [macd_sin_salida] ENTRADA ARB @ 0.1802 (22.56 €, apertura)
- 2026-10-01 02:35 [macd_momentum_regimen] ENTRADA ARB @ 0.1802 (22.63 €, apertura)
- 2026-10-01 02:35 [macd_momentum_evento] ENTRADA ARB @ 0.1802 (22.54 €, apertura)
- 2026-10-01 02:35 [c_banda_atr] ENTRADA ENA @ 0.2346 (22.53 €, apertura)
- 2026-10-01 02:35 [c_banda_atr_regimen] ENTRADA ENA @ 0.2346 (22.68 €, apertura)
- 2026-10-01 02:35 [c_banda_atr_evento] ENTRADA ENA @ 0.2346 (22.68 €, apertura)
- 2026-10-01 02:35 [c_banda_atr] ENTRADA ICP @ 3 (22.53 €, apertura)
- 2026-10-01 02:35 [macd_momentum] ENTRADA ICP @ 3 (22.41 €, apertura)
- 2026-10-01 02:35 [macd_sin_salida] ENTRADA ICP @ 3 (22.56 €, apertura)
- 2026-10-01 02:35 [ruptura_volumen_tope] ENTRADA ICP @ 3 (22.88 €, apertura)
- 2026-10-01 02:35 [c_banda_atr_regimen] ENTRADA ICP @ 3 (22.68 €, apertura)
- 2026-10-01 02:35 [macd_momentum_regimen] ENTRADA ICP @ 3 (22.63 €, apertura)
- 2026-10-01 02:35 [ruptura_volumen_regimen] ENTRADA ICP @ 3 (22.32 €, apertura)
- 2026-10-01 02:35 [c_banda_atr_evento] ENTRADA ICP @ 3 (22.68 €, apertura)
- 2026-10-01 02:35 [macd_momentum_evento] ENTRADA ICP @ 3 (22.54 €, apertura)
- 2026-10-01 02:35 [c_banda_atr_regimen] ENTRADA CRV @ 0.35308 (22.68 €, apertura)
- 2026-10-01 02:35 [macd_momentum_regimen] ENTRADA CRV @ 0.35308 (22.63 €, apertura)
- 2026-10-01 02:35 [ruptura_volumen] ENTRADA XDC @ 0.03139 (22.29 €, apertura)
- 2026-10-01 02:35 [ruptura_volumen_tope] ENTRADA XDC @ 0.03139 (22.88 €, apertura)
- 2026-10-01 02:35 [ruptura_volumen_regimen] ENTRADA XDC @ 0.03139 (22.32 €, apertura)
- 2026-10-01 02:35 [ruptura_volumen_evento] ENTRADA XDC @ 0.03139 (22.60 €, apertura)
- 2026-10-01 02:40 [macd_momentum] CIERRE NIGHT momentum perdido bruto -0.37% neto -0.87%
- 2026-10-01 02:40 [macd_momentum_evento] CIERRE NIGHT momentum perdido bruto -0.37% neto -0.87%
- 2026-10-01 02:35 [macd_momentum] ENTRADA PEPE @ 3.796e-06 (22.41 €, apertura)
- 2026-10-01 02:35 [macd_sin_salida] ENTRADA PEPE @ 3.796e-06 (22.56 €, apertura)
- 2026-10-01 02:35 [macd_momentum_regimen] ENTRADA PEPE @ 3.796e-06 (22.63 €, apertura)
- 2026-10-01 02:35 [macd_momentum_evento] ENTRADA PEPE @ 3.796e-06 (22.53 €, apertura)
- 2026-10-01 02:35 [c_banda_atr] ENTRADA PENGU @ 0.008518 (22.53 €, apertura)
- 2026-10-01 02:35 [macd_momentum] ENTRADA PENGU @ 0.008518 (22.41 €, apertura)
- 2026-10-01 02:35 [macd_sin_salida] ENTRADA PENGU @ 0.008518 (22.56 €, apertura)
- 2026-10-01 02:35 [c_banda_atr_regimen] ENTRADA PENGU @ 0.008518 (22.68 €, apertura)
- 2026-10-01 02:35 [macd_momentum_regimen] ENTRADA PENGU @ 0.008518 (22.63 €, apertura)
- 2026-10-01 02:35 [c_banda_atr_evento] ENTRADA PENGU @ 0.008518 (22.68 €, apertura)
- 2026-10-01 02:35 [macd_momentum_evento] ENTRADA PENGU @ 0.008518 (22.53 €, apertura)
- 2026-10-01 02:35 [macd_momentum] ENTRADA KSM @ 4.58 (22.41 €, apertura)
- 2026-10-01 02:35 [macd_sin_salida] ENTRADA KSM @ 4.58 (22.56 €, apertura)
- 2026-10-01 02:35 [macd_momentum_regimen] ENTRADA KSM @ 4.58 (22.63 €, apertura)
- 2026-10-01 02:35 [macd_momentum_evento] ENTRADA KSM @ 4.58 (22.53 €, apertura)
- 2026-10-01 02:35 [ruptura_volumen] ENTRADA TRUMP @ 1.876 (22.29 €, apertura)
- 2026-10-01 02:35 [macd_momentum] ENTRADA TRUMP @ 1.876 (22.41 €, apertura)
- 2026-10-01 02:35 [macd_momentum_regimen] ENTRADA TRUMP @ 1.876 (22.63 €, apertura)
- 2026-10-01 02:35 [ruptura_volumen_regimen] ENTRADA TRUMP @ 1.876 (22.32 €, apertura)
- 2026-10-01 02:35 [macd_momentum_evento] ENTRADA TRUMP @ 1.876 (22.53 €, apertura)
- 2026-10-01 02:35 [ruptura_volumen_evento] ENTRADA TRUMP @ 1.876 (22.60 €, apertura)
- 2026-10-01 02:35 [c_banda_atr] ENTRADA TON @ 1.33 (22.53 €, apertura)
- 2026-10-01 02:35 [macd_momentum] ENTRADA TON @ 1.33 (22.41 €, apertura)
- 2026-10-01 02:35 [macd_sin_salida] ENTRADA TON @ 1.33 (22.56 €, apertura)
- 2026-10-01 02:35 [c_banda_atr_regimen] ENTRADA TON @ 1.33 (22.68 €, apertura)
- 2026-10-01 02:35 [macd_momentum_regimen] ENTRADA TON @ 1.33 (22.63 €, apertura)
- 2026-10-01 02:35 [c_banda_atr_evento] ENTRADA TON @ 1.33 (22.68 €, apertura)
- 2026-10-01 02:35 [macd_momentum_evento] ENTRADA TON @ 1.33 (22.53 €, apertura)
- 2026-10-01 02:35 [estocastico_rebote] ENTRADA APT @ 0.6922 (22.55 €, apertura)
- 2026-10-01 02:35 [ruptura_volumen] ENTRADA SPX @ 0.3955 (22.29 €, apertura)
- 2026-10-01 02:35 [macd_momentum] ENTRADA SPX @ 0.3955 (22.41 €, apertura)
- 2026-10-01 02:35 [ruptura_estricta] ENTRADA SPX @ 0.3955 (22.46 €, apertura)
- 2026-10-01 02:35 [macd_sin_salida] ENTRADA SPX @ 0.3955 (22.56 €, apertura)
- 2026-10-01 02:35 [c_banda_atr_regimen] ENTRADA SPX @ 0.3955 (22.68 €, apertura)
- 2026-10-01 02:35 [macd_momentum_regimen] ENTRADA SPX @ 0.3955 (22.63 €, apertura)
- 2026-10-01 02:35 [ruptura_volumen_regimen] ENTRADA SPX @ 0.3955 (22.32 €, apertura)
- 2026-10-01 02:35 [macd_momentum_evento] ENTRADA SPX @ 0.3955 (22.53 €, apertura)
- 2026-10-01 02:35 [ruptura_volumen_evento] ENTRADA SPX @ 0.3955 (22.60 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
