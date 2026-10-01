# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 01:26 UTC · vueltas 88 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 904.62 € (-2.12%) | 91 | 25 | 27% | -0.251% | -1.037% | -1.165% | -21.67 € |
| reversion_bb | 921.69 € (-0.28%) | 13 | 3 | 38% | +0.127% | -0.973% | -1.092% | -2.92 € |
| ruptura_volumen | 894.37 € (-3.23%) | 120 | 20 | 16% | -0.420% | -1.137% | -1.252% | -31.18 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 904.87 € (-2.10%) | 76 | 6 | 17% | -0.305% | -1.152% | -1.279% | -20.07 € |
| macd_momentum | 904.95 € (-2.09%) | 140 | 32 | 24% | -0.030% | -0.716% | -0.829% | -22.95 € |
| estocastico_rebote | 904.17 € (-2.17%) | 138 | 14 | 37% | +0.021% | -0.668% | -0.791% | -21.23 € |
| ruptura_estricta | 900.10 € (-2.61%) | 56 | 16 | 16% | -1.018% | -1.989% | -2.131% | -25.63 € |
| macd_sin_salida | 905.92 € (-1.98%) | 103 | 29 | 37% | -0.113% | -0.867% | -0.988% | -20.53 € |
| c_banda_atr_tope | 918.72 € (-0.60%) | 21 | 5 | 29% | -0.083% | -1.183% | -1.319% | -5.73 € |
| ruptura_volumen_tope | 915.27 € (-0.97%) | 33 | 5 | 18% | -0.115% | -1.215% | -1.296% | -9.23 € |
| c_banda_atr_regimen | 908.33 € (-1.72%) | 47 | 11 | 23% | -0.490% | -1.546% | -1.702% | -16.72 € |
| macd_momentum_regimen | 909.71 € (-1.57%) | 78 | 15 | 24% | -0.062% | -0.896% | -1.021% | -16.08 € |
| ruptura_volumen_regimen | 895.30 € (-3.13%) | 97 | 13 | 13% | -0.563% | -1.333% | -1.455% | -29.56 € |
| c_banda_atr_evento | 910.99 € (-1.43%) | 58 | 25 | 26% | -0.217% | -1.147% | -1.256% | -15.31 € |
| macd_momentum_evento | 909.97 € (-1.54%) | 93 | 32 | 18% | -0.059% | -0.843% | -0.943% | -17.96 € |
| ruptura_volumen_evento | 907.09 € (-1.86%) | 70 | 20 | 13% | -0.272% | -1.149% | -1.238% | -18.47 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 01:25 | ruptura_volumen_evento | JUP | timeout | +0.23% | -0.27% | -0.06 |
| 2026-10-01 01:25 | macd_momentum_evento | NIGHT | take-profit | +2.03% | +1.53% | +0.35 |
| 2026-10-01 01:25 | ruptura_volumen_regimen | JUP | timeout | +0.23% | -0.27% | -0.06 |
| 2026-10-01 01:25 | macd_sin_salida | NIGHT | take-profit | +2.03% | +1.53% | +0.34 |
| 2026-10-01 01:25 | macd_sin_salida | AAVE | timeout | +0.26% | -0.24% | -0.06 |
| 2026-10-01 01:25 | macd_sin_salida | SUI | take-profit | +2.08% | +1.58% | +0.36 |
| 2026-10-01 01:25 | macd_sin_salida | ADA | timeout | +1.44% | +0.94% | +0.21 |
| 2026-10-01 01:25 | macd_momentum | NIGHT | take-profit | +2.03% | +1.53% | +0.34 |
| 2026-10-01 01:25 | ruptura_volumen | JUP | timeout | +0.23% | -0.27% | -0.06 |
| 2026-10-01 01:20 | ruptura_volumen_evento | SKY | timeout | +0.47% | -0.04% | -0.01 |
| 2026-10-01 01:20 | ruptura_volumen_evento | LINK | timeout | -0.12% | -0.62% | -0.14 |
| 2026-10-01 01:20 | c_banda_atr_evento | ONDO | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 01:20 | macd_sin_salida | SPX | timeout | +1.29% | +0.79% | +0.18 |
| 2026-10-01 01:20 | macd_sin_salida | NEAR | timeout | -1.15% | -1.65% | -0.37 |
| 2026-10-01 01:20 | estocastico_rebote | XLM | take-profit | +1.80% | +1.30% | +0.29 |

## Eventos de la última vuelta

- 2026-10-01 01:20 [ruptura_volumen] ENTRADA XRP @ 1.31819 (22.33 €, apertura)
- 2026-10-01 01:20 [ruptura_volumen_regimen] ENTRADA XRP @ 1.31819 (22.37 €, apertura)
- 2026-10-01 01:20 [ruptura_volumen_evento] ENTRADA XRP @ 1.31819 (22.65 €, apertura)
- 2026-10-01 01:20 [ruptura_volumen] ENTRADA QNT @ 259.21 (22.33 €, apertura)
- 2026-10-01 01:20 [ruptura_volumen_regimen] ENTRADA QNT @ 259.21 (22.37 €, apertura)
- 2026-10-01 01:20 [ruptura_volumen_evento] ENTRADA QNT @ 259.21 (22.65 €, apertura)
- 2026-10-01 01:20 [macd_momentum] ENTRADA LINK @ 12.7177 (22.52 €, apertura)
- 2026-10-01 01:20 [macd_momentum_regimen] ENTRADA LINK @ 12.7177 (22.70 €, apertura)
- 2026-10-01 01:20 [macd_momentum_evento] ENTRADA LINK @ 12.7177 (22.65 €, apertura)
- 2026-10-01 01:20 [ruptura_volumen] ENTRADA ADA @ 0.219206 (22.33 €, apertura)
- 2026-10-01 01:25 [macd_sin_salida] CIERRE ADA timeout bruto +1.44% neto +0.94%
- 2026-10-01 01:20 [ruptura_volumen_regimen] ENTRADA ADA @ 0.219206 (22.37 €, apertura)
- 2026-10-01 01:20 [ruptura_volumen_evento] ENTRADA ADA @ 0.219206 (22.65 €, apertura)
- 2026-10-01 01:25 [macd_sin_salida] CIERRE SUI take-profit bruto +2.08% neto +1.58%
- 2026-10-01 01:25 [macd_sin_salida] CIERRE AAVE timeout bruto +0.26% neto -0.24%
- 2026-10-01 01:20 [ruptura_volumen] ENTRADA XLM @ 0.203675 (22.33 €, apertura)
- 2026-10-01 01:20 [ruptura_volumen_regimen] ENTRADA XLM @ 0.203675 (22.37 €, apertura)
- 2026-10-01 01:20 [ruptura_volumen_evento] ENTRADA XLM @ 0.203675 (22.65 €, apertura)
- 2026-10-01 01:20 [ruptura_volumen] ENTRADA DOGE @ 0.0839576 (22.33 €, apertura)
- 2026-10-01 01:20 [ruptura_estricta] ENTRADA DOGE @ 0.0839576 (22.47 €, apertura)
- 2026-10-01 01:20 [ruptura_volumen_regimen] ENTRADA DOGE @ 0.0839576 (22.37 €, apertura)
- 2026-10-01 01:20 [ruptura_volumen_evento] ENTRADA DOGE @ 0.0839576 (22.65 €, apertura)
- 2026-10-01 01:20 [ruptura_volumen] ENTRADA ONDO @ 0.45074 (22.33 €, apertura)
- 2026-10-01 01:20 [ruptura_volumen_regimen] ENTRADA ONDO @ 0.45074 (22.37 €, apertura)
- 2026-10-01 01:20 [ruptura_volumen_evento] ENTRADA ONDO @ 0.45074 (22.65 €, apertura)
- 2026-10-01 01:20 [ruptura_volumen] ENTRADA NIGHT @ 0.03576 (22.33 €, apertura)
- 2026-10-01 01:25 [macd_momentum] CIERRE NIGHT take-profit bruto +2.03% neto +1.53%
- 2026-10-01 01:20 [ruptura_estricta] ENTRADA NIGHT @ 0.03576 (22.47 €, apertura)
- 2026-10-01 01:25 [macd_sin_salida] CIERRE NIGHT take-profit bruto +2.03% neto +1.53%
- 2026-10-01 01:20 [ruptura_volumen_regimen] ENTRADA NIGHT @ 0.03576 (22.37 €, apertura)
- 2026-10-01 01:25 [macd_momentum_evento] CIERRE NIGHT take-profit bruto +2.03% neto +1.53%
- 2026-10-01 01:20 [ruptura_volumen_evento] ENTRADA NIGHT @ 0.03576 (22.65 €, apertura)
- 2026-10-01 01:20 [c_banda_atr] ENTRADA JUP @ 0.29257 (22.56 €, apertura)
- 2026-10-01 01:25 [ruptura_volumen] CIERRE JUP timeout bruto +0.23% neto -0.27%
- 2026-10-01 01:20 [macd_momentum] ENTRADA JUP @ 0.29257 (22.53 €, apertura)
- 2026-10-01 01:20 [macd_sin_salida] ENTRADA JUP @ 0.29257 (22.59 €, apertura)
- 2026-10-01 01:20 [c_banda_atr_regimen] ENTRADA JUP @ 0.29257 (22.69 €, apertura)
- 2026-10-01 01:20 [macd_momentum_regimen] ENTRADA JUP @ 0.29257 (22.70 €, apertura)
- 2026-10-01 01:25 [ruptura_volumen_regimen] CIERRE JUP timeout bruto +0.23% neto -0.27%
- 2026-10-01 01:20 [c_banda_atr_evento] ENTRADA JUP @ 0.29257 (22.72 €, apertura)
- 2026-10-01 01:20 [macd_momentum_evento] ENTRADA JUP @ 0.29257 (22.66 €, apertura)
- 2026-10-01 01:25 [ruptura_volumen_evento] CIERRE JUP timeout bruto +0.23% neto -0.27%
- 2026-10-01 01:20 [ruptura_volumen] ENTRADA INJ @ 6.567 (22.33 €, apertura)
- 2026-10-01 01:20 [ruptura_estricta] ENTRADA INJ @ 6.567 (22.47 €, apertura)
- 2026-10-01 01:20 [ruptura_volumen_regimen] ENTRADA INJ @ 6.567 (22.37 €, apertura)
- 2026-10-01 01:20 [ruptura_volumen_evento] ENTRADA INJ @ 6.567 (22.64 €, apertura)
- 2026-10-01 01:20 [ruptura_volumen] ENTRADA FIL @ 0.934 (22.33 €, apertura)
- 2026-10-01 01:20 [ruptura_volumen_regimen] ENTRADA FIL @ 0.934 (22.37 €, apertura)
- 2026-10-01 01:20 [ruptura_volumen_evento] ENTRADA FIL @ 0.934 (22.64 €, apertura)
- 2026-10-01 01:20 [c_banda_atr] ENTRADA TRUMP @ 1.825 (22.56 €, apertura)
- 2026-10-01 01:20 [macd_sin_salida] ENTRADA TRUMP @ 1.825 (22.59 €, apertura)
- 2026-10-01 01:20 [c_banda_atr_regimen] ENTRADA TRUMP @ 1.825 (22.69 €, apertura)
- 2026-10-01 01:20 [macd_momentum_regimen] ENTRADA TRUMP @ 1.825 (22.70 €, apertura)
- 2026-10-01 01:20 [c_banda_atr_evento] ENTRADA TRUMP @ 1.825 (22.72 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
