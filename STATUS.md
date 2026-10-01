# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 00:21 UTC · vueltas 75 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 901.72 € (-2.44%) | 81 | 24 | 27% | -0.333% | -1.155% | -1.286% | -21.46 € |
| reversion_bb | 921.88 € (-0.25%) | 10 | 5 | 40% | -0.070% | -1.170% | -1.295% | -2.71 € |
| ruptura_volumen | 893.77 € (-3.30%) | 97 | 23 | 16% | -0.498% | -1.267% | -1.391% | -28.12 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 903.30 € (-2.27%) | 73 | 3 | 14% | -0.405% | -1.267% | -1.392% | -21.18 € |
| macd_momentum | 901.15 € (-2.50%) | 135 | 3 | 24% | -0.056% | -0.750% | -0.864% | -23.17 € |
| estocastico_rebote | 901.85 € (-2.42%) | 130 | 12 | 34% | -0.056% | -0.756% | -0.879% | -22.60 € |
| ruptura_estricta | 897.38 € (-2.91%) | 52 | 9 | 13% | -1.113% | -2.121% | -2.266% | -25.38 € |
| macd_sin_salida | 901.59 € (-2.45%) | 90 | 27 | 33% | -0.220% | -1.010% | -1.138% | -20.91 € |
| c_banda_atr_tope | 918.75 € (-0.59%) | 20 | 5 | 30% | -0.007% | -1.107% | -1.248% | -5.10 € |
| ruptura_volumen_tope | 915.61 € (-0.93%) | 29 | 4 | 17% | -0.158% | -1.258% | -1.342% | -8.40 € |
| c_banda_atr_regimen | 906.79 € (-1.89%) | 47 | 7 | 23% | -0.490% | -1.546% | -1.702% | -16.72 € |
| macd_momentum_regimen | 908.47 € (-1.71%) | 76 | 0 | 25% | -0.058% | -0.902% | -1.028% | -15.78 € |
| ruptura_volumen_regimen | 895.36 € (-3.13%) | 76 | 21 | 13% | -0.692% | -1.536% | -1.672% | -26.74 € |
| c_banda_atr_evento | 908.54 € (-1.70%) | 48 | 24 | 25% | -0.348% | -1.323% | -1.435% | -14.63 € |
| macd_momentum_evento | 906.14 € (-1.96%) | 88 | 3 | 17% | -0.102% | -0.902% | -1.004% | -18.18 € |
| ruptura_volumen_evento | 906.62 € (-1.91%) | 47 | 23 | 13% | -0.360% | -1.409% | -1.507% | -15.23 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 00:20 | c_banda_atr_evento | PEPE | timeout | -1.08% | -1.88% | -0.43 |
| 2026-10-01 00:20 | c_banda_atr_evento | JUP | timeout | +0.29% | -0.51% | -0.12 |
| 2026-10-01 00:20 | c_banda_atr_evento | USELESS | stop-loss | -1.57% | -2.07% | -0.47 |
| 2026-10-01 00:20 | ruptura_volumen_tope | LTC | timeout | +0.20% | -0.90% | -0.21 |
| 2026-10-01 00:20 | estocastico_rebote | PUMP | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 00:20 | pullback_tendencia | VVV | rotura de tendencia | +0.02% | -0.48% | -0.11 |
| 2026-10-01 00:20 | pullback_tendencia | LINK | rotura de tendencia | -0.06% | -0.56% | -0.13 |
| 2026-10-01 00:20 | c_banda_atr | PEPE | timeout | -1.08% | -1.58% | -0.36 |
| 2026-10-01 00:20 | c_banda_atr | JUP | timeout | +0.29% | -0.21% | -0.05 |
| 2026-10-01 00:20 | c_banda_atr | USELESS | stop-loss | -1.57% | -2.07% | -0.47 |
| 2026-10-01 00:15 | c_banda_atr_evento | SUI | timeout | -0.09% | -0.89% | -0.20 |
| 2026-10-01 00:15 | estocastico_rebote | HBAR | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 00:15 | c_banda_atr | SUI | timeout | -0.09% | -0.59% | -0.13 |
| 2026-10-01 00:10 | macd_sin_salida | XDC | timeout | +0.76% | +0.26% | +0.06 |
| 2026-10-01 00:05 | ruptura_volumen_evento | ALGO | stop-loss | -1.33% | -1.83% | -0.41 |

## Eventos de la última vuelta

- 2026-10-01 00:15 [pullback_tendencia] ENTRADA LINK @ 12.6421 (22.58 €, apertura)
- 2026-10-01 00:20 [pullback_tendencia] CIERRE LINK rotura de tendencia bruto -0.06% neto -0.56%
- 2026-10-01 00:15 [estocastico_rebote] ENTRADA ADA @ 0.216808 (22.55 €, apertura)
- 2026-10-01 00:20 [estocastico_rebote] CIERRE PUMP stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 00:20 [ruptura_volumen_tope] CIERRE LTC timeout bruto +0.20% neto -0.90%
- 2026-10-01 00:15 [macd_momentum] ENTRADA FET @ 0.2014 (22.53 €, apertura)
- 2026-10-01 00:15 [macd_momentum_evento] ENTRADA FET @ 0.2014 (22.65 €, apertura)
- 2026-10-01 00:15 [c_banda_atr] ENTRADA WLD @ 0.474 (22.59 €, apertura)
- 2026-10-01 00:15 [c_banda_atr_evento] ENTRADA WLD @ 0.474 (22.77 €, apertura)
- 2026-10-01 00:20 [c_banda_atr] CIERRE USELESS stop-loss bruto -1.57% neto -2.07%
- 2026-10-01 00:20 [c_banda_atr_evento] CIERRE USELESS stop-loss bruto -1.57% neto -2.07%
- 2026-10-01 00:20 [c_banda_atr] CIERRE JUP timeout bruto +0.29% neto -0.21%
- 2026-10-01 00:20 [c_banda_atr_evento] CIERRE JUP timeout bruto +0.29% neto -0.51%
- 2026-10-01 00:20 [c_banda_atr] CIERRE PEPE timeout bruto -1.08% neto -1.58%
- 2026-10-01 00:20 [c_banda_atr_evento] CIERRE PEPE timeout bruto -1.08% neto -1.88%
- 2026-10-01 00:15 [pullback_tendencia] ENTRADA VVV @ 24.322 (22.58 €, apertura)
- 2026-10-01 00:20 [pullback_tendencia] CIERRE VVV rotura de tendencia bruto +0.02% neto -0.48%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
