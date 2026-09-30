# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 02:01 UTC · vueltas 171 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 902.81 € (-2.32%) | 96 | 23 | 29% | -0.283% | -1.055% | -1.201% | -23.24 € |
| reversion_bb | 919.74 € (-0.49%) | 26 | 8 | 50% | +0.198% | -0.902% | -1.006% | -5.42 € |
| ruptura_volumen | 899.34 € (-2.69%) | 125 | 20 | 22% | -0.153% | -0.862% | -0.987% | -24.63 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 906.09 € (-1.96%) | 97 | 4 | 26% | -0.049% | -0.818% | -0.947% | -18.20 € |
| macd_momentum | 885.47 € (-4.19%) | 242 | 15 | 17% | -0.114% | -0.722% | -0.836% | -39.67 € |
| estocastico_rebote | 894.13 € (-3.26%) | 178 | 6 | 34% | -0.097% | -0.743% | -0.878% | -30.27 € |
| ruptura_estricta | 908.25 € (-1.73%) | 55 | 11 | 27% | -0.215% | -1.189% | -1.321% | -15.04 € |
| macd_sin_salida | 898.59 € (-2.78%) | 149 | 15 | 30% | -0.105% | -0.780% | -0.906% | -26.57 € |
| c_banda_atr_tope | 912.05 € (-1.32%) | 31 | 5 | 19% | -0.564% | -1.664% | -1.809% | -11.86 € |
| ruptura_volumen_tope | 912.78 € (-1.24%) | 44 | 5 | 18% | -0.038% | -1.117% | -1.236% | -11.31 € |
| c_banda_atr_regimen | 902.85 € (-2.31%) | 68 | 9 | 24% | -0.518% | -1.401% | -1.536% | -21.87 € |
| macd_momentum_regimen | 887.21 € (-4.01%) | 193 | 1 | 15% | -0.209% | -0.844% | -0.956% | -37.01 € |
| ruptura_volumen_regimen | 902.63 € (-2.34%) | 101 | 11 | 21% | -0.166% | -0.924% | -1.051% | -21.37 € |
| c_banda_atr_evento | 906.17 € (-1.96%) | 64 | 23 | 25% | -0.460% | -1.353% | -1.507% | -19.90 € |
| macd_momentum_evento | 897.92 € (-2.85%) | 122 | 15 | 13% | -0.260% | -0.976% | -1.088% | -27.23 € |
| ruptura_volumen_evento | 904.88 € (-2.09%) | 66 | 20 | 14% | -0.360% | -1.260% | -1.385% | -19.08 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 02:00 | ruptura_volumen_evento | JUP | stop-loss | -1.57% | -2.07% | -0.47 |
| 2026-09-30 02:00 | c_banda_atr_evento | XDC | timeout | -0.82% | -1.62% | -0.37 |
| 2026-09-30 02:00 | ruptura_volumen_regimen | JUP | stop-loss | -1.57% | -2.07% | -0.47 |
| 2026-09-30 02:00 | c_banda_atr_tope | XDC | timeout | -0.82% | -1.92% | -0.44 |
| 2026-09-30 02:00 | ruptura_volumen | JUP | stop-loss | -1.57% | -2.07% | -0.47 |
| 2026-09-30 02:00 | c_banda_atr | XDC | timeout | -0.82% | -1.32% | -0.30 |
| 2026-09-30 01:55 | macd_momentum_evento | QNT | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 01:55 | macd_momentum | QNT | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-09-30 01:50 | macd_momentum_evento | ONDO | momentum perdido | +0.06% | -0.44% | -0.10 |
| 2026-09-30 01:50 | c_banda_atr_evento | ZEC | timeout | +0.84% | +0.04% | +0.01 |
| 2026-09-30 01:50 | estocastico_rebote | NIGHT | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-09-30 01:50 | macd_momentum | ONDO | momentum perdido | +0.06% | -0.44% | -0.10 |
| 2026-09-30 01:50 | c_banda_atr | ZEC | timeout | +0.84% | +0.34% | +0.08 |
| 2026-09-30 01:45 | c_banda_atr_evento | CRV | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 01:45 | c_banda_atr_tope | BCH | timeout | -0.41% | -1.51% | -0.35 |

## Eventos de la última vuelta

- 2026-09-30 02:00 [c_banda_atr] CIERRE XDC timeout bruto -0.82% neto -1.32%
- 2026-09-30 02:00 [c_banda_atr_tope] CIERRE XDC timeout bruto -0.82% neto -1.92%
- 2026-09-30 02:00 [c_banda_atr_evento] CIERRE XDC timeout bruto -0.82% neto -1.62%
- 2026-09-30 01:55 [ruptura_volumen_regimen] ENTRADA CRV @ 0.34648 (22.58 €, apertura)
- 2026-09-30 01:55 [ruptura_volumen] ENTRADA ENA @ 0.2206 (22.50 €, apertura)
- 2026-09-30 01:55 [ruptura_volumen_regimen] ENTRADA ENA @ 0.2206 (22.58 €, apertura)
- 2026-09-30 01:55 [ruptura_volumen_evento] ENTRADA ENA @ 0.2206 (22.64 €, apertura)
- 2026-09-30 02:00 [ruptura_volumen] CIERRE JUP stop-loss bruto -1.57% neto -2.07%
- 2026-09-30 02:00 [ruptura_volumen_regimen] CIERRE JUP stop-loss bruto -1.57% neto -2.07%
- 2026-09-30 02:00 [ruptura_volumen_evento] CIERRE JUP stop-loss bruto -1.57% neto -2.07%
- 2026-09-30 01:55 [ruptura_volumen] ENTRADA TRX @ 0.295142 (22.49 €, apertura)
- 2026-09-30 01:55 [ruptura_volumen_regimen] ENTRADA TRX @ 0.295142 (22.57 €, apertura)
- 2026-09-30 01:55 [ruptura_volumen_evento] ENTRADA TRX @ 0.295142 (22.63 €, apertura)
- 2026-09-30 01:55 [c_banda_atr_tope] ENTRADA SEI @ 0.06546 (22.81 €, apertura)
- 2026-09-30 01:55 [ruptura_volumen_regimen] ENTRADA SEI @ 0.06546 (22.57 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
