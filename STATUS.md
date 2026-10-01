# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 04:11 UTC · vueltas 121 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 906.11 € (-1.96%) | 111 | 26 | 32% | -0.090% | -0.825% | -0.946% | -21.04 € |
| reversion_bb | 921.59 € (-0.29%) | 14 | 4 | 36% | +0.190% | -0.910% | -1.026% | -2.94 € |
| ruptura_volumen | 891.59 € (-3.53%) | 146 | 27 | 19% | -0.333% | -1.011% | -1.123% | -33.67 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 903.19 € (-2.28%) | 86 | 7 | 16% | -0.285% | -1.092% | -1.210% | -21.51 € |
| macd_momentum | 897.54 € (-2.89%) | 197 | 33 | 21% | -0.028% | -0.661% | -0.771% | -29.69 € |
| estocastico_rebote | 903.15 € (-2.28%) | 155 | 15 | 37% | +0.057% | -0.611% | -0.732% | -21.80 € |
| ruptura_estricta | 901.46 € (-2.46%) | 71 | 26 | 24% | -0.611% | -1.483% | -1.620% | -24.25 € |
| macd_sin_salida | 905.97 € (-1.98%) | 136 | 33 | 39% | +0.038% | -0.654% | -0.769% | -20.46 € |
| c_banda_atr_tope | 917.96 € (-0.68%) | 27 | 5 | 30% | +0.046% | -1.054% | -1.177% | -6.56 € |
| ruptura_volumen_tope | 914.70 € (-1.03%) | 41 | 5 | 22% | +0.040% | -1.060% | -1.161% | -10.00 € |
| c_banda_atr_regimen | 910.54 € (-1.48%) | 58 | 23 | 29% | -0.244% | -1.194% | -1.339% | -15.95 € |
| macd_momentum_regimen | 906.64 € (-1.90%) | 111 | 33 | 21% | -0.075% | -0.810% | -0.928% | -20.61 € |
| ruptura_volumen_regimen | 892.42 € (-3.44%) | 118 | 29 | 14% | -0.499% | -1.220% | -1.338% | -32.84 € |
| c_banda_atr_evento | 912.14 € (-1.31%) | 78 | 26 | 32% | +0.002% | -0.836% | -0.940% | -15.02 € |
| macd_momentum_evento | 902.51 € (-2.35%) | 150 | 33 | 16% | -0.046% | -0.722% | -0.823% | -24.73 € |
| ruptura_volumen_evento | 904.28 € (-2.16%) | 96 | 27 | 19% | -0.179% | -0.954% | -1.047% | -21.00 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 04:10 | ruptura_volumen_evento | ETH | timeout | +0.12% | -0.38% | -0.09 |
| 2026-10-01 04:10 | macd_momentum_evento | WLD | momentum perdido | -0.71% | -1.21% | -0.27 |
| 2026-10-01 04:10 | macd_momentum_regimen | WLD | momentum perdido | -0.71% | -1.21% | -0.27 |
| 2026-10-01 04:10 | macd_momentum | WLD | momentum perdido | -0.71% | -1.21% | -0.27 |
| 2026-10-01 04:10 | ruptura_volumen | ETH | timeout | +0.12% | -0.38% | -0.09 |
| 2026-10-01 04:05 | macd_momentum_evento | WLFI | momentum perdido | -0.20% | -0.70% | -0.16 |
| 2026-10-01 04:05 | macd_momentum_regimen | WLFI | momentum perdido | -0.20% | -0.70% | -0.16 |
| 2026-10-01 04:05 | macd_sin_salida | SEI | timeout | +0.61% | +0.11% | +0.03 |
| 2026-10-01 04:05 | macd_momentum | WLFI | momentum perdido | -0.20% | -0.70% | -0.16 |
| 2026-10-01 04:00 | ruptura_estricta | XMR | timeout | -0.02% | -0.52% | -0.12 |
| 2026-10-01 04:00 | pullback_tendencia | KAS | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 03:55 | macd_momentum_evento | XDC | stop-loss | -1.85% | -2.35% | -0.53 |
| 2026-10-01 03:55 | c_banda_atr_evento | TRX | timeout | +0.31% | -0.19% | -0.04 |
| 2026-10-01 03:55 | macd_momentum_regimen | XDC | stop-loss | -1.85% | -2.35% | -0.53 |
| 2026-10-01 03:55 | macd_sin_salida | XDC | stop-loss | -1.85% | -2.35% | -0.53 |

## Eventos de la última vuelta

- 2026-10-01 04:10 [ruptura_volumen] CIERRE ETH timeout bruto +0.12% neto -0.38%
- 2026-10-01 04:10 [ruptura_volumen_evento] CIERRE ETH timeout bruto +0.12% neto -0.38%
- 2026-10-01 04:05 [ruptura_volumen] ENTRADA ARB @ 0.1817 (22.26 €, apertura)
- 2026-10-01 04:05 [ruptura_estricta] ENTRADA ARB @ 0.1817 (22.50 €, apertura)
- 2026-10-01 04:05 [ruptura_volumen_regimen] ENTRADA ARB @ 0.1817 (22.28 €, apertura)
- 2026-10-01 04:05 [ruptura_volumen_evento] ENTRADA ARB @ 0.1817 (22.58 €, apertura)
- 2026-10-01 04:05 [macd_momentum] ENTRADA ICP @ 2.997 (22.37 €, apertura)
- 2026-10-01 04:05 [macd_momentum_regimen] ENTRADA ICP @ 2.997 (22.60 €, apertura)
- 2026-10-01 04:05 [macd_momentum_evento] ENTRADA ICP @ 2.997 (22.49 €, apertura)
- 2026-10-01 04:05 [ruptura_volumen] ENTRADA FET @ 0.2064 (22.26 €, apertura)
- 2026-10-01 04:05 [ruptura_volumen_regimen] ENTRADA FET @ 0.2064 (22.28 €, apertura)
- 2026-10-01 04:05 [ruptura_volumen_evento] ENTRADA FET @ 0.2064 (22.58 €, apertura)
- 2026-10-01 04:10 [macd_momentum] CIERRE WLD momentum perdido bruto -0.71% neto -1.21%
- 2026-10-01 04:10 [macd_momentum_regimen] CIERRE WLD momentum perdido bruto -0.71% neto -1.21%
- 2026-10-01 04:10 [macd_momentum_evento] CIERRE WLD momentum perdido bruto -0.71% neto -1.21%
- 2026-10-01 04:05 [ruptura_estricta] ENTRADA USELESS @ 0.21052 (22.50 €, apertura)
- 2026-10-01 04:05 [c_banda_atr] ENTRADA ASTER @ 0.66481 (22.58 €, apertura)
- 2026-10-01 04:05 [c_banda_atr_regimen] ENTRADA ASTER @ 0.66481 (22.71 €, apertura)
- 2026-10-01 04:05 [c_banda_atr_evento] ENTRADA ASTER @ 0.66481 (22.73 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
