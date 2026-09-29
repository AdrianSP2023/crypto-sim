# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 17:27 UTC · vueltas 93 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 909.95 € (-1.55%) | 52 | 3 | 35% | -0.136% | -1.138% | -1.277% | -13.66 € |
| reversion_bb | 918.98 € (-0.57%) | 10 | 6 | 20% | -0.912% | -2.012% | -2.122% | -4.64 € |
| ruptura_volumen | 909.50 € (-1.59%) | 70 | 1 | 27% | -0.044% | -0.917% | -1.054% | -14.76 € |
| rebote_extremo | 922.84 € (-0.15%) | 4 | 2 | 25% | -0.905% | -2.005% | -2.191% | -1.85 € |
| pullback_tendencia | 908.45 € (-1.71%) | 68 | 0 | 25% | -0.127% | -1.011% | -1.125% | -15.79 € |
| macd_momentum | 897.71 € (-2.87%) | 151 | 1 | 19% | -0.094% | -0.767% | -0.885% | -26.49 € |
| estocastico_rebote | 892.84 € (-3.40%) | 115 | 28 | 29% | -0.370% | -1.097% | -1.218% | -28.87 € |
| ruptura_estricta | 912.06 € (-1.32%) | 41 | 1 | 29% | -0.183% | -1.283% | -1.409% | -12.12 € |
| macd_sin_salida | 904.43 € (-2.14%) | 95 | 3 | 31% | -0.117% | -0.891% | -1.017% | -19.43 € |
| c_banda_atr_tope | 916.50 € (-0.84%) | 19 | 3 | 26% | -0.522% | -1.622% | -1.789% | -7.11 € |
| ruptura_volumen_tope | 919.13 € (-0.55%) | 21 | 1 | 19% | +0.041% | -1.059% | -1.189% | -5.13 € |
| c_banda_atr_regimen | 909.84 € (-1.56%) | 50 | 0 | 32% | -0.226% | -1.248% | -1.385% | -14.40 € |
| macd_momentum_regimen | 898.81 € (-2.75%) | 147 | 0 | 20% | -0.078% | -0.756% | -0.872% | -25.43 € |
| ruptura_volumen_regimen | 909.87 € (-1.55%) | 69 | 0 | 28% | -0.027% | -0.906% | -1.043% | -14.37 € |
| c_banda_atr_evento | 916.67 € (-0.82%) | 19 | 4 | 32% | -0.411% | -1.511% | -1.672% | -6.64 € |
| macd_momentum_evento | 912.12 € (-1.31%) | 31 | 1 | 13% | -0.590% | -1.690% | -1.815% | -12.08 € |
| ruptura_volumen_evento | 919.67 € (-0.49%) | 11 | 1 | 18% | -0.704% | -1.804% | -2.004% | -4.58 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 17:25 | estocastico_rebote | BNB | timeout | -1.29% | -1.79% | -0.41 |
| 2026-09-29 17:25 | estocastico_rebote | DOT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 17:25 | estocastico_rebote | PUMP | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 17:25 | estocastico_rebote | NEAR | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 17:20 | ruptura_volumen_evento | JUP | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-29 17:20 | ruptura_volumen_tope | JUP | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-29 17:20 | macd_sin_salida | ICP | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 17:20 | estocastico_rebote | BTC | timeout | -0.90% | -1.40% | -0.32 |
| 2026-09-29 17:20 | ruptura_volumen | JUP | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-29 17:15 | estocastico_rebote | RENDER | stop-loss | -1.58% | -2.08% | -0.47 |
| 2026-09-29 17:10 | macd_momentum_evento | MINA | momentum perdido | -0.68% | -1.78% | -0.41 |
| 2026-09-29 17:10 | macd_momentum | MINA | momentum perdido | -0.68% | -1.18% | -0.27 |
| 2026-09-29 17:10 | reversion_bb | ATOM | stop-loss | -1.59% | -2.69% | -0.62 |
| 2026-09-29 17:05 | estocastico_rebote | RAY | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-29 17:05 | estocastico_rebote | ENA | stop-loss | -1.50% | -2.00% | -0.45 |

## Eventos de la última vuelta

- 2026-09-29 17:25 [estocastico_rebote] CIERRE NEAR stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 17:25 [estocastico_rebote] CIERRE PUMP stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 17:25 [estocastico_rebote] CIERRE DOT stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 17:25 [estocastico_rebote] CIERRE BNB timeout bruto -1.29% neto -1.79%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
