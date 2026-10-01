# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 07:06 UTC · vueltas 155 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 908.57 € (-1.70%) | 139 | 28 | 40% | +0.148% | -0.540% | -0.656% | -17.29 € |
| reversion_bb | 921.59 € (-0.29%) | 17 | 2 | 47% | +0.422% | -0.678% | -0.789% | -2.67 € |
| ruptura_volumen | 890.31 € (-3.67%) | 192 | 10 | 24% | -0.149% | -0.785% | -0.895% | -34.36 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 902.74 € (-2.33%) | 101 | 15 | 18% | -0.202% | -0.963% | -1.074% | -22.27 € |
| macd_momentum | 891.70 € (-3.52%) | 270 | 13 | 23% | +0.064% | -0.533% | -0.638% | -32.72 € |
| estocastico_rebote | 903.56 € (-2.24%) | 176 | 32 | 39% | +0.119% | -0.529% | -0.649% | -21.42 € |
| ruptura_estricta | 901.15 € (-2.50%) | 100 | 19 | 31% | -0.267% | -1.031% | -1.157% | -23.77 € |
| macd_sin_salida | 903.85 € (-2.21%) | 177 | 34 | 44% | +0.160% | -0.488% | -0.598% | -19.87 € |
| c_banda_atr_tope | 917.51 € (-0.73%) | 30 | 5 | 30% | +0.135% | -0.965% | -1.091% | -6.68 € |
| ruptura_volumen_tope | 914.81 € (-1.02%) | 52 | 3 | 31% | +0.206% | -0.802% | -0.909% | -9.60 € |
| c_banda_atr_regimen | 912.79 € (-1.24%) | 82 | 27 | 41% | +0.146% | -0.672% | -0.808% | -12.74 € |
| macd_momentum_regimen | 900.74 € (-2.54%) | 184 | 13 | 24% | +0.079% | -0.562% | -0.671% | -23.67 € |
| ruptura_volumen_regimen | 891.17 € (-3.58%) | 165 | 10 | 22% | -0.232% | -0.890% | -1.004% | -33.50 € |
| c_banda_atr_evento | 914.61 € (-1.04%) | 106 | 28 | 42% | +0.291% | -0.458% | -0.562% | -11.25 € |
| macd_momentum_evento | 896.64 € (-2.99%) | 223 | 13 | 21% | +0.072% | -0.547% | -0.645% | -27.78 € |
| ruptura_volumen_evento | 902.98 € (-2.30%) | 142 | 10 | 26% | +0.019% | -0.667% | -0.763% | -21.69 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 07:05 | ruptura_volumen_evento | KSM | timeout | +0.86% | +0.36% | +0.08 |
| 2026-10-01 07:05 | ruptura_volumen_evento | XDC | timeout | +0.67% | +0.17% | +0.04 |
| 2026-10-01 07:05 | macd_momentum_evento | TON | momentum perdido | +0.00% | -0.50% | -0.11 |
| 2026-10-01 07:05 | ruptura_volumen_regimen | KSM | timeout | +0.86% | +0.36% | +0.08 |
| 2026-10-01 07:05 | ruptura_volumen_regimen | XDC | timeout | +0.67% | +0.17% | +0.04 |
| 2026-10-01 07:05 | macd_momentum_regimen | TON | momentum perdido | +0.00% | -0.50% | -0.11 |
| 2026-10-01 07:05 | ruptura_volumen_tope | XDC | timeout | +0.67% | +0.17% | +0.04 |
| 2026-10-01 07:05 | ruptura_estricta | ARB | timeout | +0.39% | -0.12% | -0.03 |
| 2026-10-01 07:05 | macd_momentum | TON | momentum perdido | +0.00% | -0.50% | -0.11 |
| 2026-10-01 07:05 | ruptura_volumen | KSM | timeout | +0.86% | +0.36% | +0.08 |
| 2026-10-01 07:05 | ruptura_volumen | XDC | timeout | +0.67% | +0.17% | +0.04 |
| 2026-10-01 07:00 | ruptura_estricta | KAS | timeout | -0.97% | -1.47% | -0.33 |
| 2026-10-01 07:00 | ruptura_estricta | ETH | timeout | +0.82% | +0.33% | +0.07 |
| 2026-10-01 06:55 | macd_momentum_evento | TRUMP | momentum perdido | -0.42% | -0.92% | -0.21 |
| 2026-10-01 06:55 | macd_momentum_evento | ZEC | momentum perdido | -0.37% | -0.87% | -0.19 |

## Eventos de la última vuelta

- 2026-10-01 07:00 [macd_momentum] ENTRADA XLM @ 0.201125 (22.29 €, apertura)
- 2026-10-01 07:00 [macd_sin_salida] ENTRADA XLM @ 0.201125 (22.61 €, apertura)
- 2026-10-01 07:00 [macd_momentum_regimen] ENTRADA XLM @ 0.201125 (22.52 €, apertura)
- 2026-10-01 07:00 [macd_momentum_evento] ENTRADA XLM @ 0.201125 (22.41 €, apertura)
- 2026-10-01 07:00 [macd_momentum] ENTRADA LTC @ 59.5 (22.29 €, apertura)
- 2026-10-01 07:00 [macd_momentum_regimen] ENTRADA LTC @ 59.5 (22.52 €, apertura)
- 2026-10-01 07:00 [macd_momentum_evento] ENTRADA LTC @ 59.5 (22.41 €, apertura)
- 2026-10-01 07:05 [ruptura_estricta] CIERRE ARB timeout bruto +0.39% neto -0.11%
- 2026-10-01 07:00 [c_banda_atr] ENTRADA ICP @ 2.969 (22.67 €, apertura)
- 2026-10-01 07:00 [c_banda_atr_regimen] ENTRADA ICP @ 2.969 (22.79 €, apertura)
- 2026-10-01 07:00 [c_banda_atr_evento] ENTRADA ICP @ 2.969 (22.82 €, apertura)
- 2026-10-01 07:05 [ruptura_volumen] CIERRE XDC timeout bruto +0.67% neto +0.17%
- 2026-10-01 07:05 [ruptura_volumen_tope] CIERRE XDC timeout bruto +0.67% neto +0.17%
- 2026-10-01 07:05 [ruptura_volumen_regimen] CIERRE XDC timeout bruto +0.67% neto +0.17%
- 2026-10-01 07:05 [ruptura_volumen_evento] CIERRE XDC timeout bruto +0.67% neto +0.17%
- 2026-10-01 07:05 [ruptura_volumen] CIERRE KSM timeout bruto +0.86% neto +0.36%
- 2026-10-01 07:00 [macd_momentum] ENTRADA KSM @ 4.7 (22.29 €, apertura)
- 2026-10-01 07:00 [macd_sin_salida] ENTRADA KSM @ 4.7 (22.61 €, apertura)
- 2026-10-01 07:00 [ruptura_volumen_tope] ENTRADA KSM @ 4.7 (22.87 €, apertura)
- 2026-10-01 07:00 [macd_momentum_regimen] ENTRADA KSM @ 4.7 (22.52 €, apertura)
- 2026-10-01 07:05 [ruptura_volumen_regimen] CIERRE KSM timeout bruto +0.86% neto +0.36%
- 2026-10-01 07:00 [macd_momentum_evento] ENTRADA KSM @ 4.7 (22.41 €, apertura)
- 2026-10-01 07:05 [ruptura_volumen_evento] CIERRE KSM timeout bruto +0.86% neto +0.36%
- 2026-10-01 07:05 [macd_momentum] CIERRE TON momentum perdido bruto +0.00% neto -0.50%
- 2026-10-01 07:05 [macd_momentum_regimen] CIERRE TON momentum perdido bruto +0.00% neto -0.50%
- 2026-10-01 07:05 [macd_momentum_evento] CIERRE TON momentum perdido bruto +0.00% neto -0.50%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
