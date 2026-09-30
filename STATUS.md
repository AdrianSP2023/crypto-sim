# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 09:31 UTC · vueltas 200 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 895.22 € (-3.14%) | 156 | 29 | 27% | -0.213% | -0.881% | -1.010% | -31.37 € |
| reversion_bb | 915.06 € (-0.99%) | 42 | 4 | 40% | +0.092% | -1.001% | -1.113% | -9.68 € |
| ruptura_volumen | 886.38 € (-4.10%) | 187 | 21 | 19% | -0.271% | -0.911% | -1.042% | -38.65 € |
| rebote_extremo | 923.52 € (-0.08%) | 9 | 1 | 56% | +0.558% | -0.542% | -0.703% | -1.13 € |
| pullback_tendencia | 901.55 € (-2.45%) | 123 | 3 | 24% | -0.094% | -0.806% | -0.933% | -22.68 € |
| macd_momentum | 875.68 € (-5.25%) | 345 | 26 | 17% | -0.080% | -0.656% | -0.767% | -50.98 € |
| estocastico_rebote | 888.70 € (-3.84%) | 227 | 11 | 36% | -0.090% | -0.705% | -0.839% | -36.48 € |
| ruptura_estricta | 902.31 € (-2.37%) | 81 | 8 | 22% | -0.396% | -1.218% | -1.368% | -22.60 € |
| macd_sin_salida | 889.10 € (-3.80%) | 214 | 32 | 28% | -0.147% | -0.769% | -0.890% | -37.38 € |
| c_banda_atr_tope | 910.08 € (-1.53%) | 42 | 5 | 19% | -0.440% | -1.540% | -1.669% | -14.85 € |
| ruptura_volumen_tope | 908.43 € (-1.71%) | 67 | 5 | 18% | -0.140% | -1.034% | -1.158% | -15.89 € |
| c_banda_atr_regimen | 900.59 € (-2.56%) | 78 | 6 | 22% | -0.483% | -1.317% | -1.445% | -23.56 € |
| macd_momentum_regimen | 884.96 € (-4.25%) | 205 | 9 | 14% | -0.224% | -0.852% | -0.966% | -39.61 € |
| ruptura_volumen_regimen | 894.92 € (-3.17%) | 129 | 12 | 17% | -0.297% | -0.999% | -1.130% | -29.37 € |
| c_banda_atr_evento | 898.27 € (-2.81%) | 124 | 29 | 24% | -0.286% | -0.999% | -1.128% | -28.33 € |
| macd_momentum_evento | 887.99 € (-3.92%) | 225 | 26 | 15% | -0.141% | -0.758% | -0.867% | -38.70 € |
| ruptura_volumen_evento | 891.83 € (-3.51%) | 128 | 21 | 12% | -0.432% | -1.139% | -1.273% | -33.19 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 09:30 | macd_momentum_evento | MINA | momentum perdido | -0.88% | -1.38% | -0.30 |
| 2026-09-30 09:30 | macd_momentum_evento | XDC | momentum perdido | -0.23% | -0.73% | -0.16 |
| 2026-09-30 09:30 | c_banda_atr_evento | PEPE | timeout | +0.32% | -0.18% | -0.04 |
| 2026-09-30 09:30 | c_banda_atr_evento | XLM | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 09:30 | c_banda_atr_evento | ETH | timeout | +0.19% | -0.31% | -0.07 |
| 2026-09-30 09:30 | c_banda_atr_evento | XRP | timeout | +0.44% | -0.06% | -0.01 |
| 2026-09-30 09:30 | macd_momentum_regimen | MINA | momentum perdido | -0.88% | -1.38% | -0.30 |
| 2026-09-30 09:30 | macd_momentum_regimen | XDC | momentum perdido | -0.23% | -0.73% | -0.16 |
| 2026-09-30 09:30 | estocastico_rebote | SEI | timeout | +0.51% | +0.01% | +0.00 |
| 2026-09-30 09:30 | macd_momentum | MINA | momentum perdido | -0.88% | -1.38% | -0.30 |
| 2026-09-30 09:30 | macd_momentum | XDC | momentum perdido | -0.23% | -0.73% | -0.16 |
| 2026-09-30 09:30 | c_banda_atr | PEPE | timeout | +0.32% | -0.18% | -0.04 |
| 2026-09-30 09:30 | c_banda_atr | XLM | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 09:30 | c_banda_atr | ETH | timeout | +0.19% | -0.31% | -0.07 |
| 2026-09-30 09:30 | c_banda_atr | XRP | timeout | +0.44% | -0.06% | -0.01 |

## Eventos de la última vuelta

- 2026-09-30 09:30 [c_banda_atr] CIERRE XRP timeout bruto +0.44% neto -0.06%
- 2026-09-30 09:30 [c_banda_atr_evento] CIERRE XRP timeout bruto +0.44% neto -0.06%
- 2026-09-30 09:30 [c_banda_atr] CIERRE ETH timeout bruto +0.19% neto -0.31%
- 2026-09-30 09:30 [c_banda_atr_evento] CIERRE ETH timeout bruto +0.19% neto -0.31%
- 2026-09-30 09:25 [estocastico_rebote] ENTRADA QNT @ 250.23 (22.19 €, apertura)
- 2026-09-30 09:30 [c_banda_atr] CIERRE XLM take-profit bruto +2.00% neto +1.50%
- 2026-09-30 09:30 [c_banda_atr_evento] CIERRE XLM take-profit bruto +2.00% neto +1.50%
- 2026-09-30 09:30 [macd_momentum] CIERRE XDC momentum perdido bruto -0.23% neto -0.73%
- 2026-09-30 09:30 [macd_momentum_regimen] CIERRE XDC momentum perdido bruto -0.23% neto -0.73%
- 2026-09-30 09:30 [macd_momentum_evento] CIERRE XDC momentum perdido bruto -0.23% neto -0.73%
- 2026-09-30 09:25 [ruptura_volumen] ENTRADA DASH @ 53.68 (22.14 €, apertura)
- 2026-09-30 09:25 [ruptura_volumen_regimen] ENTRADA DASH @ 53.68 (22.37 €, apertura)
- 2026-09-30 09:25 [ruptura_volumen_evento] ENTRADA DASH @ 53.68 (22.28 €, apertura)
- 2026-09-30 09:30 [c_banda_atr] CIERRE PEPE timeout bruto +0.32% neto -0.18%
- 2026-09-30 09:30 [c_banda_atr_evento] CIERRE PEPE timeout bruto +0.32% neto -0.18%
- 2026-09-30 09:30 [estocastico_rebote] CIERRE SEI timeout bruto +0.51% neto +0.01%
- 2026-09-30 09:30 [macd_momentum] CIERRE MINA momentum perdido bruto -0.88% neto -1.38%
- 2026-09-30 09:30 [macd_momentum_regimen] CIERRE MINA momentum perdido bruto -0.88% neto -1.38%
- 2026-09-30 09:30 [macd_momentum_evento] CIERRE MINA momentum perdido bruto -0.88% neto -1.38%
- 2026-09-30 09:25 [ruptura_volumen] ENTRADA NIGHT @ 0.02955 (22.14 €, apertura)
- 2026-09-30 09:25 [ruptura_estricta] ENTRADA NIGHT @ 0.02955 (22.54 €, apertura)
- 2026-09-30 09:25 [ruptura_volumen_regimen] ENTRADA NIGHT @ 0.02955 (22.37 €, apertura)
- 2026-09-30 09:25 [ruptura_volumen_evento] ENTRADA NIGHT @ 0.02955 (22.28 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
