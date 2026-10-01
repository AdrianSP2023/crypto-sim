# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 05:01 UTC · vueltas 131 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 906.71 € (-1.90%) | 123 | 26 | 35% | +0.033% | -0.679% | -0.797% | -19.21 € |
| reversion_bb | 921.95 € (-0.25%) | 15 | 4 | 40% | +0.277% | -0.823% | -0.935% | -2.85 € |
| ruptura_volumen | 892.46 € (-3.44%) | 153 | 33 | 21% | -0.277% | -0.948% | -1.058% | -33.09 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 902.82 € (-2.32%) | 90 | 7 | 17% | -0.270% | -1.063% | -1.180% | -21.90 € |
| macd_momentum | 895.72 € (-3.09%) | 221 | 28 | 22% | +0.014% | -0.604% | -0.712% | -30.44 € |
| estocastico_rebote | 902.36 € (-2.37%) | 158 | 21 | 38% | +0.056% | -0.609% | -0.730% | -22.12 € |
| ruptura_estricta | 901.80 € (-2.43%) | 78 | 28 | 24% | -0.523% | -1.362% | -1.494% | -24.46 € |
| macd_sin_salida | 906.27 € (-1.94%) | 146 | 34 | 40% | +0.070% | -0.608% | -0.722% | -20.44 € |
| c_banda_atr_tope | 917.66 € (-0.71%) | 29 | 5 | 31% | +0.111% | -0.989% | -1.117% | -6.61 € |
| ruptura_volumen_tope | 914.13 € (-1.09%) | 46 | 4 | 24% | +0.090% | -0.984% | -1.081% | -10.42 € |
| c_banda_atr_regimen | 910.75 € (-1.46%) | 67 | 26 | 34% | -0.044% | -0.934% | -1.072% | -14.43 € |
| macd_momentum_regimen | 904.80 € (-2.10%) | 135 | 28 | 22% | +0.003% | -0.691% | -0.804% | -21.37 € |
| ruptura_volumen_regimen | 893.31 € (-3.35%) | 126 | 33 | 16% | -0.418% | -1.126% | -1.240% | -32.37 € |
| c_banda_atr_evento | 912.74 € (-1.24%) | 90 | 26 | 37% | +0.159% | -0.635% | -0.737% | -13.19 € |
| macd_momentum_evento | 900.68 € (-2.55%) | 174 | 28 | 18% | +0.010% | -0.642% | -0.741% | -25.49 € |
| ruptura_volumen_evento | 905.16 € (-2.06%) | 103 | 33 | 21% | -0.108% | -0.864% | -0.954% | -20.40 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 05:00 | ruptura_volumen_evento | TAO | timeout | +0.96% | +0.46% | +0.10 |
| 2026-10-01 05:00 | ruptura_volumen_regimen | TAO | timeout | +0.96% | +0.46% | +0.10 |
| 2026-10-01 05:00 | ruptura_volumen_tope | SPX | timeout | +0.35% | -0.45% | -0.10 |
| 2026-10-01 05:00 | ruptura_volumen_tope | TAO | timeout | +0.96% | +0.16% | +0.04 |
| 2026-10-01 05:00 | estocastico_rebote | LTC | timeout | +0.71% | +0.21% | +0.05 |
| 2026-10-01 05:00 | pullback_tendencia | SUI | rotura de tendencia | -0.13% | -0.63% | -0.14 |
| 2026-10-01 05:00 | ruptura_volumen | TAO | timeout | +0.96% | +0.46% | +0.10 |
| 2026-10-01 04:55 | ruptura_volumen_evento | USELESS | take-profit | +2.50% | +2.00% | +0.45 |
| 2026-10-01 04:55 | macd_momentum_evento | SHIB | momentum perdido | +0.73% | +0.23% | +0.05 |
| 2026-10-01 04:55 | c_banda_atr_evento | PEPE | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 04:55 | c_banda_atr_evento | HBAR | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 04:55 | ruptura_volumen_regimen | USELESS | take-profit | +2.50% | +2.00% | +0.45 |
| 2026-10-01 04:55 | macd_momentum_regimen | SHIB | momentum perdido | +0.73% | +0.23% | +0.05 |
| 2026-10-01 04:55 | macd_sin_salida | MINA | timeout | +1.24% | +0.74% | +0.17 |
| 2026-10-01 04:55 | macd_sin_salida | MON | stop-loss | -1.50% | -2.00% | -0.45 |

## Eventos de la última vuelta

- 2026-10-01 04:55 [pullback_tendencia] ENTRADA SUI @ 1.0357 (22.56 €, apertura)
- 2026-10-01 05:00 [pullback_tendencia] CIERRE SUI rotura de tendencia bruto -0.13% neto -0.63%
- 2026-10-01 04:55 [macd_momentum] ENTRADA SUI @ 1.0357 (22.35 €, apertura)
- 2026-10-01 04:55 [macd_momentum_regimen] ENTRADA SUI @ 1.0357 (22.57 €, apertura)
- 2026-10-01 04:55 [macd_momentum_evento] ENTRADA SUI @ 1.0357 (22.47 €, apertura)
- 2026-10-01 05:00 [ruptura_volumen] CIERRE TAO timeout bruto +0.96% neto +0.46%
- 2026-10-01 05:00 [ruptura_volumen_tope] CIERRE TAO timeout bruto +0.96% neto +0.16%
- 2026-10-01 05:00 [ruptura_volumen_regimen] CIERRE TAO timeout bruto +0.96% neto +0.46%
- 2026-10-01 05:00 [ruptura_volumen_evento] CIERRE TAO timeout bruto +0.96% neto +0.46%
- 2026-10-01 04:55 [macd_momentum] ENTRADA LTC @ 59.69 (22.35 €, apertura)
- 2026-10-01 05:00 [estocastico_rebote] CIERRE LTC timeout bruto +0.71% neto +0.21%
- 2026-10-01 04:55 [macd_sin_salida] ENTRADA LTC @ 59.69 (22.60 €, apertura)
- 2026-10-01 04:55 [macd_momentum_regimen] ENTRADA LTC @ 59.69 (22.57 €, apertura)
- 2026-10-01 04:55 [macd_momentum_evento] ENTRADA LTC @ 59.69 (22.47 €, apertura)
- 2026-10-01 04:55 [c_banda_atr] ENTRADA ZRO @ 1.521 (22.63 €, apertura)
- 2026-10-01 04:55 [macd_momentum] ENTRADA ZRO @ 1.521 (22.35 €, apertura)
- 2026-10-01 04:55 [macd_sin_salida] ENTRADA ZRO @ 1.521 (22.60 €, apertura)
- 2026-10-01 04:55 [c_banda_atr_regimen] ENTRADA ZRO @ 1.521 (22.75 €, apertura)
- 2026-10-01 04:55 [macd_momentum_regimen] ENTRADA ZRO @ 1.521 (22.57 €, apertura)
- 2026-10-01 04:55 [c_banda_atr_evento] ENTRADA ZRO @ 1.521 (22.78 €, apertura)
- 2026-10-01 04:55 [macd_momentum_evento] ENTRADA ZRO @ 1.521 (22.47 €, apertura)
- 2026-10-01 04:55 [c_banda_atr] ENTRADA XDC @ 0.03113 (22.63 €, apertura)
- 2026-10-01 04:55 [macd_momentum] ENTRADA XDC @ 0.03113 (22.35 €, apertura)
- 2026-10-01 04:55 [macd_sin_salida] ENTRADA XDC @ 0.03113 (22.60 €, apertura)
- 2026-10-01 04:55 [c_banda_atr_regimen] ENTRADA XDC @ 0.03113 (22.75 €, apertura)
- 2026-10-01 04:55 [macd_momentum_regimen] ENTRADA XDC @ 0.03113 (22.57 €, apertura)
- 2026-10-01 04:55 [c_banda_atr_evento] ENTRADA XDC @ 0.03113 (22.78 €, apertura)
- 2026-10-01 04:55 [macd_momentum_evento] ENTRADA XDC @ 0.03113 (22.47 €, apertura)
- 2026-10-01 04:55 [ruptura_volumen_tope] ENTRADA USELESS @ 0.21319 (22.85 €, apertura)
- 2026-10-01 04:55 [ruptura_estricta] ENTRADA VVV @ 24.329 (22.49 €, apertura)
- 2026-10-01 04:55 [c_banda_atr] ENTRADA DASH @ 53.61 (22.63 €, apertura)
- 2026-10-01 04:55 [c_banda_atr_regimen] ENTRADA DASH @ 53.61 (22.75 €, apertura)
- 2026-10-01 04:55 [c_banda_atr_evento] ENTRADA DASH @ 53.61 (22.78 €, apertura)
- 2026-10-01 04:55 [macd_momentum] ENTRADA BNB @ 679.45 (22.35 €, apertura)
- 2026-10-01 04:55 [macd_momentum_regimen] ENTRADA BNB @ 679.45 (22.57 €, apertura)
- 2026-10-01 04:55 [macd_momentum_evento] ENTRADA BNB @ 679.45 (22.47 €, apertura)
- 2026-10-01 04:55 [macd_momentum] ENTRADA KAS @ 0.03942 (22.35 €, apertura)
- 2026-10-01 04:55 [macd_momentum_regimen] ENTRADA KAS @ 0.03942 (22.57 €, apertura)
- 2026-10-01 04:55 [macd_momentum_evento] ENTRADA KAS @ 0.03942 (22.47 €, apertura)
- 2026-10-01 04:55 [macd_momentum] ENTRADA SEI @ 0.06549 (22.35 €, apertura)
- 2026-10-01 04:55 [macd_sin_salida] ENTRADA SEI @ 0.06549 (22.60 €, apertura)
- 2026-10-01 04:55 [macd_momentum_regimen] ENTRADA SEI @ 0.06549 (22.57 €, apertura)
- 2026-10-01 04:55 [macd_momentum_evento] ENTRADA SEI @ 0.06549 (22.47 €, apertura)
- 2026-10-01 04:55 [macd_momentum] ENTRADA APT @ 0.6938 (22.35 €, apertura)
- 2026-10-01 04:55 [macd_momentum_regimen] ENTRADA APT @ 0.6938 (22.57 €, apertura)
- 2026-10-01 04:55 [macd_momentum_evento] ENTRADA APT @ 0.6938 (22.47 €, apertura)
- 2026-10-01 04:55 [estocastico_rebote] ENTRADA SPX @ 0.3998 (22.55 €, apertura)
- 2026-10-01 05:00 [ruptura_volumen_tope] CIERRE SPX timeout bruto +0.35% neto -0.45%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
