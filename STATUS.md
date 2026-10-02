# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 08:06 UTC · vueltas 386 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 890.91 € (-3.61%) | 333 | 23 | 39% | +0.124% | -0.454% | -0.575% | -34.48 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 863.22 € (-6.60%) | 415 | 9 | 27% | -0.096% | -0.659% | -0.768% | -61.27 € |
| rebote_extremo | 922.42 € (-0.20%) | 15 | 0 | 60% | +0.574% | -0.526% | -0.706% | -1.82 € |
| pullback_tendencia | 890.14 € (-3.69%) | 237 | 8 | 20% | -0.036% | -0.647% | -0.733% | -34.84 € |
| macd_momentum | 854.94 € (-7.50%) | 646 | 29 | 22% | +0.049% | -0.491% | -0.593% | -70.66 € |
| estocastico_rebote | 881.99 € (-4.57%) | 387 | 40 | 36% | +0.043% | -0.524% | -0.633% | -45.99 € |
| ruptura_estricta | 882.51 € (-4.52%) | 233 | 5 | 32% | -0.174% | -0.787% | -0.903% | -41.73 € |
| macd_sin_salida | 881.57 € (-4.62%) | 432 | 36 | 40% | +0.113% | -0.447% | -0.558% | -44.02 € |
| c_banda_atr_tope | 913.49 € (-1.16%) | 76 | 5 | 37% | +0.213% | -0.634% | -0.750% | -11.08 € |
| ruptura_volumen_tope | 901.43 € (-2.47%) | 127 | 5 | 24% | -0.087% | -0.795% | -0.908% | -23.06 € |
| c_banda_atr_regimen | 903.44 € (-2.25%) | 185 | 23 | 40% | +0.131% | -0.510% | -0.640% | -21.73 € |
| macd_momentum_regimen | 877.83 € (-5.02%) | 409 | 29 | 22% | +0.046% | -0.518% | -0.621% | -47.78 € |
| ruptura_volumen_regimen | 867.91 € (-6.09%) | 338 | 9 | 25% | -0.168% | -0.745% | -0.859% | -56.58 € |
| c_banda_atr_evento | 896.83 € (-2.97%) | 300 | 23 | 40% | +0.172% | -0.416% | -0.533% | -28.56 € |
| macd_momentum_evento | 859.67 € (-6.99%) | 599 | 29 | 21% | +0.051% | -0.493% | -0.592% | -65.93 € |
| ruptura_volumen_evento | 875.50 € (-5.27%) | 365 | 9 | 28% | -0.023% | -0.595% | -0.699% | -48.98 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
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
| 2026-10-02 07:55 | ruptura_volumen_regimen | PUMP | stop-loss | -1.20% | -1.70% | -0.37 |

## Eventos de la última vuelta

- 2026-10-02 08:00 [macd_momentum] ENTRADA BTC @ 76463.3 (21.33 €, apertura)
- 2026-10-02 08:00 [macd_sin_salida] ENTRADA BTC @ 76463.3 (22.01 €, apertura)
- 2026-10-02 08:00 [macd_momentum_regimen] ENTRADA BTC @ 76463.3 (21.90 €, apertura)
- 2026-10-02 08:00 [macd_momentum_evento] ENTRADA BTC @ 76463.3 (21.45 €, apertura)
- 2026-10-02 08:00 [ruptura_volumen] ENTRADA ETH @ 2431.06 (21.56 €, apertura)
- 2026-10-02 08:00 [ruptura_volumen_regimen] ENTRADA ETH @ 2431.06 (21.68 €, apertura)
- 2026-10-02 08:00 [ruptura_volumen_evento] ENTRADA ETH @ 2431.06 (21.87 €, apertura)
- 2026-10-02 08:00 [macd_momentum] ENTRADA SOL @ 108.05 (21.33 €, apertura)
- 2026-10-02 08:00 [macd_sin_salida] ENTRADA SOL @ 108.05 (22.01 €, apertura)
- 2026-10-02 08:00 [macd_momentum_regimen] ENTRADA SOL @ 108.05 (21.90 €, apertura)
- 2026-10-02 08:00 [macd_momentum_evento] ENTRADA SOL @ 108.05 (21.45 €, apertura)
- 2026-10-02 08:00 [macd_momentum] ENTRADA ADA @ 0.226798 (21.33 €, apertura)
- 2026-10-02 08:00 [macd_momentum_regimen] ENTRADA ADA @ 0.226798 (21.90 €, apertura)
- 2026-10-02 08:00 [macd_momentum_evento] ENTRADA ADA @ 0.226798 (21.45 €, apertura)
- 2026-10-02 08:00 [macd_momentum] ENTRADA AVAX @ 9.848 (21.33 €, apertura)
- 2026-10-02 08:00 [macd_sin_salida] ENTRADA AVAX @ 9.848 (22.01 €, apertura)
- 2026-10-02 08:00 [macd_momentum_regimen] ENTRADA AVAX @ 9.848 (21.90 €, apertura)
- 2026-10-02 08:00 [macd_momentum_evento] ENTRADA AVAX @ 9.848 (21.45 €, apertura)
- 2026-10-02 08:00 [macd_momentum] ENTRADA ZEC @ 1232.11 (21.33 €, apertura)
- 2026-10-02 08:00 [macd_sin_salida] ENTRADA ZEC @ 1232.11 (22.01 €, apertura)
- 2026-10-02 08:00 [macd_momentum_regimen] ENTRADA ZEC @ 1232.11 (21.90 €, apertura)
- 2026-10-02 08:00 [macd_momentum_evento] ENTRADA ZEC @ 1232.11 (21.45 €, apertura)
- 2026-10-02 08:00 [macd_momentum] ENTRADA ENA @ 0.2214 (21.33 €, apertura)
- 2026-10-02 08:00 [macd_sin_salida] ENTRADA ENA @ 0.2214 (22.01 €, apertura)
- 2026-10-02 08:00 [macd_momentum_regimen] ENTRADA ENA @ 0.2214 (21.90 €, apertura)
- 2026-10-02 08:00 [macd_momentum_evento] ENTRADA ENA @ 0.2214 (21.45 €, apertura)
- 2026-10-02 08:00 [ruptura_volumen] ENTRADA ICP @ 2.942 (21.56 €, apertura)
- 2026-10-02 08:00 [macd_momentum] ENTRADA ICP @ 2.942 (21.33 €, apertura)
- 2026-10-02 08:00 [ruptura_estricta] ENTRADA ICP @ 2.942 (22.06 €, apertura)
- 2026-10-02 08:00 [macd_sin_salida] ENTRADA ICP @ 2.942 (22.01 €, apertura)
- 2026-10-02 08:00 [macd_momentum_regimen] ENTRADA ICP @ 2.942 (21.90 €, apertura)
- 2026-10-02 08:00 [ruptura_volumen_regimen] ENTRADA ICP @ 2.942 (21.68 €, apertura)
- 2026-10-02 08:00 [macd_momentum_evento] ENTRADA ICP @ 2.942 (21.45 €, apertura)
- 2026-10-02 08:00 [ruptura_volumen_evento] ENTRADA ICP @ 2.942 (21.87 €, apertura)
- 2026-10-02 08:05 [ruptura_volumen] CIERRE ALGO take-profit bruto +2.50% neto +2.00%
- 2026-10-02 08:05 [macd_momentum] CIERRE ALGO take-profit bruto +2.00% neto +1.50%
- 2026-10-02 08:05 [macd_momentum_regimen] CIERRE ALGO take-profit bruto +2.00% neto +1.50%
- 2026-10-02 08:05 [ruptura_volumen_regimen] CIERRE ALGO take-profit bruto +2.50% neto +2.00%
- 2026-10-02 08:05 [macd_momentum_evento] CIERRE ALGO take-profit bruto +2.00% neto +1.50%
- 2026-10-02 08:05 [ruptura_volumen_evento] CIERRE ALGO take-profit bruto +2.50% neto +2.00%
- 2026-10-02 08:00 [ruptura_volumen] ENTRADA USELESS @ 0.22494 (21.57 €, apertura)
- 2026-10-02 08:00 [ruptura_volumen_regimen] ENTRADA USELESS @ 0.22494 (21.69 €, apertura)
- 2026-10-02 08:00 [ruptura_volumen_evento] ENTRADA USELESS @ 0.22494 (21.88 €, apertura)
- 2026-10-02 08:00 [macd_momentum] ENTRADA BCH @ 280.13 (21.34 €, apertura)
- 2026-10-02 08:00 [macd_sin_salida] ENTRADA BCH @ 280.13 (22.01 €, apertura)
- 2026-10-02 08:00 [macd_momentum_regimen] ENTRADA BCH @ 280.13 (21.91 €, apertura)
- 2026-10-02 08:00 [macd_momentum_evento] ENTRADA BCH @ 280.13 (21.46 €, apertura)
- 2026-10-02 08:00 [macd_momentum] ENTRADA RENDER @ 1.754 (21.34 €, apertura)
- 2026-10-02 08:00 [macd_sin_salida] ENTRADA RENDER @ 1.754 (22.01 €, apertura)
- 2026-10-02 08:00 [macd_momentum_regimen] ENTRADA RENDER @ 1.754 (21.91 €, apertura)
- 2026-10-02 08:00 [macd_momentum_evento] ENTRADA RENDER @ 1.754 (21.46 €, apertura)
- 2026-10-02 08:00 [macd_momentum] ENTRADA INJ @ 6.684 (21.34 €, apertura)
- 2026-10-02 08:00 [macd_momentum_regimen] ENTRADA INJ @ 6.684 (21.91 €, apertura)
- 2026-10-02 08:00 [macd_momentum_evento] ENTRADA INJ @ 6.684 (21.46 €, apertura)
- 2026-10-02 08:00 [pullback_tendencia] ENTRADA MINA @ 0.1457 (22.24 €, apertura)
- 2026-10-02 08:00 [ruptura_volumen] ENTRADA SHIB @ 5.269e-06 (21.57 €, apertura)
- 2026-10-02 08:00 [ruptura_volumen_regimen] ENTRADA SHIB @ 5.269e-06 (21.69 €, apertura)
- 2026-10-02 08:00 [ruptura_volumen_evento] ENTRADA SHIB @ 5.269e-06 (21.88 €, apertura)
- 2026-10-02 08:00 [macd_momentum] ENTRADA DASH @ 53.307 (21.34 €, apertura)
- 2026-10-02 08:00 [macd_sin_salida] ENTRADA DASH @ 53.307 (22.01 €, apertura)
- 2026-10-02 08:00 [macd_momentum_regimen] ENTRADA DASH @ 53.307 (21.91 €, apertura)
- 2026-10-02 08:00 [macd_momentum_evento] ENTRADA DASH @ 53.307 (21.46 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
