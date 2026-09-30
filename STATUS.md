# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 16:56 UTC · vueltas 56 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 914.81 € (-1.02%) | 37 | 12 | 35% | -0.134% | -1.234% | -1.394% | -10.56 € |
| reversion_bb | 923.92 € (-0.04%) | 4 | 0 | 75% | +0.750% | -0.350% | -0.453% | -0.33 € |
| ruptura_volumen | 905.21 € (-2.06%) | 52 | 16 | 17% | -0.578% | -1.580% | -1.725% | -18.92 € |
| rebote_extremo | 924.45 € (+0.02%) | 0 | 2 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 911.99 € (-1.32%) | 36 | 5 | 17% | -0.434% | -1.534% | -1.664% | -12.71 € |
| macd_momentum | 912.51 € (-1.27%) | 60 | 4 | 32% | +0.052% | -0.883% | -1.024% | -12.22 € |
| estocastico_rebote | 918.00 € (-0.67%) | 65 | 10 | 51% | +0.295% | -0.584% | -0.745% | -8.83 € |
| ruptura_estricta | 901.57 € (-2.45%) | 40 | 4 | 10% | -1.291% | -2.391% | -2.538% | -22.08 € |
| macd_sin_salida | 909.70 € (-1.57%) | 54 | 8 | 35% | -0.190% | -1.174% | -1.318% | -14.65 € |
| c_banda_atr_tope | 923.70 € (-0.06%) | 9 | 5 | 56% | +0.446% | -0.654% | -0.837% | -1.36 € |
| ruptura_volumen_tope | 921.53 € (-0.29%) | 10 | 5 | 30% | -0.085% | -1.185% | -1.269% | -2.74 € |
| c_banda_atr_regimen | 913.73 € (-1.14%) | 35 | 8 | 31% | -0.256% | -1.356% | -1.509% | -10.97 € |
| macd_momentum_regimen | 912.84 € (-1.23%) | 52 | 3 | 31% | +0.021% | -0.981% | -1.122% | -11.78 € |
| ruptura_volumen_regimen | 905.02 € (-2.08%) | 53 | 15 | 17% | -0.589% | -1.582% | -1.727% | -19.31 € |
| c_banda_atr_evento | 926.12 € (+0.20%) | 3 | 14 | 100% | +2.000% | +0.900% | +0.696% | +0.62 € |
| macd_momentum_evento | 921.86 € (-0.26%) | 13 | 4 | 38% | +0.140% | -0.960% | -1.113% | -2.88 € |
| ruptura_volumen_evento | 923.93 € (-0.03%) | 2 | 16 | 50% | +0.650% | -0.450% | -0.479% | -0.21 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 16:55 | estocastico_rebote | BNB | timeout | +0.17% | -0.63% | -0.14 |
| 2026-09-30 16:55 | estocastico_rebote | ASTER | timeout | -1.05% | -1.85% | -0.43 |
| 2026-09-30 16:55 | pullback_tendencia | XDC | rotura de tendencia | -0.36% | -1.46% | -0.33 |
| 2026-09-30 16:50 | c_banda_atr_evento | ONDO | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-30 16:50 | c_banda_atr_regimen | ONDO | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-30 16:50 | estocastico_rebote | PENGU | take-profit | +1.80% | +1.00% | +0.23 |
| 2026-09-30 16:50 | estocastico_rebote | BCH | take-profit | +1.84% | +1.04% | +0.24 |
| 2026-09-30 16:50 | c_banda_atr | ONDO | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-30 16:45 | estocastico_rebote | XLM | take-profit | +1.80% | +1.00% | +0.23 |
| 2026-09-30 16:40 | ruptura_volumen_evento | HYPE | take-profit | +2.50% | +1.40% | +0.32 |
| 2026-09-30 16:40 | macd_momentum_evento | TRUMP | momentum perdido | -0.49% | -1.59% | -0.37 |
| 2026-09-30 16:40 | macd_momentum_evento | HBAR | momentum perdido | -0.74% | -1.84% | -0.42 |
| 2026-09-30 16:40 | ruptura_volumen_regimen | HYPE | take-profit | +2.50% | +2.00% | +0.45 |
| 2026-09-30 16:40 | c_banda_atr_regimen | XMR | timeout | +0.32% | -0.78% | -0.18 |
| 2026-09-30 16:40 | ruptura_volumen_tope | HYPE | take-profit | +2.50% | +1.40% | +0.32 |

## Eventos de la última vuelta

- 2026-09-30 16:50 [pullback_tendencia] ENTRADA HBAR @ 0.09526 (22.80 €, apertura)
- 2026-09-30 16:50 [ruptura_volumen] ENTRADA AAVE @ 142.43 (22.63 €, apertura)
- 2026-09-30 16:50 [ruptura_volumen_regimen] ENTRADA AAVE @ 142.43 (22.62 €, apertura)
- 2026-09-30 16:50 [ruptura_volumen_evento] ENTRADA AAVE @ 142.43 (23.10 €, apertura)
- 2026-09-30 16:50 [ruptura_volumen] ENTRADA ZEC @ 1301.75 (22.63 €, apertura)
- 2026-09-30 16:50 [ruptura_volumen_regimen] ENTRADA ZEC @ 1301.75 (22.62 €, apertura)
- 2026-09-30 16:50 [ruptura_volumen_evento] ENTRADA ZEC @ 1301.75 (23.10 €, apertura)
- 2026-09-30 16:55 [pullback_tendencia] CIERRE XDC rotura de tendencia bruto -0.36% neto -1.46%
- 2026-09-30 16:50 [c_banda_atr] ENTRADA USELESS @ 0.22143 (22.84 €, apertura)
- 2026-09-30 16:50 [c_banda_atr_regimen] ENTRADA USELESS @ 0.22143 (22.83 €, apertura)
- 2026-09-30 16:50 [c_banda_atr_evento] ENTRADA USELESS @ 0.22143 (23.12 €, apertura)
- 2026-09-30 16:50 [ruptura_volumen] ENTRADA PEPE @ 3.856e-06 (22.63 €, apertura)
- 2026-09-30 16:50 [ruptura_volumen_regimen] ENTRADA PEPE @ 3.856e-06 (22.62 €, apertura)
- 2026-09-30 16:50 [ruptura_volumen_evento] ENTRADA PEPE @ 3.856e-06 (23.10 €, apertura)
- 2026-09-30 16:55 [estocastico_rebote] CIERRE ASTER timeout bruto -1.05% neto -1.85%
- 2026-09-30 16:50 [ruptura_volumen] ENTRADA DASH @ 54.609 (22.63 €, apertura)
- 2026-09-30 16:50 [ruptura_volumen_regimen] ENTRADA DASH @ 54.609 (22.62 €, apertura)
- 2026-09-30 16:50 [ruptura_volumen_evento] ENTRADA DASH @ 54.609 (23.10 €, apertura)
- 2026-09-30 16:50 [ruptura_volumen] ENTRADA PENGU @ 0.008832 (22.63 €, apertura)
- 2026-09-30 16:50 [ruptura_volumen_regimen] ENTRADA PENGU @ 0.008832 (22.62 €, apertura)
- 2026-09-30 16:50 [ruptura_volumen_evento] ENTRADA PENGU @ 0.008832 (23.10 €, apertura)
- 2026-09-30 16:55 [estocastico_rebote] CIERRE BNB timeout bruto +0.17% neto -0.63%
- 2026-09-30 16:50 [c_banda_atr] ENTRADA TON @ 1.338 (22.84 €, apertura)
- 2026-09-30 16:50 [c_banda_atr_regimen] ENTRADA TON @ 1.338 (22.83 €, apertura)
- 2026-09-30 16:50 [c_banda_atr_evento] ENTRADA TON @ 1.338 (23.12 €, apertura)
- 2026-09-30 16:50 [c_banda_atr] ENTRADA KAS @ 0.0385 (22.84 €, apertura)
- 2026-09-30 16:50 [ruptura_volumen] ENTRADA KAS @ 0.0385 (22.63 €, apertura)
- 2026-09-30 16:50 [c_banda_atr_regimen] ENTRADA KAS @ 0.0385 (22.83 €, apertura)
- 2026-09-30 16:50 [ruptura_volumen_regimen] ENTRADA KAS @ 0.0385 (22.62 €, apertura)
- 2026-09-30 16:50 [c_banda_atr_evento] ENTRADA KAS @ 0.0385 (23.12 €, apertura)
- 2026-09-30 16:50 [ruptura_volumen_evento] ENTRADA KAS @ 0.0385 (23.10 €, apertura)
- 2026-09-30 16:50 [ruptura_volumen] ENTRADA SEI @ 0.06564 (22.63 €, apertura)
- 2026-09-30 16:50 [ruptura_volumen_regimen] ENTRADA SEI @ 0.06564 (22.62 €, apertura)
- 2026-09-30 16:50 [ruptura_volumen_evento] ENTRADA SEI @ 0.06564 (23.10 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
