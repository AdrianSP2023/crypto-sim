# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 07:41 UTC · vueltas 162 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 899.55 € (-2.67%) | 158 | 9 | 37% | +0.014% | -0.652% | -0.775% | -23.62 € |
| reversion_bb | 919.87 € (-0.47%) | 20 | 9 | 40% | +0.134% | -0.966% | -1.078% | -4.46 € |
| ruptura_volumen | 885.94 € (-4.14%) | 202 | 2 | 23% | -0.199% | -0.828% | -0.938% | -38.03 € |
| rebote_extremo | 924.12 € (-0.01%) | 3 | 2 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 897.95 € (-2.84%) | 119 | 1 | 16% | -0.244% | -0.965% | -1.071% | -26.23 € |
| macd_momentum | 885.25 € (-4.22%) | 288 | 1 | 22% | -0.006% | -0.597% | -0.704% | -39.00 € |
| estocastico_rebote | 890.17 € (-3.69%) | 200 | 32 | 35% | -0.057% | -0.688% | -0.805% | -31.45 € |
| ruptura_estricta | 892.73 € (-3.41%) | 111 | 11 | 28% | -0.431% | -1.169% | -1.296% | -29.75 € |
| macd_sin_salida | 890.68 € (-3.63%) | 204 | 11 | 38% | -0.057% | -0.685% | -0.798% | -31.95 € |
| c_banda_atr_tope | 914.88 € (-1.01%) | 35 | 1 | 26% | -0.052% | -1.152% | -1.273% | -9.28 € |
| ruptura_volumen_tope | 912.77 € (-1.24%) | 56 | 1 | 29% | +0.088% | -0.884% | -0.999% | -11.38 € |
| c_banda_atr_regimen | 903.78 € (-2.21%) | 103 | 6 | 36% | -0.077% | -0.831% | -0.972% | -19.68 € |
| macd_momentum_regimen | 894.23 € (-3.25%) | 202 | 1 | 22% | -0.022% | -0.652% | -0.763% | -30.01 € |
| ruptura_volumen_regimen | 886.80 € (-4.05%) | 175 | 2 | 21% | -0.284% | -0.934% | -1.047% | -37.18 € |
| c_banda_atr_evento | 905.53 € (-2.02%) | 125 | 9 | 38% | +0.099% | -0.612% | -0.727% | -17.62 € |
| macd_momentum_evento | 890.16 € (-3.69%) | 241 | 1 | 19% | -0.013% | -0.623% | -0.724% | -34.09 € |
| ruptura_volumen_evento | 898.55 € (-2.78%) | 152 | 2 | 24% | -0.058% | -0.731% | -0.829% | -25.41 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
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
| 2026-10-01 07:35 | pullback_tendencia | QNT | rotura de tendencia | -0.09% | -0.59% | -0.13 |
| 2026-10-01 07:30 | ruptura_volumen_evento | SPX | stop-loss | -2.50% | -3.00% | -0.68 |

## Eventos de la última vuelta

- 2026-10-01 07:35 [estocastico_rebote] ENTRADA XRP @ 1.31929 (22.33 €, apertura)
- 2026-10-01 07:35 [estocastico_rebote] ENTRADA ETH @ 2381.04 (22.33 €, apertura)
- 2026-10-01 07:35 [estocastico_rebote] ENTRADA SOL @ 104.41 (22.33 €, apertura)
- 2026-10-01 07:35 [estocastico_rebote] ENTRADA NEAR @ 4.771 (22.33 €, apertura)
- 2026-10-01 07:35 [estocastico_rebote] ENTRADA LINK @ 12.6621 (22.33 €, apertura)
- 2026-10-01 07:35 [estocastico_rebote] ENTRADA ADA @ 0.220994 (22.33 €, apertura)
- 2026-10-01 07:35 [estocastico_rebote] ENTRADA SUI @ 1.018 (22.33 €, apertura)
- 2026-10-01 07:35 [estocastico_rebote] ENTRADA AAVE @ 146.32 (22.33 €, apertura)
- 2026-10-01 07:35 [estocastico_rebote] ENTRADA ZEC @ 1252.32 (22.33 €, apertura)
- 2026-10-01 07:35 [estocastico_rebote] ENTRADA PUMP @ 0.005127 (22.33 €, apertura)
- 2026-10-01 07:35 [estocastico_rebote] ENTRADA UNI @ 7.8175 (22.33 €, apertura)
- 2026-10-01 07:35 [estocastico_rebote] ENTRADA DOGE @ 0.0836183 (22.33 €, apertura)
- 2026-10-01 07:40 [c_banda_atr] CIERRE ONDO timeout bruto -0.77% neto -1.27%
- 2026-10-01 07:40 [c_banda_atr_tope] CIERRE ONDO timeout bruto -0.77% neto -1.87%
- 2026-10-01 07:40 [c_banda_atr_regimen] CIERRE ONDO timeout bruto -0.77% neto -1.27%
- 2026-10-01 07:40 [c_banda_atr_evento] CIERRE ONDO timeout bruto -0.77% neto -1.27%
- 2026-10-01 07:35 [estocastico_rebote] ENTRADA BCH @ 271.26 (22.33 €, apertura)
- 2026-10-01 07:35 [estocastico_rebote] ENTRADA INJ @ 6.651 (22.33 €, apertura)
- 2026-10-01 07:35 [estocastico_rebote] ENTRADA OP @ 0.1144 (22.33 €, apertura)
- 2026-10-01 07:35 [estocastico_rebote] ENTRADA MINA @ 0.1291 (22.33 €, apertura)
- 2026-10-01 07:35 [estocastico_rebote] ENTRADA PENGU @ 0.008583 (22.33 €, apertura)
- 2026-10-01 07:40 [reversion_bb] CIERRE TRUMP stop-loss bruto -1.50% neto -2.60%
- 2026-10-01 07:40 [estocastico_rebote] CIERRE TRUMP stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:35 [estocastico_rebote] ENTRADA TON @ 1.327 (22.32 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
