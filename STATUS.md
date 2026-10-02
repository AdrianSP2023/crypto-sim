# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 08:51 UTC · vueltas 395 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 891.95 € (-3.49%) | 338 | 24 | 40% | +0.140% | -0.437% | -0.557% | -33.69 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 863.53 € (-6.57%) | 417 | 25 | 27% | -0.090% | -0.652% | -0.762% | -60.99 € |
| rebote_extremo | 922.42 € (-0.20%) | 15 | 0 | 60% | +0.574% | -0.526% | -0.706% | -1.82 € |
| pullback_tendencia | 890.40 € (-3.66%) | 239 | 8 | 21% | -0.032% | -0.642% | -0.729% | -34.86 € |
| macd_momentum | 858.52 € (-7.11%) | 649 | 39 | 23% | +0.055% | -0.485% | -0.587% | -70.14 € |
| estocastico_rebote | 884.31 € (-4.32%) | 398 | 32 | 37% | +0.075% | -0.490% | -0.598% | -44.27 € |
| ruptura_estricta | 882.55 € (-4.51%) | 237 | 6 | 32% | -0.154% | -0.765% | -0.882% | -41.27 € |
| macd_sin_salida | 884.04 € (-4.35%) | 436 | 38 | 40% | +0.114% | -0.445% | -0.556% | -44.22 € |
| c_banda_atr_tope | 913.56 € (-1.16%) | 77 | 5 | 38% | +0.227% | -0.616% | -0.732% | -10.91 € |
| ruptura_volumen_tope | 901.50 € (-2.46%) | 128 | 5 | 24% | -0.088% | -0.794% | -0.908% | -23.22 € |
| c_banda_atr_regimen | 904.61 € (-2.12%) | 190 | 24 | 41% | +0.155% | -0.483% | -0.611% | -21.12 € |
| macd_momentum_regimen | 881.50 € (-4.62%) | 412 | 39 | 22% | +0.055% | -0.508% | -0.612% | -47.25 € |
| ruptura_volumen_regimen | 868.22 € (-6.06%) | 340 | 25 | 25% | -0.160% | -0.737% | -0.851% | -56.30 € |
| c_banda_atr_evento | 897.89 € (-2.85%) | 305 | 24 | 41% | +0.189% | -0.398% | -0.513% | -27.76 € |
| macd_momentum_evento | 863.27 € (-6.60%) | 602 | 39 | 22% | +0.057% | -0.487% | -0.586% | -65.41 € |
| ruptura_volumen_evento | 875.82 € (-5.24%) | 367 | 25 | 28% | -0.017% | -0.589% | -0.693% | -48.70 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 08:50 | estocastico_rebote | BNB | timeout | +0.20% | -0.30% | -0.07 |
| 2026-10-02 08:50 | estocastico_rebote | BTC | timeout | +0.31% | -0.19% | -0.04 |
| 2026-10-02 08:45 | estocastico_rebote | FET | timeout | +0.33% | -0.17% | -0.04 |
| 2026-10-02 08:40 | ruptura_volumen_evento | VVV | take-profit | +2.50% | +2.00% | +0.44 |
| 2026-10-02 08:40 | macd_momentum_evento | VVV | take-profit | +2.00% | +1.50% | +0.32 |
| 2026-10-02 08:40 | ruptura_volumen_regimen | VVV | take-profit | +2.50% | +2.00% | +0.43 |
| 2026-10-02 08:40 | macd_momentum_regimen | VVV | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 08:40 | ruptura_estricta | VVV | take-profit | +3.00% | +2.50% | +0.55 |
| 2026-10-02 08:40 | estocastico_rebote | SHIB | take-profit | +1.80% | +1.30% | +0.28 |
| 2026-10-02 08:40 | macd_momentum | VVV | take-profit | +2.00% | +1.50% | +0.32 |
| 2026-10-02 08:40 | ruptura_volumen | VVV | take-profit | +2.50% | +2.00% | +0.43 |
| 2026-10-02 08:35 | macd_sin_salida | FIL | timeout | +0.43% | -0.07% | -0.01 |
| 2026-10-02 08:35 | macd_sin_salida | AAVE | stop-loss | -1.55% | -2.05% | -0.45 |
| 2026-10-02 08:35 | ruptura_estricta | ASTER | timeout | +0.70% | +0.20% | +0.04 |
| 2026-10-02 08:30 | estocastico_rebote | TON | timeout | -0.36% | -0.86% | -0.19 |

## Eventos de la última vuelta

- 2026-10-02 08:50 [estocastico_rebote] CIERRE BTC timeout bruto +0.31% neto -0.19%
- 2026-10-02 08:50 [estocastico_rebote] CIERRE BNB timeout bruto +0.20% neto -0.30%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
