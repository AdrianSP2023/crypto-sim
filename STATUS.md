# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 09:16 UTC · vueltas 197 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 895.52 € (-3.11%) | 152 | 33 | 27% | -0.238% | -0.910% | -1.042% | -31.59 € |
| reversion_bb | 915.36 € (-0.96%) | 40 | 6 | 42% | +0.065% | -1.035% | -1.149% | -9.53 € |
| ruptura_volumen | 886.64 € (-4.07%) | 184 | 18 | 18% | -0.302% | -0.944% | -1.076% | -39.41 € |
| rebote_extremo | 923.46 € (-0.08%) | 9 | 1 | 56% | +0.558% | -0.542% | -0.703% | -1.13 € |
| pullback_tendencia | 901.68 € (-2.44%) | 123 | 2 | 24% | -0.094% | -0.806% | -0.933% | -22.68 € |
| macd_momentum | 875.69 € (-5.25%) | 342 | 26 | 17% | -0.076% | -0.652% | -0.763% | -50.28 € |
| estocastico_rebote | 888.68 € (-3.85%) | 226 | 11 | 35% | -0.093% | -0.708% | -0.842% | -36.48 € |
| ruptura_estricta | 902.52 € (-2.35%) | 81 | 7 | 22% | -0.396% | -1.218% | -1.368% | -22.60 € |
| macd_sin_salida | 888.92 € (-3.82%) | 214 | 29 | 28% | -0.147% | -0.769% | -0.890% | -37.38 € |
| c_banda_atr_tope | 910.12 € (-1.53%) | 42 | 5 | 19% | -0.440% | -1.540% | -1.669% | -14.85 € |
| ruptura_volumen_tope | 908.86 € (-1.66%) | 65 | 5 | 17% | -0.181% | -1.087% | -1.213% | -16.21 € |
| c_banda_atr_regimen | 900.71 € (-2.55%) | 78 | 6 | 22% | -0.483% | -1.317% | -1.445% | -23.56 € |
| macd_momentum_regimen | 885.35 € (-4.21%) | 202 | 9 | 14% | -0.219% | -0.848% | -0.962% | -38.90 € |
| ruptura_volumen_regimen | 894.90 € (-3.17%) | 128 | 6 | 16% | -0.319% | -1.022% | -1.152% | -29.82 € |
| c_banda_atr_evento | 898.57 € (-2.78%) | 120 | 33 | 24% | -0.320% | -1.040% | -1.173% | -28.54 € |
| macd_momentum_evento | 888.00 € (-3.92%) | 222 | 26 | 15% | -0.135% | -0.754% | -0.862% | -37.98 € |
| ruptura_volumen_evento | 892.10 € (-3.48%) | 125 | 18 | 11% | -0.482% | -1.193% | -1.328% | -33.95 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 09:15 | macd_momentum_evento | CRV | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-09-30 09:15 | c_banda_atr_evento | CRV | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 09:15 | macd_sin_salida | CRV | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-09-30 09:15 | ruptura_estricta | ENA | take-profit | +3.00% | +2.50% | +0.56 |
| 2026-09-30 09:15 | estocastico_rebote | RENDER | timeout | +0.82% | +0.32% | +0.07 |
| 2026-09-30 09:15 | macd_momentum | CRV | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-09-30 09:15 | c_banda_atr | CRV | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-09-30 09:10 | macd_momentum_evento | ASTER | momentum perdido | +0.92% | +0.42% | +0.09 |
| 2026-09-30 09:10 | macd_momentum_evento | ICP | momentum perdido | +0.49% | -0.01% | -0.00 |
| 2026-09-30 09:10 | macd_momentum | ASTER | momentum perdido | +0.92% | +0.42% | +0.09 |
| 2026-09-30 09:10 | macd_momentum | ICP | momentum perdido | +0.49% | -0.01% | -0.00 |
| 2026-09-30 09:05 | c_banda_atr_evento | SHIB | timeout | +0.12% | -0.38% | -0.09 |
| 2026-09-30 09:05 | c_banda_atr_evento | ZRO | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 09:05 | rebote_extremo | JUP | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-30 09:05 | c_banda_atr | SHIB | timeout | +0.12% | -0.38% | -0.09 |

## Eventos de la última vuelta

- 2026-09-30 09:15 [c_banda_atr] CIERRE CRV take-profit bruto +2.00% neto +1.50%
- 2026-09-30 09:15 [macd_momentum] CIERRE CRV take-profit bruto +2.00% neto +1.50%
- 2026-09-30 09:15 [macd_sin_salida] CIERRE CRV take-profit bruto +2.00% neto +1.50%
- 2026-09-30 09:15 [c_banda_atr_evento] CIERRE CRV take-profit bruto +2.00% neto +1.50%
- 2026-09-30 09:15 [macd_momentum_evento] CIERRE CRV take-profit bruto +2.00% neto +1.50%
- 2026-09-30 09:15 [ruptura_estricta] CIERRE ENA take-profit bruto +3.00% neto +2.50%
- 2026-09-30 09:10 [macd_momentum] ENTRADA VVV @ 23.815 (21.85 €, apertura)
- 2026-09-30 09:10 [macd_sin_salida] ENTRADA VVV @ 23.815 (22.17 €, apertura)
- 2026-09-30 09:10 [macd_momentum_regimen] ENTRADA VVV @ 23.815 (22.13 €, apertura)
- 2026-09-30 09:10 [macd_momentum_evento] ENTRADA VVV @ 23.815 (22.16 €, apertura)
- 2026-09-30 09:10 [c_banda_atr] ENTRADA TRX @ 0.297983 (22.32 €, apertura)
- 2026-09-30 09:10 [c_banda_atr_regimen] ENTRADA TRX @ 0.297983 (22.52 €, apertura)
- 2026-09-30 09:10 [c_banda_atr_evento] ENTRADA TRX @ 0.297983 (22.39 €, apertura)
- 2026-09-30 09:15 [estocastico_rebote] CIERRE RENDER timeout bruto +0.82% neto +0.32%
- 2026-09-30 09:10 [macd_momentum] ENTRADA MINA @ 0.1256 (21.85 €, apertura)
- 2026-09-30 09:10 [macd_momentum_regimen] ENTRADA MINA @ 0.1256 (22.13 €, apertura)
- 2026-09-30 09:10 [macd_momentum_evento] ENTRADA MINA @ 0.1256 (22.16 €, apertura)
- 2026-09-30 09:10 [ruptura_volumen] ENTRADA XPL @ 0.0851 (22.12 €, apertura)
- 2026-09-30 09:10 [ruptura_volumen_regimen] ENTRADA XPL @ 0.0851 (22.36 €, apertura)
- 2026-09-30 09:10 [ruptura_volumen_evento] ENTRADA XPL @ 0.0851 (22.26 €, apertura)
- 2026-09-30 09:10 [c_banda_atr_regimen] ENTRADA SPX @ 0.3753 (22.52 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
