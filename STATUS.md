# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 23:36 UTC · vueltas 108 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 905.07 € (-2.07%) | 71 | 31 | 27% | -0.390% | -1.258% | -1.400% | -20.51 € |
| reversion_bb | 921.89 € (-0.25%) | 10 | 5 | 40% | -0.070% | -1.170% | -1.296% | -2.71 € |
| ruptura_volumen | 895.03 € (-3.16%) | 95 | 24 | 17% | -0.481% | -1.256% | -1.391% | -27.32 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 904.37 € (-2.15%) | 66 | 5 | 15% | -0.407% | -1.307% | -1.444% | -19.77 € |
| macd_momentum | 903.79 € (-2.21%) | 113 | 22 | 23% | -0.088% | -0.819% | -0.945% | -21.21 € |
| estocastico_rebote | 903.18 € (-2.28%) | 127 | 8 | 35% | -0.037% | -0.743% | -0.875% | -21.70 € |
| ruptura_estricta | 898.21 € (-2.82%) | 52 | 8 | 13% | -1.113% | -2.121% | -2.268% | -25.38 € |
| macd_sin_salida | 903.69 € (-2.22%) | 88 | 28 | 33% | -0.217% | -1.013% | -1.141% | -20.50 € |
| c_banda_atr_tope | 919.24 € (-0.54%) | 20 | 5 | 30% | -0.007% | -1.107% | -1.258% | -5.10 € |
| ruptura_volumen_tope | 915.93 € (-0.90%) | 27 | 5 | 19% | -0.185% | -1.285% | -1.398% | -8.00 € |
| c_banda_atr_regimen | 907.93 € (-1.76%) | 45 | 9 | 24% | -0.442% | -1.522% | -1.680% | -15.77 € |
| macd_momentum_regimen | 909.93 € (-1.55%) | 65 | 11 | 29% | -0.022% | -0.923% | -1.059% | -13.83 € |
| ruptura_volumen_regimen | 896.48 € (-3.00%) | 74 | 22 | 14% | -0.676% | -1.529% | -1.667% | -25.94 € |
| c_banda_atr_evento | 912.48 € (-1.27%) | 38 | 31 | 24% | -0.461% | -1.498% | -1.623% | -13.11 € |
| macd_momentum_evento | 908.87 € (-1.66%) | 66 | 22 | 15% | -0.171% | -1.066% | -1.184% | -16.14 € |
| ruptura_volumen_evento | 907.90 € (-1.77%) | 45 | 24 | 13% | -0.319% | -1.392% | -1.511% | -14.42 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 23:35 | macd_momentum_evento | WLD | momentum perdido | -1.05% | -1.55% | -0.35 |
| 2026-09-30 23:35 | macd_momentum_evento | SUI | momentum perdido | +0.44% | -0.06% | -0.01 |
| 2026-09-30 23:35 | macd_momentum_evento | ETH | momentum perdido | -0.04% | -0.54% | -0.12 |
| 2026-09-30 23:35 | macd_momentum_regimen | WLD | momentum perdido | -1.05% | -1.55% | -0.35 |
| 2026-09-30 23:35 | macd_momentum_regimen | ETH | momentum perdido | -0.14% | -0.64% | -0.15 |
| 2026-09-30 23:35 | ruptura_estricta | MON | take-profit | +3.00% | +2.50% | +0.56 |
| 2026-09-30 23:35 | macd_momentum | WLD | momentum perdido | -1.05% | -1.55% | -0.35 |
| 2026-09-30 23:35 | macd_momentum | SUI | momentum perdido | +0.44% | -0.06% | -0.01 |
| 2026-09-30 23:35 | macd_momentum | ETH | momentum perdido | -0.04% | -0.54% | -0.12 |
| 2026-09-30 23:30 | macd_momentum_evento | FET | momentum perdido | +0.00% | -0.50% | -0.11 |
| 2026-09-30 23:30 | macd_sin_salida | ALGO | timeout | -0.43% | -0.93% | -0.21 |
| 2026-09-30 23:30 | macd_momentum | FET | momentum perdido | +0.00% | -0.50% | -0.11 |
| 2026-09-30 23:25 | ruptura_volumen_evento | MON | take-profit | +2.50% | +2.00% | +0.46 |
| 2026-09-30 23:25 | macd_momentum_evento | MON | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 23:25 | c_banda_atr_evento | ASTER | timeout | +1.62% | +0.82% | +0.19 |

## Eventos de la última vuelta

- 2026-09-30 23:35 [macd_momentum] CIERRE ETH momentum perdido bruto -0.04% neto -0.54%
- 2026-09-30 23:35 [macd_momentum_regimen] CIERRE ETH momentum perdido bruto -0.14% neto -0.64%
- 2026-09-30 23:35 [macd_momentum_evento] CIERRE ETH momentum perdido bruto -0.04% neto -0.54%
- 2026-09-30 23:35 [macd_momentum] CIERRE SUI momentum perdido bruto +0.44% neto -0.06%
- 2026-09-30 23:35 [macd_momentum_evento] CIERRE SUI momentum perdido bruto +0.44% neto -0.06%
- 2026-09-30 23:35 [macd_momentum] CIERRE WLD momentum perdido bruto -1.05% neto -1.55%
- 2026-09-30 23:35 [macd_momentum_regimen] CIERRE WLD momentum perdido bruto -1.05% neto -1.55%
- 2026-09-30 23:35 [macd_momentum_evento] CIERRE WLD momentum perdido bruto -1.05% neto -1.55%
- 2026-09-30 23:35 [ruptura_estricta] CIERRE MON take-profit bruto +3.00% neto +2.50%
- 2026-09-30 23:30 [reversion_bb] ENTRADA TON @ 1.322 (23.04 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
