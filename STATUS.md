# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 17:47 UTC · vueltas 97 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 909.59 € (-1.59%) | 53 | 2 | 34% | -0.162% | -1.154% | -1.293% | -14.12 € |
| reversion_bb | 918.34 € (-0.64%) | 12 | 4 | 17% | -1.026% | -2.126% | -2.232% | -5.89 € |
| ruptura_volumen | 909.50 € (-1.60%) | 70 | 1 | 27% | -0.044% | -0.917% | -1.054% | -14.76 € |
| rebote_extremo | 923.04 € (-0.13%) | 4 | 2 | 25% | -0.905% | -2.005% | -2.191% | -1.85 € |
| pullback_tendencia | 907.99 € (-1.76%) | 69 | 0 | 25% | -0.147% | -1.026% | -1.140% | -16.25 € |
| macd_momentum | 897.63 € (-2.88%) | 151 | 1 | 19% | -0.094% | -0.767% | -0.885% | -26.49 € |
| estocastico_rebote | 892.99 € (-3.38%) | 117 | 27 | 28% | -0.389% | -1.112% | -1.234% | -29.76 € |
| ruptura_estricta | 911.41 € (-1.39%) | 42 | 0 | 29% | -0.226% | -1.326% | -1.452% | -12.83 € |
| macd_sin_salida | 904.12 € (-2.18%) | 96 | 2 | 30% | -0.131% | -0.903% | -1.029% | -19.88 € |
| c_banda_atr_tope | 916.00 € (-0.89%) | 20 | 2 | 25% | -0.571% | -1.671% | -1.836% | -7.70 € |
| ruptura_volumen_tope | 919.13 € (-0.55%) | 21 | 1 | 19% | +0.041% | -1.059% | -1.189% | -5.13 € |
| c_banda_atr_regimen | 909.84 € (-1.56%) | 50 | 0 | 32% | -0.226% | -1.248% | -1.385% | -14.40 € |
| macd_momentum_regimen | 898.81 € (-2.75%) | 147 | 0 | 20% | -0.078% | -0.756% | -0.872% | -25.43 € |
| ruptura_volumen_regimen | 909.87 € (-1.55%) | 69 | 0 | 28% | -0.027% | -0.906% | -1.043% | -14.37 € |
| c_banda_atr_evento | 916.18 € (-0.87%) | 20 | 3 | 30% | -0.465% | -1.565% | -1.725% | -7.23 € |
| macd_momentum_evento | 912.04 € (-1.32%) | 31 | 1 | 13% | -0.590% | -1.690% | -1.815% | -12.08 € |
| ruptura_volumen_evento | 919.67 € (-0.49%) | 11 | 1 | 18% | -0.704% | -1.804% | -2.004% | -4.58 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 17:45 | reversion_bb | BCH | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 17:40 | macd_sin_salida | MINA | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 17:40 | estocastico_rebote | CRV | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-09-29 17:40 | reversion_bb | ZRO | stop-loss | -1.70% | -2.80% | -0.64 |
| 2026-09-29 17:35 | c_banda_atr_evento | VVV | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 17:35 | c_banda_atr_tope | VVV | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 17:35 | ruptura_estricta | JUP | stop-loss | -2.00% | -3.10% | -0.71 |
| 2026-09-29 17:35 | estocastico_rebote | ZRO | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 17:35 | pullback_tendencia | JUP | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 17:35 | c_banda_atr | VVV | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-09-29 17:25 | estocastico_rebote | BNB | timeout | -1.29% | -1.79% | -0.41 |
| 2026-09-29 17:25 | estocastico_rebote | DOT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 17:25 | estocastico_rebote | PUMP | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 17:25 | estocastico_rebote | NEAR | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 17:20 | ruptura_volumen_evento | JUP | stop-loss | -1.20% | -2.30% | -0.53 |

## Eventos de la última vuelta

- 2026-09-29 17:45 [reversion_bb] CIERRE BCH stop-loss bruto -1.50% neto -2.60%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
