# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 00:46 UTC · vueltas 80 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 902.81 € (-2.32%) | 87 | 22 | 26% | -0.292% | -1.092% | -1.221% | -21.79 € |
| reversion_bb | 921.79 € (-0.27%) | 11 | 5 | 45% | +0.111% | -0.989% | -1.119% | -2.52 € |
| ruptura_volumen | 894.15 € (-3.26%) | 111 | 13 | 15% | -0.469% | -1.204% | -1.321% | -30.54 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 904.23 € (-2.16%) | 74 | 5 | 15% | -0.373% | -1.229% | -1.355% | -20.84 € |
| macd_momentum | 902.29 € (-2.37%) | 135 | 16 | 24% | -0.056% | -0.750% | -0.864% | -23.17 € |
| estocastico_rebote | 902.60 € (-2.34%) | 133 | 19 | 35% | -0.037% | -0.733% | -0.856% | -22.42 € |
| ruptura_estricta | 898.65 € (-2.77%) | 54 | 11 | 15% | -1.039% | -2.028% | -2.170% | -25.21 € |
| macd_sin_salida | 903.33 € (-2.26%) | 93 | 32 | 34% | -0.191% | -0.971% | -1.099% | -20.77 € |
| c_banda_atr_tope | 918.88 € (-0.58%) | 20 | 5 | 30% | -0.007% | -1.107% | -1.248% | -5.10 € |
| ruptura_volumen_tope | 915.55 € (-0.94%) | 32 | 4 | 19% | -0.117% | -1.217% | -1.299% | -8.97 € |
| c_banda_atr_regimen | 907.15 € (-1.85%) | 47 | 7 | 23% | -0.490% | -1.546% | -1.702% | -16.72 € |
| macd_momentum_regimen | 908.47 € (-1.71%) | 76 | 0 | 25% | -0.058% | -0.902% | -1.028% | -15.78 € |
| ruptura_volumen_regimen | 895.27 € (-3.13%) | 90 | 7 | 12% | -0.622% | -1.412% | -1.536% | -29.07 € |
| c_banda_atr_evento | 909.30 € (-1.62%) | 54 | 22 | 24% | -0.281% | -1.231% | -1.342% | -15.30 € |
| macd_momentum_evento | 907.29 € (-1.83%) | 88 | 16 | 17% | -0.102% | -0.902% | -1.004% | -18.18 € |
| ruptura_volumen_evento | 906.87 € (-1.88%) | 61 | 13 | 11% | -0.340% | -1.272% | -1.362% | -17.82 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 00:45 | ruptura_volumen_evento | BNB | timeout | +0.07% | -0.43% | -0.10 |
| 2026-10-01 00:45 | ruptura_volumen_evento | ZEC | timeout | -0.74% | -1.24% | -0.28 |
| 2026-10-01 00:45 | c_banda_atr_evento | APT | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 00:45 | c_banda_atr_evento | WLFI | timeout | -0.82% | -1.62% | -0.37 |
| 2026-10-01 00:45 | ruptura_volumen_regimen | BNB | timeout | +0.07% | -0.43% | -0.10 |
| 2026-10-01 00:45 | ruptura_volumen_regimen | ZEC | timeout | -0.74% | -1.24% | -0.28 |
| 2026-10-01 00:45 | ruptura_volumen_regimen | ETH | timeout | -0.18% | -0.68% | -0.15 |
| 2026-10-01 00:45 | macd_sin_salida | TRUMP | timeout | +1.00% | +0.50% | +0.11 |
| 2026-10-01 00:45 | ruptura_estricta | HYPE | timeout | -1.24% | -1.74% | -0.39 |
| 2026-10-01 00:45 | ruptura_volumen | BNB | timeout | +0.07% | -0.43% | -0.10 |
| 2026-10-01 00:45 | ruptura_volumen | ZEC | timeout | -0.74% | -1.24% | -0.28 |
| 2026-10-01 00:45 | c_banda_atr | APT | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 00:45 | c_banda_atr | WLFI | timeout | -0.82% | -1.32% | -0.30 |
| 2026-10-01 00:40 | ruptura_volumen_evento | DASH | timeout | -0.91% | -1.41% | -0.32 |
| 2026-10-01 00:40 | ruptura_volumen_evento | ENA | timeout | +0.30% | -0.20% | -0.05 |

## Eventos de la última vuelta

- 2026-10-01 00:45 [ruptura_volumen_regimen] CIERRE ETH timeout bruto -0.18% neto -0.68%
- 2026-10-01 00:40 [c_banda_atr] ENTRADA SUI @ 1.0322 (22.56 €, apertura)
- 2026-10-01 00:40 [macd_momentum] ENTRADA SUI @ 1.0322 (22.53 €, apertura)
- 2026-10-01 00:40 [c_banda_atr_evento] ENTRADA SUI @ 1.0322 (22.72 €, apertura)
- 2026-10-01 00:40 [macd_momentum_evento] ENTRADA SUI @ 1.0322 (22.65 €, apertura)
- 2026-10-01 00:45 [ruptura_volumen] CIERRE ZEC timeout bruto -0.74% neto -1.24%
- 2026-10-01 00:45 [ruptura_volumen_regimen] CIERRE ZEC timeout bruto -0.74% neto -1.24%
- 2026-10-01 00:45 [ruptura_volumen_evento] CIERRE ZEC timeout bruto -0.74% neto -1.24%
- 2026-10-01 00:45 [ruptura_estricta] CIERRE HYPE timeout bruto -1.24% neto -1.74%
- 2026-10-01 00:40 [estocastico_rebote] ENTRADA XLM @ 0.200049 (22.55 €, apertura)
- 2026-10-01 00:40 [pullback_tendencia] ENTRADA LTC @ 59.42 (22.59 €, apertura)
- 2026-10-01 00:40 [macd_momentum] ENTRADA LTC @ 59.42 (22.53 €, apertura)
- 2026-10-01 00:40 [macd_sin_salida] ENTRADA LTC @ 59.42 (22.58 €, apertura)
- 2026-10-01 00:40 [macd_momentum_evento] ENTRADA LTC @ 59.42 (22.65 €, apertura)
- 2026-10-01 00:40 [macd_momentum] ENTRADA ENA @ 0.2359 (22.53 €, apertura)
- 2026-10-01 00:40 [macd_sin_salida] ENTRADA ENA @ 0.2359 (22.58 €, apertura)
- 2026-10-01 00:40 [macd_momentum_evento] ENTRADA ENA @ 0.2359 (22.65 €, apertura)
- 2026-10-01 00:40 [macd_momentum] ENTRADA ONDO @ 0.44525 (22.53 €, apertura)
- 2026-10-01 00:40 [macd_momentum_evento] ENTRADA ONDO @ 0.44525 (22.65 €, apertura)
- 2026-10-01 00:40 [macd_momentum] ENTRADA FIL @ 0.924 (22.53 €, apertura)
- 2026-10-01 00:40 [macd_momentum_evento] ENTRADA FIL @ 0.924 (22.65 €, apertura)
- 2026-10-01 00:40 [reversion_bb] ENTRADA VVV @ 24.196 (23.04 €, apertura)
- 2026-10-01 00:40 [estocastico_rebote] ENTRADA VVV @ 24.196 (22.55 €, apertura)
- 2026-10-01 00:45 [c_banda_atr] CIERRE WLFI timeout bruto -0.82% neto -1.32%
- 2026-10-01 00:45 [c_banda_atr_evento] CIERRE WLFI timeout bruto -0.82% neto -1.62%
- 2026-10-01 00:45 [macd_sin_salida] CIERRE TRUMP timeout bruto +1.00% neto +0.50%
- 2026-10-01 00:45 [ruptura_volumen] CIERRE BNB timeout bruto +0.06% neto -0.44%
- 2026-10-01 00:45 [ruptura_volumen_regimen] CIERRE BNB timeout bruto +0.06% neto -0.44%
- 2026-10-01 00:45 [ruptura_volumen_evento] CIERRE BNB timeout bruto +0.06% neto -0.44%
- 2026-10-01 00:45 [c_banda_atr] CIERRE APT take-profit bruto +2.00% neto +1.50%
- 2026-10-01 00:45 [c_banda_atr_evento] CIERRE APT take-profit bruto +2.00% neto +1.50%
- 2026-10-01 00:40 [estocastico_rebote] ENTRADA SPX @ 0.3888 (22.55 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
