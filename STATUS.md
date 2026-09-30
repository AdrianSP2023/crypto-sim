# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 22:36 UTC · vueltas 96 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 905.46 € (-2.03%) | 66 | 31 | 21% | -0.544% | -1.439% | -1.585% | -21.79 € |
| reversion_bb | 922.12 € (-0.23%) | 9 | 5 | 44% | -0.167% | -1.267% | -1.401% | -2.64 € |
| ruptura_volumen | 896.61 € (-2.99%) | 92 | 4 | 16% | -0.530% | -1.314% | -1.452% | -27.67 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 904.86 € (-2.10%) | 65 | 1 | 15% | -0.413% | -1.319% | -1.456% | -19.65 € |
| macd_momentum | 906.31 € (-1.94%) | 101 | 18 | 25% | -0.079% | -0.837% | -0.968% | -19.41 € |
| estocastico_rebote | 903.64 € (-2.23%) | 126 | 9 | 35% | -0.025% | -0.732% | -0.864% | -21.23 € |
| ruptura_estricta | 899.35 € (-2.69%) | 48 | 6 | 10% | -1.282% | -2.332% | -2.480% | -25.75 € |
| macd_sin_salida | 905.43 € (-2.04%) | 82 | 20 | 33% | -0.260% | -1.079% | -1.210% | -20.34 € |
| c_banda_atr_tope | 919.50 € (-0.51%) | 19 | 5 | 32% | -0.054% | -1.154% | -1.311% | -5.05 € |
| ruptura_volumen_tope | 917.26 € (-0.75%) | 25 | 5 | 20% | -0.209% | -1.309% | -1.428% | -7.54 € |
| c_banda_atr_regimen | 908.47 € (-1.71%) | 45 | 0 | 24% | -0.442% | -1.522% | -1.680% | -15.77 € |
| macd_momentum_regimen | 911.23 € (-1.41%) | 60 | 0 | 30% | -0.005% | -0.940% | -1.079% | -13.01 € |
| ruptura_volumen_regimen | 898.23 € (-2.81%) | 72 | 0 | 12% | -0.713% | -1.576% | -1.715% | -26.01 € |
| c_banda_atr_evento | 913.15 € (-1.20%) | 33 | 31 | 12% | -0.778% | -1.860% | -1.991% | -14.13 € |
| macd_momentum_evento | 911.40 € (-1.39%) | 54 | 18 | 17% | -0.172% | -1.155% | -1.281% | -14.32 € |
| ruptura_volumen_evento | 909.64 € (-1.58%) | 42 | 4 | 12% | -0.414% | -1.514% | -1.639% | -14.64 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 22:35 | ruptura_volumen_evento | ZRO | take-profit | +2.50% | +1.40% | +0.32 |
| 2026-09-30 22:35 | macd_momentum_evento | PUMP | take-profit | +2.00% | +1.20% | +0.28 |
| 2026-09-30 22:35 | c_banda_atr_evento | BNB | timeout | +0.08% | -0.72% | -0.17 |
| 2026-09-30 22:35 | c_banda_atr_evento | CRV | take-profit | +2.00% | +1.20% | +0.28 |
| 2026-09-30 22:35 | ruptura_volumen_tope | ZRO | take-profit | +2.50% | +1.40% | +0.32 |
| 2026-09-30 22:35 | c_banda_atr_tope | CRV | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-30 22:35 | macd_sin_salida | CRV | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 22:35 | macd_sin_salida | PUMP | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 22:35 | estocastico_rebote | SPX | take-profit | +1.96% | +1.46% | +0.33 |
| 2026-09-30 22:35 | estocastico_rebote | ENA | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-09-30 22:35 | macd_momentum | PUMP | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 22:35 | ruptura_volumen | ZRO | take-profit | +2.50% | +2.00% | +0.45 |
| 2026-09-30 22:35 | c_banda_atr | BNB | timeout | +0.08% | -0.42% | -0.10 |
| 2026-09-30 22:35 | c_banda_atr | CRV | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 22:30 | ruptura_volumen_evento | JUP | timeout | -0.56% | -1.66% | -0.38 |

## Eventos de la última vuelta

- 2026-09-30 22:30 [macd_momentum] ENTRADA ETH @ 2371.37 (22.61 €, apertura)
- 2026-09-30 22:30 [macd_sin_salida] ENTRADA ETH @ 2371.37 (22.58 €, apertura)
- 2026-09-30 22:30 [macd_momentum_evento] ENTRADA ETH @ 2371.37 (22.74 €, apertura)
- 2026-09-30 22:35 [macd_momentum] CIERRE PUMP take-profit bruto +2.00% neto +1.50%
- 2026-09-30 22:35 [macd_sin_salida] CIERRE PUMP take-profit bruto +2.00% neto +1.50%
- 2026-09-30 22:35 [macd_momentum_evento] CIERRE PUMP take-profit bruto +2.00% neto +1.20%
- 2026-09-30 22:30 [macd_momentum] ENTRADA UNI @ 7.8242 (22.62 €, apertura)
- 2026-09-30 22:30 [macd_momentum_evento] ENTRADA UNI @ 7.8242 (22.75 €, apertura)
- 2026-09-30 22:35 [ruptura_volumen] CIERRE ZRO take-profit bruto +2.50% neto +2.00%
- 2026-09-30 22:35 [ruptura_volumen_tope] CIERRE ZRO take-profit bruto +2.50% neto +1.40%
- 2026-09-30 22:35 [ruptura_volumen_evento] CIERRE ZRO take-profit bruto +2.50% neto +1.40%
- 2026-09-30 22:30 [c_banda_atr] ENTRADA ARB @ 0.1801 (22.56 €, apertura)
- 2026-09-30 22:30 [c_banda_atr_evento] ENTRADA ARB @ 0.1801 (22.75 €, apertura)
- 2026-09-30 22:35 [estocastico_rebote] CIERRE ENA take-profit bruto +1.80% neto +1.30%
- 2026-09-30 22:30 [macd_momentum] ENTRADA FET @ 0.2004 (22.62 €, apertura)
- 2026-09-30 22:30 [macd_sin_salida] ENTRADA FET @ 0.2004 (22.59 €, apertura)
- 2026-09-30 22:30 [macd_momentum_evento] ENTRADA FET @ 0.2004 (22.75 €, apertura)
- 2026-09-30 22:30 [macd_momentum] ENTRADA POL @ 0.09911 (22.62 €, apertura)
- 2026-09-30 22:30 [macd_momentum_evento] ENTRADA POL @ 0.09911 (22.75 €, apertura)
- 2026-09-30 22:35 [c_banda_atr] CIERRE CRV take-profit bruto +2.00% neto +1.50%
- 2026-09-30 22:30 [ruptura_volumen] ENTRADA CRV @ 0.35009 (22.41 €, apertura)
- 2026-09-30 22:30 [macd_momentum] ENTRADA CRV @ 0.35009 (22.62 €, apertura)
- 2026-09-30 22:35 [macd_sin_salida] CIERRE CRV take-profit bruto +2.00% neto +1.50%
- 2026-09-30 22:35 [c_banda_atr_tope] CIERRE CRV take-profit bruto +2.00% neto +0.90%
- 2026-09-30 22:30 [ruptura_volumen_tope] ENTRADA CRV @ 0.35009 (22.92 €, apertura)
- 2026-09-30 22:35 [c_banda_atr_evento] CIERRE CRV take-profit bruto +2.00% neto +1.20%
- 2026-09-30 22:30 [macd_momentum_evento] ENTRADA CRV @ 0.35009 (22.75 €, apertura)
- 2026-09-30 22:30 [ruptura_volumen_evento] ENTRADA CRV @ 0.35009 (22.74 €, apertura)
- 2026-09-30 22:30 [c_banda_atr] ENTRADA BCH @ 269.95 (22.56 €, apertura)
- 2026-09-30 22:30 [c_banda_atr_tope] ENTRADA BCH @ 269.95 (22.98 €, apertura)
- 2026-09-30 22:30 [c_banda_atr_evento] ENTRADA BCH @ 269.95 (22.76 €, apertura)
- 2026-09-30 22:30 [c_banda_atr] ENTRADA MON @ 0.02652 (22.56 €, apertura)
- 2026-09-30 22:30 [c_banda_atr_evento] ENTRADA MON @ 0.02652 (22.76 €, apertura)
- 2026-09-30 22:30 [ruptura_volumen] ENTRADA INJ @ 6.561 (22.41 €, apertura)
- 2026-09-30 22:30 [macd_momentum] ENTRADA INJ @ 6.561 (22.62 €, apertura)
- 2026-09-30 22:30 [macd_sin_salida] ENTRADA INJ @ 6.561 (22.60 €, apertura)
- 2026-09-30 22:30 [macd_momentum_evento] ENTRADA INJ @ 6.561 (22.75 €, apertura)
- 2026-09-30 22:30 [ruptura_volumen_evento] ENTRADA INJ @ 6.561 (22.74 €, apertura)
- 2026-09-30 22:35 [c_banda_atr] CIERRE BNB timeout bruto +0.08% neto -0.42%
- 2026-09-30 22:30 [macd_momentum] ENTRADA BNB @ 677.32 (22.62 €, apertura)
- 2026-09-30 22:30 [macd_sin_salida] ENTRADA BNB @ 677.32 (22.60 €, apertura)
- 2026-09-30 22:35 [c_banda_atr_evento] CIERRE BNB timeout bruto +0.08% neto -0.72%
- 2026-09-30 22:30 [macd_momentum_evento] ENTRADA BNB @ 677.32 (22.75 €, apertura)
- 2026-09-30 22:35 [estocastico_rebote] CIERRE SPX take-profit bruto +1.96% neto +1.46%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
