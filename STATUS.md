# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 04:41 UTC · vueltas 203 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 898.89 € (-2.74%) | 116 | 23 | 27% | -0.266% | -0.991% | -1.126% | -26.34 € |
| reversion_bb | 918.35 € (-0.64%) | 32 | 7 | 50% | +0.236% | -0.864% | -0.973% | -6.38 € |
| ruptura_volumen | 893.14 € (-3.36%) | 151 | 10 | 20% | -0.234% | -0.907% | -1.032% | -31.19 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 905.27 € (-2.05%) | 110 | 0 | 26% | -0.015% | -0.752% | -0.880% | -18.97 € |
| macd_momentum | 882.27 € (-4.54%) | 272 | 24 | 17% | -0.124% | -0.720% | -0.833% | -44.29 € |
| estocastico_rebote | 892.40 € (-3.45%) | 191 | 19 | 34% | -0.133% | -0.770% | -0.902% | -33.57 € |
| ruptura_estricta | 905.50 € (-2.03%) | 66 | 8 | 24% | -0.359% | -1.255% | -1.397% | -19.00 € |
| macd_sin_salida | 894.60 € (-3.21%) | 169 | 24 | 28% | -0.149% | -0.804% | -0.930% | -30.97 € |
| c_banda_atr_tope | 910.77 € (-1.46%) | 36 | 5 | 19% | -0.494% | -1.594% | -1.730% | -13.18 € |
| ruptura_volumen_tope | 910.51 € (-1.49%) | 54 | 5 | 17% | -0.149% | -1.138% | -1.257% | -14.11 € |
| c_banda_atr_regimen | 900.77 € (-2.54%) | 77 | 1 | 22% | -0.490% | -1.329% | -1.458% | -23.47 € |
| macd_momentum_regimen | 886.75 € (-4.06%) | 196 | 0 | 15% | -0.209% | -0.842% | -0.955% | -37.49 € |
| ruptura_volumen_regimen | 898.84 € (-2.75%) | 116 | 0 | 18% | -0.234% | -0.959% | -1.087% | -25.40 € |
| c_banda_atr_evento | 901.95 € (-2.41%) | 84 | 23 | 23% | -0.394% | -1.209% | -1.345% | -23.28 € |
| macd_momentum_evento | 894.67 € (-3.20%) | 152 | 24 | 12% | -0.248% | -0.921% | -1.033% | -31.92 € |
| ruptura_volumen_evento | 898.64 € (-2.77%) | 92 | 10 | 12% | -0.434% | -1.221% | -1.346% | -25.69 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 04:40 | macd_momentum_evento | SOL | momentum perdido | -0.19% | -0.69% | -0.15 |
| 2026-09-30 04:40 | macd_momentum | SOL | momentum perdido | -0.19% | -0.69% | -0.15 |
| 2026-09-30 04:35 | c_banda_atr_evento | JUP | timeout | -0.13% | -0.63% | -0.14 |
| 2026-09-30 04:35 | c_banda_atr_evento | ARB | timeout | -0.56% | -1.06% | -0.24 |
| 2026-09-30 04:35 | macd_sin_salida | NIGHT | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 04:35 | c_banda_atr | JUP | timeout | -0.13% | -0.63% | -0.14 |
| 2026-09-30 04:35 | c_banda_atr | ARB | timeout | -0.56% | -1.06% | -0.24 |
| 2026-09-30 04:30 | pullback_tendencia | ZRO | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 04:25 | macd_sin_salida | DASH | timeout | -0.45% | -0.95% | -0.21 |
| 2026-09-30 04:25 | reversion_bb | TON | take-profit | +1.69% | +0.59% | +0.14 |
| 2026-09-30 04:20 | macd_sin_salida | ZRO | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 04:20 | reversion_bb | ICP | take-profit | +1.76% | +0.66% | +0.15 |
| 2026-09-30 04:15 | ruptura_volumen_evento | BNB | timeout | +0.27% | -0.23% | -0.05 |
| 2026-09-30 04:15 | macd_momentum_evento | QNT | stop-loss | -1.58% | -2.08% | -0.47 |
| 2026-09-30 04:15 | c_banda_atr_evento | SPX | take-profit | +2.00% | +1.50% | +0.34 |

## Eventos de la última vuelta

- 2026-09-30 04:40 [macd_momentum] CIERRE SOL momentum perdido bruto -0.19% neto -0.69%
- 2026-09-30 04:40 [macd_momentum_evento] CIERRE SOL momentum perdido bruto -0.19% neto -0.69%
- 2026-09-30 04:35 [estocastico_rebote] ENTRADA QNT @ 250.9 (22.27 €, apertura)
- 2026-09-30 04:35 [ruptura_volumen] ENTRADA TRX @ 0.296804 (22.33 €, apertura)
- 2026-09-30 04:35 [ruptura_estricta] ENTRADA TRX @ 0.296804 (22.63 €, apertura)
- 2026-09-30 04:35 [ruptura_volumen_evento] ENTRADA TRX @ 0.296804 (22.46 €, apertura)
- 2026-09-30 04:35 [ruptura_volumen] ENTRADA NIGHT @ 0.02931 (22.33 €, apertura)
- 2026-09-30 04:35 [ruptura_volumen_evento] ENTRADA NIGHT @ 0.02931 (22.46 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
