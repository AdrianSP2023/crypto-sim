# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 13:46 UTC · vueltas 414 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 889.46 € (-3.76%) | 375 | 27 | 40% | +0.143% | -0.427% | -0.548% | -36.43 € |
| reversion_bb | 920.38 € (-0.42%) | 74 | 2 | 62% | +0.594% | -0.259% | -0.363% | -4.43 € |
| ruptura_volumen | 859.23 € (-7.03%) | 472 | 23 | 27% | -0.077% | -0.633% | -0.743% | -66.71 € |
| rebote_extremo | 922.62 € (-0.17%) | 16 | 0 | 62% | +0.663% | -0.437% | -0.608% | -1.62 € |
| pullback_tendencia | 885.94 € (-4.14%) | 279 | 14 | 20% | -0.023% | -0.617% | -0.703% | -39.04 € |
| macd_momentum | 846.67 € (-8.39%) | 769 | 32 | 24% | +0.068% | -0.466% | -0.565% | -79.31 € |
| estocastico_rebote | 877.41 € (-5.07%) | 473 | 18 | 37% | +0.114% | -0.441% | -0.547% | -47.27 € |
| ruptura_estricta | 881.85 € (-4.59%) | 258 | 16 | 32% | -0.132% | -0.734% | -0.849% | -43.05 € |
| macd_sin_salida | 877.18 € (-5.09%) | 505 | 30 | 40% | +0.127% | -0.425% | -0.534% | -48.65 € |
| c_banda_atr_tope | 913.76 € (-1.13%) | 84 | 5 | 38% | +0.258% | -0.556% | -0.676% | -10.75 € |
| ruptura_volumen_tope | 899.72 € (-2.65%) | 142 | 5 | 23% | -0.095% | -0.780% | -0.894% | -25.29 € |
| c_banda_atr_regimen | 901.99 € (-2.41%) | 227 | 27 | 41% | +0.159% | -0.456% | -0.585% | -23.78 € |
| macd_momentum_regimen | 869.34 € (-5.94%) | 532 | 32 | 24% | +0.074% | -0.475% | -0.575% | -56.67 € |
| ruptura_volumen_regimen | 863.89 € (-6.53%) | 395 | 23 | 25% | -0.135% | -0.701% | -0.816% | -62.06 € |
| c_banda_atr_evento | 894.47 € (-3.22%) | 338 | 5 | 41% | +0.186% | -0.392% | -0.508% | -30.30 € |
| macd_momentum_evento | 851.60 € (-7.86%) | 699 | 1 | 23% | +0.069% | -0.468% | -0.564% | -72.78 € |
| ruptura_volumen_evento | 867.02 € (-6.19%) | 414 | 0 | 26% | -0.052% | -0.616% | -0.719% | -57.21 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 13:45 | ruptura_volumen_regimen | WLD | take-profit | +2.50% | +2.00% | +0.43 |
| 2026-10-02 13:45 | c_banda_atr_regimen | QNT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-02 13:45 | estocastico_rebote | ASTER | timeout | -0.20% | -0.69% | -0.15 |
| 2026-10-02 13:45 | ruptura_volumen | WLD | take-profit | +2.50% | +2.00% | +0.43 |
| 2026-10-02 13:45 | c_banda_atr | QNT | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-02 13:40 | ruptura_volumen_evento | JUP | timeout | +1.07% | +0.57% | +0.12 |
| 2026-10-02 13:40 | ruptura_volumen_regimen | JUP | timeout | +1.07% | +0.57% | +0.12 |
| 2026-10-02 13:40 | macd_sin_salida | SEI | timeout | -0.65% | -1.15% | -0.24 |
| 2026-10-02 13:40 | macd_sin_salida | ALGO | timeout | +0.46% | -0.04% | -0.01 |
| 2026-10-02 13:40 | macd_sin_salida | LINK | timeout | -0.13% | -0.63% | -0.14 |
| 2026-10-02 13:40 | estocastico_rebote | FIL | take-profit | +1.85% | +1.35% | +0.30 |
| 2026-10-02 13:40 | ruptura_volumen | JUP | timeout | +1.07% | +0.57% | +0.12 |
| 2026-10-02 13:35 | ruptura_volumen_regimen | APT | take-profit | +2.50% | +2.00% | +0.43 |
| 2026-10-02 13:35 | ruptura_volumen_regimen | ZRO | take-profit | +2.68% | +2.18% | +0.47 |
| 2026-10-02 13:35 | macd_momentum_regimen | SEI | momentum perdido | -0.51% | -1.01% | -0.22 |

## Eventos de la última vuelta

- 2026-10-02 13:40 [macd_momentum] ENTRADA BTC @ 77416.5 (21.12 €, apertura)
- 2026-10-02 13:40 [macd_momentum_regimen] ENTRADA BTC @ 77416.5 (21.69 €, apertura)
- 2026-10-02 13:40 [macd_momentum] ENTRADA XRP @ 1.37632 (21.12 €, apertura)
- 2026-10-02 13:40 [macd_sin_salida] ENTRADA XRP @ 1.37632 (21.89 €, apertura)
- 2026-10-02 13:40 [macd_momentum_regimen] ENTRADA XRP @ 1.37632 (21.69 €, apertura)
- 2026-10-02 13:40 [c_banda_atr] ENTRADA QNT @ 222.49 (22.21 €, apertura)
- 2026-10-02 13:45 [c_banda_atr] CIERRE QNT stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 13:40 [c_banda_atr_regimen] ENTRADA QNT @ 222.49 (22.52 €, apertura)
- 2026-10-02 13:45 [c_banda_atr_regimen] CIERRE QNT stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 13:40 [macd_momentum] ENTRADA LINK @ 12.8538 (21.12 €, apertura)
- 2026-10-02 13:40 [macd_momentum_regimen] ENTRADA LINK @ 12.8538 (21.69 €, apertura)
- 2026-10-02 13:40 [ruptura_volumen] ENTRADA ZEC @ 1246.64 (21.43 €, apertura)
- 2026-10-02 13:40 [ruptura_volumen_regimen] ENTRADA ZEC @ 1246.64 (21.54 €, apertura)
- 2026-10-02 13:40 [macd_momentum] ENTRADA ENA @ 0.2197 (21.12 €, apertura)
- 2026-10-02 13:40 [macd_momentum_regimen] ENTRADA ENA @ 0.2197 (21.69 €, apertura)
- 2026-10-02 13:40 [ruptura_volumen] ENTRADA FET @ 0.208 (21.43 €, apertura)
- 2026-10-02 13:40 [ruptura_volumen_regimen] ENTRADA FET @ 0.208 (21.54 €, apertura)
- 2026-10-02 13:40 [macd_momentum] ENTRADA TRX @ 0.297893 (21.12 €, apertura)
- 2026-10-02 13:40 [macd_sin_salida] ENTRADA TRX @ 0.297893 (21.89 €, apertura)
- 2026-10-02 13:40 [macd_momentum_regimen] ENTRADA TRX @ 0.297893 (21.69 €, apertura)
- 2026-10-02 13:45 [ruptura_volumen] CIERRE WLD take-profit bruto +2.50% neto +2.00%
- 2026-10-02 13:45 [ruptura_volumen_regimen] CIERRE WLD take-profit bruto +2.50% neto +2.00%
- 2026-10-02 13:40 [ruptura_volumen] ENTRADA RENDER @ 1.777 (21.44 €, apertura)
- 2026-10-02 13:40 [ruptura_estricta] ENTRADA RENDER @ 1.777 (22.03 €, apertura)
- 2026-10-02 13:40 [ruptura_volumen_regimen] ENTRADA RENDER @ 1.777 (21.55 €, apertura)
- 2026-10-02 13:40 [ruptura_volumen] ENTRADA INJ @ 6.725 (21.44 €, apertura)
- 2026-10-02 13:40 [ruptura_volumen_regimen] ENTRADA INJ @ 6.725 (21.55 €, apertura)
- 2026-10-02 13:45 [estocastico_rebote] CIERRE ASTER timeout bruto -0.19% neto -0.69%
- 2026-10-02 13:40 [ruptura_volumen] ENTRADA WLFI @ 0.0502 (21.44 €, apertura)
- 2026-10-02 13:40 [ruptura_volumen_regimen] ENTRADA WLFI @ 0.0502 (21.55 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
