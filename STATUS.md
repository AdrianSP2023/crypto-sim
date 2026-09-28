# Simulación P1 (sin dinero real)

Config `P1-v8` · inicio 2026-09-28 08:49 UTC · última vuelta 2026-09-28 17:46 UTC · vueltas 109 · 60 activos · velas 5 min · comisión 1.1% ida+vuelta

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 897.49 € (-2.89%) | 48 | 29 | 29% | -0.350% | -1.450% | -1.568% | -24.06 € |
| reversion_bb | 924.65 € (+0.04%) | 7 | 0 | 86% | +1.124% | +0.024% | -0.188% | +0.41 € |
| ruptura_volumen | 893.10 € (-3.37%) | 60 | 10 | 15% | -0.451% | -1.551% | -1.675% | -31.25 € |
| rebote_extremo | 922.71 € (-0.17%) | 7 | 0 | 71% | +0.910% | -0.190% | -0.602% | -1.53 € |
| pullback_tendencia | 914.35 € (-1.07%) | 29 | 4 | 28% | -0.183% | -1.283% | -1.406% | -10.08 € |
| macd_momentum | 911.58 € (-1.37%) | 31 | 20 | 16% | -0.311% | -1.411% | -1.547% | -11.30 € |
| estocastico_rebote | 907.64 € (-1.80%) | 39 | 8 | 26% | -0.626% | -1.726% | -1.825% | -16.68 € |
| c_banda_atr_filtro | 917.38 € (-0.74%) | 9 | 28 | 22% | -0.745% | -1.845% | -2.000% | -3.83 € |
| ruptura_volumen_filtro | 917.17 € (-0.76%) | 15 | 10 | 7% | -0.976% | -2.076% | -2.201% | -7.18 € |
| macd_momentum_filtro | 921.75 € (-0.27%) | 3 | 18 | 33% | -0.198% | -1.298% | -1.504% | -0.90 € |
| pullback_tendencia_filtro | 922.95 € (-0.14%) | 5 | 4 | 40% | +0.131% | -0.969% | -1.073% | -1.12 € |
| estocastico_rebote_filtro | 924.25 € (+0.00%) | 1 | 6 | 100% | +1.800% | +0.700% | +0.567% | +0.16 € |
| ruptura_estricta | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-28 17:45 | pullback_tendencia_filtro | MON | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-28 17:45 | pullback_tendencia | MON | stop-loss | -1.50% | -2.60% | -0.59 |
| 2026-09-28 17:40 | c_banda_atr_filtro | OP | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-28 17:40 | c_banda_atr | WLFI | timeout | +1.21% | +0.10% | +0.02 |
| 2026-09-28 17:40 | c_banda_atr | OP | stop-loss | -1.50% | -2.60% | -0.59 |
| 2026-09-28 17:35 | pullback_tendencia_filtro | HBAR | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-28 17:35 | macd_momentum_filtro | UNI | momentum perdido | -0.78% | -1.88% | -0.43 |
| 2026-09-28 17:35 | estocastico_rebote | TRX | timeout | +0.07% | -1.03% | -0.24 |
| 2026-09-28 17:35 | macd_momentum | UNI | momentum perdido | -0.78% | -1.88% | -0.43 |
| 2026-09-28 17:35 | pullback_tendencia | HBAR | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-28 17:30 | pullback_tendencia_filtro | PUMP | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-28 17:30 | ruptura_volumen_filtro | CRV | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-28 17:30 | ruptura_volumen_filtro | XLM | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-28 17:30 | ruptura_volumen_filtro | ARB | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-28 17:30 | c_banda_atr_filtro | VIRTUAL | stop-loss | -1.50% | -2.60% | -0.60 |

## Eventos de la última vuelta

- 2026-09-28 17:45 [estocastico_rebote] ENTRADA PUMP @ 0.004651 (22.69 €)
- 2026-09-28 17:45 [pullback_tendencia_filtro] ENTRADA PUMP @ 0.004651 (23.09 €)
- 2026-09-28 17:45 [estocastico_rebote_filtro] ENTRADA PUMP @ 0.004651 (23.11 €)
- 2026-09-28 17:45 [pullback_tendencia] CIERRE MON stop-loss bruto -1.50% neto -2.60%
- 2026-09-28 17:45 [pullback_tendencia_filtro] CIERRE MON stop-loss bruto -1.50% neto -2.60%
- 2026-09-28 17:45 [estocastico_rebote] ENTRADA VIRTUAL @ 0.7135 (22.69 €)
- 2026-09-28 17:45 [estocastico_rebote_filtro] ENTRADA VIRTUAL @ 0.7135 (23.11 €)

Universo: BTC, SOL, ETH, XRP, SUI, NEAR, LINK, ZEC, LTC, HBAR, ONDO, ADA, UNI, PUMP, TAO, ARB, AVAX, DOGE, BCH, ENA, XLM, XDC, HYPE, DOT, AAVE, ALGO, PEPE, MON, POL, DASH, XPL, JUP, W, GRT, USELESS, FET, ZRO, SEI, ATOM, WLD, INJ, FIL, ICP, TRX, RENDER, PENGU, TON, VVV, RAY, SHIB, SKY, TRUMP, CRV, VIRTUAL, OP, NIGHT, KAS, CC, EIGEN, WLFI
