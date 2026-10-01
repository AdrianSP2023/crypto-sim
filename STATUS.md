# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 08:11 UTC · vueltas 168 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 898.81 € (-2.75%) | 160 | 8 | 36% | -0.002% | -0.665% | -0.791% | -24.41 € |
| reversion_bb | 918.85 € (-0.58%) | 20 | 9 | 40% | +0.134% | -0.966% | -1.078% | -4.46 € |
| ruptura_volumen | 885.55 € (-4.19%) | 204 | 2 | 23% | -0.203% | -0.831% | -0.940% | -38.53 € |
| rebote_extremo | 924.16 € (-0.01%) | 3 | 3 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 898.23 € (-2.81%) | 119 | 1 | 16% | -0.244% | -0.965% | -1.071% | -26.23 € |
| macd_momentum | 885.12 € (-4.23%) | 289 | 2 | 22% | -0.006% | -0.597% | -0.705% | -39.11 € |
| estocastico_rebote | 885.46 € (-4.20%) | 208 | 37 | 34% | -0.105% | -0.730% | -0.848% | -34.67 € |
| ruptura_estricta | 891.62 € (-3.53%) | 117 | 5 | 26% | -0.454% | -1.180% | -1.307% | -31.62 € |
| macd_sin_salida | 889.38 € (-3.77%) | 209 | 8 | 37% | -0.082% | -0.707% | -0.819% | -33.75 € |
| c_banda_atr_tope | 915.02 € (-1.00%) | 35 | 2 | 26% | -0.052% | -1.152% | -1.273% | -9.28 € |
| ruptura_volumen_tope | 912.49 € (-1.27%) | 57 | 2 | 28% | +0.080% | -0.884% | -0.999% | -11.58 € |
| c_banda_atr_regimen | 903.05 € (-2.29%) | 105 | 4 | 35% | -0.100% | -0.848% | -0.992% | -20.47 € |
| macd_momentum_regimen | 894.12 € (-3.26%) | 203 | 0 | 22% | -0.022% | -0.651% | -0.763% | -30.12 € |
| ruptura_volumen_regimen | 886.57 € (-4.08%) | 177 | 0 | 20% | -0.288% | -0.936% | -1.049% | -37.67 € |
| c_banda_atr_evento | 904.80 € (-2.10%) | 127 | 8 | 38% | +0.078% | -0.630% | -0.747% | -18.41 € |
| macd_momentum_evento | 890.03 € (-3.70%) | 242 | 2 | 19% | -0.013% | -0.622% | -0.725% | -34.20 € |
| ruptura_volumen_evento | 898.15 € (-2.82%) | 154 | 2 | 24% | -0.065% | -0.736% | -0.833% | -25.91 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 08:10 | c_banda_atr_evento | SKY | stop-loss | -1.53% | -2.03% | -0.46 |
| 2026-10-01 08:10 | c_banda_atr_regimen | SKY | stop-loss | -1.53% | -2.03% | -0.46 |
| 2026-10-01 08:10 | macd_sin_salida | ALGO | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 08:10 | macd_sin_salida | DOT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 08:10 | ruptura_estricta | INJ | timeout | -1.12% | -1.62% | -0.36 |
| 2026-10-01 08:10 | ruptura_estricta | FET | stop-loss | -2.00% | -2.50% | -0.56 |
| 2026-10-01 08:10 | estocastico_rebote | KSM | stop-loss | -1.51% | -2.01% | -0.45 |
| 2026-10-01 08:10 | estocastico_rebote | DOT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 08:10 | c_banda_atr | SKY | stop-loss | -1.53% | -2.03% | -0.46 |
| 2026-10-01 08:05 | ruptura_estricta | KSM | timeout | -1.07% | -1.57% | -0.35 |
| 2026-10-01 08:00 | macd_momentum_evento | WLFI | momentum perdido | +0.00% | -0.50% | -0.11 |
| 2026-10-01 08:00 | c_banda_atr_evento | POL | timeout | -0.96% | -1.46% | -0.33 |
| 2026-10-01 08:00 | macd_momentum_regimen | WLFI | momentum perdido | +0.00% | -0.50% | -0.11 |
| 2026-10-01 08:00 | c_banda_atr_regimen | POL | timeout | -0.96% | -1.46% | -0.33 |
| 2026-10-01 08:00 | estocastico_rebote | SEI | stop-loss | -1.55% | -2.05% | -0.46 |

## Eventos de la última vuelta

- 2026-10-01 08:05 [estocastico_rebote] ENTRADA NEAR @ 4.6918 (22.26 €, apertura)
- 2026-10-01 08:10 [estocastico_rebote] CIERRE DOT stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 08:10 [macd_sin_salida] CIERRE DOT stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 08:05 [estocastico_rebote] ENTRADA ENA @ 0.2324 (22.25 €, apertura)
- 2026-10-01 08:10 [ruptura_estricta] CIERRE FET stop-loss bruto -2.00% neto -2.50%
- 2026-10-01 08:05 [ruptura_volumen] ENTRADA TRX @ 0.298542 (22.14 €, apertura)
- 2026-10-01 08:05 [ruptura_volumen_tope] ENTRADA TRX @ 0.298542 (22.82 €, apertura)
- 2026-10-01 08:05 [ruptura_volumen_evento] ENTRADA TRX @ 0.298542 (22.46 €, apertura)
- 2026-10-01 08:10 [macd_sin_salida] CIERRE ALGO stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 08:05 [ruptura_volumen] ENTRADA NIGHT @ 0.03736 (22.14 €, apertura)
- 2026-10-01 08:05 [macd_momentum] ENTRADA NIGHT @ 0.03736 (22.13 €, apertura)
- 2026-10-01 08:05 [macd_sin_salida] ENTRADA NIGHT @ 0.03736 (22.26 €, apertura)
- 2026-10-01 08:05 [ruptura_volumen_tope] ENTRADA NIGHT @ 0.03736 (22.82 €, apertura)
- 2026-10-01 08:05 [macd_momentum_evento] ENTRADA NIGHT @ 0.03736 (22.25 €, apertura)
- 2026-10-01 08:05 [ruptura_volumen_evento] ENTRADA NIGHT @ 0.03736 (22.46 €, apertura)
- 2026-10-01 08:05 [estocastico_rebote] ENTRADA MON @ 0.02865 (22.25 €, apertura)
- 2026-10-01 08:10 [ruptura_estricta] CIERRE INJ timeout bruto -1.12% neto -1.62%
- 2026-10-01 08:10 [estocastico_rebote] CIERRE KSM stop-loss bruto -1.51% neto -2.01%
- 2026-10-01 08:10 [c_banda_atr] CIERRE SKY stop-loss bruto -1.53% neto -2.03%
- 2026-10-01 08:10 [c_banda_atr_regimen] CIERRE SKY stop-loss bruto -1.53% neto -2.03%
- 2026-10-01 08:10 [c_banda_atr_evento] CIERRE SKY stop-loss bruto -1.53% neto -2.03%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
