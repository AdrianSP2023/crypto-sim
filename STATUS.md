# Simulación P3 (sin dinero real)

Config `P3-v1` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 13:46 UTC · vueltas 50 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 920.55 € (-0.40%) | 18 | 20 | 56% | +0.536% | -0.564% | -0.674% | -2.35 € |
| reversion_bb | 923.04 € (-0.13%) | 2 | 0 | 0% | -1.500% | -2.600% | -2.720% | -1.20 € |
| ruptura_volumen | 916.21 € (-0.87%) | 43 | 13 | 30% | +0.174% | -0.863% | -1.010% | -8.56 € |
| rebote_extremo | 924.46 € (+0.02%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 917.23 € (-0.76%) | 36 | 9 | 33% | +0.229% | -0.871% | -0.976% | -7.23 € |
| macd_momentum | 908.06 € (-1.75%) | 103 | 5 | 19% | +0.062% | -0.692% | -0.802% | -16.39 € |
| estocastico_rebote | 922.53 € (-0.19%) | 36 | 31 | 67% | +0.929% | -0.088% | -0.211% | -0.72 € |
| ruptura_estricta | 920.66 € (-0.39%) | 21 | 15 | 33% | +0.190% | -0.910% | -1.043% | -4.42 € |
| macd_sin_salida | 916.03 € (-0.89%) | 49 | 19 | 39% | +0.337% | -0.647% | -0.765% | -7.28 € |
| c_banda_atr_tope | 922.63 € (-0.17%) | 6 | 4 | 33% | -0.058% | -1.158% | -1.299% | -1.61 € |
| ruptura_volumen_tope | 921.89 € (-0.25%) | 13 | 3 | 23% | +0.215% | -0.885% | -1.016% | -2.66 € |
| c_banda_atr_regimen | 920.55 € (-0.40%) | 18 | 20 | 56% | +0.536% | -0.564% | -0.674% | -2.35 € |
| macd_momentum_regimen | 908.06 € (-1.75%) | 103 | 5 | 19% | +0.062% | -0.692% | -0.802% | -16.39 € |
| ruptura_volumen_regimen | 916.21 € (-0.87%) | 43 | 13 | 30% | +0.174% | -0.863% | -1.010% | -8.56 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 13:45 | ruptura_volumen_regimen | RENDER | timeout | -0.46% | -1.26% | -0.29 |
| 2026-09-29 13:45 | estocastico_rebote | ADA | timeout | +0.50% | -0.30% | -0.07 |
| 2026-09-29 13:45 | ruptura_volumen | RENDER | timeout | -0.46% | -1.26% | -0.29 |
| 2026-09-29 13:40 | ruptura_volumen_regimen | XPL | timeout | -0.56% | -1.36% | -0.31 |
| 2026-09-29 13:40 | macd_momentum_regimen | SPX | momentum perdido | -0.35% | -0.85% | -0.19 |
| 2026-09-29 13:40 | macd_momentum_regimen | BNB | momentum perdido | -0.07% | -0.57% | -0.13 |
| 2026-09-29 13:40 | macd_momentum_regimen | RAY | momentum perdido | -0.59% | -1.09% | -0.25 |
| 2026-09-29 13:40 | macd_momentum_regimen | BCH | momentum perdido | -0.58% | -1.08% | -0.24 |
| 2026-09-29 13:40 | macd_momentum_regimen | ICP | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-29 13:40 | macd_momentum_regimen | DOGE | momentum perdido | +0.39% | -0.11% | -0.02 |
| 2026-09-29 13:40 | macd_momentum_regimen | HYPE | momentum perdido | -0.40% | -0.90% | -0.20 |
| 2026-09-29 13:40 | macd_momentum_regimen | TAO | momentum perdido | -0.01% | -0.51% | -0.12 |
| 2026-09-29 13:40 | macd_momentum_regimen | AAVE | momentum perdido | -0.77% | -1.27% | -0.29 |
| 2026-09-29 13:40 | macd_momentum_regimen | BTC | momentum perdido | -0.15% | -0.65% | -0.15 |
| 2026-09-29 13:40 | c_banda_atr_regimen | SEI | timeout | -0.38% | -1.48% | -0.34 |

## Eventos de la última vuelta

- 2026-09-29 13:45 [estocastico_rebote] CIERRE ADA timeout bruto +0.50% neto -0.30%
- 2026-09-29 13:40 [c_banda_atr] ENTRADA PUMP @ 0.005169 (23.05 €, apertura)
- 2026-09-29 13:40 [c_banda_atr_tope] ENTRADA PUMP @ 0.005169 (23.07 €, apertura)
- 2026-09-29 13:40 [c_banda_atr_regimen] ENTRADA PUMP @ 0.005169 (23.05 €, apertura)
- 2026-09-29 13:40 [ruptura_volumen] ENTRADA ICP @ 3.006 (22.90 €, apertura)
- 2026-09-29 13:40 [ruptura_estricta] ENTRADA ICP @ 3.006 (23.00 €, apertura)
- 2026-09-29 13:40 [ruptura_volumen_tope] ENTRADA ICP @ 3.006 (23.04 €, apertura)
- 2026-09-29 13:40 [ruptura_volumen_regimen] ENTRADA ICP @ 3.006 (22.90 €, apertura)
- 2026-09-29 13:45 [ruptura_volumen] CIERRE RENDER timeout bruto -0.46% neto -1.26%
- 2026-09-29 13:45 [ruptura_volumen_regimen] CIERRE RENDER timeout bruto -0.46% neto -1.26%
- 2026-09-29 13:40 [macd_momentum] ENTRADA ZRO @ 1.455 (22.70 €, apertura)
- 2026-09-29 13:40 [macd_sin_salida] ENTRADA ZRO @ 1.455 (22.92 €, apertura)
- 2026-09-29 13:40 [macd_momentum_regimen] ENTRADA ZRO @ 1.455 (22.70 €, apertura)
- 2026-09-29 13:40 [pullback_tendencia] ENTRADA PEPE @ 3.847e-06 (22.93 €, apertura)
- 2026-09-29 13:40 [c_banda_atr] ENTRADA USELESS @ 0.21579 (23.05 €, apertura)
- 2026-09-29 13:40 [c_banda_atr_tope] ENTRADA USELESS @ 0.21579 (23.07 €, apertura)
- 2026-09-29 13:40 [c_banda_atr_regimen] ENTRADA USELESS @ 0.21579 (23.05 €, apertura)
- 2026-09-29 13:40 [estocastico_rebote] ENTRADA MINA @ 0.1304 (23.09 €, apertura)
- 2026-09-29 13:40 [pullback_tendencia] ENTRADA POL @ 0.1094 (22.93 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
