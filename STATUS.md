# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 03:26 UTC · vueltas 112 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 903.60 € (-2.23%) | 105 | 27 | 29% | -0.196% | -0.944% | -1.067% | -22.74 € |
| reversion_bb | 921.39 € (-0.31%) | 13 | 5 | 38% | +0.127% | -0.973% | -1.092% | -2.92 € |
| ruptura_volumen | 890.42 € (-3.66%) | 143 | 13 | 19% | -0.357% | -1.040% | -1.153% | -33.89 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 903.05 € (-2.29%) | 85 | 4 | 15% | -0.312% | -1.123% | -1.240% | -21.85 € |
| macd_momentum | 896.64 € (-2.99%) | 187 | 24 | 20% | -0.042% | -0.682% | -0.790% | -29.07 € |
| estocastico_rebote | 902.89 € (-2.31%) | 153 | 16 | 38% | +0.064% | -0.607% | -0.728% | -21.37 € |
| ruptura_estricta | 899.94 € (-2.63%) | 64 | 20 | 19% | -0.790% | -1.702% | -1.842% | -25.08 € |
| macd_sin_salida | 904.04 € (-2.19%) | 123 | 38 | 36% | -0.043% | -0.755% | -0.872% | -21.35 € |
| c_banda_atr_tope | 917.99 € (-0.68%) | 25 | 5 | 24% | -0.111% | -1.211% | -1.337% | -6.98 € |
| ruptura_volumen_tope | 914.13 € (-1.09%) | 41 | 5 | 22% | +0.040% | -1.060% | -1.161% | -10.00 € |
| c_banda_atr_regimen | 908.40 € (-1.71%) | 55 | 20 | 25% | -0.370% | -1.345% | -1.492% | -17.02 € |
| macd_momentum_regimen | 905.47 € (-2.03%) | 101 | 24 | 20% | -0.104% | -0.863% | -0.980% | -19.99 € |
| ruptura_volumen_regimen | 891.49 € (-3.54%) | 114 | 15 | 13% | -0.529% | -1.258% | -1.377% | -32.73 € |
| c_banda_atr_evento | 909.61 € (-1.58%) | 72 | 27 | 28% | -0.144% | -1.011% | -1.116% | -16.73 € |
| macd_momentum_evento | 901.61 € (-2.45%) | 140 | 24 | 15% | -0.066% | -0.754% | -0.853% | -24.12 € |
| ruptura_volumen_evento | 903.09 € (-2.29%) | 93 | 13 | 18% | -0.212% | -0.996% | -1.090% | -21.22 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 03:25 | c_banda_atr_evento | DOGE | timeout | +0.44% | -0.06% | -0.01 |
| 2026-10-01 03:25 | ruptura_volumen_regimen | RENDER | timeout | +0.06% | -0.44% | -0.10 |
| 2026-10-01 03:25 | c_banda_atr_regimen | SHIB | timeout | +0.18% | -0.32% | -0.07 |
| 2026-10-01 03:25 | c_banda_atr_regimen | DOGE | timeout | +0.44% | -0.06% | -0.01 |
| 2026-10-01 03:25 | ruptura_estricta | MINA | timeout | +0.62% | +0.12% | +0.03 |
| 2026-10-01 03:25 | pullback_tendencia | SUI | rotura de tendencia | -0.62% | -1.12% | -0.25 |
| 2026-10-01 03:25 | pullback_tendencia | ETH | rotura de tendencia | -0.02% | -0.52% | -0.12 |
| 2026-10-01 03:25 | c_banda_atr | DOGE | timeout | +0.44% | -0.06% | -0.01 |
| 2026-10-01 03:20 | ruptura_volumen_evento | DOGE | timeout | +0.01% | -0.49% | -0.11 |
| 2026-10-01 03:20 | ruptura_volumen_evento | ADA | timeout | +0.17% | -0.33% | -0.07 |
| 2026-10-01 03:20 | ruptura_volumen_evento | XRP | timeout | +0.02% | -0.48% | -0.11 |
| 2026-10-01 03:20 | macd_momentum_evento | MINA | momentum perdido | +0.23% | -0.27% | -0.06 |
| 2026-10-01 03:20 | macd_momentum_evento | ICP | momentum perdido | -0.13% | -0.63% | -0.14 |
| 2026-10-01 03:20 | macd_momentum_evento | SUI | momentum perdido | -0.64% | -1.14% | -0.26 |
| 2026-10-01 03:20 | ruptura_volumen_regimen | DOGE | timeout | +0.01% | -0.49% | -0.11 |

## Eventos de la última vuelta

- 2026-10-01 03:25 [pullback_tendencia] CIERRE ETH rotura de tendencia bruto -0.02% neto -0.52%
- 2026-10-01 03:20 [pullback_tendencia] ENTRADA QNT @ 262.7 (22.57 €, apertura)
- 2026-10-01 03:25 [pullback_tendencia] CIERRE SUI rotura de tendencia bruto -0.62% neto -1.12%
- 2026-10-01 03:25 [c_banda_atr] CIERRE DOGE timeout bruto +0.44% neto -0.06%
- 2026-10-01 03:25 [c_banda_atr_regimen] CIERRE DOGE timeout bruto +0.44% neto -0.06%
- 2026-10-01 03:25 [c_banda_atr_evento] CIERRE DOGE timeout bruto +0.44% neto -0.06%
- 2026-10-01 03:20 [estocastico_rebote] ENTRADA TRX @ 0.298271 (22.57 €, apertura)
- 2026-10-01 03:25 [ruptura_volumen_regimen] CIERRE RENDER timeout bruto +0.06% neto -0.44%
- 2026-10-01 03:25 [ruptura_estricta] CIERRE MINA timeout bruto +0.62% neto +0.12%
- 2026-10-01 03:25 [c_banda_atr_regimen] CIERRE SHIB timeout bruto +0.18% neto -0.32%
- 2026-10-01 03:20 [c_banda_atr] ENTRADA KSM @ 4.57 (22.54 €, apertura)
- 2026-10-01 03:20 [macd_momentum] ENTRADA KSM @ 4.57 (22.38 €, apertura)
- 2026-10-01 03:20 [c_banda_atr_regimen] ENTRADA KSM @ 4.57 (22.68 €, apertura)
- 2026-10-01 03:20 [macd_momentum_regimen] ENTRADA KSM @ 4.57 (22.61 €, apertura)
- 2026-10-01 03:20 [c_banda_atr_evento] ENTRADA KSM @ 4.57 (22.69 €, apertura)
- 2026-10-01 03:20 [macd_momentum_evento] ENTRADA KSM @ 4.57 (22.50 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
