# Simulación P3 (sin dinero real)

Config `P3-v1` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 13:41 UTC · vueltas 49 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 920.86 € (-0.37%) | 18 | 18 | 56% | +0.536% | -0.564% | -0.674% | -2.35 € |
| reversion_bb | 923.04 € (-0.13%) | 2 | 0 | 0% | -1.500% | -2.600% | -2.720% | -1.20 € |
| ruptura_volumen | 916.50 € (-0.84%) | 42 | 13 | 31% | +0.189% | -0.853% | -1.000% | -8.27 € |
| rebote_extremo | 924.30 € (+0.01%) | 0 | 1 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 917.41 € (-0.74%) | 36 | 7 | 33% | +0.229% | -0.871% | -0.976% | -7.23 € |
| macd_momentum | 908.35 € (-1.72%) | 103 | 4 | 19% | +0.062% | -0.692% | -0.802% | -16.39 € |
| estocastico_rebote | 923.10 € (-0.12%) | 35 | 31 | 69% | +0.942% | -0.081% | -0.207% | -0.65 € |
| ruptura_estricta | 920.89 € (-0.36%) | 21 | 14 | 33% | +0.190% | -0.910% | -1.043% | -4.42 € |
| macd_sin_salida | 916.48 € (-0.84%) | 49 | 18 | 39% | +0.337% | -0.647% | -0.765% | -7.28 € |
| c_banda_atr_tope | 922.65 € (-0.17%) | 6 | 2 | 33% | -0.058% | -1.158% | -1.299% | -1.61 € |
| ruptura_volumen_tope | 921.93 € (-0.25%) | 13 | 2 | 23% | +0.215% | -0.885% | -1.016% | -2.66 € |
| c_banda_atr_regimen | 920.86 € (-0.37%) | 18 | 18 | 56% | +0.536% | -0.564% | -0.674% | -2.35 € |
| macd_momentum_regimen | 908.35 € (-1.72%) | 103 | 4 | 19% | +0.062% | -0.692% | -0.802% | -16.39 € |
| ruptura_volumen_regimen | 916.50 € (-0.84%) | 42 | 13 | 31% | +0.189% | -0.853% | -1.000% | -8.27 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
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
| 2026-09-29 13:40 | c_banda_atr_regimen | MON | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-29 13:40 | c_banda_atr_regimen | DASH | timeout | -0.41% | -1.51% | -0.35 |
| 2026-09-29 13:40 | ruptura_volumen_tope | XPL | timeout | -0.56% | -1.66% | -0.38 |

## Eventos de la última vuelta

- 2026-09-29 13:40 [macd_momentum] CIERRE BTC momentum perdido bruto -0.15% neto -0.65%
- 2026-09-29 13:40 [macd_momentum_regimen] CIERRE BTC momentum perdido bruto -0.15% neto -0.65%
- 2026-09-29 13:40 [ruptura_volumen_tope] CIERRE NEAR timeout bruto +0.68% neto -0.42%
- 2026-09-29 13:35 [pullback_tendencia] ENTRADA AAVE @ 152.17 (22.92 €, apertura)
- 2026-09-29 13:40 [macd_momentum] CIERRE AAVE momentum perdido bruto -0.77% neto -1.27%
- 2026-09-29 13:40 [macd_momentum_regimen] CIERRE AAVE momentum perdido bruto -0.77% neto -1.27%
- 2026-09-29 13:40 [macd_momentum] CIERRE TAO momentum perdido bruto -0.01% neto -0.51%
- 2026-09-29 13:40 [estocastico_rebote] CIERRE TAO timeout bruto +0.01% neto -0.79%
- 2026-09-29 13:40 [macd_momentum_regimen] CIERRE TAO momentum perdido bruto -0.01% neto -0.51%
- 2026-09-29 13:40 [macd_momentum] CIERRE HYPE momentum perdido bruto -0.40% neto -0.90%
- 2026-09-29 13:40 [macd_momentum_regimen] CIERRE HYPE momentum perdido bruto -0.40% neto -0.90%
- 2026-09-29 13:40 [macd_momentum] CIERRE DOGE momentum perdido bruto +0.39% neto -0.11%
- 2026-09-29 13:40 [macd_momentum_regimen] CIERRE DOGE momentum perdido bruto +0.39% neto -0.11%
- 2026-09-29 13:40 [c_banda_atr] CIERRE DASH timeout bruto -0.41% neto -1.51%
- 2026-09-29 13:40 [c_banda_atr_tope] CIERRE DASH timeout bruto -0.41% neto -1.51%
- 2026-09-29 13:40 [c_banda_atr_regimen] CIERRE DASH timeout bruto -0.41% neto -1.51%
- 2026-09-29 13:40 [c_banda_atr] CIERRE MON stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 13:40 [macd_sin_salida] CIERRE MON stop-loss bruto -1.50% neto -2.30%
- 2026-09-29 13:40 [c_banda_atr_tope] CIERRE MON stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 13:40 [c_banda_atr_regimen] CIERRE MON stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 13:40 [pullback_tendencia] CIERRE ICP take-profit bruto +2.00% neto +0.90%
- 2026-09-29 13:40 [macd_momentum] CIERRE ICP take-profit bruto +2.00% neto +1.50%
- 2026-09-29 13:40 [macd_sin_salida] CIERRE ICP take-profit bruto +2.00% neto +1.50%
- 2026-09-29 13:40 [macd_momentum_regimen] CIERRE ICP take-profit bruto +2.00% neto +1.50%
- 2026-09-29 13:40 [macd_momentum] CIERRE BCH momentum perdido bruto -0.58% neto -1.08%
- 2026-09-29 13:40 [macd_momentum_regimen] CIERRE BCH momentum perdido bruto -0.58% neto -1.08%
- 2026-09-29 13:40 [estocastico_rebote] CIERRE TRX timeout bruto -0.11% neto -0.91%
- 2026-09-29 13:40 [macd_momentum] CIERRE RAY momentum perdido bruto -0.59% neto -1.09%
- 2026-09-29 13:40 [macd_momentum_regimen] CIERRE RAY momentum perdido bruto -0.59% neto -1.09%
- 2026-09-29 13:40 [c_banda_atr] CIERRE SEI timeout bruto -0.38% neto -1.48%
- 2026-09-29 13:40 [c_banda_atr_tope] CIERRE SEI timeout bruto -0.38% neto -1.48%
- 2026-09-29 13:40 [c_banda_atr_regimen] CIERRE SEI timeout bruto -0.38% neto -1.48%
- 2026-09-29 13:40 [ruptura_volumen_tope] CIERRE POL stop-loss bruto -1.20% neto -2.30%
- 2026-09-29 13:40 [macd_momentum] CIERRE BNB momentum perdido bruto -0.07% neto -0.57%
- 2026-09-29 13:40 [macd_momentum_regimen] CIERRE BNB momentum perdido bruto -0.07% neto -0.57%
- 2026-09-29 13:40 [ruptura_volumen] CIERRE XPL timeout bruto -0.56% neto -1.36%
- 2026-09-29 13:40 [ruptura_volumen_tope] CIERRE XPL timeout bruto -0.56% neto -1.66%
- 2026-09-29 13:40 [ruptura_volumen_regimen] CIERRE XPL timeout bruto -0.56% neto -1.36%
- 2026-09-29 13:40 [macd_momentum] CIERRE SPX momentum perdido bruto -0.35% neto -0.85%
- 2026-09-29 13:40 [macd_momentum_regimen] CIERRE SPX momentum perdido bruto -0.35% neto -0.85%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
