# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 16:51 UTC · vueltas 55 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 915.04 € (-1.00%) | 37 | 9 | 35% | -0.134% | -1.234% | -1.394% | -10.56 € |
| reversion_bb | 923.92 € (-0.04%) | 4 | 0 | 75% | +0.750% | -0.350% | -0.453% | -0.33 € |
| ruptura_volumen | 905.52 € (-2.03%) | 52 | 9 | 17% | -0.578% | -1.580% | -1.725% | -18.92 € |
| rebote_extremo | 924.45 € (+0.02%) | 0 | 2 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 912.11 € (-1.31%) | 35 | 5 | 17% | -0.436% | -1.536% | -1.666% | -12.38 € |
| macd_momentum | 912.85 € (-1.23%) | 60 | 4 | 32% | +0.052% | -0.883% | -1.024% | -12.22 € |
| estocastico_rebote | 918.25 € (-0.65%) | 63 | 12 | 52% | +0.318% | -0.563% | -0.726% | -8.25 € |
| ruptura_estricta | 901.80 € (-2.43%) | 40 | 4 | 10% | -1.291% | -2.391% | -2.538% | -22.08 € |
| macd_sin_salida | 910.13 € (-1.53%) | 54 | 8 | 35% | -0.190% | -1.174% | -1.318% | -14.65 € |
| c_banda_atr_tope | 923.84 € (-0.04%) | 9 | 5 | 56% | +0.446% | -0.654% | -0.837% | -1.36 € |
| ruptura_volumen_tope | 921.67 € (-0.28%) | 10 | 5 | 30% | -0.085% | -1.185% | -1.269% | -2.74 € |
| c_banda_atr_regimen | 913.82 € (-1.13%) | 35 | 5 | 31% | -0.256% | -1.356% | -1.509% | -10.97 € |
| macd_momentum_regimen | 913.18 € (-1.20%) | 52 | 3 | 31% | +0.021% | -0.981% | -1.122% | -11.78 € |
| ruptura_volumen_regimen | 905.29 € (-2.05%) | 53 | 8 | 17% | -0.589% | -1.582% | -1.727% | -19.31 € |
| c_banda_atr_evento | 926.35 € (+0.23%) | 3 | 11 | 100% | +2.000% | +0.900% | +0.696% | +0.62 € |
| macd_momentum_evento | 922.20 € (-0.22%) | 13 | 4 | 38% | +0.140% | -0.960% | -1.113% | -2.88 € |
| ruptura_volumen_evento | 924.25 € (+0.00%) | 2 | 9 | 50% | +0.650% | -0.450% | -0.479% | -0.21 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 16:50 | c_banda_atr_evento | ONDO | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-30 16:50 | c_banda_atr_regimen | ONDO | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-30 16:50 | estocastico_rebote | PENGU | take-profit | +1.80% | +1.00% | +0.23 |
| 2026-09-30 16:50 | estocastico_rebote | BCH | take-profit | +1.84% | +1.04% | +0.24 |
| 2026-09-30 16:50 | c_banda_atr | ONDO | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-09-30 16:45 | estocastico_rebote | XLM | take-profit | +1.80% | +1.00% | +0.23 |
| 2026-09-30 16:40 | ruptura_volumen_evento | HYPE | take-profit | +2.50% | +1.40% | +0.32 |
| 2026-09-30 16:40 | macd_momentum_evento | TRUMP | momentum perdido | -0.49% | -1.59% | -0.37 |
| 2026-09-30 16:40 | macd_momentum_evento | HBAR | momentum perdido | -0.74% | -1.84% | -0.42 |
| 2026-09-30 16:40 | ruptura_volumen_regimen | HYPE | take-profit | +2.50% | +2.00% | +0.45 |
| 2026-09-30 16:40 | c_banda_atr_regimen | XMR | timeout | +0.32% | -0.78% | -0.18 |
| 2026-09-30 16:40 | ruptura_volumen_tope | HYPE | take-profit | +2.50% | +1.40% | +0.32 |
| 2026-09-30 16:40 | ruptura_estricta | MON | stop-loss | -2.00% | -3.10% | -0.70 |
| 2026-09-30 16:40 | estocastico_rebote | ONDO | take-profit | +1.80% | +1.00% | +0.23 |
| 2026-09-30 16:40 | macd_momentum | TRUMP | momentum perdido | -0.49% | -0.99% | -0.23 |

## Eventos de la última vuelta

- 2026-09-30 16:45 [ruptura_volumen] ENTRADA NEAR @ 4.8169 (22.63 €, apertura)
- 2026-09-30 16:45 [ruptura_estricta] ENTRADA NEAR @ 4.8169 (22.55 €, apertura)
- 2026-09-30 16:45 [ruptura_volumen_tope] ENTRADA NEAR @ 4.8169 (23.04 €, apertura)
- 2026-09-30 16:45 [ruptura_volumen_regimen] ENTRADA NEAR @ 4.8169 (22.62 €, apertura)
- 2026-09-30 16:45 [ruptura_volumen_evento] ENTRADA NEAR @ 4.8169 (23.10 €, apertura)
- 2026-09-30 16:50 [c_banda_atr] CIERRE ONDO take-profit bruto +2.00% neto +0.90%
- 2026-09-30 16:45 [ruptura_volumen] ENTRADA ONDO @ 0.45021 (22.63 €, apertura)
- 2026-09-30 16:50 [c_banda_atr_regimen] CIERRE ONDO take-profit bruto +2.00% neto +0.90%
- 2026-09-30 16:45 [ruptura_volumen_regimen] ENTRADA ONDO @ 0.45021 (22.62 €, apertura)
- 2026-09-30 16:50 [c_banda_atr_evento] CIERRE ONDO take-profit bruto +2.00% neto +0.90%
- 2026-09-30 16:45 [ruptura_volumen_evento] ENTRADA ONDO @ 0.45021 (23.10 €, apertura)
- 2026-09-30 16:45 [c_banda_atr] ENTRADA WLD @ 0.4793 (22.84 €, apertura)
- 2026-09-30 16:45 [c_banda_atr_regimen] ENTRADA WLD @ 0.4793 (22.83 €, apertura)
- 2026-09-30 16:45 [c_banda_atr_evento] ENTRADA WLD @ 0.4793 (23.12 €, apertura)
- 2026-09-30 16:45 [pullback_tendencia] ENTRADA XDC @ 0.03024 (22.80 €, apertura)
- 2026-09-30 16:50 [estocastico_rebote] CIERRE BCH take-profit bruto +1.84% neto +1.04%
- 2026-09-30 16:45 [c_banda_atr] ENTRADA INJ @ 6.558 (22.84 €, apertura)
- 2026-09-30 16:45 [c_banda_atr_regimen] ENTRADA INJ @ 6.558 (22.83 €, apertura)
- 2026-09-30 16:45 [c_banda_atr_evento] ENTRADA INJ @ 6.558 (23.12 €, apertura)
- 2026-09-30 16:45 [c_banda_atr] ENTRADA OP @ 0.1168 (22.84 €, apertura)
- 2026-09-30 16:45 [c_banda_atr_regimen] ENTRADA OP @ 0.1168 (22.83 €, apertura)
- 2026-09-30 16:45 [c_banda_atr_evento] ENTRADA OP @ 0.1168 (23.12 €, apertura)
- 2026-09-30 16:50 [estocastico_rebote] CIERRE PENGU take-profit bruto +1.80% neto +1.00%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
