# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 12:41 UTC · vueltas 401 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 888.87 € (-3.83%) | 370 | 22 | 41% | +0.143% | -0.427% | -0.548% | -35.99 € |
| reversion_bb | 920.12 € (-0.45%) | 73 | 3 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 855.64 € (-7.42%) | 462 | 16 | 26% | -0.115% | -0.671% | -0.780% | -69.20 € |
| rebote_extremo | 922.62 € (-0.17%) | 16 | 0 | 62% | +0.663% | -0.437% | -0.608% | -1.62 € |
| pullback_tendencia | 888.22 € (-3.90%) | 267 | 11 | 21% | -0.004% | -0.603% | -0.689% | -36.56 € |
| macd_momentum | 847.74 € (-8.28%) | 748 | 27 | 24% | +0.066% | -0.469% | -0.569% | -77.74 € |
| estocastico_rebote | 879.61 € (-4.83%) | 453 | 32 | 38% | +0.111% | -0.447% | -0.554% | -45.85 € |
| ruptura_estricta | 881.15 € (-4.66%) | 251 | 11 | 32% | -0.145% | -0.750% | -0.865% | -42.80 € |
| macd_sin_salida | 878.03 € (-5.00%) | 489 | 32 | 40% | +0.126% | -0.427% | -0.537% | -47.49 € |
| c_banda_atr_tope | 913.62 € (-1.15%) | 84 | 5 | 38% | +0.258% | -0.556% | -0.676% | -10.75 € |
| ruptura_volumen_tope | 898.76 € (-2.76%) | 140 | 5 | 23% | -0.110% | -0.799% | -0.913% | -25.51 € |
| c_banda_atr_regimen | 901.40 € (-2.47%) | 222 | 22 | 42% | +0.160% | -0.457% | -0.586% | -23.33 € |
| macd_momentum_regimen | 870.43 € (-5.82%) | 511 | 27 | 24% | +0.071% | -0.480% | -0.580% | -55.06 € |
| ruptura_volumen_regimen | 860.28 € (-6.92%) | 385 | 16 | 23% | -0.182% | -0.749% | -0.862% | -64.56 € |
| c_banda_atr_evento | 894.26 € (-3.24%) | 335 | 8 | 41% | +0.188% | -0.390% | -0.505% | -29.89 € |
| macd_momentum_evento | 851.76 € (-7.84%) | 698 | 2 | 23% | +0.069% | -0.469% | -0.565% | -72.74 € |
| ruptura_volumen_evento | 867.27 € (-6.16%) | 410 | 4 | 26% | -0.056% | -0.621% | -0.723% | -57.09 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 12:40 | ruptura_volumen_regimen | ZRO | stop-loss | -1.20% | -1.70% | -0.36 |
| 2026-10-02 12:40 | macd_sin_salida | XDC | timeout | +0.87% | +0.37% | +0.08 |
| 2026-10-02 12:40 | ruptura_volumen | ZRO | stop-loss | -1.20% | -1.70% | -0.36 |
| 2026-10-02 12:35 | ruptura_volumen_regimen | NIGHT | take-profit | +2.50% | +2.00% | +0.43 |
| 2026-10-02 12:35 | ruptura_volumen_tope | NIGHT | take-profit | +2.50% | +2.00% | +0.45 |
| 2026-10-02 12:35 | macd_sin_salida | ENA | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 12:35 | ruptura_estricta | WLD | timeout | +2.97% | +2.47% | +0.55 |
| 2026-10-02 12:35 | ruptura_estricta | XLM | timeout | +0.18% | -0.32% | -0.07 |
| 2026-10-02 12:35 | estocastico_rebote | PUMP | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-10-02 12:35 | estocastico_rebote | ADA | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-10-02 12:35 | estocastico_rebote | BTC | timeout | +0.58% | +0.08% | +0.02 |
| 2026-10-02 12:35 | pullback_tendencia | ADA | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 12:35 | rebote_extremo | PEPE | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-10-02 12:35 | ruptura_volumen | NIGHT | take-profit | +2.50% | +2.00% | +0.43 |
| 2026-10-02 12:30 | ruptura_volumen_evento | DASH | timeout | -0.06% | -0.56% | -0.12 |

## Eventos de la última vuelta

- 2026-10-02 12:35 [pullback_tendencia] ENTRADA XRP @ 1.37376 (22.19 €, apertura)
- 2026-10-02 12:35 [macd_momentum] ENTRADA ETH @ 2447.54 (21.16 €, apertura)
- 2026-10-02 12:35 [macd_momentum_regimen] ENTRADA ETH @ 2447.54 (21.73 €, apertura)
- 2026-10-02 12:35 [macd_momentum] ENTRADA SOL @ 108.73 (21.16 €, apertura)
- 2026-10-02 12:35 [macd_sin_salida] ENTRADA SOL @ 108.73 (21.92 €, apertura)
- 2026-10-02 12:35 [macd_momentum_regimen] ENTRADA SOL @ 108.73 (21.73 €, apertura)
- 2026-10-02 12:35 [ruptura_volumen] ENTRADA ADA @ 0.228797 (21.39 €, apertura)
- 2026-10-02 12:35 [ruptura_volumen_regimen] ENTRADA ADA @ 0.228797 (21.50 €, apertura)
- 2026-10-02 12:35 [ruptura_volumen] ENTRADA SUI @ 1.0566 (21.39 €, apertura)
- 2026-10-02 12:35 [ruptura_volumen_regimen] ENTRADA SUI @ 1.0566 (21.50 €, apertura)
- 2026-10-02 12:35 [macd_momentum] ENTRADA PUMP @ 0.005222 (21.16 €, apertura)
- 2026-10-02 12:35 [macd_sin_salida] ENTRADA PUMP @ 0.005222 (21.92 €, apertura)
- 2026-10-02 12:35 [macd_momentum_regimen] ENTRADA PUMP @ 0.005222 (21.73 €, apertura)
- 2026-10-02 12:35 [pullback_tendencia] ENTRADA XLM @ 0.200584 (22.19 €, apertura)
- 2026-10-02 12:35 [macd_momentum] ENTRADA TAO @ 276.756 (21.16 €, apertura)
- 2026-10-02 12:35 [macd_momentum_regimen] ENTRADA TAO @ 276.756 (21.73 €, apertura)
- 2026-10-02 12:40 [ruptura_volumen] CIERRE ZRO stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 12:40 [ruptura_volumen_regimen] CIERRE ZRO stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 12:35 [ruptura_volumen] ENTRADA ARB @ 0.1826 (21.38 €, apertura)
- 2026-10-02 12:35 [ruptura_volumen_regimen] ENTRADA ARB @ 0.1826 (21.49 €, apertura)
- 2026-10-02 12:35 [c_banda_atr] ENTRADA ENA @ 0.2201 (22.21 €, apertura)
- 2026-10-02 12:35 [c_banda_atr_regimen] ENTRADA ENA @ 0.2201 (22.52 €, apertura)
- 2026-10-02 12:40 [macd_sin_salida] CIERRE XDC timeout bruto +0.87% neto +0.37%
- 2026-10-02 12:35 [c_banda_atr] ENTRADA INJ @ 6.676 (22.21 €, apertura)
- 2026-10-02 12:35 [macd_momentum] ENTRADA INJ @ 6.676 (21.16 €, apertura)
- 2026-10-02 12:35 [macd_sin_salida] ENTRADA INJ @ 6.676 (21.92 €, apertura)
- 2026-10-02 12:35 [c_banda_atr_regimen] ENTRADA INJ @ 6.676 (22.52 €, apertura)
- 2026-10-02 12:35 [macd_momentum_regimen] ENTRADA INJ @ 6.676 (21.73 €, apertura)
- 2026-10-02 12:35 [ruptura_volumen] ENTRADA OP @ 0.1184 (21.38 €, apertura)
- 2026-10-02 12:35 [ruptura_volumen_regimen] ENTRADA OP @ 0.1184 (21.49 €, apertura)
- 2026-10-02 12:35 [c_banda_atr] ENTRADA VVV @ 26.5 (22.21 €, apertura)
- 2026-10-02 12:35 [c_banda_atr_regimen] ENTRADA VVV @ 26.5 (22.52 €, apertura)
- 2026-10-02 12:35 [ruptura_volumen] ENTRADA DASH @ 53.484 (21.38 €, apertura)
- 2026-10-02 12:35 [ruptura_estricta] ENTRADA DASH @ 53.484 (22.04 €, apertura)
- 2026-10-02 12:35 [ruptura_volumen_regimen] ENTRADA DASH @ 53.484 (21.49 €, apertura)
- 2026-10-02 12:35 [macd_momentum] ENTRADA TON @ 1.371 (21.16 €, apertura)
- 2026-10-02 12:35 [macd_sin_salida] ENTRADA TON @ 1.371 (21.92 €, apertura)
- 2026-10-02 12:35 [macd_momentum_regimen] ENTRADA TON @ 1.371 (21.73 €, apertura)
- 2026-10-02 12:35 [macd_momentum] ENTRADA KAS @ 0.03831 (21.16 €, apertura)
- 2026-10-02 12:35 [macd_momentum_regimen] ENTRADA KAS @ 0.03831 (21.73 €, apertura)
- 2026-10-02 12:35 [pullback_tendencia] ENTRADA SEI @ 0.06413 (22.19 €, apertura)
- 2026-10-02 12:35 [macd_momentum] ENTRADA SPX @ 0.4006 (21.16 €, apertura)
- 2026-10-02 12:35 [macd_sin_salida] ENTRADA SPX @ 0.4006 (21.92 €, apertura)
- 2026-10-02 12:35 [macd_momentum_regimen] ENTRADA SPX @ 0.4006 (21.73 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
