# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 12:11 UTC · vueltas 395 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 887.40 € (-3.99%) | 366 | 12 | 40% | +0.141% | -0.430% | -0.548% | -35.88 € |
| reversion_bb | 919.76 € (-0.48%) | 73 | 2 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 855.15 € (-7.48%) | 456 | 9 | 26% | -0.125% | -0.682% | -0.789% | -69.36 € |
| rebote_extremo | 922.52 € (-0.19%) | 15 | 1 | 60% | +0.574% | -0.526% | -0.706% | -1.82 € |
| pullback_tendencia | 887.88 € (-3.93%) | 265 | 7 | 21% | -0.011% | -0.610% | -0.696% | -36.69 € |
| macd_momentum | 846.81 € (-8.38%) | 743 | 4 | 24% | +0.064% | -0.471% | -0.569% | -77.55 € |
| estocastico_rebote | 877.79 € (-5.03%) | 440 | 36 | 38% | +0.108% | -0.451% | -0.558% | -45.00 € |
| ruptura_estricta | 880.08 € (-4.78%) | 248 | 10 | 31% | -0.171% | -0.778% | -0.893% | -43.82 € |
| macd_sin_salida | 875.48 € (-5.28%) | 483 | 22 | 39% | +0.113% | -0.441% | -0.549% | -48.37 € |
| c_banda_atr_tope | 912.62 € (-1.26%) | 82 | 5 | 38% | +0.248% | -0.574% | -0.689% | -10.83 € |
| ruptura_volumen_tope | 898.32 € (-2.80%) | 139 | 2 | 22% | -0.129% | -0.819% | -0.932% | -25.96 € |
| c_banda_atr_regimen | 899.89 € (-2.63%) | 218 | 13 | 42% | +0.157% | -0.463% | -0.587% | -23.22 € |
| macd_momentum_regimen | 869.49 € (-5.92%) | 506 | 4 | 24% | +0.069% | -0.483% | -0.581% | -54.86 € |
| ruptura_volumen_regimen | 859.79 € (-6.97%) | 379 | 9 | 23% | -0.194% | -0.763% | -0.875% | -64.72 € |
| c_banda_atr_evento | 893.20 € (-3.36%) | 333 | 10 | 41% | +0.186% | -0.394% | -0.508% | -29.97 € |
| macd_momentum_evento | 851.51 € (-7.87%) | 696 | 4 | 23% | +0.067% | -0.471% | -0.567% | -72.86 € |
| ruptura_volumen_evento | 867.26 € (-6.16%) | 406 | 8 | 26% | -0.063% | -0.628% | -0.730% | -57.19 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 12:10 | macd_momentum_evento | MON | momentum perdido | +0.60% | +0.10% | +0.02 |
| 2026-10-02 12:10 | macd_momentum_regimen | MON | momentum perdido | +0.60% | +0.10% | +0.02 |
| 2026-10-02 12:10 | macd_momentum | MON | momentum perdido | +0.60% | +0.10% | +0.02 |
| 2026-10-02 12:05 | ruptura_volumen_evento | ONDO | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 12:05 | macd_momentum_evento | NIGHT | take-profit | +2.00% | +1.50% | +0.32 |
| 2026-10-02 12:05 | macd_momentum_evento | LINK | momentum perdido | -0.56% | -1.06% | -0.23 |
| 2026-10-02 12:05 | macd_momentum_evento | ETH | momentum perdido | -0.17% | -0.67% | -0.14 |
| 2026-10-02 12:05 | c_banda_atr_evento | BNB | timeout | +0.41% | -0.09% | -0.02 |
| 2026-10-02 12:05 | c_banda_atr_evento | UNI | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-02 12:05 | c_banda_atr_evento | HYPE | timeout | +0.75% | +0.25% | +0.06 |
| 2026-10-02 12:05 | c_banda_atr_evento | AAVE | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-02 12:05 | c_banda_atr_evento | SUI | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-02 12:05 | ruptura_volumen_regimen | ONDO | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 12:05 | macd_momentum_regimen | NIGHT | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 12:05 | macd_momentum_regimen | LINK | momentum perdido | -0.56% | -1.06% | -0.23 |

## Eventos de la última vuelta

- 2026-10-02 12:05 [estocastico_rebote] ENTRADA PUMP @ 0.005176 (21.98 €, apertura)
- 2026-10-02 12:05 [reversion_bb] ENTRADA TAO @ 274.281 (22.99 €, apertura)
- 2026-10-02 12:05 [ruptura_volumen] ENTRADA NIGHT @ 0.0417 (21.37 €, apertura)
- 2026-10-02 12:05 [ruptura_estricta] ENTRADA NIGHT @ 0.0417 (22.01 €, apertura)
- 2026-10-02 12:05 [ruptura_volumen_tope] ENTRADA NIGHT @ 0.0417 (22.46 €, apertura)
- 2026-10-02 12:05 [ruptura_volumen_regimen] ENTRADA NIGHT @ 0.0417 (21.49 €, apertura)
- 2026-10-02 12:05 [rebote_extremo] ENTRADA PEPE @ 3.921e-06 (23.06 €, apertura)
- 2026-10-02 12:10 [macd_momentum] CIERRE MON momentum perdido bruto +0.60% neto +0.10%
- 2026-10-02 12:10 [macd_momentum_regimen] CIERRE MON momentum perdido bruto +0.60% neto +0.10%
- 2026-10-02 12:10 [macd_momentum_evento] CIERRE MON momentum perdido bruto +0.60% neto +0.10%
- 2026-10-02 12:05 [c_banda_atr] ENTRADA WLFI @ 0.05 (22.21 €, apertura)
- 2026-10-02 12:05 [c_banda_atr_regimen] ENTRADA WLFI @ 0.05 (22.53 €, apertura)
- 2026-10-02 12:05 [c_banda_atr] ENTRADA TRUMP @ 1.92 (22.21 €, apertura)
- 2026-10-02 12:05 [c_banda_atr_regimen] ENTRADA TRUMP @ 1.92 (22.53 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
