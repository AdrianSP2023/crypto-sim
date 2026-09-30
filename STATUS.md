# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 09:26 UTC · vueltas 199 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 895.40 € (-3.12%) | 152 | 33 | 27% | -0.238% | -0.910% | -1.042% | -31.59 € |
| reversion_bb | 915.05 € (-0.99%) | 42 | 4 | 40% | +0.092% | -1.001% | -1.113% | -9.68 € |
| ruptura_volumen | 886.07 € (-4.13%) | 187 | 19 | 19% | -0.271% | -0.911% | -1.042% | -38.65 € |
| rebote_extremo | 923.50 € (-0.08%) | 9 | 1 | 56% | +0.558% | -0.542% | -0.703% | -1.13 € |
| pullback_tendencia | 901.57 € (-2.45%) | 123 | 3 | 24% | -0.094% | -0.806% | -0.933% | -22.68 € |
| macd_momentum | 875.37 € (-5.29%) | 343 | 28 | 17% | -0.077% | -0.653% | -0.764% | -50.52 € |
| estocastico_rebote | 888.61 € (-3.85%) | 226 | 11 | 35% | -0.093% | -0.708% | -0.842% | -36.48 € |
| ruptura_estricta | 902.19 € (-2.39%) | 81 | 7 | 22% | -0.396% | -1.218% | -1.368% | -22.60 € |
| macd_sin_salida | 888.83 € (-3.83%) | 214 | 32 | 28% | -0.147% | -0.769% | -0.890% | -37.38 € |
| c_banda_atr_tope | 910.17 € (-1.52%) | 42 | 5 | 19% | -0.440% | -1.540% | -1.669% | -14.85 € |
| ruptura_volumen_tope | 908.45 € (-1.71%) | 67 | 5 | 18% | -0.140% | -1.034% | -1.158% | -15.89 € |
| c_banda_atr_regimen | 900.55 € (-2.56%) | 78 | 6 | 22% | -0.483% | -1.317% | -1.445% | -23.56 € |
| macd_momentum_regimen | 885.11 € (-4.23%) | 203 | 11 | 14% | -0.221% | -0.850% | -0.963% | -39.15 € |
| ruptura_volumen_regimen | 894.81 € (-3.18%) | 129 | 10 | 17% | -0.297% | -0.999% | -1.130% | -29.37 € |
| c_banda_atr_evento | 898.45 € (-2.79%) | 120 | 33 | 24% | -0.320% | -1.040% | -1.173% | -28.54 € |
| macd_momentum_evento | 887.68 € (-3.96%) | 223 | 28 | 15% | -0.137% | -0.755% | -0.863% | -38.23 € |
| ruptura_volumen_evento | 891.53 € (-3.54%) | 128 | 19 | 12% | -0.432% | -1.139% | -1.273% | -33.19 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 09:25 | ruptura_volumen_evento | CRV | take-profit | +2.50% | +2.00% | +0.45 |
| 2026-09-30 09:25 | ruptura_volumen_tope | CRV | take-profit | +2.50% | +2.00% | +0.45 |
| 2026-09-30 09:25 | ruptura_volumen | CRV | take-profit | +2.50% | +2.00% | +0.44 |
| 2026-09-30 09:20 | ruptura_volumen_evento | NIGHT | take-profit | +2.50% | +2.00% | +0.45 |
| 2026-09-30 09:20 | ruptura_volumen_evento | HBAR | timeout | -0.10% | -0.60% | -0.13 |
| 2026-09-30 09:20 | macd_momentum_evento | HBAR | momentum perdido | -0.62% | -1.12% | -0.25 |
| 2026-09-30 09:20 | ruptura_volumen_regimen | NIGHT | take-profit | +2.50% | +2.00% | +0.45 |
| 2026-09-30 09:20 | macd_momentum_regimen | HBAR | momentum perdido | -0.62% | -1.12% | -0.25 |
| 2026-09-30 09:20 | ruptura_volumen_tope | HBAR | timeout | -0.10% | -0.60% | -0.14 |
| 2026-09-30 09:20 | macd_momentum | HBAR | momentum perdido | -0.62% | -1.12% | -0.24 |
| 2026-09-30 09:20 | ruptura_volumen | NIGHT | take-profit | +2.50% | +2.00% | +0.44 |
| 2026-09-30 09:20 | ruptura_volumen | HBAR | timeout | -0.10% | -0.60% | -0.13 |
| 2026-09-30 09:20 | reversion_bb | DOGE | timeout | +0.74% | -0.06% | -0.01 |
| 2026-09-30 09:20 | reversion_bb | ARB | timeout | +0.50% | -0.60% | -0.14 |
| 2026-09-30 09:15 | macd_momentum_evento | CRV | take-profit | +2.00% | +1.50% | +0.33 |

## Eventos de la última vuelta

- 2026-09-30 09:20 [ruptura_volumen] ENTRADA ONDO @ 0.44338 (22.13 €, apertura)
- 2026-09-30 09:20 [ruptura_volumen_regimen] ENTRADA ONDO @ 0.44338 (22.37 €, apertura)
- 2026-09-30 09:20 [ruptura_volumen_evento] ENTRADA ONDO @ 0.44338 (22.27 €, apertura)
- 2026-09-30 09:25 [ruptura_volumen] CIERRE CRV take-profit bruto +2.50% neto +2.00%
- 2026-09-30 09:25 [ruptura_volumen_tope] CIERRE CRV take-profit bruto +2.50% neto +2.00%
- 2026-09-30 09:25 [ruptura_volumen_evento] CIERRE CRV take-profit bruto +2.50% neto +2.00%
- 2026-09-30 09:20 [macd_momentum] ENTRADA MON @ 0.02391 (21.84 €, apertura)
- 2026-09-30 09:20 [macd_sin_salida] ENTRADA MON @ 0.02391 (22.17 €, apertura)
- 2026-09-30 09:20 [macd_momentum_regimen] ENTRADA MON @ 0.02391 (22.13 €, apertura)
- 2026-09-30 09:20 [macd_momentum_evento] ENTRADA MON @ 0.02391 (22.15 €, apertura)
- 2026-09-30 09:20 [ruptura_volumen] ENTRADA BCH @ 272.18 (22.14 €, apertura)
- 2026-09-30 09:20 [ruptura_volumen_tope] ENTRADA BCH @ 272.18 (22.71 €, apertura)
- 2026-09-30 09:20 [ruptura_volumen_regimen] ENTRADA BCH @ 272.18 (22.37 €, apertura)
- 2026-09-30 09:20 [ruptura_volumen_evento] ENTRADA BCH @ 272.18 (22.28 €, apertura)
- 2026-09-30 09:20 [pullback_tendencia] ENTRADA ASTER @ 0.67263 (22.54 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
