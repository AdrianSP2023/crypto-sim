# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 07:46 UTC · vueltas 163 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 899.34 € (-2.69%) | 158 | 9 | 37% | +0.014% | -0.652% | -0.775% | -23.62 € |
| reversion_bb | 919.52 € (-0.51%) | 20 | 9 | 40% | +0.134% | -0.966% | -1.078% | -4.46 € |
| ruptura_volumen | 885.95 € (-4.14%) | 202 | 2 | 23% | -0.199% | -0.828% | -0.938% | -38.03 € |
| rebote_extremo | 924.05 € (-0.02%) | 3 | 2 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 897.77 € (-2.86%) | 119 | 1 | 16% | -0.244% | -0.965% | -1.071% | -26.23 € |
| macd_momentum | 885.25 € (-4.22%) | 288 | 1 | 22% | -0.006% | -0.597% | -0.704% | -39.00 € |
| estocastico_rebote | 888.92 € (-3.82%) | 201 | 38 | 35% | -0.064% | -0.694% | -0.811% | -31.89 € |
| ruptura_estricta | 892.54 € (-3.43%) | 111 | 11 | 28% | -0.431% | -1.169% | -1.296% | -29.75 € |
| macd_sin_salida | 890.36 € (-3.67%) | 205 | 10 | 38% | -0.061% | -0.688% | -0.801% | -32.24 € |
| c_banda_atr_tope | 914.87 € (-1.01%) | 35 | 1 | 26% | -0.052% | -1.152% | -1.273% | -9.28 € |
| ruptura_volumen_tope | 912.77 € (-1.24%) | 56 | 1 | 29% | +0.088% | -0.884% | -0.999% | -11.38 € |
| c_banda_atr_regimen | 903.66 € (-2.23%) | 103 | 6 | 36% | -0.077% | -0.831% | -0.972% | -19.68 € |
| macd_momentum_regimen | 894.23 € (-3.25%) | 202 | 1 | 22% | -0.022% | -0.652% | -0.763% | -30.01 € |
| ruptura_volumen_regimen | 886.80 € (-4.05%) | 175 | 2 | 21% | -0.284% | -0.934% | -1.047% | -37.18 € |
| c_banda_atr_evento | 905.33 € (-2.05%) | 125 | 9 | 38% | +0.099% | -0.612% | -0.727% | -17.62 € |
| macd_momentum_evento | 890.16 € (-3.69%) | 241 | 1 | 19% | -0.013% | -0.623% | -0.724% | -34.09 € |
| ruptura_volumen_evento | 898.56 € (-2.78%) | 152 | 2 | 24% | -0.058% | -0.731% | -0.829% | -25.41 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 07:45 | macd_sin_salida | TAO | timeout | -0.81% | -1.31% | -0.30 |
| 2026-10-01 07:45 | estocastico_rebote | NEAR | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 07:40 | c_banda_atr_evento | ONDO | timeout | -0.77% | -1.27% | -0.29 |
| 2026-10-01 07:40 | c_banda_atr_regimen | ONDO | timeout | -0.77% | -1.27% | -0.29 |
| 2026-10-01 07:40 | c_banda_atr_tope | ONDO | timeout | -0.77% | -1.87% | -0.43 |
| 2026-10-01 07:40 | estocastico_rebote | TRUMP | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 07:40 | reversion_bb | TRUMP | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-10-01 07:40 | c_banda_atr | ONDO | timeout | -0.77% | -1.27% | -0.29 |
| 2026-10-01 07:35 | macd_momentum_evento | XMR | momentum perdido | -0.85% | -1.35% | -0.30 |
| 2026-10-01 07:35 | macd_momentum_evento | DOT | momentum perdido | -0.77% | -1.27% | -0.29 |
| 2026-10-01 07:35 | macd_momentum_regimen | XMR | momentum perdido | -0.85% | -1.35% | -0.30 |
| 2026-10-01 07:35 | macd_momentum_regimen | DOT | momentum perdido | -0.77% | -1.27% | -0.29 |
| 2026-10-01 07:35 | macd_momentum | XMR | momentum perdido | -0.85% | -1.35% | -0.30 |
| 2026-10-01 07:35 | macd_momentum | DOT | momentum perdido | -0.77% | -1.27% | -0.28 |
| 2026-10-01 07:35 | pullback_tendencia | XDC | rotura de tendencia | -1.14% | -1.64% | -0.37 |

## Eventos de la última vuelta

- 2026-10-01 07:45 [estocastico_rebote] CIERRE NEAR stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:40 [estocastico_rebote] ENTRADA TAO @ 270.826 (22.31 €, apertura)
- 2026-10-01 07:45 [macd_sin_salida] CIERRE TAO timeout bruto -0.81% neto -1.31%
- 2026-10-01 07:40 [estocastico_rebote] ENTRADA ARB @ 0.1761 (22.31 €, apertura)
- 2026-10-01 07:40 [estocastico_rebote] ENTRADA ONDO @ 0.44502 (22.31 €, apertura)
- 2026-10-01 07:40 [estocastico_rebote] ENTRADA USELESS @ 0.20906 (22.31 €, apertura)
- 2026-10-01 07:40 [estocastico_rebote] ENTRADA PEPE @ 3.803e-06 (22.31 €, apertura)
- 2026-10-01 07:40 [estocastico_rebote] ENTRADA RENDER @ 1.683 (22.31 €, apertura)
- 2026-10-01 07:40 [estocastico_rebote] ENTRADA APT @ 0.6839 (22.31 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
