# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 13:36 UTC · vueltas 412 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 890.31 € (-3.67%) | 374 | 21 | 40% | +0.147% | -0.422% | -0.544% | -35.99 € |
| reversion_bb | 920.17 € (-0.44%) | 74 | 2 | 62% | +0.594% | -0.259% | -0.363% | -4.43 € |
| ruptura_volumen | 859.04 € (-7.05%) | 470 | 18 | 26% | -0.085% | -0.641% | -0.750% | -67.26 € |
| rebote_extremo | 922.62 € (-0.17%) | 16 | 0 | 62% | +0.663% | -0.437% | -0.608% | -1.62 € |
| pullback_tendencia | 885.90 € (-4.15%) | 279 | 12 | 20% | -0.023% | -0.617% | -0.703% | -39.04 € |
| macd_momentum | 847.29 € (-8.33%) | 769 | 24 | 24% | +0.068% | -0.466% | -0.565% | -79.31 € |
| estocastico_rebote | 878.52 € (-4.95%) | 471 | 17 | 37% | +0.111% | -0.445% | -0.551% | -47.41 € |
| ruptura_estricta | 881.97 € (-4.57%) | 258 | 14 | 32% | -0.132% | -0.734% | -0.849% | -43.05 € |
| macd_sin_salida | 878.14 € (-4.99%) | 502 | 28 | 40% | +0.129% | -0.423% | -0.533% | -48.26 € |
| c_banda_atr_tope | 913.74 € (-1.14%) | 84 | 5 | 38% | +0.258% | -0.556% | -0.676% | -10.75 € |
| ruptura_volumen_tope | 899.52 € (-2.68%) | 142 | 5 | 23% | -0.095% | -0.780% | -0.894% | -25.29 € |
| c_banda_atr_regimen | 902.86 € (-2.31%) | 226 | 21 | 42% | +0.167% | -0.449% | -0.579% | -23.33 € |
| macd_momentum_regimen | 869.98 € (-5.87%) | 532 | 24 | 24% | +0.074% | -0.475% | -0.575% | -56.67 € |
| ruptura_volumen_regimen | 863.70 € (-6.55%) | 393 | 18 | 24% | -0.145% | -0.711% | -0.826% | -62.62 € |
| c_banda_atr_evento | 894.64 € (-3.20%) | 338 | 5 | 41% | +0.186% | -0.392% | -0.508% | -30.30 € |
| macd_momentum_evento | 851.56 € (-7.86%) | 699 | 1 | 23% | +0.069% | -0.468% | -0.564% | -72.78 € |
| ruptura_volumen_evento | 867.13 € (-6.18%) | 413 | 1 | 26% | -0.055% | -0.619% | -0.722% | -57.34 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 13:35 | ruptura_volumen_regimen | APT | take-profit | +2.50% | +2.00% | +0.43 |
| 2026-10-02 13:35 | ruptura_volumen_regimen | ZRO | take-profit | +2.68% | +2.18% | +0.47 |
| 2026-10-02 13:35 | macd_momentum_regimen | SEI | momentum perdido | -0.51% | -1.01% | -0.22 |
| 2026-10-02 13:35 | macd_momentum_regimen | SUI | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 13:35 | macd_sin_salida | SUI | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 13:35 | ruptura_estricta | ONDO | timeout | +0.18% | -0.32% | -0.07 |
| 2026-10-02 13:35 | estocastico_rebote | ARB | timeout | +0.99% | +0.49% | +0.11 |
| 2026-10-02 13:35 | estocastico_rebote | TAO | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-10-02 13:35 | macd_momentum | SEI | momentum perdido | -0.51% | -1.01% | -0.21 |
| 2026-10-02 13:35 | macd_momentum | SUI | take-profit | +2.00% | +1.50% | +0.32 |
| 2026-10-02 13:35 | ruptura_volumen | APT | take-profit | +2.50% | +2.00% | +0.43 |
| 2026-10-02 13:35 | ruptura_volumen | ZRO | take-profit | +2.68% | +2.18% | +0.47 |
| 2026-10-02 13:30 | c_banda_atr_evento | TON | timeout | +0.43% | -0.07% | -0.01 |
| 2026-10-02 13:30 | macd_momentum_regimen | ZRO | take-profit | +2.34% | +1.84% | +0.40 |
| 2026-10-02 13:30 | macd_momentum_regimen | ADA | momentum perdido | -0.34% | -0.84% | -0.18 |

## Eventos de la última vuelta

- 2026-10-02 13:35 [macd_momentum] CIERRE SUI take-profit bruto +2.00% neto +1.50%
- 2026-10-02 13:35 [macd_sin_salida] CIERRE SUI take-profit bruto +2.00% neto +1.50%
- 2026-10-02 13:35 [macd_momentum_regimen] CIERRE SUI take-profit bruto +2.00% neto +1.50%
- 2026-10-02 13:35 [estocastico_rebote] CIERRE TAO take-profit bruto +1.80% neto +1.30%
- 2026-10-02 13:35 [ruptura_volumen] CIERRE ZRO take-profit bruto +2.68% neto +2.18%
- 2026-10-02 13:35 [ruptura_volumen_regimen] CIERRE ZRO take-profit bruto +2.68% neto +2.18%
- 2026-10-02 13:30 [pullback_tendencia] ENTRADA DOT @ 1.0878 (22.13 €, apertura)
- 2026-10-02 13:35 [estocastico_rebote] CIERRE ARB timeout bruto +0.99% neto +0.49%
- 2026-10-02 13:30 [pullback_tendencia] ENTRADA ALGO @ 0.11633 (22.13 €, apertura)
- 2026-10-02 13:30 [macd_momentum] ENTRADA ALGO @ 0.11633 (21.13 €, apertura)
- 2026-10-02 13:30 [macd_momentum_regimen] ENTRADA ALGO @ 0.11633 (21.69 €, apertura)
- 2026-10-02 13:35 [ruptura_estricta] CIERRE ONDO timeout bruto +0.18% neto -0.32%
- 2026-10-02 13:30 [ruptura_volumen] ENTRADA MON @ 0.03142 (21.41 €, apertura)
- 2026-10-02 13:30 [ruptura_volumen_regimen] ENTRADA MON @ 0.03142 (21.53 €, apertura)
- 2026-10-02 13:35 [macd_momentum] CIERRE SEI momentum perdido bruto -0.51% neto -1.01%
- 2026-10-02 13:35 [macd_momentum_regimen] CIERRE SEI momentum perdido bruto -0.51% neto -1.01%
- 2026-10-02 13:35 [ruptura_volumen] CIERRE APT take-profit bruto +2.50% neto +2.00%
- 2026-10-02 13:35 [ruptura_volumen_regimen] CIERRE APT take-profit bruto +2.50% neto +2.00%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
