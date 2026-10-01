# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 07:21 UTC · vueltas 158 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 906.18 € (-1.95%) | 144 | 23 | 40% | +0.165% | -0.516% | -0.635% | -17.15 € |
| reversion_bb | 921.38 € (-0.31%) | 17 | 3 | 47% | +0.422% | -0.678% | -0.789% | -2.67 € |
| ruptura_volumen | 888.52 € (-3.86%) | 195 | 9 | 24% | -0.158% | -0.792% | -0.902% | -35.20 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 899.45 € (-2.68%) | 113 | 5 | 17% | -0.218% | -0.952% | -1.057% | -24.58 € |
| macd_momentum | 889.55 € (-3.75%) | 276 | 12 | 23% | +0.053% | -0.542% | -0.647% | -34.01 € |
| estocastico_rebote | 900.19 € (-2.60%) | 178 | 33 | 39% | +0.122% | -0.525% | -0.645% | -21.50 € |
| ruptura_estricta | 898.41 € (-2.79%) | 103 | 18 | 30% | -0.306% | -1.062% | -1.190% | -25.17 € |
| macd_sin_salida | 900.02 € (-2.62%) | 183 | 31 | 42% | +0.114% | -0.529% | -0.639% | -22.23 € |
| c_banda_atr_tope | 916.72 € (-0.81%) | 31 | 4 | 29% | +0.082% | -1.018% | -1.143% | -7.27 € |
| ruptura_volumen_tope | 914.18 € (-1.09%) | 53 | 4 | 30% | +0.180% | -0.819% | -0.927% | -9.99 € |
| c_banda_atr_regimen | 910.48 € (-1.49%) | 87 | 22 | 43% | +0.174% | -0.626% | -0.764% | -12.59 € |
| macd_momentum_regimen | 898.57 € (-2.78%) | 190 | 12 | 24% | +0.062% | -0.575% | -0.683% | -24.97 € |
| ruptura_volumen_regimen | 889.37 € (-3.77%) | 168 | 9 | 21% | -0.241% | -0.897% | -1.010% | -34.34 € |
| c_banda_atr_evento | 912.21 € (-1.30%) | 111 | 23 | 43% | +0.306% | -0.432% | -0.538% | -11.10 € |
| macd_momentum_evento | 894.48 € (-3.22%) | 229 | 12 | 20% | +0.058% | -0.558% | -0.655% | -29.07 € |
| ruptura_volumen_evento | 901.16 € (-2.50%) | 145 | 9 | 26% | +0.003% | -0.679% | -0.775% | -22.53 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 07:20 | ruptura_volumen_evento | USELESS | stop-loss | -1.26% | -1.76% | -0.40 |
| 2026-10-01 07:20 | ruptura_volumen_evento | FET | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-01 07:20 | macd_momentum_evento | ONDO | momentum perdido | -0.30% | -0.80% | -0.18 |
| 2026-10-01 07:20 | macd_momentum_evento | DOGE | momentum perdido | -0.27% | -0.77% | -0.17 |
| 2026-10-01 07:20 | macd_momentum_evento | SUI | momentum perdido | -0.82% | -1.32% | -0.30 |
| 2026-10-01 07:20 | c_banda_atr_evento | JUP | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-10-01 07:20 | ruptura_volumen_regimen | USELESS | stop-loss | -1.26% | -1.76% | -0.39 |
| 2026-10-01 07:20 | ruptura_volumen_regimen | FET | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-01 07:20 | macd_momentum_regimen | ONDO | momentum perdido | -0.30% | -0.80% | -0.18 |
| 2026-10-01 07:20 | macd_momentum_regimen | DOGE | momentum perdido | -0.27% | -0.77% | -0.17 |
| 2026-10-01 07:20 | macd_momentum_regimen | SUI | momentum perdido | -0.82% | -1.32% | -0.30 |
| 2026-10-01 07:20 | c_banda_atr_regimen | JUP | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-10-01 07:20 | ruptura_volumen_tope | FET | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-10-01 07:20 | c_banda_atr_tope | JUP | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-10-01 07:20 | macd_sin_salida | PENGU | stop-loss | -1.50% | -2.00% | -0.45 |

## Eventos de la última vuelta

- 2026-10-01 07:20 [pullback_tendencia] CIERRE XRP rotura de tendencia bruto -0.63% neto -1.13%
- 2026-10-01 07:20 [pullback_tendencia] CIERRE ETH rotura de tendencia bruto +0.77% neto +0.27%
- 2026-10-01 07:20 [pullback_tendencia] CIERRE SOL rotura de tendencia bruto -0.58% neto -1.08%
- 2026-10-01 07:20 [pullback_tendencia] CIERRE ADA rotura de tendencia bruto -0.46% neto -0.96%
- 2026-10-01 07:20 [macd_momentum] CIERRE SUI momentum perdido bruto -0.82% neto -1.32%
- 2026-10-01 07:20 [macd_momentum_regimen] CIERRE SUI momentum perdido bruto -0.82% neto -1.32%
- 2026-10-01 07:20 [macd_momentum_evento] CIERRE SUI momentum perdido bruto -0.82% neto -1.32%
- 2026-10-01 07:20 [pullback_tendencia] CIERRE AVAX rotura de tendencia bruto -0.07% neto -0.57%
- 2026-10-01 07:20 [pullback_tendencia] CIERRE ZEC rotura de tendencia bruto -0.55% neto -1.05%
- 2026-10-01 07:20 [pullback_tendencia] CIERRE UNI rotura de tendencia bruto -0.52% neto -1.02%
- 2026-10-01 07:20 [pullback_tendencia] CIERRE DOGE rotura de tendencia bruto -0.37% neto -0.87%
- 2026-10-01 07:20 [macd_momentum] CIERRE DOGE momentum perdido bruto -0.27% neto -0.77%
- 2026-10-01 07:20 [macd_momentum_regimen] CIERRE DOGE momentum perdido bruto -0.27% neto -0.77%
- 2026-10-01 07:20 [macd_momentum_evento] CIERRE DOGE momentum perdido bruto -0.27% neto -0.77%
- 2026-10-01 07:20 [macd_sin_salida] CIERRE ARB stop-loss bruto -1.52% neto -2.02%
- 2026-10-01 07:20 [ruptura_volumen] CIERRE FET stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 07:20 [ruptura_volumen_tope] CIERRE FET stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 07:20 [ruptura_volumen_regimen] CIERRE FET stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 07:20 [ruptura_volumen_evento] CIERRE FET stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 07:20 [macd_momentum] CIERRE ONDO momentum perdido bruto -0.30% neto -0.80%
- 2026-10-01 07:20 [macd_momentum_regimen] CIERRE ONDO momentum perdido bruto -0.30% neto -0.80%
- 2026-10-01 07:20 [macd_momentum_evento] CIERRE ONDO momentum perdido bruto -0.30% neto -0.80%
- 2026-10-01 07:20 [ruptura_volumen] CIERRE USELESS stop-loss bruto -1.26% neto -1.76%
- 2026-10-01 07:20 [ruptura_estricta] CIERRE USELESS stop-loss bruto -2.45% neto -2.95%
- 2026-10-01 07:20 [ruptura_volumen_regimen] CIERRE USELESS stop-loss bruto -1.26% neto -1.76%
- 2026-10-01 07:20 [ruptura_volumen_evento] CIERRE USELESS stop-loss bruto -1.26% neto -1.76%
- 2026-10-01 07:20 [pullback_tendencia] CIERRE BCH rotura de tendencia bruto -0.35% neto -0.85%
- 2026-10-01 07:20 [c_banda_atr] CIERRE JUP stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:15 [reversion_bb] ENTRADA JUP @ 0.2887 (23.04 €, apertura)
- 2026-10-01 07:20 [estocastico_rebote] CIERRE JUP stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:20 [macd_sin_salida] CIERRE JUP stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:20 [c_banda_atr_tope] CIERRE JUP stop-loss bruto -1.50% neto -2.60%
- 2026-10-01 07:20 [c_banda_atr_regimen] CIERRE JUP stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:20 [c_banda_atr_evento] CIERRE JUP stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:15 [pullback_tendencia] ENTRADA ASTER @ 0.67548 (22.50 €, apertura)
- 2026-10-01 07:20 [macd_sin_salida] CIERRE PENGU stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:15 [estocastico_rebote] ENTRADA BNB @ 680.25 (22.57 €, apertura)
- 2026-10-01 07:20 [pullback_tendencia] CIERRE TON rotura de tendencia bruto -0.22% neto -0.72%
- 2026-10-01 07:15 [estocastico_rebote] ENTRADA KAS @ 0.03864 (22.57 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
