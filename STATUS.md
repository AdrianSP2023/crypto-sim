# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 12:16 UTC · vueltas 396 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 887.49 € (-3.98%) | 366 | 16 | 40% | +0.141% | -0.430% | -0.548% | -35.88 € |
| reversion_bb | 919.76 € (-0.48%) | 73 | 2 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 855.27 € (-7.46%) | 456 | 9 | 26% | -0.125% | -0.682% | -0.789% | -69.36 € |
| rebote_extremo | 922.49 € (-0.19%) | 15 | 1 | 60% | +0.574% | -0.526% | -0.706% | -1.82 € |
| pullback_tendencia | 887.67 € (-3.96%) | 265 | 8 | 21% | -0.011% | -0.610% | -0.696% | -36.69 € |
| macd_momentum | 846.77 € (-8.38%) | 743 | 7 | 24% | +0.064% | -0.471% | -0.569% | -77.55 € |
| estocastico_rebote | 877.50 € (-5.06%) | 443 | 37 | 38% | +0.106% | -0.453% | -0.559% | -45.50 € |
| ruptura_estricta | 880.43 € (-4.74%) | 248 | 10 | 31% | -0.171% | -0.778% | -0.893% | -43.82 € |
| macd_sin_salida | 875.35 € (-5.29%) | 484 | 23 | 39% | +0.117% | -0.437% | -0.545% | -48.04 € |
| c_banda_atr_tope | 912.90 € (-1.23%) | 82 | 5 | 38% | +0.248% | -0.574% | -0.689% | -10.83 € |
| ruptura_volumen_tope | 898.43 € (-2.79%) | 139 | 3 | 22% | -0.129% | -0.819% | -0.932% | -25.96 € |
| c_banda_atr_regimen | 899.95 € (-2.63%) | 218 | 17 | 42% | +0.157% | -0.463% | -0.587% | -23.22 € |
| macd_momentum_regimen | 869.44 € (-5.93%) | 506 | 7 | 24% | +0.069% | -0.483% | -0.581% | -54.86 € |
| ruptura_volumen_regimen | 859.91 € (-6.96%) | 379 | 9 | 23% | -0.194% | -0.763% | -0.875% | -64.72 € |
| c_banda_atr_evento | 893.63 € (-3.31%) | 333 | 10 | 41% | +0.186% | -0.394% | -0.508% | -29.97 € |
| macd_momentum_evento | 851.67 € (-7.85%) | 696 | 4 | 23% | +0.067% | -0.471% | -0.567% | -72.86 € |
| ruptura_volumen_evento | 867.25 € (-6.17%) | 406 | 8 | 26% | -0.063% | -0.628% | -0.730% | -57.19 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 12:15 | macd_sin_salida | WLD | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 12:15 | estocastico_rebote | OP | timeout | -0.84% | -1.34% | -0.30 |
| 2026-10-02 12:15 | estocastico_rebote | ALGO | timeout | +0.21% | -0.29% | -0.07 |
| 2026-10-02 12:15 | estocastico_rebote | ICP | timeout | -0.14% | -0.64% | -0.14 |
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

## Eventos de la última vuelta

- 2026-10-02 12:10 [estocastico_rebote] ENTRADA AVAX @ 9.926 (21.98 €, apertura)
- 2026-10-02 12:10 [c_banda_atr] ENTRADA HBAR @ 0.0949 (22.21 €, apertura)
- 2026-10-02 12:10 [c_banda_atr_regimen] ENTRADA HBAR @ 0.0949 (22.53 €, apertura)
- 2026-10-02 12:10 [estocastico_rebote] ENTRADA HYPE @ 81.15 (21.98 €, apertura)
- 2026-10-02 12:10 [estocastico_rebote] ENTRADA TAO @ 274.833 (21.98 €, apertura)
- 2026-10-02 12:10 [c_banda_atr] ENTRADA DOT @ 1.0859 (22.21 €, apertura)
- 2026-10-02 12:10 [c_banda_atr_regimen] ENTRADA DOT @ 1.0859 (22.53 €, apertura)
- 2026-10-02 12:15 [estocastico_rebote] CIERRE ICP timeout bruto -0.14% neto -0.64%
- 2026-10-02 12:10 [pullback_tendencia] ENTRADA ALGO @ 0.11666 (22.19 €, apertura)
- 2026-10-02 12:15 [estocastico_rebote] CIERRE ALGO timeout bruto +0.21% neto -0.29%
- 2026-10-02 12:10 [estocastico_rebote] ENTRADA ONDO @ 0.45221 (21.98 €, apertura)
- 2026-10-02 12:10 [macd_momentum] ENTRADA CRV @ 0.33987 (21.17 €, apertura)
- 2026-10-02 12:10 [macd_momentum_regimen] ENTRADA CRV @ 0.33987 (21.73 €, apertura)
- 2026-10-02 12:15 [macd_sin_salida] CIERRE WLD take-profit bruto +2.00% neto +1.50%
- 2026-10-02 12:15 [estocastico_rebote] CIERRE OP timeout bruto -0.84% neto -1.34%
- 2026-10-02 12:10 [c_banda_atr] ENTRADA MINA @ 0.1451 (22.21 €, apertura)
- 2026-10-02 12:10 [macd_momentum] ENTRADA MINA @ 0.1451 (21.17 €, apertura)
- 2026-10-02 12:10 [macd_sin_salida] ENTRADA MINA @ 0.1451 (21.91 €, apertura)
- 2026-10-02 12:10 [c_banda_atr_regimen] ENTRADA MINA @ 0.1451 (22.53 €, apertura)
- 2026-10-02 12:10 [macd_momentum_regimen] ENTRADA MINA @ 0.1451 (21.73 €, apertura)
- 2026-10-02 12:10 [c_banda_atr] ENTRADA DASH @ 53.425 (22.21 €, apertura)
- 2026-10-02 12:10 [ruptura_volumen_tope] ENTRADA DASH @ 53.425 (22.46 €, apertura)
- 2026-10-02 12:10 [c_banda_atr_regimen] ENTRADA DASH @ 53.425 (22.53 €, apertura)
- 2026-10-02 12:10 [macd_momentum] ENTRADA TRUMP @ 1.929 (21.17 €, apertura)
- 2026-10-02 12:10 [macd_sin_salida] ENTRADA TRUMP @ 1.929 (21.91 €, apertura)
- 2026-10-02 12:10 [macd_momentum_regimen] ENTRADA TRUMP @ 1.929 (21.73 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
