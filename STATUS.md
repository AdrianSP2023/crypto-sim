# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 07:36 UTC · vueltas 161 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 899.59 € (-2.67%) | 157 | 10 | 37% | +0.018% | -0.648% | -0.772% | -23.34 € |
| reversion_bb | 920.72 € (-0.38%) | 19 | 10 | 42% | +0.220% | -0.880% | -0.993% | -3.86 € |
| ruptura_volumen | 885.97 € (-4.14%) | 202 | 2 | 23% | -0.199% | -0.828% | -0.938% | -38.03 € |
| rebote_extremo | 924.20 € (-0.00%) | 3 | 2 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 897.84 € (-2.86%) | 119 | 1 | 16% | -0.244% | -0.965% | -1.071% | -26.23 € |
| macd_momentum | 885.25 € (-4.22%) | 288 | 1 | 22% | -0.006% | -0.597% | -0.704% | -39.00 € |
| estocastico_rebote | 891.35 € (-3.56%) | 199 | 15 | 35% | -0.050% | -0.681% | -0.798% | -31.00 € |
| ruptura_estricta | 892.90 € (-3.39%) | 111 | 11 | 28% | -0.431% | -1.169% | -1.296% | -29.75 € |
| macd_sin_salida | 890.92 € (-3.61%) | 204 | 11 | 38% | -0.057% | -0.685% | -0.798% | -31.95 € |
| c_banda_atr_tope | 915.19 € (-0.98%) | 34 | 2 | 26% | -0.031% | -1.131% | -1.253% | -8.85 € |
| ruptura_volumen_tope | 912.77 € (-1.24%) | 56 | 1 | 29% | +0.088% | -0.884% | -0.999% | -11.38 € |
| c_banda_atr_regimen | 903.78 € (-2.21%) | 102 | 7 | 36% | -0.071% | -0.827% | -0.968% | -19.39 € |
| macd_momentum_regimen | 894.23 € (-3.25%) | 202 | 1 | 22% | -0.022% | -0.652% | -0.763% | -30.01 € |
| ruptura_volumen_regimen | 886.82 € (-4.05%) | 175 | 2 | 21% | -0.284% | -0.934% | -1.047% | -37.18 € |
| c_banda_atr_evento | 905.58 € (-2.02%) | 124 | 10 | 39% | +0.106% | -0.607% | -0.722% | -17.33 € |
| macd_momentum_evento | 890.16 € (-3.69%) | 241 | 1 | 19% | -0.013% | -0.623% | -0.724% | -34.09 € |
| ruptura_volumen_evento | 898.57 € (-2.78%) | 152 | 2 | 24% | -0.058% | -0.731% | -0.829% | -25.41 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 07:35 | macd_momentum_evento | XMR | momentum perdido | -0.85% | -1.35% | -0.30 |
| 2026-10-01 07:35 | macd_momentum_evento | DOT | momentum perdido | -0.77% | -1.27% | -0.29 |
| 2026-10-01 07:35 | macd_momentum_regimen | XMR | momentum perdido | -0.85% | -1.35% | -0.30 |
| 2026-10-01 07:35 | macd_momentum_regimen | DOT | momentum perdido | -0.77% | -1.27% | -0.29 |
| 2026-10-01 07:35 | macd_momentum | XMR | momentum perdido | -0.85% | -1.35% | -0.30 |
| 2026-10-01 07:35 | macd_momentum | DOT | momentum perdido | -0.77% | -1.27% | -0.28 |
| 2026-10-01 07:35 | pullback_tendencia | XDC | rotura de tendencia | -1.14% | -1.64% | -0.37 |
| 2026-10-01 07:35 | pullback_tendencia | QNT | rotura de tendencia | -0.09% | -0.59% | -0.13 |
| 2026-10-01 07:30 | ruptura_volumen_evento | SPX | stop-loss | -2.50% | -3.00% | -0.68 |
| 2026-10-01 07:30 | ruptura_volumen_evento | SEI | stop-loss | -1.49% | -1.99% | -0.45 |
| 2026-10-01 07:30 | ruptura_volumen_evento | PEPE | stop-loss | -1.42% | -1.92% | -0.43 |
| 2026-10-01 07:30 | ruptura_volumen_evento | DOT | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-01 07:30 | macd_momentum_evento | APT | stop-loss | -1.57% | -2.07% | -0.47 |
| 2026-10-01 07:30 | macd_momentum_evento | SEI | momentum perdido | -1.49% | -1.99% | -0.45 |
| 2026-10-01 07:30 | macd_momentum_evento | KSM | stop-loss | -1.92% | -2.42% | -0.54 |

## Eventos de la última vuelta

- 2026-10-01 07:30 [pullback_tendencia] ENTRADA QNT @ 259.07 (22.46 €, apertura)
- 2026-10-01 07:35 [pullback_tendencia] CIERRE QNT rotura de tendencia bruto -0.09% neto -0.59%
- 2026-10-01 07:35 [macd_momentum] CIERRE DOT momentum perdido bruto -0.77% neto -1.27%
- 2026-10-01 07:35 [macd_momentum_regimen] CIERRE DOT momentum perdido bruto -0.77% neto -1.27%
- 2026-10-01 07:35 [macd_momentum_evento] CIERRE DOT momentum perdido bruto -0.77% neto -1.27%
- 2026-10-01 07:30 [rebote_extremo] ENTRADA ARB @ 0.1766 (23.10 €, apertura)
- 2026-10-01 07:30 [estocastico_rebote] ENTRADA ENA @ 0.2369 (22.33 €, apertura)
- 2026-10-01 07:30 [estocastico_rebote] ENTRADA POL @ 0.09903 (22.33 €, apertura)
- 2026-10-01 07:30 [reversion_bb] ENTRADA ONDO @ 0.44532 (23.01 €, apertura)
- 2026-10-01 07:35 [pullback_tendencia] CIERRE XDC rotura de tendencia bruto -1.14% neto -1.64%
- 2026-10-01 07:30 [rebote_extremo] ENTRADA JUP @ 0.28567 (23.10 €, apertura)
- 2026-10-01 07:30 [reversion_bb] ENTRADA OP @ 0.1144 (23.01 €, apertura)
- 2026-10-01 07:30 [reversion_bb] ENTRADA TRUMP @ 1.868 (23.01 €, apertura)
- 2026-10-01 07:30 [estocastico_rebote] ENTRADA TRUMP @ 1.868 (22.33 €, apertura)
- 2026-10-01 07:35 [macd_momentum] CIERRE XMR momentum perdido bruto -0.85% neto -1.35%
- 2026-10-01 07:35 [macd_momentum_regimen] CIERRE XMR momentum perdido bruto -0.85% neto -1.35%
- 2026-10-01 07:35 [macd_momentum_evento] CIERRE XMR momentum perdido bruto -0.85% neto -1.35%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
