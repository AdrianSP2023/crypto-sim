# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 12:36 UTC · vueltas 400 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 888.80 € (-3.83%) | 370 | 19 | 41% | +0.143% | -0.427% | -0.548% | -35.99 € |
| reversion_bb | 920.15 € (-0.44%) | 73 | 3 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 855.66 € (-7.42%) | 461 | 12 | 26% | -0.113% | -0.669% | -0.777% | -68.83 € |
| rebote_extremo | 922.62 € (-0.17%) | 16 | 0 | 62% | +0.663% | -0.437% | -0.608% | -1.62 € |
| pullback_tendencia | 888.33 € (-3.89%) | 267 | 8 | 21% | -0.004% | -0.603% | -0.689% | -36.56 € |
| macd_momentum | 847.27 € (-8.33%) | 748 | 19 | 24% | +0.066% | -0.469% | -0.569% | -77.74 € |
| estocastico_rebote | 879.55 € (-4.84%) | 453 | 32 | 38% | +0.111% | -0.447% | -0.554% | -45.85 € |
| ruptura_estricta | 881.38 € (-4.64%) | 251 | 10 | 32% | -0.145% | -0.750% | -0.865% | -42.80 € |
| macd_sin_salida | 877.73 € (-5.03%) | 488 | 28 | 40% | +0.124% | -0.429% | -0.539% | -47.57 € |
| c_banda_atr_tope | 913.55 € (-1.16%) | 84 | 5 | 38% | +0.258% | -0.556% | -0.676% | -10.75 € |
| ruptura_volumen_tope | 898.76 € (-2.76%) | 140 | 5 | 23% | -0.110% | -0.799% | -0.913% | -25.51 € |
| c_banda_atr_regimen | 901.33 € (-2.48%) | 222 | 19 | 42% | +0.160% | -0.457% | -0.586% | -23.33 € |
| macd_momentum_regimen | 869.95 € (-5.87%) | 511 | 19 | 24% | +0.071% | -0.480% | -0.580% | -55.06 € |
| ruptura_volumen_regimen | 860.30 € (-6.92%) | 384 | 12 | 23% | -0.179% | -0.747% | -0.859% | -64.20 € |
| c_banda_atr_evento | 894.40 € (-3.23%) | 335 | 8 | 41% | +0.188% | -0.390% | -0.505% | -29.89 € |
| macd_momentum_evento | 851.62 € (-7.86%) | 698 | 2 | 23% | +0.069% | -0.469% | -0.565% | -72.74 € |
| ruptura_volumen_evento | 867.15 € (-6.18%) | 410 | 4 | 26% | -0.056% | -0.621% | -0.723% | -57.09 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
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
| 2026-10-02 12:30 | ruptura_volumen_evento | HYPE | timeout | -0.20% | -0.70% | -0.15 |
| 2026-10-02 12:30 | macd_momentum_evento | DOT | momentum perdido | -0.42% | -0.92% | -0.20 |
| 2026-10-02 12:30 | ruptura_volumen_regimen | DASH | timeout | -0.06% | -0.56% | -0.12 |

## Eventos de la última vuelta

- 2026-10-02 12:35 [estocastico_rebote] CIERRE BTC timeout bruto +0.58% neto +0.08%
- 2026-10-02 12:35 [pullback_tendencia] CIERRE ADA take-profit bruto +2.00% neto +1.50%
- 2026-10-02 12:35 [estocastico_rebote] CIERRE ADA take-profit bruto +1.80% neto +1.30%
- 2026-10-02 12:30 [macd_momentum] ENTRADA AVAX @ 9.965 (21.16 €, apertura)
- 2026-10-02 12:30 [macd_sin_salida] ENTRADA AVAX @ 9.965 (21.91 €, apertura)
- 2026-10-02 12:30 [macd_momentum_regimen] ENTRADA AVAX @ 9.965 (21.73 €, apertura)
- 2026-10-02 12:30 [macd_momentum] ENTRADA ZEC @ 1235.15 (21.16 €, apertura)
- 2026-10-02 12:30 [macd_sin_salida] ENTRADA ZEC @ 1235.15 (21.91 €, apertura)
- 2026-10-02 12:30 [macd_momentum_regimen] ENTRADA ZEC @ 1235.15 (21.73 €, apertura)
- 2026-10-02 12:35 [estocastico_rebote] CIERRE PUMP take-profit bruto +1.80% neto +1.30%
- 2026-10-02 12:35 [ruptura_estricta] CIERRE XLM timeout bruto +0.18% neto -0.32%
- 2026-10-02 12:30 [ruptura_volumen] ENTRADA ZRO @ 1.66 (21.37 €, apertura)
- 2026-10-02 12:30 [ruptura_volumen_regimen] ENTRADA ZRO @ 1.66 (21.49 €, apertura)
- 2026-10-02 12:30 [ruptura_volumen] ENTRADA DOGE @ 0.0862301 (21.37 €, apertura)
- 2026-10-02 12:30 [macd_momentum] ENTRADA DOGE @ 0.0862301 (21.16 €, apertura)
- 2026-10-02 12:30 [macd_sin_salida] ENTRADA DOGE @ 0.0862301 (21.91 €, apertura)
- 2026-10-02 12:30 [macd_momentum_regimen] ENTRADA DOGE @ 0.0862301 (21.73 €, apertura)
- 2026-10-02 12:30 [ruptura_volumen_regimen] ENTRADA DOGE @ 0.0862301 (21.49 €, apertura)
- 2026-10-02 12:35 [macd_sin_salida] CIERRE ENA take-profit bruto +2.00% neto +1.50%
- 2026-10-02 12:35 [ruptura_estricta] CIERRE WLD timeout bruto +2.97% neto +2.47%
- 2026-10-02 12:35 [ruptura_volumen] CIERRE NIGHT take-profit bruto +2.50% neto +2.00%
- 2026-10-02 12:35 [ruptura_volumen_tope] CIERRE NIGHT take-profit bruto +2.50% neto +2.00%
- 2026-10-02 12:35 [ruptura_volumen_regimen] CIERRE NIGHT take-profit bruto +2.50% neto +2.00%
- 2026-10-02 12:35 [rebote_extremo] CIERRE PEPE take-profit bruto +2.00% neto +0.90%
- 2026-10-02 12:30 [ruptura_volumen] ENTRADA MON @ 0.03067 (21.39 €, apertura)
- 2026-10-02 12:30 [macd_momentum] ENTRADA MON @ 0.03067 (21.16 €, apertura)
- 2026-10-02 12:30 [ruptura_estricta] ENTRADA MON @ 0.03067 (22.04 €, apertura)
- 2026-10-02 12:30 [ruptura_volumen_tope] ENTRADA MON @ 0.03067 (22.47 €, apertura)
- 2026-10-02 12:30 [macd_momentum_regimen] ENTRADA MON @ 0.03067 (21.73 €, apertura)
- 2026-10-02 12:30 [ruptura_volumen_regimen] ENTRADA MON @ 0.03067 (21.50 €, apertura)
- 2026-10-02 12:30 [c_banda_atr] ENTRADA SPX @ 0.3989 (22.21 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
