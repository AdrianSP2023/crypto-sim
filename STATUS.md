# Simulación P1 (sin dinero real)

Config `P1-v9` · inicio 2026-09-28 08:49 UTC · última vuelta 2026-09-28 20:56 UTC · vueltas 147 · 60 activos · velas 5 min · comisión 1.1% ida+vuelta

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 877.07 € (-5.10%) | 86 | 18 | 17% | -0.819% | -1.919% | -2.039% | -45.56 € |
| reversion_bb | 924.50 € (+0.03%) | 12 | 7 | 75% | +0.836% | -0.264% | -0.473% | -0.36 € |
| ruptura_volumen | 886.34 € (-4.10%) | 79 | 2 | 14% | -0.443% | -1.543% | -1.666% | -37.69 € |
| rebote_extremo | 922.84 € (-0.15%) | 7 | 3 | 71% | +0.910% | -0.190% | -0.602% | -1.53 € |
| pullback_tendencia | 908.44 € (-1.71%) | 44 | 3 | 20% | -0.340% | -1.440% | -1.542% | -16.06 € |
| macd_momentum | 895.64 € (-3.09%) | 78 | 11 | 12% | -0.397% | -1.497% | -1.610% | -27.88 € |
| estocastico_rebote | 902.73 € (-2.33%) | 60 | 12 | 30% | -0.380% | -1.480% | -1.577% | -21.55 € |
| c_banda_atr_filtro | 899.71 € (-2.65%) | 44 | 2 | 7% | -1.296% | -2.396% | -2.522% | -24.31 € |
| ruptura_volumen_filtro | 910.44 € (-1.49%) | 34 | 0 | 9% | -0.664% | -1.764% | -1.886% | -13.80 € |
| macd_momentum_filtro | 911.02 € (-1.43%) | 40 | 0 | 12% | -0.335% | -1.435% | -1.538% | -13.22 € |
| pullback_tendencia_filtro | 917.83 € (-0.69%) | 18 | 0 | 17% | -0.443% | -1.543% | -1.609% | -6.41 € |
| estocastico_rebote_filtro | 920.42 € (-0.41%) | 11 | 2 | 27% | -0.318% | -1.418% | -1.547% | -3.60 € |
| ruptura_estricta | 921.76 € (-0.27%) | 5 | 0 | 20% | -1.045% | -2.145% | -2.276% | -2.48 € |
| macd_sin_salida | 920.49 € (-0.41%) | 4 | 14 | 0% | -1.500% | -2.600% | -2.713% | -2.40 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-28 20:55 | macd_sin_salida | CRV | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-28 20:55 | macd_sin_salida | ENA | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-28 20:55 | ruptura_volumen_filtro | TRX | timeout | -0.18% | -1.28% | -0.29 |
| 2026-09-28 20:55 | macd_momentum | VVV | momentum perdido | -0.93% | -2.03% | -0.46 |
| 2026-09-28 20:55 | macd_momentum | MON | momentum perdido | -0.98% | -2.08% | -0.47 |
| 2026-09-28 20:55 | ruptura_volumen | TRX | timeout | -0.18% | -1.28% | -0.28 |
| 2026-09-28 20:50 | estocastico_rebote | HBAR | take-profit | +1.80% | +0.70% | +0.16 |
| 2026-09-28 20:50 | macd_momentum | CRV | momentum perdido | -0.86% | -1.96% | -0.44 |
| 2026-09-28 20:50 | macd_momentum | INJ | momentum perdido | -1.11% | -2.21% | -0.50 |
| 2026-09-28 20:50 | macd_momentum | ENA | momentum perdido | -1.43% | -2.53% | -0.57 |
| 2026-09-28 20:50 | c_banda_atr | MON | stop-loss | -1.50% | -2.60% | -0.57 |
| 2026-09-28 20:45 | macd_sin_salida | PUMP | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-28 20:45 | c_banda_atr_filtro | TRX | timeout | +0.40% | -0.70% | -0.16 |
| 2026-09-28 20:45 | macd_momentum | PUMP | stop-loss | -1.50% | -2.60% | -0.58 |
| 2026-09-28 20:45 | c_banda_atr | PUMP | stop-loss | -1.50% | -2.60% | -0.57 |

## Eventos de la última vuelta

- 2026-09-28 20:55 [macd_sin_salida] CIERRE ENA stop-loss bruto -1.50% neto -2.60%
- 2026-09-28 20:55 [macd_momentum] CIERRE MON momentum perdido bruto -0.98% neto -2.08%
- 2026-09-28 20:55 [ruptura_volumen] CIERRE TRX timeout bruto -0.18% neto -1.28%
- 2026-09-28 20:55 [ruptura_volumen_filtro] CIERRE TRX timeout bruto -0.18% neto -1.28%
- 2026-09-28 20:55 [macd_momentum] CIERRE VVV momentum perdido bruto -0.93% neto -2.03%
- 2026-09-28 20:55 [macd_sin_salida] CIERRE CRV stop-loss bruto -1.50% neto -2.60%
- 2026-09-28 20:55 [c_banda_atr] ENTRADA KAS @ 0.03976 (21.97 €)

Universo: BTC, SOL, ETH, XRP, SUI, NEAR, LINK, ZEC, LTC, HBAR, ONDO, ADA, UNI, PUMP, TAO, ARB, AVAX, DOGE, BCH, ENA, XLM, XDC, HYPE, DOT, AAVE, ALGO, PEPE, MON, POL, DASH, XPL, JUP, W, GRT, USELESS, FET, ZRO, SEI, ATOM, WLD, INJ, FIL, ICP, TRX, RENDER, PENGU, TON, VVV, RAY, SHIB, SKY, TRUMP, CRV, VIRTUAL, OP, NIGHT, KAS, CC, EIGEN, WLFI
