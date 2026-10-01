# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 20:41 UTC · vueltas 309 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 889.70 € (-3.74%) | 246 | 25 | 35% | -0.033% | -0.639% | -0.762% | -35.80 € |
| reversion_bb | 917.17 € (-0.76%) | 49 | 2 | 51% | +0.367% | -0.665% | -0.762% | -7.52 € |
| ruptura_volumen | 873.03 € (-5.54%) | 290 | 4 | 25% | -0.193% | -0.783% | -0.890% | -51.19 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 889.99 € (-3.71%) | 178 | 6 | 15% | -0.200% | -0.848% | -0.940% | -34.29 € |
| macd_momentum | 869.41 € (-5.93%) | 444 | 34 | 22% | +0.012% | -0.547% | -0.651% | -54.58 € |
| estocastico_rebote | 877.71 € (-5.03%) | 296 | 24 | 32% | -0.106% | -0.695% | -0.806% | -46.53 € |
| ruptura_estricta | 883.73 € (-4.38%) | 159 | 7 | 25% | -0.438% | -1.104% | -1.219% | -39.96 € |
| macd_sin_salida | 879.98 € (-4.79%) | 314 | 31 | 37% | -0.021% | -0.604% | -0.718% | -43.12 € |
| c_banda_atr_tope | 911.94 € (-1.33%) | 57 | 5 | 30% | +0.019% | -0.944% | -1.059% | -12.37 € |
| ruptura_volumen_tope | 907.53 € (-1.81%) | 95 | 5 | 28% | +0.008% | -0.770% | -0.884% | -16.78 € |
| c_banda_atr_regimen | 900.42 € (-2.58%) | 119 | 19 | 33% | -0.145% | -0.864% | -1.002% | -23.58 € |
| macd_momentum_regimen | 890.44 € (-3.66%) | 242 | 33 | 21% | -0.000% | -0.608% | -0.717% | -33.48 € |
| ruptura_volumen_regimen | 875.79 € (-5.24%) | 224 | 3 | 20% | -0.339% | -0.955% | -1.070% | -48.36 € |
| c_banda_atr_evento | 895.62 € (-3.10%) | 213 | 25 | 36% | +0.010% | -0.614% | -0.732% | -29.88 € |
| macd_momentum_evento | 874.23 € (-5.41%) | 397 | 34 | 20% | +0.010% | -0.557% | -0.656% | -49.77 € |
| ruptura_volumen_evento | 885.45 € (-4.20%) | 240 | 4 | 26% | -0.102% | -0.712% | -0.811% | -38.75 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 20:40 | ruptura_volumen_evento | LINK | timeout | -0.20% | -0.70% | -0.16 |
| 2026-10-01 20:40 | macd_momentum_evento | ETH | momentum perdido | -0.17% | -0.67% | -0.15 |
| 2026-10-01 20:40 | c_banda_atr_evento | KSM | timeout | -0.66% | -1.16% | -0.26 |
| 2026-10-01 20:40 | ruptura_volumen_regimen | LINK | timeout | -0.20% | -0.70% | -0.15 |
| 2026-10-01 20:40 | macd_momentum_regimen | ETH | momentum perdido | -0.17% | -0.67% | -0.15 |
| 2026-10-01 20:40 | ruptura_estricta | PENGU | timeout | -0.11% | -0.61% | -0.13 |
| 2026-10-01 20:40 | ruptura_estricta | FIL | timeout | -0.88% | -1.38% | -0.30 |
| 2026-10-01 20:40 | macd_momentum | ETH | momentum perdido | -0.17% | -0.67% | -0.15 |
| 2026-10-01 20:40 | pullback_tendencia | ETH | rotura de tendencia | -0.13% | -0.63% | -0.14 |
| 2026-10-01 20:40 | ruptura_volumen | LINK | timeout | -0.20% | -0.70% | -0.15 |
| 2026-10-01 20:40 | c_banda_atr | KSM | timeout | -0.66% | -1.16% | -0.26 |
| 2026-10-01 20:35 | ruptura_volumen_evento | MINA | timeout | +0.97% | +0.47% | +0.10 |
| 2026-10-01 20:35 | macd_momentum_evento | KAS | momentum perdido | -1.04% | -1.54% | -0.34 |
| 2026-10-01 20:35 | macd_momentum_evento | ZRO | momentum perdido | +0.67% | +0.17% | +0.04 |
| 2026-10-01 20:35 | c_banda_atr_evento | CRV | timeout | +0.34% | -0.16% | -0.04 |

## Eventos de la última vuelta

- 2026-10-01 20:35 [pullback_tendencia] ENTRADA XRP @ 1.33435 (22.25 €, apertura)
- 2026-10-01 20:40 [pullback_tendencia] CIERRE ETH rotura de tendencia bruto -0.13% neto -0.63%
- 2026-10-01 20:40 [macd_momentum] CIERRE ETH momentum perdido bruto -0.17% neto -0.67%
- 2026-10-01 20:40 [macd_momentum_regimen] CIERRE ETH momentum perdido bruto -0.17% neto -0.67%
- 2026-10-01 20:40 [macd_momentum_evento] CIERRE ETH momentum perdido bruto -0.17% neto -0.67%
- 2026-10-01 20:40 [ruptura_volumen] CIERRE LINK timeout bruto -0.20% neto -0.70%
- 2026-10-01 20:40 [ruptura_volumen_regimen] CIERRE LINK timeout bruto -0.20% neto -0.70%
- 2026-10-01 20:40 [ruptura_volumen_evento] CIERRE LINK timeout bruto -0.20% neto -0.70%
- 2026-10-01 20:35 [ruptura_volumen] ENTRADA LTC @ 60.88 (21.83 €, apertura)
- 2026-10-01 20:35 [ruptura_volumen_tope] ENTRADA LTC @ 60.88 (22.69 €, apertura)
- 2026-10-01 20:35 [ruptura_volumen_regimen] ENTRADA LTC @ 60.88 (21.90 €, apertura)
- 2026-10-01 20:35 [ruptura_volumen_evento] ENTRADA LTC @ 60.88 (22.14 €, apertura)
- 2026-10-01 20:35 [macd_momentum] ENTRADA FET @ 0.2044 (21.74 €, apertura)
- 2026-10-01 20:35 [macd_sin_salida] ENTRADA FET @ 0.2044 (22.03 €, apertura)
- 2026-10-01 20:35 [c_banda_atr_tope] ENTRADA FET @ 0.2044 (22.80 €, apertura)
- 2026-10-01 20:35 [macd_momentum_regimen] ENTRADA FET @ 0.2044 (22.27 €, apertura)
- 2026-10-01 20:35 [macd_momentum_evento] ENTRADA FET @ 0.2044 (21.86 €, apertura)
- 2026-10-01 20:40 [ruptura_estricta] CIERRE FIL timeout bruto -0.88% neto -1.38%
- 2026-10-01 20:40 [ruptura_estricta] CIERRE PENGU timeout bruto -0.11% neto -0.61%
- 2026-10-01 20:40 [c_banda_atr] CIERRE KSM timeout bruto -0.66% neto -1.16%
- 2026-10-01 20:40 [c_banda_atr_evento] CIERRE KSM timeout bruto -0.66% neto -1.16%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
