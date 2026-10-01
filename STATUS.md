# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 00:06 UTC · vueltas 72 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 903.77 € (-2.21%) | 77 | 26 | 29% | -0.318% | -1.157% | -1.290% | -20.46 € |
| reversion_bb | 921.85 € (-0.26%) | 10 | 5 | 40% | -0.070% | -1.170% | -1.295% | -2.71 € |
| ruptura_volumen | 894.48 € (-3.22%) | 97 | 23 | 16% | -0.498% | -1.267% | -1.391% | -28.12 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 903.43 € (-2.25%) | 71 | 2 | 14% | -0.416% | -1.288% | -1.415% | -20.94 € |
| macd_momentum | 901.10 € (-2.50%) | 135 | 2 | 24% | -0.056% | -0.750% | -0.864% | -23.17 € |
| estocastico_rebote | 902.77 € (-2.32%) | 128 | 12 | 34% | -0.033% | -0.737% | -0.860% | -21.70 € |
| ruptura_estricta | 897.88 € (-2.85%) | 52 | 9 | 13% | -1.113% | -2.121% | -2.266% | -25.38 € |
| macd_sin_salida | 902.87 € (-2.31%) | 89 | 28 | 33% | -0.231% | -1.025% | -1.153% | -20.96 € |
| c_banda_atr_tope | 919.23 € (-0.54%) | 20 | 5 | 30% | -0.007% | -1.107% | -1.248% | -5.10 € |
| ruptura_volumen_tope | 915.93 € (-0.90%) | 28 | 5 | 18% | -0.171% | -1.271% | -1.357% | -8.20 € |
| c_banda_atr_regimen | 907.18 € (-1.85%) | 47 | 7 | 23% | -0.490% | -1.546% | -1.702% | -16.72 € |
| macd_momentum_regimen | 908.47 € (-1.71%) | 76 | 0 | 25% | -0.058% | -0.902% | -1.028% | -15.78 € |
| ruptura_volumen_regimen | 896.07 € (-3.05%) | 76 | 21 | 13% | -0.692% | -1.536% | -1.672% | -26.74 € |
| c_banda_atr_evento | 910.83 € (-1.45%) | 44 | 26 | 27% | -0.324% | -1.322% | -1.436% | -13.40 € |
| macd_momentum_evento | 906.09 € (-1.96%) | 88 | 2 | 17% | -0.102% | -0.902% | -1.004% | -18.18 € |
| ruptura_volumen_evento | 907.35 € (-1.83%) | 47 | 23 | 13% | -0.360% | -1.409% | -1.507% | -15.23 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 00:05 | ruptura_volumen_evento | ALGO | stop-loss | -1.33% | -1.83% | -0.41 |
| 2026-10-01 00:05 | ruptura_volumen_evento | SUI | stop-loss | -1.24% | -1.74% | -0.40 |
| 2026-10-01 00:05 | macd_momentum_evento | XDC | momentum perdido | +0.79% | -0.01% | -0.00 |
| 2026-10-01 00:05 | c_banda_atr_evento | MINA | take-profit | +2.00% | +1.20% | +0.27 |
| 2026-10-01 00:05 | ruptura_volumen_regimen | ALGO | stop-loss | -1.33% | -1.83% | -0.41 |
| 2026-10-01 00:05 | ruptura_volumen_regimen | SUI | stop-loss | -1.24% | -1.74% | -0.39 |
| 2026-10-01 00:05 | estocastico_rebote | XDC | timeout | +0.49% | -0.01% | -0.00 |
| 2026-10-01 00:05 | macd_momentum | XDC | momentum perdido | +0.79% | +0.29% | +0.07 |
| 2026-10-01 00:05 | pullback_tendencia | ENA | rotura de tendencia | -0.21% | -0.71% | -0.16 |
| 2026-10-01 00:05 | pullback_tendencia | ZRO | rotura de tendencia | -1.29% | -1.79% | -0.41 |
| 2026-10-01 00:05 | pullback_tendencia | ETH | rotura de tendencia | -0.22% | -0.72% | -0.16 |
| 2026-10-01 00:05 | ruptura_volumen | ALGO | stop-loss | -1.33% | -1.83% | -0.41 |
| 2026-10-01 00:05 | ruptura_volumen | SUI | stop-loss | -1.24% | -1.74% | -0.39 |
| 2026-10-01 00:05 | c_banda_atr | MINA | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 00:00 | macd_momentum_evento | BNB | momentum perdido | +0.14% | -0.35% | -0.08 |

## Eventos de la última vuelta

- 2026-10-01 00:05 [pullback_tendencia] CIERRE ETH rotura de tendencia bruto -0.22% neto -0.72%
- 2026-10-01 00:05 [ruptura_volumen] CIERRE SUI stop-loss bruto -1.24% neto -1.74%
- 2026-10-01 00:05 [ruptura_volumen_regimen] CIERRE SUI stop-loss bruto -1.24% neto -1.74%
- 2026-10-01 00:05 [ruptura_volumen_evento] CIERRE SUI stop-loss bruto -1.24% neto -1.74%
- 2026-10-01 00:05 [pullback_tendencia] CIERRE ZRO rotura de tendencia bruto -1.29% neto -1.79%
- 2026-10-01 00:05 [pullback_tendencia] CIERRE ENA rotura de tendencia bruto -0.21% neto -0.71%
- 2026-10-01 00:05 [ruptura_volumen] CIERRE ALGO stop-loss bruto -1.33% neto -1.83%
- 2026-10-01 00:05 [ruptura_volumen_regimen] CIERRE ALGO stop-loss bruto -1.33% neto -1.83%
- 2026-10-01 00:05 [ruptura_volumen_evento] CIERRE ALGO stop-loss bruto -1.33% neto -1.83%
- 2026-10-01 00:05 [macd_momentum] CIERRE XDC momentum perdido bruto +0.79% neto +0.29%
- 2026-10-01 00:05 [estocastico_rebote] CIERRE XDC timeout bruto +0.49% neto -0.01%
- 2026-10-01 00:05 [macd_momentum_evento] CIERRE XDC momentum perdido bruto +0.79% neto -0.01%
- 2026-10-01 00:00 [pullback_tendencia] ENTRADA NIGHT @ 0.03468 (22.58 €, apertura)
- 2026-10-01 00:05 [c_banda_atr] CIERRE MINA take-profit bruto +2.00% neto +1.50%
- 2026-10-01 00:05 [c_banda_atr_evento] CIERRE MINA take-profit bruto +2.00% neto +1.20%
- 2026-10-01 00:00 [estocastico_rebote] ENTRADA SEI @ 0.06487 (22.56 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
