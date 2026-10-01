# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 06:11 UTC · vueltas 144 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 908.11 € (-1.75%) | 135 | 20 | 40% | +0.164% | -0.529% | -0.647% | -16.49 € |
| reversion_bb | 921.57 € (-0.29%) | 17 | 2 | 47% | +0.422% | -0.678% | -0.789% | -2.67 € |
| ruptura_volumen | 891.77 € (-3.51%) | 178 | 22 | 24% | -0.166% | -0.812% | -0.920% | -32.99 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 902.78 € (-2.32%) | 95 | 14 | 17% | -0.242% | -1.020% | -1.134% | -22.18 € |
| macd_momentum | 893.65 € (-3.31%) | 256 | 12 | 25% | +0.078% | -0.524% | -0.629% | -30.58 € |
| estocastico_rebote | 902.57 € (-2.34%) | 173 | 18 | 39% | +0.102% | -0.549% | -0.669% | -21.86 € |
| ruptura_estricta | 902.81 € (-2.32%) | 87 | 30 | 29% | -0.359% | -1.162% | -1.295% | -23.31 € |
| macd_sin_salida | 905.58 € (-2.02%) | 169 | 27 | 44% | +0.187% | -0.468% | -0.580% | -18.23 € |
| c_banda_atr_tope | 917.32 € (-0.75%) | 30 | 5 | 30% | +0.135% | -0.965% | -1.091% | -6.68 € |
| ruptura_volumen_tope | 915.29 € (-0.97%) | 47 | 5 | 26% | +0.141% | -0.921% | -1.019% | -9.96 € |
| c_banda_atr_regimen | 912.29 € (-1.29%) | 79 | 18 | 42% | +0.174% | -0.656% | -0.794% | -12.00 € |
| macd_momentum_regimen | 902.71 € (-2.33%) | 170 | 12 | 26% | +0.101% | -0.552% | -0.661% | -21.51 € |
| ruptura_volumen_regimen | 892.54 € (-3.43%) | 152 | 21 | 21% | -0.256% | -0.927% | -1.038% | -32.18 € |
| c_banda_atr_evento | 914.15 € (-1.09%) | 102 | 20 | 43% | +0.317% | -0.442% | -0.546% | -10.44 € |
| macd_momentum_evento | 898.60 € (-2.77%) | 209 | 12 | 22% | +0.089% | -0.537% | -0.635% | -25.63 € |
| ruptura_volumen_evento | 904.46 € (-2.14%) | 128 | 22 | 26% | +0.014% | -0.692% | -0.784% | -20.30 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 06:10 | ruptura_volumen_evento | PUMP | timeout | +1.13% | +0.63% | +0.14 |
| 2026-10-01 06:10 | macd_momentum_evento | SOL | momentum perdido | +1.02% | +0.52% | +0.12 |
| 2026-10-01 06:10 | macd_momentum_evento | ETH | momentum perdido | +0.92% | +0.42% | +0.09 |
| 2026-10-01 06:10 | c_banda_atr_evento | SOL | timeout | +0.99% | +0.49% | +0.11 |
| 2026-10-01 06:10 | c_banda_atr_evento | BTC | timeout | +0.81% | +0.31% | +0.07 |
| 2026-10-01 06:10 | ruptura_volumen_regimen | PUMP | timeout | +1.13% | +0.63% | +0.14 |
| 2026-10-01 06:10 | macd_momentum_regimen | SOL | momentum perdido | +1.02% | +0.52% | +0.12 |
| 2026-10-01 06:10 | macd_momentum_regimen | ETH | momentum perdido | +0.92% | +0.42% | +0.09 |
| 2026-10-01 06:10 | ruptura_estricta | SKY | timeout | +1.36% | +0.86% | +0.19 |
| 2026-10-01 06:10 | macd_momentum | SOL | momentum perdido | +1.02% | +0.52% | +0.12 |
| 2026-10-01 06:10 | macd_momentum | ETH | momentum perdido | +0.92% | +0.42% | +0.09 |
| 2026-10-01 06:10 | ruptura_volumen | PUMP | timeout | +1.13% | +0.63% | +0.14 |
| 2026-10-01 06:10 | c_banda_atr | SOL | timeout | +0.99% | +0.49% | +0.11 |
| 2026-10-01 06:10 | c_banda_atr | BTC | timeout | +0.81% | +0.31% | +0.07 |
| 2026-10-01 06:05 | ruptura_volumen_evento | ARB | timeout | +1.21% | +0.71% | +0.16 |

## Eventos de la última vuelta

- 2026-10-01 06:10 [c_banda_atr] CIERRE BTC timeout bruto +0.81% neto +0.31%
- 2026-10-01 06:10 [c_banda_atr_evento] CIERRE BTC timeout bruto +0.81% neto +0.31%
- 2026-10-01 06:10 [macd_momentum] CIERRE ETH momentum perdido bruto +0.92% neto +0.42%
- 2026-10-01 06:10 [macd_momentum_regimen] CIERRE ETH momentum perdido bruto +0.92% neto +0.42%
- 2026-10-01 06:10 [macd_momentum_evento] CIERRE ETH momentum perdido bruto +0.92% neto +0.42%
- 2026-10-01 06:10 [c_banda_atr] CIERRE SOL timeout bruto +0.99% neto +0.49%
- 2026-10-01 06:10 [macd_momentum] CIERRE SOL momentum perdido bruto +1.02% neto +0.52%
- 2026-10-01 06:10 [macd_momentum_regimen] CIERRE SOL momentum perdido bruto +1.02% neto +0.52%
- 2026-10-01 06:10 [c_banda_atr_evento] CIERRE SOL timeout bruto +0.99% neto +0.49%
- 2026-10-01 06:10 [macd_momentum_evento] CIERRE SOL momentum perdido bruto +1.02% neto +0.52%
- 2026-10-01 06:05 [pullback_tendencia] ENTRADA LINK @ 12.7863 (22.55 €, apertura)
- 2026-10-01 06:05 [ruptura_volumen] ENTRADA SUI @ 1.0404 (22.28 €, apertura)
- 2026-10-01 06:05 [ruptura_volumen_regimen] ENTRADA SUI @ 1.0404 (22.30 €, apertura)
- 2026-10-01 06:05 [ruptura_volumen_evento] ENTRADA SUI @ 1.0404 (22.59 €, apertura)
- 2026-10-01 06:05 [macd_momentum] ENTRADA AAVE @ 148.3 (22.34 €, apertura)
- 2026-10-01 06:05 [macd_sin_salida] ENTRADA AAVE @ 148.3 (22.65 €, apertura)
- 2026-10-01 06:05 [macd_momentum_regimen] ENTRADA AAVE @ 148.3 (22.57 €, apertura)
- 2026-10-01 06:05 [macd_momentum_evento] ENTRADA AAVE @ 148.3 (22.47 €, apertura)
- 2026-10-01 06:10 [ruptura_volumen] CIERRE PUMP timeout bruto +1.13% neto +0.63%
- 2026-10-01 06:10 [ruptura_volumen_regimen] CIERRE PUMP timeout bruto +1.13% neto +0.63%
- 2026-10-01 06:10 [ruptura_volumen_evento] CIERRE PUMP timeout bruto +1.13% neto +0.63%
- 2026-10-01 06:05 [estocastico_rebote] ENTRADA LTC @ 59.5 (22.56 €, apertura)
- 2026-10-01 06:05 [pullback_tendencia] ENTRADA DOGE @ 0.0845487 (22.55 €, apertura)
- 2026-10-01 06:05 [macd_momentum] ENTRADA POL @ 0.10059 (22.34 €, apertura)
- 2026-10-01 06:05 [macd_sin_salida] ENTRADA POL @ 0.10059 (22.65 €, apertura)
- 2026-10-01 06:05 [macd_momentum_regimen] ENTRADA POL @ 0.10059 (22.57 €, apertura)
- 2026-10-01 06:05 [macd_momentum_evento] ENTRADA POL @ 0.10059 (22.47 €, apertura)
- 2026-10-01 06:05 [macd_momentum] ENTRADA ALGO @ 0.11365 (22.34 €, apertura)
- 2026-10-01 06:05 [macd_sin_salida] ENTRADA ALGO @ 0.11365 (22.65 €, apertura)
- 2026-10-01 06:05 [macd_momentum_regimen] ENTRADA ALGO @ 0.11365 (22.57 €, apertura)
- 2026-10-01 06:05 [macd_momentum_evento] ENTRADA ALGO @ 0.11365 (22.47 €, apertura)
- 2026-10-01 06:05 [estocastico_rebote] ENTRADA ONDO @ 0.44978 (22.56 €, apertura)
- 2026-10-01 06:05 [pullback_tendencia] ENTRADA BCH @ 272.65 (22.55 €, apertura)
- 2026-10-01 06:05 [ruptura_volumen] ENTRADA PEPE @ 3.869e-06 (22.28 €, apertura)
- 2026-10-01 06:05 [ruptura_volumen_regimen] ENTRADA PEPE @ 3.869e-06 (22.30 €, apertura)
- 2026-10-01 06:05 [ruptura_volumen_evento] ENTRADA PEPE @ 3.869e-06 (22.60 €, apertura)
- 2026-10-01 06:05 [macd_momentum] ENTRADA TRUMP @ 1.906 (22.34 €, apertura)
- 2026-10-01 06:05 [macd_sin_salida] ENTRADA TRUMP @ 1.906 (22.65 €, apertura)
- 2026-10-01 06:05 [macd_momentum_regimen] ENTRADA TRUMP @ 1.906 (22.57 €, apertura)
- 2026-10-01 06:05 [macd_momentum_evento] ENTRADA TRUMP @ 1.906 (22.47 €, apertura)
- 2026-10-01 06:10 [ruptura_estricta] CIERRE SKY timeout bruto +1.36% neto +0.86%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
