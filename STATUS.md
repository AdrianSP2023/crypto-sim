# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 07:11 UTC · vueltas 233 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 890.55 € (-3.65%) | 138 | 16 | 25% | -0.319% | -1.008% | -1.138% | -31.75 € |
| reversion_bb | 914.39 € (-1.07%) | 38 | 8 | 42% | +0.066% | -1.034% | -1.145% | -9.05 € |
| ruptura_volumen | 885.33 € (-4.21%) | 174 | 4 | 17% | -0.325% | -0.975% | -1.104% | -38.50 € |
| rebote_extremo | 922.81 € (-0.16%) | 8 | 2 | 50% | +0.378% | -0.722% | -0.879% | -1.33 € |
| pullback_tendencia | 902.69 € (-2.33%) | 119 | 0 | 24% | -0.072% | -0.791% | -0.916% | -21.55 € |
| macd_momentum | 874.72 € (-5.36%) | 321 | 2 | 16% | -0.105% | -0.686% | -0.796% | -49.69 € |
| estocastico_rebote | 886.13 € (-4.12%) | 216 | 15 | 34% | -0.134% | -0.755% | -0.887% | -37.11 € |
| ruptura_estricta | 901.64 € (-2.45%) | 73 | 7 | 22% | -0.453% | -1.311% | -1.451% | -21.92 € |
| macd_sin_salida | 885.73 € (-4.17%) | 193 | 16 | 27% | -0.195% | -0.830% | -0.955% | -36.40 € |
| c_banda_atr_tope | 909.20 € (-1.63%) | 41 | 2 | 17% | -0.500% | -1.600% | -1.726% | -15.06 € |
| ruptura_volumen_tope | 908.15 € (-1.74%) | 63 | 1 | 16% | -0.208% | -1.127% | -1.246% | -16.28 € |
| c_banda_atr_regimen | 900.68 € (-2.55%) | 78 | 0 | 22% | -0.483% | -1.317% | -1.445% | -23.56 € |
| macd_momentum_regimen | 885.34 € (-4.21%) | 202 | 0 | 14% | -0.219% | -0.848% | -0.963% | -38.90 € |
| ruptura_volumen_regimen | 895.38 € (-3.12%) | 123 | 3 | 17% | -0.301% | -1.014% | -1.145% | -28.43 € |
| c_banda_atr_evento | 893.58 € (-3.32%) | 106 | 16 | 22% | -0.436% | -1.185% | -1.315% | -28.71 € |
| macd_momentum_evento | 887.02 € (-4.03%) | 201 | 2 | 13% | -0.188% | -0.819% | -0.924% | -37.39 € |
| ruptura_volumen_evento | 890.78 € (-3.62%) | 115 | 4 | 10% | -0.532% | -1.262% | -1.392% | -33.04 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 07:10 | c_banda_atr_evento | ASTER | timeout | -0.20% | -0.70% | -0.16 |
| 2026-09-30 07:10 | c_banda_atr_tope | ASTER | timeout | -0.20% | -1.30% | -0.30 |
| 2026-09-30 07:10 | macd_sin_salida | SHIB | timeout | -0.53% | -1.03% | -0.23 |
| 2026-09-30 07:10 | macd_sin_salida | RENDER | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 07:10 | macd_sin_salida | CRV | timeout | +0.53% | +0.03% | +0.01 |
| 2026-09-30 07:10 | macd_sin_salida | TAO | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 07:10 | reversion_bb | AVAX | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-30 07:10 | c_banda_atr | ASTER | timeout | -0.20% | -0.70% | -0.16 |
| 2026-09-30 07:05 | ruptura_volumen_evento | SHIB | stop-loss | -1.33% | -1.83% | -0.41 |
| 2026-09-30 07:05 | ruptura_volumen_evento | MINA | stop-loss | -1.41% | -1.91% | -0.43 |
| 2026-09-30 07:05 | c_banda_atr_evento | GRT | stop-loss | -1.68% | -2.18% | -0.49 |
| 2026-09-30 07:05 | c_banda_atr_evento | OP | stop-loss | -1.56% | -2.06% | -0.46 |
| 2026-09-30 07:05 | ruptura_volumen_regimen | SHIB | stop-loss | -1.33% | -1.83% | -0.41 |
| 2026-09-30 07:05 | ruptura_volumen_regimen | MINA | stop-loss | -1.41% | -1.91% | -0.43 |
| 2026-09-30 07:05 | estocastico_rebote | SUI | timeout | +0.32% | -0.18% | -0.04 |

## Eventos de la última vuelta

- 2026-09-30 07:10 [reversion_bb] CIERRE AVAX stop-loss bruto -1.50% neto -2.60%
- 2026-09-30 07:10 [macd_sin_salida] CIERRE TAO stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 07:10 [macd_sin_salida] CIERRE CRV timeout bruto +0.53% neto +0.03%
- 2026-09-30 07:05 [c_banda_atr_tope] ENTRADA MON @ 0.02358 (22.74 €, apertura)
- 2026-09-30 07:05 [c_banda_atr] ENTRADA VVV @ 23.535 (22.32 €, apertura)
- 2026-09-30 07:05 [c_banda_atr_tope] ENTRADA VVV @ 23.535 (22.74 €, apertura)
- 2026-09-30 07:05 [c_banda_atr_evento] ENTRADA VVV @ 23.535 (22.39 €, apertura)
- 2026-09-30 07:10 [macd_sin_salida] CIERRE RENDER stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 07:10 [macd_sin_salida] CIERRE SHIB timeout bruto -0.53% neto -1.03%
- 2026-09-30 07:10 [c_banda_atr] CIERRE ASTER timeout bruto -0.20% neto -0.70%
- 2026-09-30 07:10 [c_banda_atr_tope] CIERRE ASTER timeout bruto -0.20% neto -1.30%
- 2026-09-30 07:10 [c_banda_atr_evento] CIERRE ASTER timeout bruto -0.20% neto -0.70%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
