# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 07:06 UTC · vueltas 232 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 890.99 € (-3.60%) | 137 | 16 | 26% | -0.319% | -1.010% | -1.141% | -31.59 € |
| reversion_bb | 914.70 € (-1.03%) | 37 | 9 | 43% | +0.108% | -0.992% | -1.105% | -8.45 € |
| ruptura_volumen | 885.44 € (-4.20%) | 174 | 4 | 17% | -0.325% | -0.975% | -1.104% | -38.50 € |
| rebote_extremo | 922.82 € (-0.15%) | 8 | 2 | 50% | +0.378% | -0.722% | -0.879% | -1.33 € |
| pullback_tendencia | 902.69 € (-2.33%) | 119 | 0 | 24% | -0.072% | -0.791% | -0.916% | -21.55 € |
| macd_momentum | 874.70 € (-5.36%) | 321 | 2 | 16% | -0.105% | -0.686% | -0.796% | -49.69 € |
| estocastico_rebote | 886.11 € (-4.13%) | 216 | 15 | 34% | -0.134% | -0.755% | -0.887% | -37.11 € |
| ruptura_estricta | 901.82 € (-2.43%) | 73 | 7 | 22% | -0.453% | -1.311% | -1.451% | -21.92 € |
| macd_sin_salida | 886.66 € (-4.07%) | 189 | 20 | 28% | -0.183% | -0.821% | -0.947% | -35.28 € |
| c_banda_atr_tope | 909.43 € (-1.60%) | 40 | 1 | 18% | -0.507% | -1.607% | -1.736% | -14.76 € |
| ruptura_volumen_tope | 908.15 € (-1.74%) | 63 | 1 | 16% | -0.208% | -1.127% | -1.246% | -16.28 € |
| c_banda_atr_regimen | 900.68 € (-2.55%) | 78 | 0 | 22% | -0.483% | -1.317% | -1.445% | -23.56 € |
| macd_momentum_regimen | 885.34 € (-4.21%) | 202 | 0 | 14% | -0.219% | -0.848% | -0.963% | -38.90 € |
| ruptura_volumen_regimen | 895.43 € (-3.12%) | 123 | 3 | 17% | -0.301% | -1.014% | -1.145% | -28.43 € |
| c_banda_atr_evento | 894.02 € (-3.27%) | 105 | 16 | 22% | -0.438% | -1.189% | -1.321% | -28.55 € |
| macd_momentum_evento | 887.00 € (-4.03%) | 201 | 2 | 13% | -0.188% | -0.819% | -0.924% | -37.39 € |
| ruptura_volumen_evento | 890.89 € (-3.61%) | 115 | 4 | 10% | -0.532% | -1.262% | -1.392% | -33.04 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 07:05 | ruptura_volumen_evento | SHIB | stop-loss | -1.33% | -1.83% | -0.41 |
| 2026-09-30 07:05 | ruptura_volumen_evento | MINA | stop-loss | -1.41% | -1.91% | -0.43 |
| 2026-09-30 07:05 | c_banda_atr_evento | GRT | stop-loss | -1.68% | -2.18% | -0.49 |
| 2026-09-30 07:05 | c_banda_atr_evento | OP | stop-loss | -1.56% | -2.06% | -0.46 |
| 2026-09-30 07:05 | ruptura_volumen_regimen | SHIB | stop-loss | -1.33% | -1.83% | -0.41 |
| 2026-09-30 07:05 | ruptura_volumen_regimen | MINA | stop-loss | -1.41% | -1.91% | -0.43 |
| 2026-09-30 07:05 | estocastico_rebote | SUI | timeout | +0.32% | -0.18% | -0.04 |
| 2026-09-30 07:05 | ruptura_volumen | SHIB | stop-loss | -1.33% | -1.83% | -0.41 |
| 2026-09-30 07:05 | ruptura_volumen | MINA | stop-loss | -1.41% | -1.91% | -0.43 |
| 2026-09-30 07:05 | reversion_bb | PUMP | stop-loss | -1.62% | -2.72% | -0.62 |
| 2026-09-30 07:05 | c_banda_atr | GRT | stop-loss | -1.68% | -2.18% | -0.49 |
| 2026-09-30 07:05 | c_banda_atr | OP | stop-loss | -1.56% | -2.06% | -0.46 |
| 2026-09-30 07:00 | c_banda_atr_evento | RENDER | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 07:00 | macd_sin_salida | KAS | timeout | +0.36% | -0.14% | -0.03 |
| 2026-09-30 07:00 | macd_sin_salida | POL | stop-loss | -1.66% | -2.16% | -0.48 |

## Eventos de la última vuelta

- 2026-09-30 07:05 [estocastico_rebote] CIERRE SUI timeout bruto +0.32% neto -0.18%
- 2026-09-30 07:05 [reversion_bb] CIERRE PUMP stop-loss bruto -1.62% neto -2.72%
- 2026-09-30 07:00 [estocastico_rebote] ENTRADA CRV @ 0.34388 (22.18 €, apertura)
- 2026-09-30 07:00 [estocastico_rebote] ENTRADA VIRTUAL @ 0.69 (22.18 €, apertura)
- 2026-09-30 07:05 [ruptura_volumen] CIERRE MINA stop-loss bruto -1.41% neto -1.91%
- 2026-09-30 07:05 [ruptura_volumen_regimen] CIERRE MINA stop-loss bruto -1.41% neto -1.91%
- 2026-09-30 07:05 [ruptura_volumen_evento] CIERRE MINA stop-loss bruto -1.41% neto -1.91%
- 2026-09-30 07:05 [c_banda_atr] CIERRE OP stop-loss bruto -1.56% neto -2.06%
- 2026-09-30 07:05 [c_banda_atr_evento] CIERRE OP stop-loss bruto -1.56% neto -2.06%
- 2026-09-30 07:05 [ruptura_volumen] CIERRE SHIB stop-loss bruto -1.33% neto -1.83%
- 2026-09-30 07:05 [ruptura_volumen_regimen] CIERRE SHIB stop-loss bruto -1.33% neto -1.83%
- 2026-09-30 07:05 [ruptura_volumen_evento] CIERRE SHIB stop-loss bruto -1.33% neto -1.83%
- 2026-09-30 07:05 [c_banda_atr] CIERRE GRT stop-loss bruto -1.68% neto -2.18%
- 2026-09-30 07:05 [c_banda_atr_evento] CIERRE GRT stop-loss bruto -1.68% neto -2.18%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
