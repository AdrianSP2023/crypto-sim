# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 09:21 UTC · vueltas 198 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 895.09 € (-3.15%) | 152 | 33 | 27% | -0.238% | -0.910% | -1.042% | -31.59 € |
| reversion_bb | 915.00 € (-1.00%) | 42 | 4 | 40% | +0.092% | -1.001% | -1.113% | -9.68 € |
| ruptura_volumen | 886.28 € (-4.11%) | 186 | 18 | 18% | -0.286% | -0.926% | -1.058% | -39.10 € |
| rebote_extremo | 923.48 € (-0.08%) | 9 | 1 | 56% | +0.558% | -0.542% | -0.703% | -1.13 € |
| pullback_tendencia | 901.63 € (-2.45%) | 123 | 2 | 24% | -0.094% | -0.806% | -0.933% | -22.68 € |
| macd_momentum | 875.15 € (-5.31%) | 343 | 27 | 17% | -0.077% | -0.653% | -0.764% | -50.52 € |
| estocastico_rebote | 888.56 € (-3.86%) | 226 | 11 | 35% | -0.093% | -0.708% | -0.842% | -36.48 € |
| ruptura_estricta | 902.21 € (-2.38%) | 81 | 7 | 22% | -0.396% | -1.218% | -1.368% | -22.60 € |
| macd_sin_salida | 888.49 € (-3.87%) | 214 | 31 | 28% | -0.147% | -0.769% | -0.890% | -37.38 € |
| c_banda_atr_tope | 910.10 € (-1.53%) | 42 | 5 | 19% | -0.440% | -1.540% | -1.669% | -14.85 € |
| ruptura_volumen_tope | 908.58 € (-1.69%) | 66 | 5 | 17% | -0.180% | -1.080% | -1.204% | -16.34 € |
| c_banda_atr_regimen | 900.53 € (-2.57%) | 78 | 6 | 22% | -0.483% | -1.317% | -1.445% | -23.56 € |
| macd_momentum_regimen | 884.99 € (-4.25%) | 203 | 10 | 14% | -0.221% | -0.850% | -0.963% | -39.15 € |
| ruptura_volumen_regimen | 894.93 € (-3.17%) | 129 | 8 | 17% | -0.297% | -0.999% | -1.130% | -29.37 € |
| c_banda_atr_evento | 898.14 € (-2.82%) | 120 | 33 | 24% | -0.320% | -1.040% | -1.173% | -28.54 € |
| macd_momentum_evento | 887.45 € (-3.98%) | 223 | 27 | 15% | -0.137% | -0.755% | -0.863% | -38.23 € |
| ruptura_volumen_evento | 891.74 € (-3.52%) | 127 | 18 | 12% | -0.456% | -1.163% | -1.298% | -33.64 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
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
| 2026-09-30 09:15 | c_banda_atr_evento | CRV | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 09:15 | macd_sin_salida | CRV | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-09-30 09:15 | ruptura_estricta | ENA | take-profit | +3.00% | +2.50% | +0.56 |

## Eventos de la última vuelta

- 2026-09-30 09:15 [macd_momentum] ENTRADA BTC @ 73335.9 (21.85 €, apertura)
- 2026-09-30 09:15 [macd_sin_salida] ENTRADA BTC @ 73335.9 (22.17 €, apertura)
- 2026-09-30 09:15 [macd_momentum_regimen] ENTRADA BTC @ 73335.9 (22.13 €, apertura)
- 2026-09-30 09:15 [macd_momentum_evento] ENTRADA BTC @ 73335.9 (22.16 €, apertura)
- 2026-09-30 09:20 [ruptura_volumen] CIERRE HBAR timeout bruto -0.10% neto -0.60%
- 2026-09-30 09:20 [macd_momentum] CIERRE HBAR momentum perdido bruto -0.62% neto -1.12%
- 2026-09-30 09:20 [ruptura_volumen_tope] CIERRE HBAR timeout bruto -0.10% neto -0.60%
- 2026-09-30 09:20 [macd_momentum_regimen] CIERRE HBAR momentum perdido bruto -0.62% neto -1.12%
- 2026-09-30 09:20 [macd_momentum_evento] CIERRE HBAR momentum perdido bruto -0.62% neto -1.12%
- 2026-09-30 09:20 [ruptura_volumen_evento] CIERRE HBAR timeout bruto -0.10% neto -0.60%
- 2026-09-30 09:20 [reversion_bb] CIERRE ARB timeout bruto +0.50% neto -0.60%
- 2026-09-30 09:15 [macd_momentum] ENTRADA XDC @ 0.03063 (21.84 €, apertura)
- 2026-09-30 09:15 [macd_sin_salida] ENTRADA XDC @ 0.03063 (22.17 €, apertura)
- 2026-09-30 09:15 [macd_momentum_regimen] ENTRADA XDC @ 0.03063 (22.13 €, apertura)
- 2026-09-30 09:15 [macd_momentum_evento] ENTRADA XDC @ 0.03063 (22.15 €, apertura)
- 2026-09-30 09:20 [reversion_bb] CIERRE DOGE timeout bruto +0.74% neto -0.06%
- 2026-09-30 09:15 [ruptura_volumen] ENTRADA ENA @ 0.2308 (22.12 €, apertura)
- 2026-09-30 09:15 [ruptura_volumen_tope] ENTRADA ENA @ 0.2308 (22.70 €, apertura)
- 2026-09-30 09:15 [ruptura_volumen_regimen] ENTRADA ENA @ 0.2308 (22.36 €, apertura)
- 2026-09-30 09:15 [ruptura_volumen_evento] ENTRADA ENA @ 0.2308 (22.25 €, apertura)
- 2026-09-30 09:15 [ruptura_volumen_regimen] ENTRADA ATOM @ 1.5163 (22.36 €, apertura)
- 2026-09-30 09:15 [ruptura_volumen] ENTRADA VIRTUAL @ 0.6943 (22.12 €, apertura)
- 2026-09-30 09:15 [ruptura_volumen_regimen] ENTRADA VIRTUAL @ 0.6943 (22.36 €, apertura)
- 2026-09-30 09:15 [ruptura_volumen_evento] ENTRADA VIRTUAL @ 0.6943 (22.25 €, apertura)
- 2026-09-30 09:20 [ruptura_volumen] CIERRE NIGHT take-profit bruto +2.50% neto +2.00%
- 2026-09-30 09:20 [ruptura_volumen_regimen] CIERRE NIGHT take-profit bruto +2.50% neto +2.00%
- 2026-09-30 09:20 [ruptura_volumen_evento] CIERRE NIGHT take-profit bruto +2.50% neto +2.00%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
