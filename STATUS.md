# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 04:51 UTC · vueltas 129 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 907.73 € (-1.79%) | 121 | 21 | 34% | +0.001% | -0.715% | -0.834% | -19.89 € |
| reversion_bb | 921.93 € (-0.25%) | 15 | 4 | 40% | +0.277% | -0.823% | -0.935% | -2.85 € |
| ruptura_volumen | 893.19 € (-3.36%) | 151 | 28 | 20% | -0.304% | -0.977% | -1.087% | -33.64 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 903.37 € (-2.26%) | 89 | 7 | 17% | -0.271% | -1.068% | -1.185% | -21.76 € |
| macd_momentum | 896.68 € (-2.98%) | 220 | 18 | 21% | +0.011% | -0.608% | -0.716% | -30.49 € |
| estocastico_rebote | 903.38 € (-2.26%) | 156 | 18 | 37% | +0.047% | -0.620% | -0.740% | -22.25 € |
| ruptura_estricta | 902.05 € (-2.40%) | 78 | 23 | 24% | -0.523% | -1.362% | -1.494% | -24.46 € |
| macd_sin_salida | 907.62 € (-1.80%) | 144 | 31 | 40% | +0.073% | -0.608% | -0.722% | -20.15 € |
| c_banda_atr_tope | 918.03 € (-0.67%) | 29 | 3 | 31% | +0.111% | -0.989% | -1.117% | -6.61 € |
| ruptura_volumen_tope | 914.68 € (-1.03%) | 44 | 5 | 23% | +0.064% | -1.022% | -1.120% | -10.35 € |
| c_banda_atr_regimen | 911.55 € (-1.37%) | 67 | 17 | 34% | -0.044% | -0.934% | -1.072% | -14.43 € |
| macd_momentum_regimen | 905.78 € (-2.00%) | 134 | 18 | 22% | -0.003% | -0.697% | -0.811% | -21.42 € |
| ruptura_volumen_regimen | 894.04 € (-3.27%) | 124 | 29 | 15% | -0.453% | -1.164% | -1.279% | -32.92 € |
| c_banda_atr_evento | 913.78 € (-1.13%) | 88 | 21 | 35% | +0.117% | -0.683% | -0.787% | -13.87 € |
| macd_momentum_evento | 901.65 € (-2.44%) | 173 | 18 | 17% | +0.006% | -0.647% | -0.746% | -25.54 € |
| ruptura_volumen_evento | 905.89 € (-1.98%) | 101 | 28 | 20% | -0.144% | -0.906% | -0.996% | -20.96 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 04:50 | macd_momentum_evento | INJ | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 04:50 | macd_momentum_evento | ADA | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 04:50 | c_banda_atr_evento | INJ | take-profit | +2.08% | +1.58% | +0.36 |
| 2026-10-01 04:50 | c_banda_atr_evento | USELESS | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 04:50 | c_banda_atr_evento | ADA | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 04:50 | macd_momentum_regimen | INJ | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 04:50 | macd_momentum_regimen | ADA | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 04:50 | c_banda_atr_regimen | OP | take-profit | +2.02% | +1.52% | +0.34 |
| 2026-10-01 04:50 | c_banda_atr_regimen | INJ | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 04:50 | c_banda_atr_regimen | USELESS | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 04:50 | c_banda_atr_regimen | TAO | take-profit | +2.11% | +1.61% | +0.37 |
| 2026-10-01 04:50 | c_banda_atr_regimen | ADA | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 04:50 | c_banda_atr_tope | KSM | timeout | +0.00% | -1.10% | -0.25 |
| 2026-10-01 04:50 | c_banda_atr_tope | USELESS | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-10-01 04:50 | macd_sin_salida | INJ | take-profit | +2.00% | +1.50% | +0.34 |

## Eventos de la última vuelta

- 2026-10-01 04:45 [estocastico_rebote] ENTRADA QNT @ 258.04 (22.55 €, apertura)
- 2026-10-01 04:50 [c_banda_atr] CIERRE ADA take-profit bruto +2.00% neto +1.50%
- 2026-10-01 04:50 [macd_momentum] CIERRE ADA take-profit bruto +2.00% neto +1.50%
- 2026-10-01 04:50 [macd_sin_salida] CIERRE ADA take-profit bruto +2.00% neto +1.50%
- 2026-10-01 04:50 [c_banda_atr_regimen] CIERRE ADA take-profit bruto +2.00% neto +1.50%
- 2026-10-01 04:50 [macd_momentum_regimen] CIERRE ADA take-profit bruto +2.00% neto +1.50%
- 2026-10-01 04:50 [c_banda_atr_evento] CIERRE ADA take-profit bruto +2.00% neto +1.50%
- 2026-10-01 04:50 [macd_momentum_evento] CIERRE ADA take-profit bruto +2.00% neto +1.50%
- 2026-10-01 04:45 [macd_momentum] ENTRADA TAO @ 272.5 (22.34 €, apertura)
- 2026-10-01 04:45 [macd_sin_salida] ENTRADA TAO @ 272.5 (22.59 €, apertura)
- 2026-10-01 04:50 [c_banda_atr_regimen] CIERRE TAO take-profit bruto +2.11% neto +1.61%
- 2026-10-01 04:45 [macd_momentum_regimen] ENTRADA TAO @ 272.5 (22.56 €, apertura)
- 2026-10-01 04:45 [macd_momentum_evento] ENTRADA TAO @ 272.5 (22.46 €, apertura)
- 2026-10-01 04:50 [reversion_bb] CIERRE UNI take-profit bruto +1.50% neto +0.40%
- 2026-10-01 04:45 [reversion_bb] ENTRADA CRV @ 0.34853 (23.03 €, apertura)
- 2026-10-01 04:50 [macd_sin_salida] CIERRE NIGHT take-profit bruto +2.00% neto +1.50%
- 2026-10-01 04:50 [c_banda_atr] CIERRE USELESS take-profit bruto +2.00% neto +1.50%
- 2026-10-01 04:50 [c_banda_atr_tope] CIERRE USELESS take-profit bruto +2.00% neto +0.90%
- 2026-10-01 04:50 [c_banda_atr_regimen] CIERRE USELESS take-profit bruto +2.00% neto +1.50%
- 2026-10-01 04:50 [c_banda_atr_evento] CIERRE USELESS take-profit bruto +2.00% neto +1.50%
- 2026-10-01 04:45 [estocastico_rebote] ENTRADA RENDER @ 1.708 (22.55 €, apertura)
- 2026-10-01 04:50 [c_banda_atr] CIERRE INJ take-profit bruto +2.08% neto +1.58%
- 2026-10-01 04:50 [macd_momentum] CIERRE INJ take-profit bruto +2.00% neto +1.50%
- 2026-10-01 04:50 [macd_sin_salida] CIERRE INJ take-profit bruto +2.00% neto +1.50%
- 2026-10-01 04:50 [c_banda_atr_regimen] CIERRE INJ take-profit bruto +2.00% neto +1.50%
- 2026-10-01 04:50 [macd_momentum_regimen] CIERRE INJ take-profit bruto +2.00% neto +1.50%
- 2026-10-01 04:50 [c_banda_atr_evento] CIERRE INJ take-profit bruto +2.08% neto +1.58%
- 2026-10-01 04:50 [macd_momentum_evento] CIERRE INJ take-profit bruto +2.00% neto +1.50%
- 2026-10-01 04:50 [c_banda_atr_regimen] CIERRE OP take-profit bruto +2.02% neto +1.52%
- 2026-10-01 04:45 [ruptura_volumen] ENTRADA VVV @ 24.175 (22.27 €, apertura)
- 2026-10-01 04:45 [ruptura_volumen_regimen] ENTRADA VVV @ 24.175 (22.28 €, apertura)
- 2026-10-01 04:45 [ruptura_volumen_evento] ENTRADA VVV @ 24.175 (22.58 €, apertura)
- 2026-10-01 04:50 [c_banda_atr_tope] CIERRE KSM timeout bruto +0.00% neto -1.10%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
