# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 21:46 UTC · vueltas 86 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 905.28 € (-2.05%) | 56 | 26 | 23% | -0.471% | -1.437% | -1.587% | -18.50 € |
| reversion_bb | 922.13 € (-0.23%) | 8 | 4 | 50% | +0.000% | -1.100% | -1.225% | -2.04 € |
| ruptura_volumen | 898.40 € (-2.80%) | 79 | 13 | 15% | -0.605% | -1.436% | -1.575% | -26.00 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 905.33 € (-2.05%) | 63 | 2 | 16% | -0.397% | -1.316% | -1.453% | -19.02 € |
| macd_momentum | 906.62 € (-1.91%) | 92 | 7 | 24% | -0.091% | -0.874% | -1.005% | -18.47 € |
| estocastico_rebote | 904.01 € (-2.19%) | 117 | 11 | 35% | -0.028% | -0.751% | -0.882% | -20.23 € |
| ruptura_estricta | 898.85 € (-2.75%) | 46 | 5 | 11% | -1.277% | -2.350% | -2.498% | -24.89 € |
| macd_sin_salida | 905.13 € (-2.07%) | 73 | 15 | 33% | -0.288% | -1.146% | -1.279% | -19.25 € |
| c_banda_atr_tope | 920.74 € (-0.38%) | 15 | 5 | 33% | +0.120% | -0.980% | -1.135% | -3.39 € |
| ruptura_volumen_tope | 917.46 € (-0.73%) | 21 | 5 | 19% | -0.273% | -1.373% | -1.471% | -6.65 € |
| c_banda_atr_regimen | 908.47 € (-1.71%) | 45 | 0 | 24% | -0.442% | -1.522% | -1.680% | -15.77 € |
| macd_momentum_regimen | 911.23 € (-1.41%) | 60 | 0 | 30% | -0.005% | -0.940% | -1.079% | -13.01 € |
| ruptura_volumen_regimen | 898.23 € (-2.81%) | 72 | 0 | 12% | -0.713% | -1.576% | -1.715% | -26.01 € |
| c_banda_atr_evento | 913.95 € (-1.11%) | 24 | 25 | 12% | -0.698% | -1.798% | -1.936% | -9.95 € |
| macd_momentum_evento | 911.92 € (-1.33%) | 45 | 7 | 16% | -0.215% | -1.275% | -1.399% | -13.18 € |
| ruptura_volumen_evento | 913.24 € (-1.19%) | 29 | 13 | 10% | -0.569% | -1.669% | -1.789% | -11.16 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 21:45 | ruptura_volumen_evento | CRV | timeout | -0.09% | -1.19% | -0.27 |
| 2026-09-30 21:45 | macd_momentum_evento | POL | momentum perdido | -0.19% | -0.99% | -0.23 |
| 2026-09-30 21:45 | ruptura_volumen_tope | CRV | timeout | -0.09% | -1.19% | -0.27 |
| 2026-09-30 21:45 | macd_sin_salida | HYPE | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 21:45 | estocastico_rebote | SUI | timeout | +0.16% | -0.34% | -0.08 |
| 2026-09-30 21:45 | macd_momentum | POL | momentum perdido | -0.19% | -0.69% | -0.16 |
| 2026-09-30 21:45 | ruptura_volumen | CRV | timeout | -0.09% | -0.59% | -0.13 |
| 2026-09-30 21:40 | ruptura_volumen_evento | NIGHT | take-profit | +2.50% | +1.40% | +0.32 |
| 2026-09-30 21:40 | macd_sin_salida | XMR | timeout | -0.81% | -1.31% | -0.30 |
| 2026-09-30 21:40 | estocastico_rebote | MINA | timeout | -0.79% | -1.29% | -0.29 |
| 2026-09-30 21:40 | ruptura_volumen | NIGHT | take-profit | +2.50% | +2.00% | +0.45 |
| 2026-09-30 21:35 | macd_momentum_evento | ARB | momentum perdido | -1.10% | -1.90% | -0.44 |
| 2026-09-30 21:35 | c_banda_atr_evento | PENGU | stop-loss | -1.59% | -2.69% | -0.62 |
| 2026-09-30 21:35 | macd_momentum | ARB | momentum perdido | -1.10% | -1.60% | -0.36 |
| 2026-09-30 21:35 | c_banda_atr | PENGU | stop-loss | -1.59% | -2.09% | -0.47 |

## Eventos de la última vuelta

- 2026-09-30 21:45 [estocastico_rebote] CIERRE SUI timeout bruto +0.16% neto -0.34%
- 2026-09-30 21:45 [macd_sin_salida] CIERRE HYPE take-profit bruto +2.00% neto +1.50%
- 2026-09-30 21:45 [macd_momentum] CIERRE POL momentum perdido bruto -0.19% neto -0.69%
- 2026-09-30 21:45 [macd_momentum_evento] CIERRE POL momentum perdido bruto -0.19% neto -0.99%
- 2026-09-30 21:40 [macd_momentum] ENTRADA ONDO @ 0.43891 (22.64 €, apertura)
- 2026-09-30 21:40 [macd_sin_salida] ENTRADA ONDO @ 0.43891 (22.62 €, apertura)
- 2026-09-30 21:40 [macd_momentum_evento] ENTRADA ONDO @ 0.43891 (22.78 €, apertura)
- 2026-09-30 21:45 [ruptura_volumen] CIERRE CRV timeout bruto -0.09% neto -0.59%
- 2026-09-30 21:45 [ruptura_volumen_tope] CIERRE CRV timeout bruto -0.09% neto -1.19%
- 2026-09-30 21:45 [ruptura_volumen_evento] CIERRE CRV timeout bruto -0.09% neto -1.19%
- 2026-09-30 21:40 [ruptura_volumen_tope] ENTRADA NIGHT @ 0.03458 (22.94 €, apertura)
- 2026-09-30 21:40 [estocastico_rebote] ENTRADA KAS @ 0.0384 (22.60 €, apertura)
- 2026-09-30 21:40 [macd_momentum] ENTRADA SEI @ 0.06505 (22.64 €, apertura)
- 2026-09-30 21:40 [macd_sin_salida] ENTRADA SEI @ 0.06505 (22.62 €, apertura)
- 2026-09-30 21:40 [macd_momentum_evento] ENTRADA SEI @ 0.06505 (22.78 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
