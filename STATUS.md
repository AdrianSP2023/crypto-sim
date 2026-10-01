# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 01:46 UTC · vueltas 92 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 901.94 € (-2.41%) | 93 | 26 | 27% | -0.278% | -1.058% | -1.185% | -22.57 € |
| reversion_bb | 921.41 € (-0.31%) | 13 | 3 | 38% | +0.127% | -0.973% | -1.092% | -2.92 € |
| ruptura_volumen | 892.17 € (-3.47%) | 124 | 17 | 16% | -0.418% | -1.129% | -1.242% | -31.96 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 903.86 € (-2.21%) | 78 | 5 | 17% | -0.317% | -1.156% | -1.281% | -20.66 € |
| macd_momentum | 900.86 € (-2.53%) | 149 | 24 | 23% | -0.050% | -0.725% | -0.839% | -24.72 € |
| estocastico_rebote | 902.93 € (-2.31%) | 138 | 15 | 37% | +0.021% | -0.668% | -0.791% | -21.23 € |
| ruptura_estricta | 897.64 € (-2.88%) | 59 | 16 | 15% | -0.964% | -1.911% | -2.052% | -25.94 € |
| macd_sin_salida | 901.88 € (-2.42%) | 116 | 17 | 34% | -0.113% | -0.838% | -0.954% | -22.32 € |
| c_banda_atr_tope | 917.91 € (-0.69%) | 22 | 5 | 27% | -0.148% | -1.248% | -1.380% | -6.33 € |
| ruptura_volumen_tope | 915.28 € (-0.97%) | 33 | 5 | 18% | -0.115% | -1.215% | -1.296% | -9.23 € |
| c_banda_atr_regimen | 906.76 € (-1.89%) | 48 | 13 | 23% | -0.511% | -1.555% | -1.710% | -17.17 € |
| macd_momentum_regimen | 907.26 € (-1.84%) | 82 | 12 | 23% | -0.078% | -0.896% | -1.020% | -16.90 € |
| ruptura_volumen_regimen | 892.93 € (-3.39%) | 101 | 13 | 14% | -0.556% | -1.314% | -1.435% | -30.34 € |
| c_banda_atr_evento | 908.22 € (-1.73%) | 60 | 26 | 25% | -0.260% | -1.180% | -1.289% | -16.29 € |
| macd_momentum_evento | 905.85 € (-1.99%) | 102 | 24 | 18% | -0.087% | -0.845% | -0.948% | -19.74 € |
| ruptura_volumen_evento | 904.86 € (-2.10%) | 74 | 17 | 14% | -0.277% | -1.134% | -1.223% | -19.26 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 01:45 | macd_momentum_evento | APT | momentum perdido | +0.82% | +0.32% | +0.07 |
| 2026-10-01 01:45 | macd_momentum_evento | SEI | momentum perdido | -0.98% | -1.48% | -0.34 |
| 2026-10-01 01:45 | macd_momentum_evento | TRUMP | momentum perdido | -0.06% | -0.56% | -0.13 |
| 2026-10-01 01:45 | macd_momentum_regimen | TRUMP | momentum perdido | -0.33% | -0.83% | -0.19 |
| 2026-10-01 01:45 | macd_sin_salida | KSM | timeout | -0.44% | -0.94% | -0.21 |
| 2026-10-01 01:45 | ruptura_estricta | SUI | timeout | +0.45% | -0.05% | -0.01 |
| 2026-10-01 01:45 | macd_momentum | APT | momentum perdido | +0.82% | +0.32% | +0.07 |
| 2026-10-01 01:45 | macd_momentum | SEI | momentum perdido | -0.98% | -1.48% | -0.33 |
| 2026-10-01 01:45 | macd_momentum | TRUMP | momentum perdido | -0.06% | -0.56% | -0.12 |
| 2026-10-01 01:40 | ruptura_volumen_evento | OP | stop-loss | -1.30% | -1.80% | -0.41 |
| 2026-10-01 01:40 | ruptura_volumen_evento | NIGHT | stop-loss | -1.48% | -1.98% | -0.45 |
| 2026-10-01 01:40 | macd_momentum_evento | KSM | momentum perdido | -1.09% | -1.59% | -0.36 |
| 2026-10-01 01:40 | macd_momentum_evento | OP | momentum perdido | -0.87% | -1.37% | -0.31 |
| 2026-10-01 01:40 | macd_momentum_evento | LTC | momentum perdido | -0.30% | -0.80% | -0.18 |
| 2026-10-01 01:40 | c_banda_atr_evento | DASH | stop-loss | -1.50% | -2.00% | -0.46 |

## Eventos de la última vuelta

- 2026-10-01 01:40 [pullback_tendencia] ENTRADA ETH @ 2371.95 (22.59 €, apertura)
- 2026-10-01 01:45 [ruptura_estricta] CIERRE SUI timeout bruto +0.45% neto -0.05%
- 2026-10-01 01:45 [macd_sin_salida] CIERRE KSM timeout bruto -0.44% neto -0.94%
- 2026-10-01 01:45 [macd_momentum] CIERRE TRUMP momentum perdido bruto -0.05% neto -0.55%
- 2026-10-01 01:45 [macd_momentum_regimen] CIERRE TRUMP momentum perdido bruto -0.33% neto -0.83%
- 2026-10-01 01:45 [macd_momentum_evento] CIERRE TRUMP momentum perdido bruto -0.05% neto -0.55%
- 2026-10-01 01:45 [macd_momentum] CIERRE SEI momentum perdido bruto -0.98% neto -1.48%
- 2026-10-01 01:45 [macd_momentum_evento] CIERRE SEI momentum perdido bruto -0.98% neto -1.48%
- 2026-10-01 01:45 [macd_momentum] CIERRE APT momentum perdido bruto +0.82% neto +0.32%
- 2026-10-01 01:45 [macd_momentum_evento] CIERRE APT momentum perdido bruto +0.82% neto +0.32%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
