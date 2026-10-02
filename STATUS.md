# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 00:51 UTC · vueltas 345 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 886.05 € (-4.13%) | 273 | 22 | 34% | -0.040% | -0.636% | -0.757% | -39.41 € |
| reversion_bb | 918.77 € (-0.59%) | 54 | 15 | 52% | +0.367% | -0.616% | -0.726% | -7.67 € |
| ruptura_volumen | 871.46 € (-5.71%) | 300 | 29 | 24% | -0.201% | -0.788% | -0.896% | -53.22 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 888.63 € (-3.85%) | 190 | 5 | 15% | -0.201% | -0.840% | -0.929% | -36.21 € |
| macd_momentum | 863.51 € (-6.57%) | 498 | 9 | 20% | -0.005% | -0.557% | -0.660% | -62.09 € |
| estocastico_rebote | 873.63 € (-5.48%) | 337 | 10 | 31% | -0.100% | -0.678% | -0.788% | -51.53 € |
| ruptura_estricta | 882.53 € (-4.51%) | 167 | 7 | 25% | -0.443% | -1.101% | -1.217% | -41.82 € |
| macd_sin_salida | 872.68 € (-5.58%) | 350 | 15 | 34% | -0.089% | -0.664% | -0.775% | -52.49 € |
| c_banda_atr_tope | 911.85 € (-1.34%) | 62 | 5 | 31% | +0.026% | -0.900% | -1.015% | -12.81 € |
| ruptura_volumen_tope | 905.23 € (-2.06%) | 103 | 5 | 26% | -0.041% | -0.797% | -0.913% | -18.80 € |
| c_banda_atr_regimen | 896.14 € (-3.04%) | 138 | 6 | 29% | -0.213% | -0.902% | -1.036% | -28.48 € |
| macd_momentum_regimen | 885.52 € (-4.19%) | 278 | 3 | 19% | -0.029% | -0.623% | -0.728% | -39.27 € |
| ruptura_volumen_regimen | 874.86 € (-5.34%) | 231 | 26 | 19% | -0.342% | -0.955% | -1.069% | -49.79 € |
| c_banda_atr_evento | 891.95 € (-3.49%) | 240 | 22 | 35% | -0.003% | -0.613% | -0.729% | -33.51 € |
| macd_momentum_evento | 868.29 € (-6.05%) | 451 | 9 | 19% | -0.008% | -0.567% | -0.666% | -57.31 € |
| ruptura_volumen_evento | 883.86 € (-4.37%) | 250 | 29 | 25% | -0.115% | -0.721% | -0.821% | -40.82 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 00:50 | macd_momentum_evento | WLD | momentum perdido | +1.51% | +1.01% | +0.22 |
| 2026-10-02 00:50 | c_banda_atr_evento | AAVE | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 00:50 | estocastico_rebote | MINA | take-profit | +1.80% | +1.30% | +0.28 |
| 2026-10-02 00:50 | estocastico_rebote | MON | timeout | +0.73% | +0.23% | +0.05 |
| 2026-10-02 00:50 | estocastico_rebote | BCH | timeout | -0.99% | -1.49% | -0.33 |
| 2026-10-02 00:50 | macd_momentum | WLD | momentum perdido | +1.51% | +1.01% | +0.22 |
| 2026-10-02 00:50 | reversion_bb | APT | take-profit | +1.67% | +1.17% | +0.27 |
| 2026-10-02 00:50 | c_banda_atr | AAVE | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 00:45 | ruptura_volumen_evento | SKY | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-02 00:45 | macd_momentum_evento | POL | momentum perdido | -0.24% | -0.74% | -0.16 |
| 2026-10-02 00:45 | macd_momentum_evento | AVAX | momentum perdido | -0.16% | -0.66% | -0.14 |
| 2026-10-02 00:45 | macd_momentum_evento | ETH | momentum perdido | +0.23% | -0.27% | -0.06 |
| 2026-10-02 00:45 | ruptura_volumen_regimen | SKY | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 00:45 | macd_momentum_regimen | ETH | momentum perdido | +0.05% | -0.45% | -0.10 |
| 2026-10-02 00:45 | macd_sin_salida | WLFI | timeout | +0.61% | +0.11% | +0.02 |

## Eventos de la última vuelta

- 2026-10-02 00:50 [c_banda_atr] CIERRE AAVE take-profit bruto +2.00% neto +1.50%
- 2026-10-02 00:45 [ruptura_volumen] ENTRADA AAVE @ 155.25 (21.78 €, apertura)
- 2026-10-02 00:45 [ruptura_estricta] ENTRADA AAVE @ 155.25 (22.06 €, apertura)
- 2026-10-02 00:45 [ruptura_volumen_regimen] ENTRADA AAVE @ 155.25 (21.86 €, apertura)
- 2026-10-02 00:50 [c_banda_atr_evento] CIERRE AAVE take-profit bruto +2.00% neto +1.50%
- 2026-10-02 00:45 [ruptura_volumen_evento] ENTRADA AAVE @ 155.25 (22.09 €, apertura)
- 2026-10-02 00:50 [macd_momentum] CIERRE WLD momentum perdido bruto +1.51% neto +1.01%
- 2026-10-02 00:50 [macd_momentum_evento] CIERRE WLD momentum perdido bruto +1.51% neto +1.01%
- 2026-10-02 00:50 [estocastico_rebote] CIERRE BCH timeout bruto -0.99% neto -1.49%
- 2026-10-02 00:45 [c_banda_atr] ENTRADA MON @ 0.03015 (22.12 €, apertura)
- 2026-10-02 00:50 [estocastico_rebote] CIERRE MON timeout bruto +0.73% neto +0.23%
- 2026-10-02 00:45 [c_banda_atr_regimen] ENTRADA MON @ 0.03015 (22.39 €, apertura)
- 2026-10-02 00:45 [c_banda_atr_evento] ENTRADA MON @ 0.03015 (22.27 €, apertura)
- 2026-10-02 00:45 [ruptura_volumen] ENTRADA MINA @ 0.1368 (21.78 €, apertura)
- 2026-10-02 00:50 [estocastico_rebote] CIERRE MINA take-profit bruto +1.80% neto +1.30%
- 2026-10-02 00:45 [ruptura_estricta] ENTRADA MINA @ 0.1368 (22.06 €, apertura)
- 2026-10-02 00:45 [ruptura_volumen_regimen] ENTRADA MINA @ 0.1368 (21.86 €, apertura)
- 2026-10-02 00:45 [ruptura_volumen_evento] ENTRADA MINA @ 0.1368 (22.09 €, apertura)
- 2026-10-02 00:45 [ruptura_volumen] ENTRADA DASH @ 51.99 (21.78 €, apertura)
- 2026-10-02 00:45 [ruptura_volumen_regimen] ENTRADA DASH @ 51.99 (21.86 €, apertura)
- 2026-10-02 00:45 [ruptura_volumen_evento] ENTRADA DASH @ 51.99 (22.09 €, apertura)
- 2026-10-02 00:50 [reversion_bb] CIERRE APT take-profit bruto +1.67% neto +1.17%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
