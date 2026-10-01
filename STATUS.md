# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 04:21 UTC · vueltas 123 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 905.43 € (-2.03%) | 112 | 26 | 31% | -0.090% | -0.823% | -0.944% | -21.16 € |
| reversion_bb | 921.60 € (-0.29%) | 14 | 4 | 36% | +0.190% | -0.910% | -1.026% | -2.94 € |
| ruptura_volumen | 890.34 € (-3.67%) | 147 | 29 | 19% | -0.340% | -1.018% | -1.129% | -34.11 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 903.00 € (-2.30%) | 87 | 6 | 16% | -0.297% | -1.101% | -1.219% | -21.92 € |
| macd_momentum | 895.81 € (-3.08%) | 203 | 29 | 21% | -0.035% | -0.664% | -0.773% | -30.70 € |
| estocastico_rebote | 902.60 € (-2.34%) | 155 | 15 | 37% | +0.057% | -0.611% | -0.732% | -21.80 € |
| ruptura_estricta | 900.74 € (-2.54%) | 74 | 24 | 24% | -0.565% | -1.422% | -1.555% | -24.24 € |
| macd_sin_salida | 904.69 € (-2.12%) | 138 | 33 | 38% | +0.026% | -0.663% | -0.779% | -21.05 € |
| c_banda_atr_tope | 917.96 € (-0.68%) | 27 | 5 | 30% | +0.046% | -1.054% | -1.177% | -6.56 € |
| ruptura_volumen_tope | 914.44 € (-1.06%) | 41 | 5 | 22% | +0.040% | -1.060% | -1.161% | -10.00 € |
| c_banda_atr_regimen | 909.87 € (-1.55%) | 58 | 24 | 29% | -0.244% | -1.194% | -1.339% | -15.95 € |
| macd_momentum_regimen | 904.89 € (-2.09%) | 117 | 29 | 21% | -0.084% | -0.807% | -0.924% | -21.64 € |
| ruptura_volumen_regimen | 891.13 € (-3.58%) | 119 | 31 | 13% | -0.507% | -1.226% | -1.343% | -33.27 € |
| c_banda_atr_evento | 911.46 € (-1.38%) | 79 | 26 | 32% | +0.002% | -0.832% | -0.937% | -15.15 € |
| macd_momentum_evento | 900.77 € (-2.54%) | 156 | 29 | 16% | -0.054% | -0.723% | -0.824% | -25.75 € |
| ruptura_volumen_evento | 903.01 € (-2.30%) | 97 | 29 | 19% | -0.192% | -0.965% | -1.057% | -21.43 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 04:20 | ruptura_volumen_evento | ZRO | stop-loss | -1.45% | -1.95% | -0.44 |
| 2026-10-01 04:20 | macd_momentum_evento | SPX | momentum perdido | +0.73% | +0.23% | +0.05 |
| 2026-10-01 04:20 | macd_momentum_evento | APT | momentum perdido | -0.76% | -1.26% | -0.28 |
| 2026-10-01 04:20 | macd_momentum_evento | ONDO | momentum perdido | +0.23% | -0.27% | -0.06 |
| 2026-10-01 04:20 | macd_momentum_evento | TRX | momentum perdido | -0.03% | -0.53% | -0.12 |
| 2026-10-01 04:20 | ruptura_volumen_regimen | ZRO | stop-loss | -1.45% | -1.95% | -0.43 |
| 2026-10-01 04:20 | macd_momentum_regimen | SPX | momentum perdido | +0.73% | +0.23% | +0.05 |
| 2026-10-01 04:20 | macd_momentum_regimen | APT | momentum perdido | -0.76% | -1.26% | -0.28 |
| 2026-10-01 04:20 | macd_momentum_regimen | ONDO | momentum perdido | +0.23% | -0.27% | -0.06 |
| 2026-10-01 04:20 | macd_momentum_regimen | TRX | momentum perdido | -0.03% | -0.53% | -0.12 |
| 2026-10-01 04:20 | macd_sin_salida | JUP | timeout | -0.11% | -0.61% | -0.14 |
| 2026-10-01 04:20 | ruptura_estricta | INJ | timeout | +0.47% | -0.03% | -0.01 |
| 2026-10-01 04:20 | ruptura_estricta | NIGHT | timeout | +0.64% | +0.14% | +0.03 |
| 2026-10-01 04:20 | ruptura_estricta | DOGE | timeout | +0.44% | -0.06% | -0.01 |
| 2026-10-01 04:20 | macd_momentum | SPX | momentum perdido | +0.73% | +0.23% | +0.05 |

## Eventos de la última vuelta

- 2026-10-01 04:15 [ruptura_volumen] ENTRADA ZEC @ 1259.29 (22.26 €, apertura)
- 2026-10-01 04:15 [ruptura_volumen_regimen] ENTRADA ZEC @ 1259.29 (22.28 €, apertura)
- 2026-10-01 04:15 [ruptura_volumen_evento] ENTRADA ZEC @ 1259.29 (22.58 €, apertura)
- 2026-10-01 04:15 [c_banda_atr] ENTRADA HYPE @ 78.63 (22.58 €, apertura)
- 2026-10-01 04:15 [c_banda_atr_regimen] ENTRADA HYPE @ 78.63 (22.71 €, apertura)
- 2026-10-01 04:15 [c_banda_atr_evento] ENTRADA HYPE @ 78.63 (22.73 €, apertura)
- 2026-10-01 04:20 [ruptura_volumen] CIERRE ZRO stop-loss bruto -1.44% neto -1.94%
- 2026-10-01 04:20 [ruptura_volumen_regimen] CIERRE ZRO stop-loss bruto -1.44% neto -1.94%
- 2026-10-01 04:20 [ruptura_volumen_evento] CIERRE ZRO stop-loss bruto -1.44% neto -1.94%
- 2026-10-01 04:20 [ruptura_estricta] CIERRE DOGE timeout bruto +0.44% neto -0.06%
- 2026-10-01 04:20 [macd_momentum] CIERRE TRX momentum perdido bruto -0.03% neto -0.53%
- 2026-10-01 04:20 [macd_momentum_regimen] CIERRE TRX momentum perdido bruto -0.03% neto -0.53%
- 2026-10-01 04:20 [macd_momentum_evento] CIERRE TRX momentum perdido bruto -0.03% neto -0.53%
- 2026-10-01 04:20 [macd_momentum] CIERRE ONDO momentum perdido bruto +0.23% neto -0.27%
- 2026-10-01 04:20 [macd_momentum_regimen] CIERRE ONDO momentum perdido bruto +0.23% neto -0.27%
- 2026-10-01 04:20 [macd_momentum_evento] CIERRE ONDO momentum perdido bruto +0.23% neto -0.27%
- 2026-10-01 04:20 [ruptura_estricta] CIERRE NIGHT timeout bruto +0.64% neto +0.14%
- 2026-10-01 04:20 [macd_sin_salida] CIERRE JUP timeout bruto -0.11% neto -0.61%
- 2026-10-01 04:20 [ruptura_estricta] CIERRE INJ timeout bruto +0.47% neto -0.03%
- 2026-10-01 04:15 [ruptura_volumen] ENTRADA XMR @ 483.16 (22.25 €, apertura)
- 2026-10-01 04:15 [macd_momentum] ENTRADA XMR @ 483.16 (22.34 €, apertura)
- 2026-10-01 04:15 [ruptura_estricta] ENTRADA XMR @ 483.16 (22.50 €, apertura)
- 2026-10-01 04:15 [macd_sin_salida] ENTRADA XMR @ 483.16 (22.58 €, apertura)
- 2026-10-01 04:15 [macd_momentum_regimen] ENTRADA XMR @ 483.16 (22.57 €, apertura)
- 2026-10-01 04:15 [ruptura_volumen_regimen] ENTRADA XMR @ 483.16 (22.27 €, apertura)
- 2026-10-01 04:15 [macd_momentum_evento] ENTRADA XMR @ 483.16 (22.47 €, apertura)
- 2026-10-01 04:15 [ruptura_volumen_evento] ENTRADA XMR @ 483.16 (22.57 €, apertura)
- 2026-10-01 04:20 [macd_momentum] CIERRE APT momentum perdido bruto -0.76% neto -1.26%
- 2026-10-01 04:20 [macd_momentum_regimen] CIERRE APT momentum perdido bruto -0.76% neto -1.26%
- 2026-10-01 04:20 [macd_momentum_evento] CIERRE APT momentum perdido bruto -0.76% neto -1.26%
- 2026-10-01 04:20 [macd_momentum] CIERRE SPX momentum perdido bruto +0.73% neto +0.23%
- 2026-10-01 04:20 [macd_momentum_regimen] CIERRE SPX momentum perdido bruto +0.73% neto +0.23%
- 2026-10-01 04:20 [macd_momentum_evento] CIERRE SPX momentum perdido bruto +0.73% neto +0.23%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
