# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 14:46 UTC · vueltas 30 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 913.43 € (-1.17%) | 30 | 4 | 33% | -0.317% | -1.417% | -1.579% | -9.83 € |
| reversion_bb | 923.51 € (-0.08%) | 2 | 2 | 50% | +0.000% | -1.100% | -1.219% | -0.51 € |
| ruptura_volumen | 905.25 € (-2.06%) | 50 | 0 | 16% | -0.627% | -1.649% | -1.799% | -18.99 € |
| rebote_extremo | 924.11 € (-0.01%) | 0 | 2 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 913.65 € (-1.15%) | 30 | 0 | 20% | -0.432% | -1.532% | -1.666% | -10.60 € |
| macd_momentum | 912.50 € (-1.27%) | 48 | 1 | 29% | -0.003% | -1.047% | -1.184% | -11.61 € |
| estocastico_rebote | 913.78 € (-1.13%) | 27 | 35 | 30% | -0.509% | -1.609% | -1.781% | -10.02 € |
| ruptura_estricta | 903.79 € (-2.21%) | 32 | 7 | 12% | -1.372% | -2.472% | -2.634% | -18.27 € |
| macd_sin_salida | 909.59 € (-1.58%) | 41 | 7 | 34% | -0.309% | -1.395% | -1.539% | -13.21 € |
| c_banda_atr_tope | 922.67 € (-0.17%) | 8 | 0 | 50% | +0.252% | -0.849% | -1.012% | -1.57 € |
| ruptura_volumen_tope | 921.18 € (-0.33%) | 9 | 0 | 22% | -0.373% | -1.473% | -1.564% | -3.06 € |
| c_banda_atr_regimen | 913.43 € (-1.17%) | 30 | 4 | 33% | -0.317% | -1.417% | -1.579% | -9.83 € |
| macd_momentum_regimen | 912.50 € (-1.27%) | 48 | 1 | 29% | -0.003% | -1.047% | -1.184% | -11.61 € |
| ruptura_volumen_regimen | 905.25 € (-2.06%) | 50 | 0 | 16% | -0.627% | -1.649% | -1.799% | -18.99 € |
| c_banda_atr_evento | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| macd_momentum_evento | 923.51 € (-0.08%) | 1 | 1 | 0% | -1.500% | -2.600% | -2.685% | -0.60 € |
| ruptura_volumen_evento | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 14:45 | estocastico_rebote | ZRO | stop-loss | -1.50% | -2.60% | -0.59 |
| 2026-09-30 14:40 | ruptura_volumen_regimen | MON | stop-loss | -1.20% | -2.00% | -0.46 |
| 2026-09-30 14:40 | ruptura_volumen | MON | stop-loss | -1.20% | -2.00% | -0.46 |
| 2026-09-30 14:35 | ruptura_volumen_regimen | XMR | stop-loss | -1.20% | -2.00% | -0.46 |
| 2026-09-30 14:35 | ruptura_volumen_regimen | TRUMP | stop-loss | -1.20% | -2.00% | -0.46 |
| 2026-09-30 14:35 | ruptura_volumen_regimen | BTC | timeout | -1.03% | -1.83% | -0.42 |
| 2026-09-30 14:35 | ruptura_volumen_tope | BTC | timeout | -1.03% | -2.13% | -0.49 |
| 2026-09-30 14:35 | macd_sin_salida | TRUMP | stop-loss | -1.50% | -2.30% | -0.53 |
| 2026-09-30 14:35 | ruptura_estricta | LTC | stop-loss | -2.00% | -3.10% | -0.72 |
| 2026-09-30 14:35 | ruptura_estricta | SOL | stop-loss | -2.00% | -3.10% | -0.72 |
| 2026-09-30 14:35 | estocastico_rebote | MINA | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-30 14:35 | estocastico_rebote | LTC | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-30 14:35 | pullback_tendencia | TRX | rotura de tendencia | -0.19% | -1.29% | -0.30 |
| 2026-09-30 14:35 | ruptura_volumen | XMR | stop-loss | -1.20% | -2.00% | -0.46 |
| 2026-09-30 14:35 | ruptura_volumen | TRUMP | stop-loss | -1.20% | -2.00% | -0.46 |

## Eventos de la última vuelta

- 2026-09-30 14:40 [estocastico_rebote] ENTRADA BTC @ 73613.9 (22.87 €, apertura)
- 2026-09-30 14:40 [estocastico_rebote] ENTRADA SOL @ 104.65 (22.87 €, apertura)
- 2026-09-30 14:40 [estocastico_rebote] ENTRADA QNT @ 256.2 (22.87 €, apertura)
- 2026-09-30 14:40 [estocastico_rebote] ENTRADA SUI @ 1.0151 (22.87 €, apertura)
- 2026-09-30 14:40 [estocastico_rebote] ENTRADA XLM @ 0.19518 (22.87 €, apertura)
- 2026-09-30 14:40 [estocastico_rebote] ENTRADA UNI @ 7.7523 (22.87 €, apertura)
- 2026-09-30 14:40 [estocastico_rebote] ENTRADA LTC @ 58.62 (22.87 €, apertura)
- 2026-09-30 14:40 [estocastico_rebote] ENTRADA ZRO @ 1.513 (22.87 €, apertura)
- 2026-09-30 14:45 [estocastico_rebote] CIERRE ZRO stop-loss bruto -1.50% neto -2.60%
- 2026-09-30 14:40 [estocastico_rebote] ENTRADA ARB @ 0.1783 (22.86 €, apertura)
- 2026-09-30 14:40 [estocastico_rebote] ENTRADA ICP @ 2.973 (22.86 €, apertura)
- 2026-09-30 14:40 [estocastico_rebote] ENTRADA FET @ 0.1935 (22.86 €, apertura)
- 2026-09-30 14:40 [estocastico_rebote] ENTRADA USELESS @ 0.21283 (22.86 €, apertura)
- 2026-09-30 14:40 [estocastico_rebote] ENTRADA RENDER @ 1.688 (22.86 €, apertura)
- 2026-09-30 14:40 [estocastico_rebote] ENTRADA MINA @ 0.1274 (22.86 €, apertura)
- 2026-09-30 14:40 [estocastico_rebote] ENTRADA VVV @ 24.391 (22.86 €, apertura)
- 2026-09-30 14:40 [estocastico_rebote] ENTRADA SHIB @ 5.11e-06 (22.86 €, apertura)
- 2026-09-30 14:40 [estocastico_rebote] ENTRADA TON @ 1.306 (22.86 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
