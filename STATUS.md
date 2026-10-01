# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 01:01 UTC · vueltas 83 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 903.04 € (-2.29%) | 88 | 22 | 26% | -0.307% | -1.103% | -1.232% | -22.27 € |
| reversion_bb | 921.61 € (-0.29%) | 12 | 4 | 42% | +0.121% | -0.979% | -1.107% | -2.72 € |
| ruptura_volumen | 893.57 € (-3.32%) | 115 | 12 | 16% | -0.448% | -1.175% | -1.291% | -30.87 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 904.24 € (-2.16%) | 74 | 6 | 15% | -0.373% | -1.229% | -1.355% | -20.84 € |
| macd_momentum | 902.12 € (-2.39%) | 137 | 22 | 23% | -0.057% | -0.748% | -0.862% | -23.45 € |
| estocastico_rebote | 902.68 € (-2.33%) | 135 | 17 | 36% | -0.009% | -0.702% | -0.825% | -21.81 € |
| ruptura_estricta | 898.84 € (-2.75%) | 55 | 13 | 16% | -1.004% | -1.984% | -2.128% | -25.12 € |
| macd_sin_salida | 903.50 € (-2.24%) | 95 | 34 | 35% | -0.195% | -0.970% | -1.096% | -21.17 € |
| c_banda_atr_tope | 918.76 € (-0.59%) | 21 | 5 | 29% | -0.083% | -1.183% | -1.319% | -5.73 € |
| ruptura_volumen_tope | 915.34 € (-0.96%) | 33 | 4 | 18% | -0.115% | -1.215% | -1.296% | -9.23 € |
| c_banda_atr_regimen | 907.46 € (-1.82%) | 47 | 9 | 23% | -0.490% | -1.546% | -1.702% | -16.72 € |
| macd_momentum_regimen | 908.42 € (-1.71%) | 77 | 8 | 25% | -0.058% | -0.897% | -1.024% | -15.90 € |
| ruptura_volumen_regimen | 894.68 € (-3.20%) | 94 | 6 | 13% | -0.590% | -1.367% | -1.490% | -29.39 € |
| c_banda_atr_evento | 909.47 € (-1.60%) | 55 | 22 | 24% | -0.305% | -1.252% | -1.362% | -15.85 € |
| macd_momentum_evento | 907.12 € (-1.85%) | 90 | 22 | 17% | -0.102% | -0.895% | -0.997% | -18.46 € |
| ruptura_volumen_evento | 906.28 € (-1.94%) | 65 | 12 | 12% | -0.310% | -1.216% | -1.306% | -18.15 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 01:00 | macd_momentum_evento | ARB | momentum perdido | -0.06% | -0.56% | -0.13 |
| 2026-10-01 01:00 | macd_momentum_regimen | ARB | momentum perdido | -0.06% | -0.56% | -0.13 |
| 2026-10-01 01:00 | ruptura_volumen_tope | BCH | timeout | -0.03% | -1.13% | -0.26 |
| 2026-10-01 01:00 | macd_momentum | ARB | momentum perdido | -0.06% | -0.56% | -0.12 |
| 2026-10-01 00:55 | ruptura_volumen_evento | BCH | timeout | -0.06% | -0.56% | -0.13 |
| 2026-10-01 00:55 | macd_momentum_evento | LTC | momentum perdido | -0.18% | -0.69% | -0.15 |
| 2026-10-01 00:55 | c_banda_atr_evento | HYPE | stop-loss | -1.60% | -2.40% | -0.55 |
| 2026-10-01 00:55 | ruptura_volumen_regimen | BCH | timeout | -0.06% | -0.56% | -0.13 |
| 2026-10-01 00:55 | c_banda_atr_tope | HYPE | stop-loss | -1.60% | -2.70% | -0.62 |
| 2026-10-01 00:55 | macd_sin_salida | HYPE | stop-loss | -1.60% | -2.10% | -0.47 |
| 2026-10-01 00:55 | macd_momentum | LTC | momentum perdido | -0.18% | -0.69% | -0.15 |
| 2026-10-01 00:55 | ruptura_volumen | BCH | timeout | -0.06% | -0.56% | -0.13 |
| 2026-10-01 00:55 | c_banda_atr | HYPE | stop-loss | -1.60% | -2.10% | -0.47 |
| 2026-10-01 00:50 | ruptura_volumen_evento | SPX | timeout | -0.43% | -0.94% | -0.21 |
| 2026-10-01 00:50 | ruptura_volumen_evento | ONDO | timeout | +1.20% | +0.70% | +0.16 |

## Eventos de la última vuelta

- 2026-10-01 01:00 [macd_momentum] CIERRE ARB momentum perdido bruto -0.06% neto -0.56%
- 2026-10-01 01:00 [macd_momentum_regimen] CIERRE ARB momentum perdido bruto -0.06% neto -0.56%
- 2026-10-01 01:00 [macd_momentum_evento] CIERRE ARB momentum perdido bruto -0.06% neto -0.56%
- 2026-10-01 01:00 [ruptura_volumen_tope] CIERRE BCH timeout bruto -0.03% neto -1.13%
- 2026-10-01 00:55 [pullback_tendencia] ENTRADA MON @ 0.02834 (22.59 €, apertura)
- 2026-10-01 00:55 [macd_momentum] ENTRADA KSM @ 4.6 (22.52 €, apertura)
- 2026-10-01 00:55 [macd_momentum_regimen] ENTRADA KSM @ 4.6 (22.71 €, apertura)
- 2026-10-01 00:55 [macd_momentum_evento] ENTRADA KSM @ 4.6 (22.64 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
