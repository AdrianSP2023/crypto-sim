# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 01:01 UTC · vueltas 347 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 885.23 € (-4.22%) | 273 | 22 | 34% | -0.040% | -0.636% | -0.757% | -39.41 € |
| reversion_bb | 918.07 € (-0.67%) | 56 | 13 | 54% | +0.408% | -0.558% | -0.666% | -7.21 € |
| ruptura_volumen | 869.99 € (-5.87%) | 300 | 32 | 24% | -0.201% | -0.788% | -0.896% | -53.22 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 888.55 € (-3.86%) | 190 | 5 | 15% | -0.201% | -0.840% | -0.929% | -36.21 € |
| macd_momentum | 862.70 € (-6.66%) | 501 | 10 | 20% | -0.003% | -0.555% | -0.657% | -62.18 € |
| estocastico_rebote | 873.16 € (-5.53%) | 337 | 10 | 31% | -0.100% | -0.678% | -0.788% | -51.53 € |
| ruptura_estricta | 882.14 € (-4.56%) | 167 | 9 | 25% | -0.443% | -1.101% | -1.217% | -41.82 € |
| macd_sin_salida | 872.43 € (-5.61%) | 350 | 16 | 34% | -0.089% | -0.664% | -0.775% | -52.49 € |
| c_banda_atr_tope | 911.86 € (-1.34%) | 62 | 5 | 31% | +0.026% | -0.900% | -1.015% | -12.81 € |
| ruptura_volumen_tope | 905.06 € (-2.08%) | 103 | 5 | 26% | -0.041% | -0.797% | -0.913% | -18.80 € |
| c_banda_atr_regimen | 895.60 € (-3.10%) | 138 | 6 | 29% | -0.213% | -0.902% | -1.036% | -28.48 € |
| macd_momentum_regimen | 885.14 € (-4.23%) | 278 | 7 | 19% | -0.029% | -0.623% | -0.728% | -39.27 € |
| ruptura_volumen_regimen | 873.44 € (-5.50%) | 231 | 29 | 19% | -0.342% | -0.955% | -1.069% | -49.79 € |
| c_banda_atr_evento | 891.12 € (-3.58%) | 240 | 22 | 35% | -0.003% | -0.613% | -0.729% | -33.51 € |
| macd_momentum_evento | 867.48 € (-6.14%) | 454 | 10 | 19% | -0.006% | -0.564% | -0.663% | -57.41 € |
| ruptura_volumen_evento | 882.37 € (-4.53%) | 250 | 32 | 25% | -0.115% | -0.721% | -0.821% | -40.82 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 01:00 | macd_momentum_evento | BNB | momentum perdido | +0.01% | -0.49% | -0.11 |
| 2026-10-02 01:00 | macd_momentum_evento | ICP | momentum perdido | +0.48% | -0.02% | -0.00 |
| 2026-10-02 01:00 | macd_momentum | BNB | momentum perdido | +0.01% | -0.49% | -0.10 |
| 2026-10-02 01:00 | macd_momentum | ICP | momentum perdido | +0.48% | -0.02% | -0.00 |
| 2026-10-02 00:55 | macd_momentum_evento | FIL | momentum perdido | +0.56% | +0.06% | +0.01 |
| 2026-10-02 00:55 | macd_momentum | FIL | momentum perdido | +0.56% | +0.06% | +0.01 |
| 2026-10-02 00:55 | reversion_bb | INJ | take-profit | +1.50% | +1.00% | +0.23 |
| 2026-10-02 00:55 | reversion_bb | HYPE | take-profit | +1.51% | +1.01% | +0.23 |
| 2026-10-02 00:50 | macd_momentum_evento | WLD | momentum perdido | +1.51% | +1.01% | +0.22 |
| 2026-10-02 00:50 | c_banda_atr_evento | AAVE | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 00:50 | estocastico_rebote | MINA | take-profit | +1.80% | +1.30% | +0.28 |
| 2026-10-02 00:50 | estocastico_rebote | MON | timeout | +0.73% | +0.23% | +0.05 |
| 2026-10-02 00:50 | estocastico_rebote | BCH | timeout | -0.99% | -1.49% | -0.33 |
| 2026-10-02 00:50 | macd_momentum | WLD | momentum perdido | +1.51% | +1.01% | +0.22 |
| 2026-10-02 00:50 | reversion_bb | APT | take-profit | +1.67% | +1.17% | +0.27 |

## Eventos de la última vuelta

- 2026-10-02 00:55 [macd_momentum] ENTRADA ETH @ 2409.23 (21.55 €, apertura)
- 2026-10-02 00:55 [macd_momentum_regimen] ENTRADA ETH @ 2409.23 (22.12 €, apertura)
- 2026-10-02 00:55 [macd_momentum_evento] ENTRADA ETH @ 2409.23 (21.67 €, apertura)
- 2026-10-02 00:55 [macd_momentum] ENTRADA PUMP @ 0.005198 (21.55 €, apertura)
- 2026-10-02 00:55 [macd_momentum_regimen] ENTRADA PUMP @ 0.005198 (22.12 €, apertura)
- 2026-10-02 00:55 [macd_momentum_evento] ENTRADA PUMP @ 0.005198 (21.67 €, apertura)
- 2026-10-02 00:55 [ruptura_volumen] ENTRADA HYPE @ 78.55 (21.78 €, apertura)
- 2026-10-02 00:55 [ruptura_estricta] ENTRADA HYPE @ 78.55 (22.06 €, apertura)
- 2026-10-02 00:55 [ruptura_volumen_regimen] ENTRADA HYPE @ 78.55 (21.86 €, apertura)
- 2026-10-02 00:55 [ruptura_volumen_evento] ENTRADA HYPE @ 78.55 (22.09 €, apertura)
- 2026-10-02 00:55 [macd_momentum] ENTRADA TAO @ 269.966 (21.55 €, apertura)
- 2026-10-02 00:55 [macd_sin_salida] ENTRADA TAO @ 269.966 (21.79 €, apertura)
- 2026-10-02 00:55 [macd_momentum_regimen] ENTRADA TAO @ 269.966 (22.12 €, apertura)
- 2026-10-02 00:55 [macd_momentum_evento] ENTRADA TAO @ 269.966 (21.67 €, apertura)
- 2026-10-02 00:55 [ruptura_volumen] ENTRADA ZRO @ 1.639 (21.78 €, apertura)
- 2026-10-02 00:55 [ruptura_volumen_regimen] ENTRADA ZRO @ 1.639 (21.86 €, apertura)
- 2026-10-02 00:55 [ruptura_volumen_evento] ENTRADA ZRO @ 1.639 (22.09 €, apertura)
- 2026-10-02 01:00 [macd_momentum] CIERRE ICP momentum perdido bruto +0.48% neto -0.02%
- 2026-10-02 01:00 [macd_momentum_evento] CIERRE ICP momentum perdido bruto +0.48% neto -0.02%
- 2026-10-02 01:00 [macd_momentum] CIERRE BNB momentum perdido bruto +0.01% neto -0.49%
- 2026-10-02 01:00 [macd_momentum_evento] CIERRE BNB momentum perdido bruto +0.01% neto -0.49%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
