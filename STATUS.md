# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 00:56 UTC · vueltas 346 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 885.44 € (-4.20%) | 273 | 22 | 34% | -0.040% | -0.636% | -0.757% | -39.41 € |
| reversion_bb | 918.19 € (-0.65%) | 56 | 13 | 54% | +0.408% | -0.558% | -0.666% | -7.21 € |
| ruptura_volumen | 870.69 € (-5.79%) | 300 | 30 | 24% | -0.201% | -0.788% | -0.896% | -53.22 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 888.66 € (-3.85%) | 190 | 5 | 15% | -0.201% | -0.840% | -0.929% | -36.21 € |
| macd_momentum | 863.25 € (-6.60%) | 499 | 9 | 20% | -0.004% | -0.556% | -0.659% | -62.07 € |
| estocastico_rebote | 873.46 € (-5.49%) | 337 | 10 | 31% | -0.100% | -0.678% | -0.788% | -51.53 € |
| ruptura_estricta | 882.44 € (-4.52%) | 167 | 8 | 25% | -0.443% | -1.101% | -1.217% | -41.82 € |
| macd_sin_salida | 872.66 € (-5.58%) | 350 | 15 | 34% | -0.089% | -0.664% | -0.775% | -52.49 € |
| c_banda_atr_tope | 911.83 € (-1.34%) | 62 | 5 | 31% | +0.026% | -0.900% | -1.015% | -12.81 € |
| ruptura_volumen_tope | 905.16 € (-2.06%) | 103 | 5 | 26% | -0.041% | -0.797% | -0.913% | -18.80 € |
| c_banda_atr_regimen | 895.77 € (-3.08%) | 138 | 6 | 29% | -0.213% | -0.902% | -1.036% | -28.48 € |
| macd_momentum_regimen | 885.44 € (-4.20%) | 278 | 4 | 19% | -0.029% | -0.623% | -0.728% | -39.27 € |
| ruptura_volumen_regimen | 874.15 € (-5.42%) | 231 | 27 | 19% | -0.342% | -0.955% | -1.069% | -49.79 € |
| c_banda_atr_evento | 891.33 € (-3.56%) | 240 | 22 | 35% | -0.003% | -0.613% | -0.729% | -33.51 € |
| macd_momentum_evento | 868.04 € (-6.08%) | 452 | 9 | 19% | -0.007% | -0.565% | -0.664% | -57.30 € |
| ruptura_volumen_evento | 883.07 € (-4.45%) | 250 | 30 | 25% | -0.115% | -0.721% | -0.821% | -40.82 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
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
| 2026-10-02 00:50 | c_banda_atr | AAVE | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 00:45 | ruptura_volumen_evento | SKY | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-02 00:45 | macd_momentum_evento | POL | momentum perdido | -0.24% | -0.74% | -0.16 |
| 2026-10-02 00:45 | macd_momentum_evento | AVAX | momentum perdido | -0.16% | -0.66% | -0.14 |

## Eventos de la última vuelta

- 2026-10-02 00:50 [macd_momentum] ENTRADA ZEC @ 1193.25 (21.55 €, apertura)
- 2026-10-02 00:50 [macd_momentum_regimen] ENTRADA ZEC @ 1193.25 (22.12 €, apertura)
- 2026-10-02 00:50 [macd_momentum_evento] ENTRADA ZEC @ 1193.25 (21.67 €, apertura)
- 2026-10-02 00:55 [reversion_bb] CIERRE HYPE take-profit bruto +1.51% neto +1.01%
- 2026-10-02 00:55 [reversion_bb] CIERRE INJ take-profit bruto +1.50% neto +1.00%
- 2026-10-02 00:55 [macd_momentum] CIERRE FIL momentum perdido bruto +0.55% neto +0.05%
- 2026-10-02 00:55 [macd_momentum_evento] CIERRE FIL momentum perdido bruto +0.55% neto +0.05%
- 2026-10-02 00:50 [ruptura_volumen] ENTRADA APT @ 0.6953 (21.78 €, apertura)
- 2026-10-02 00:50 [ruptura_estricta] ENTRADA APT @ 0.6953 (22.06 €, apertura)
- 2026-10-02 00:50 [ruptura_volumen_regimen] ENTRADA APT @ 0.6953 (21.86 €, apertura)
- 2026-10-02 00:50 [ruptura_volumen_evento] ENTRADA APT @ 0.6953 (22.09 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
