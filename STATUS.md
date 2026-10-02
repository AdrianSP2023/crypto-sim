# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 08:16 UTC · vueltas 388 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 890.54 € (-3.65%) | 333 | 25 | 39% | +0.124% | -0.454% | -0.575% | -34.48 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 862.85 € (-6.64%) | 416 | 14 | 27% | -0.096% | -0.659% | -0.768% | -61.42 € |
| rebote_extremo | 922.42 € (-0.20%) | 15 | 0 | 60% | +0.574% | -0.526% | -0.706% | -1.82 € |
| pullback_tendencia | 889.40 € (-3.77%) | 237 | 9 | 20% | -0.036% | -0.647% | -0.733% | -34.84 € |
| macd_momentum | 854.18 € (-7.58%) | 647 | 38 | 22% | +0.049% | -0.492% | -0.593% | -70.81 € |
| estocastico_rebote | 881.35 € (-4.64%) | 389 | 38 | 37% | +0.052% | -0.515% | -0.623% | -45.39 € |
| ruptura_estricta | 882.35 € (-4.53%) | 233 | 7 | 32% | -0.174% | -0.787% | -0.903% | -41.73 € |
| macd_sin_salida | 880.63 € (-4.72%) | 432 | 40 | 40% | +0.113% | -0.447% | -0.558% | -44.02 € |
| c_banda_atr_tope | 913.35 € (-1.18%) | 76 | 5 | 37% | +0.213% | -0.634% | -0.750% | -11.08 € |
| ruptura_volumen_tope | 901.31 € (-2.48%) | 128 | 4 | 24% | -0.088% | -0.794% | -0.908% | -23.22 € |
| c_banda_atr_regimen | 903.12 € (-2.28%) | 185 | 25 | 40% | +0.131% | -0.510% | -0.640% | -21.73 € |
| macd_momentum_regimen | 877.05 € (-5.11%) | 410 | 38 | 22% | +0.045% | -0.518% | -0.622% | -47.94 € |
| ruptura_volumen_regimen | 867.54 € (-6.14%) | 339 | 14 | 24% | -0.168% | -0.745% | -0.859% | -56.74 € |
| c_banda_atr_evento | 896.46 € (-3.01%) | 300 | 25 | 40% | +0.172% | -0.416% | -0.533% | -28.56 € |
| macd_momentum_evento | 858.91 € (-7.07%) | 600 | 38 | 21% | +0.050% | -0.494% | -0.593% | -66.08 € |
| ruptura_volumen_evento | 875.13 € (-5.31%) | 366 | 14 | 28% | -0.024% | -0.596% | -0.700% | -49.14 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 08:15 | ruptura_volumen_evento | WLFI | timeout | -0.20% | -0.70% | -0.15 |
| 2026-10-02 08:15 | macd_momentum_evento | KSM | momentum perdido | -0.22% | -0.72% | -0.15 |
| 2026-10-02 08:15 | ruptura_volumen_regimen | WLFI | timeout | -0.20% | -0.70% | -0.15 |
| 2026-10-02 08:15 | macd_momentum_regimen | KSM | momentum perdido | -0.22% | -0.72% | -0.16 |
| 2026-10-02 08:15 | ruptura_volumen_tope | WLFI | timeout | -0.20% | -0.70% | -0.16 |
| 2026-10-02 08:15 | estocastico_rebote | CRV | take-profit | +1.80% | +1.30% | +0.28 |
| 2026-10-02 08:15 | macd_momentum | KSM | momentum perdido | -0.22% | -0.72% | -0.15 |
| 2026-10-02 08:15 | ruptura_volumen | WLFI | timeout | -0.20% | -0.70% | -0.15 |
| 2026-10-02 08:10 | estocastico_rebote | VVV | take-profit | +1.93% | +1.43% | +0.31 |
| 2026-10-02 08:05 | ruptura_volumen_evento | ALGO | take-profit | +2.50% | +2.00% | +0.44 |
| 2026-10-02 08:05 | macd_momentum_evento | ALGO | take-profit | +2.00% | +1.50% | +0.32 |
| 2026-10-02 08:05 | ruptura_volumen_regimen | ALGO | take-profit | +2.50% | +2.00% | +0.43 |
| 2026-10-02 08:05 | macd_momentum_regimen | ALGO | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 08:05 | macd_momentum | ALGO | take-profit | +2.00% | +1.50% | +0.32 |
| 2026-10-02 08:05 | ruptura_volumen | ALGO | take-profit | +2.50% | +2.00% | +0.43 |

## Eventos de la última vuelta

- 2026-10-02 08:10 [pullback_tendencia] ENTRADA PUMP @ 0.005299 (22.24 €, apertura)
- 2026-10-02 08:15 [estocastico_rebote] CIERRE CRV take-profit bruto +1.80% neto +1.30%
- 2026-10-02 08:10 [ruptura_estricta] ENTRADA CRV @ 0.34192 (22.06 €, apertura)
- 2026-10-02 08:10 [macd_momentum] ENTRADA VVV @ 25.724 (21.34 €, apertura)
- 2026-10-02 08:10 [macd_momentum_regimen] ENTRADA VVV @ 25.724 (21.91 €, apertura)
- 2026-10-02 08:10 [macd_momentum_evento] ENTRADA VVV @ 25.724 (21.46 €, apertura)
- 2026-10-02 08:15 [ruptura_volumen] CIERRE WLFI timeout bruto -0.20% neto -0.70%
- 2026-10-02 08:15 [ruptura_volumen_tope] CIERRE WLFI timeout bruto -0.20% neto -0.70%
- 2026-10-02 08:15 [ruptura_volumen_regimen] CIERRE WLFI timeout bruto -0.20% neto -0.70%
- 2026-10-02 08:15 [ruptura_volumen_evento] CIERRE WLFI timeout bruto -0.20% neto -0.70%
- 2026-10-02 08:15 [macd_momentum] CIERRE KSM momentum perdido bruto -0.22% neto -0.72%
- 2026-10-02 08:15 [macd_momentum_regimen] CIERRE KSM momentum perdido bruto -0.22% neto -0.72%
- 2026-10-02 08:15 [macd_momentum_evento] CIERRE KSM momentum perdido bruto -0.22% neto -0.72%
- 2026-10-02 08:10 [macd_momentum] ENTRADA SEI @ 0.06347 (21.34 €, apertura)
- 2026-10-02 08:10 [macd_momentum_regimen] ENTRADA SEI @ 0.06347 (21.91 €, apertura)
- 2026-10-02 08:10 [macd_momentum_evento] ENTRADA SEI @ 0.06347 (21.45 €, apertura)
- 2026-10-02 08:10 [macd_momentum] ENTRADA APT @ 0.7373 (21.34 €, apertura)
- 2026-10-02 08:10 [macd_momentum_regimen] ENTRADA APT @ 0.7373 (21.91 €, apertura)
- 2026-10-02 08:10 [macd_momentum_evento] ENTRADA APT @ 0.7373 (21.45 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
