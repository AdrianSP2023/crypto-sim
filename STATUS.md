# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 08:11 UTC · vueltas 387 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 890.59 € (-3.64%) | 333 | 25 | 39% | +0.124% | -0.454% | -0.575% | -34.48 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 863.23 € (-6.60%) | 415 | 15 | 27% | -0.096% | -0.659% | -0.768% | -61.27 € |
| rebote_extremo | 922.42 € (-0.20%) | 15 | 0 | 60% | +0.574% | -0.526% | -0.706% | -1.82 € |
| pullback_tendencia | 889.80 € (-3.73%) | 237 | 8 | 20% | -0.036% | -0.647% | -0.733% | -34.84 € |
| macd_momentum | 854.64 € (-7.53%) | 646 | 36 | 22% | +0.049% | -0.491% | -0.593% | -70.66 € |
| estocastico_rebote | 881.52 € (-4.62%) | 388 | 39 | 36% | +0.048% | -0.519% | -0.628% | -45.67 € |
| ruptura_estricta | 882.42 € (-4.53%) | 233 | 6 | 32% | -0.174% | -0.787% | -0.903% | -41.73 € |
| macd_sin_salida | 881.12 € (-4.67%) | 432 | 40 | 40% | +0.113% | -0.447% | -0.558% | -44.02 € |
| c_banda_atr_tope | 913.40 € (-1.17%) | 76 | 5 | 37% | +0.213% | -0.634% | -0.750% | -11.08 € |
| ruptura_volumen_tope | 901.47 € (-2.46%) | 127 | 5 | 24% | -0.087% | -0.795% | -0.908% | -23.06 € |
| c_banda_atr_regimen | 903.14 € (-2.28%) | 185 | 25 | 40% | +0.131% | -0.510% | -0.640% | -21.73 € |
| macd_momentum_regimen | 877.52 € (-5.05%) | 409 | 36 | 22% | +0.046% | -0.518% | -0.621% | -47.78 € |
| ruptura_volumen_regimen | 867.91 € (-6.09%) | 338 | 15 | 25% | -0.168% | -0.745% | -0.859% | -56.58 € |
| c_banda_atr_evento | 896.51 € (-3.00%) | 300 | 25 | 40% | +0.172% | -0.416% | -0.533% | -28.56 € |
| macd_momentum_evento | 859.38 € (-7.02%) | 599 | 36 | 21% | +0.051% | -0.493% | -0.592% | -65.93 € |
| ruptura_volumen_evento | 875.51 € (-5.27%) | 365 | 15 | 28% | -0.023% | -0.595% | -0.699% | -48.98 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 08:10 | estocastico_rebote | VVV | take-profit | +1.93% | +1.43% | +0.31 |
| 2026-10-02 08:05 | ruptura_volumen_evento | ALGO | take-profit | +2.50% | +2.00% | +0.44 |
| 2026-10-02 08:05 | macd_momentum_evento | ALGO | take-profit | +2.00% | +1.50% | +0.32 |
| 2026-10-02 08:05 | ruptura_volumen_regimen | ALGO | take-profit | +2.50% | +2.00% | +0.43 |
| 2026-10-02 08:05 | macd_momentum_regimen | ALGO | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 08:05 | macd_momentum | ALGO | take-profit | +2.00% | +1.50% | +0.32 |
| 2026-10-02 08:05 | ruptura_volumen | ALGO | take-profit | +2.50% | +2.00% | +0.43 |
| 2026-10-02 08:00 | ruptura_volumen_evento | NIGHT | take-profit | +4.16% | +3.66% | +0.80 |
| 2026-10-02 08:00 | ruptura_volumen_regimen | NIGHT | take-profit | +4.16% | +3.66% | +0.79 |
| 2026-10-02 08:00 | ruptura_estricta | MINA | stop-loss | -2.00% | -2.50% | -0.55 |
| 2026-10-02 08:00 | ruptura_estricta | NIGHT | take-profit | +4.16% | +3.66% | +0.81 |
| 2026-10-02 08:00 | ruptura_volumen | NIGHT | take-profit | +4.16% | +3.66% | +0.79 |
| 2026-10-02 07:55 | ruptura_volumen_evento | VVV | timeout | +0.91% | +0.41% | +0.09 |
| 2026-10-02 07:55 | ruptura_volumen_evento | PUMP | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 07:55 | ruptura_volumen_regimen | VVV | timeout | +0.91% | +0.41% | +0.09 |

## Eventos de la última vuelta

- 2026-10-02 08:05 [ruptura_volumen] ENTRADA BTC @ 76581.9 (21.57 €, apertura)
- 2026-10-02 08:05 [ruptura_volumen_regimen] ENTRADA BTC @ 76581.9 (21.69 €, apertura)
- 2026-10-02 08:05 [ruptura_volumen_evento] ENTRADA BTC @ 76581.9 (21.88 €, apertura)
- 2026-10-02 08:05 [ruptura_volumen] ENTRADA XRP @ 1.36217 (21.57 €, apertura)
- 2026-10-02 08:05 [ruptura_volumen_regimen] ENTRADA XRP @ 1.36217 (21.69 €, apertura)
- 2026-10-02 08:05 [ruptura_volumen_evento] ENTRADA XRP @ 1.36217 (21.88 €, apertura)
- 2026-10-02 08:05 [c_banda_atr] ENTRADA HYPE @ 80.31 (22.24 €, apertura)
- 2026-10-02 08:05 [c_banda_atr_regimen] ENTRADA HYPE @ 80.31 (22.56 €, apertura)
- 2026-10-02 08:05 [c_banda_atr_evento] ENTRADA HYPE @ 80.31 (22.39 €, apertura)
- 2026-10-02 08:05 [ruptura_volumen] ENTRADA DOGE @ 0.0856423 (21.57 €, apertura)
- 2026-10-02 08:05 [ruptura_volumen_regimen] ENTRADA DOGE @ 0.0856423 (21.69 €, apertura)
- 2026-10-02 08:05 [ruptura_volumen_evento] ENTRADA DOGE @ 0.0856423 (21.88 €, apertura)
- 2026-10-02 08:05 [macd_momentum] ENTRADA ARB @ 0.1821 (21.34 €, apertura)
- 2026-10-02 08:05 [macd_sin_salida] ENTRADA ARB @ 0.1821 (22.01 €, apertura)
- 2026-10-02 08:05 [macd_momentum_regimen] ENTRADA ARB @ 0.1821 (21.91 €, apertura)
- 2026-10-02 08:05 [macd_momentum_evento] ENTRADA ARB @ 0.1821 (21.46 €, apertura)
- 2026-10-02 08:05 [ruptura_volumen] ENTRADA ENA @ 0.2215 (21.57 €, apertura)
- 2026-10-02 08:05 [ruptura_volumen_regimen] ENTRADA ENA @ 0.2215 (21.69 €, apertura)
- 2026-10-02 08:05 [ruptura_volumen_evento] ENTRADA ENA @ 0.2215 (21.88 €, apertura)
- 2026-10-02 08:05 [ruptura_volumen] ENTRADA TRX @ 0.297054 (21.57 €, apertura)
- 2026-10-02 08:05 [ruptura_volumen_regimen] ENTRADA TRX @ 0.297054 (21.69 €, apertura)
- 2026-10-02 08:05 [ruptura_volumen_evento] ENTRADA TRX @ 0.297054 (21.88 €, apertura)
- 2026-10-02 08:05 [macd_momentum] ENTRADA ONDO @ 0.44778 (21.34 €, apertura)
- 2026-10-02 08:05 [macd_momentum_regimen] ENTRADA ONDO @ 0.44778 (21.91 €, apertura)
- 2026-10-02 08:05 [macd_momentum_evento] ENTRADA ONDO @ 0.44778 (21.46 €, apertura)
- 2026-10-02 08:05 [macd_momentum] ENTRADA PEPE @ 4.039e-06 (21.34 €, apertura)
- 2026-10-02 08:05 [macd_sin_salida] ENTRADA PEPE @ 4.039e-06 (22.01 €, apertura)
- 2026-10-02 08:05 [macd_momentum_regimen] ENTRADA PEPE @ 4.039e-06 (21.91 €, apertura)
- 2026-10-02 08:05 [macd_momentum_evento] ENTRADA PEPE @ 4.039e-06 (21.46 €, apertura)
- 2026-10-02 08:05 [ruptura_volumen] ENTRADA VVV @ 25.627 (21.57 €, apertura)
- 2026-10-02 08:10 [estocastico_rebote] CIERRE VVV take-profit bruto +1.93% neto +1.43%
- 2026-10-02 08:05 [ruptura_estricta] ENTRADA VVV @ 25.627 (22.06 €, apertura)
- 2026-10-02 08:05 [ruptura_volumen_regimen] ENTRADA VVV @ 25.627 (21.69 €, apertura)
- 2026-10-02 08:05 [ruptura_volumen_evento] ENTRADA VVV @ 25.627 (21.88 €, apertura)
- 2026-10-02 08:05 [macd_momentum] ENTRADA PENGU @ 0.008821 (21.34 €, apertura)
- 2026-10-02 08:05 [macd_sin_salida] ENTRADA PENGU @ 0.008821 (22.01 €, apertura)
- 2026-10-02 08:05 [macd_momentum_regimen] ENTRADA PENGU @ 0.008821 (21.91 €, apertura)
- 2026-10-02 08:05 [macd_momentum_evento] ENTRADA PENGU @ 0.008821 (21.46 €, apertura)
- 2026-10-02 08:05 [c_banda_atr] ENTRADA BNB @ 689.86 (22.24 €, apertura)
- 2026-10-02 08:05 [macd_momentum] ENTRADA BNB @ 689.86 (21.34 €, apertura)
- 2026-10-02 08:05 [macd_sin_salida] ENTRADA BNB @ 689.86 (21.43 €, apertura)
- 2026-10-02 08:05 [c_banda_atr_regimen] ENTRADA BNB @ 689.86 (22.56 €, apertura)
- 2026-10-02 08:05 [macd_momentum_regimen] ENTRADA BNB @ 689.86 (21.91 €, apertura)
- 2026-10-02 08:05 [c_banda_atr_evento] ENTRADA BNB @ 689.86 (22.39 €, apertura)
- 2026-10-02 08:05 [macd_momentum_evento] ENTRADA BNB @ 689.86 (21.46 €, apertura)
- 2026-10-02 08:05 [macd_momentum] ENTRADA KAS @ 0.03773 (21.34 €, apertura)
- 2026-10-02 08:05 [macd_momentum_regimen] ENTRADA KAS @ 0.03773 (21.91 €, apertura)
- 2026-10-02 08:05 [macd_momentum_evento] ENTRADA KAS @ 0.03773 (21.46 €, apertura)
- 2026-10-02 08:05 [macd_momentum] ENTRADA XMR @ 488.64 (21.34 €, apertura)
- 2026-10-02 08:05 [macd_momentum_regimen] ENTRADA XMR @ 488.64 (21.91 €, apertura)
- 2026-10-02 08:05 [macd_momentum_evento] ENTRADA XMR @ 488.64 (21.46 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
