# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 08:41 UTC · vueltas 393 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 892.40 € (-3.45%) | 338 | 24 | 40% | +0.140% | -0.437% | -0.557% | -33.69 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 864.30 € (-6.49%) | 417 | 23 | 27% | -0.090% | -0.652% | -0.762% | -60.99 € |
| rebote_extremo | 922.42 € (-0.20%) | 15 | 0 | 60% | +0.574% | -0.526% | -0.706% | -1.82 € |
| pullback_tendencia | 890.65 € (-3.63%) | 239 | 8 | 21% | -0.032% | -0.642% | -0.729% | -34.86 € |
| macd_momentum | 859.51 € (-7.00%) | 649 | 39 | 23% | +0.055% | -0.485% | -0.587% | -70.14 € |
| estocastico_rebote | 885.31 € (-4.21%) | 395 | 33 | 37% | +0.074% | -0.492% | -0.601% | -44.12 € |
| ruptura_estricta | 882.80 € (-4.48%) | 237 | 6 | 32% | -0.154% | -0.765% | -0.882% | -41.27 € |
| macd_sin_salida | 885.22 € (-4.22%) | 436 | 38 | 40% | +0.114% | -0.445% | -0.556% | -44.22 € |
| c_banda_atr_tope | 913.68 € (-1.14%) | 77 | 5 | 38% | +0.227% | -0.616% | -0.732% | -10.91 € |
| ruptura_volumen_tope | 901.69 € (-2.44%) | 128 | 5 | 24% | -0.088% | -0.794% | -0.908% | -23.22 € |
| c_banda_atr_regimen | 905.06 € (-2.08%) | 190 | 24 | 41% | +0.155% | -0.483% | -0.611% | -21.12 € |
| macd_momentum_regimen | 882.52 € (-4.51%) | 412 | 39 | 22% | +0.055% | -0.508% | -0.612% | -47.25 € |
| ruptura_volumen_regimen | 868.99 € (-5.98%) | 340 | 23 | 25% | -0.160% | -0.737% | -0.851% | -56.30 € |
| c_banda_atr_evento | 898.34 € (-2.80%) | 305 | 24 | 41% | +0.189% | -0.398% | -0.513% | -27.76 € |
| macd_momentum_evento | 864.27 € (-6.49%) | 602 | 39 | 22% | +0.057% | -0.487% | -0.586% | -65.41 € |
| ruptura_volumen_evento | 876.60 € (-5.15%) | 367 | 23 | 28% | -0.017% | -0.589% | -0.693% | -48.70 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
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
| 2026-10-02 08:30 | pullback_tendencia | AAVE | rotura de tendencia | -1.09% | -1.59% | -0.35 |
| 2026-10-02 08:25 | c_banda_atr_evento | CRV | timeout | +1.61% | +1.11% | +0.25 |
| 2026-10-02 08:25 | c_banda_atr_evento | LTC | timeout | +1.35% | +0.85% | +0.19 |

## Eventos de la última vuelta

- 2026-10-02 08:40 [ruptura_volumen] CIERRE VVV take-profit bruto +2.50% neto +2.00%
- 2026-10-02 08:40 [macd_momentum] CIERRE VVV take-profit bruto +2.00% neto +1.50%
- 2026-10-02 08:40 [ruptura_estricta] CIERRE VVV take-profit bruto +3.00% neto +2.50%
- 2026-10-02 08:40 [macd_momentum_regimen] CIERRE VVV take-profit bruto +2.00% neto +1.50%
- 2026-10-02 08:40 [ruptura_volumen_regimen] CIERRE VVV take-profit bruto +2.50% neto +2.00%
- 2026-10-02 08:40 [macd_momentum_evento] CIERRE VVV take-profit bruto +2.00% neto +1.50%
- 2026-10-02 08:40 [ruptura_volumen_evento] CIERRE VVV take-profit bruto +2.50% neto +2.00%
- 2026-10-02 08:40 [estocastico_rebote] CIERRE SHIB take-profit bruto +1.80% neto +1.30%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
