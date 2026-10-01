# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 07:26 UTC · vueltas 159 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 902.60 € (-2.34%) | 148 | 19 | 39% | +0.117% | -0.560% | -0.680% | -19.06 € |
| reversion_bb | 920.75 € (-0.38%) | 18 | 2 | 44% | +0.315% | -0.785% | -0.896% | -3.26 € |
| ruptura_volumen | 887.17 € (-4.01%) | 198 | 6 | 24% | -0.169% | -0.801% | -0.912% | -36.11 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 898.41 € (-2.79%) | 117 | 1 | 16% | -0.237% | -0.963% | -1.067% | -25.73 € |
| macd_momentum | 886.89 € (-4.04%) | 282 | 7 | 22% | +0.026% | -0.567% | -0.673% | -36.31 € |
| estocastico_rebote | 894.46 € (-3.22%) | 188 | 23 | 37% | +0.035% | -0.603% | -0.723% | -26.01 € |
| ruptura_estricta | 896.02 € (-3.05%) | 103 | 19 | 30% | -0.306% | -1.062% | -1.190% | -25.17 € |
| macd_sin_salida | 894.81 € (-3.18%) | 190 | 25 | 41% | +0.061% | -0.576% | -0.688% | -25.12 € |
| c_banda_atr_tope | 916.01 € (-0.89%) | 32 | 4 | 28% | +0.032% | -1.068% | -1.190% | -7.87 € |
| ruptura_volumen_tope | 913.66 € (-1.14%) | 53 | 4 | 30% | +0.180% | -0.819% | -0.927% | -9.99 € |
| c_banda_atr_regimen | 906.99 € (-1.87%) | 92 | 17 | 40% | +0.078% | -0.706% | -0.845% | -14.97 € |
| macd_momentum_regimen | 895.88 € (-3.07%) | 196 | 7 | 23% | +0.023% | -0.610% | -0.719% | -27.29 € |
| ruptura_volumen_regimen | 888.02 € (-3.92%) | 171 | 6 | 21% | -0.252% | -0.905% | -1.019% | -35.26 € |
| c_banda_atr_evento | 908.60 € (-1.69%) | 115 | 19 | 42% | +0.239% | -0.491% | -0.600% | -13.03 € |
| macd_momentum_evento | 891.80 € (-3.51%) | 235 | 7 | 20% | +0.025% | -0.587% | -0.686% | -31.38 € |
| ruptura_volumen_evento | 899.79 € (-2.65%) | 148 | 6 | 25% | -0.015% | -0.693% | -0.790% | -23.46 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 07:25 | ruptura_volumen_evento | SKY | timeout | -0.21% | -0.71% | -0.16 |
| 2026-10-01 07:25 | ruptura_volumen_evento | OP | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-01 07:25 | ruptura_volumen_evento | SUI | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-01 07:25 | macd_momentum_evento | NIGHT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 07:25 | macd_momentum_evento | LTC | momentum perdido | -0.72% | -1.22% | -0.27 |
| 2026-10-01 07:25 | macd_momentum_evento | UNI | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 07:25 | macd_momentum_evento | TAO | momentum perdido | -0.94% | -1.44% | -0.32 |
| 2026-10-01 07:25 | macd_momentum_evento | XLM | momentum perdido | -1.32% | -1.82% | -0.41 |
| 2026-10-01 07:25 | macd_momentum_evento | AVAX | momentum perdido | -1.33% | -1.83% | -0.41 |
| 2026-10-01 07:25 | c_banda_atr_evento | KAS | stop-loss | -1.92% | -2.42% | -0.55 |
| 2026-10-01 07:25 | c_banda_atr_evento | MINA | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-10-01 07:25 | c_banda_atr_evento | ARB | stop-loss | -1.53% | -2.03% | -0.46 |
| 2026-10-01 07:25 | c_banda_atr_evento | ZEC | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-10-01 07:25 | ruptura_volumen_regimen | SKY | timeout | -0.21% | -0.71% | -0.16 |
| 2026-10-01 07:25 | ruptura_volumen_regimen | OP | stop-loss | -1.20% | -1.70% | -0.38 |

## Eventos de la última vuelta

- 2026-10-01 07:25 [pullback_tendencia] CIERRE NEAR stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:25 [c_banda_atr_tope] CIERRE LINK stop-loss bruto -1.50% neto -2.60%
- 2026-10-01 07:25 [c_banda_atr_regimen] CIERRE LINK stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:25 [ruptura_volumen] CIERRE SUI stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 07:25 [estocastico_rebote] CIERRE SUI stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:25 [macd_sin_salida] CIERRE SUI stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:25 [ruptura_volumen_regimen] CIERRE SUI stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 07:25 [ruptura_volumen_evento] CIERRE SUI stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 07:25 [macd_momentum] CIERRE AVAX momentum perdido bruto -1.33% neto -1.83%
- 2026-10-01 07:25 [macd_momentum_regimen] CIERRE AVAX momentum perdido bruto -1.33% neto -1.83%
- 2026-10-01 07:25 [macd_momentum_evento] CIERRE AVAX momentum perdido bruto -1.33% neto -1.83%
- 2026-10-01 07:25 [macd_sin_salida] CIERRE HBAR timeout bruto -0.27% neto -0.77%
- 2026-10-01 07:25 [c_banda_atr] CIERRE ZEC stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:25 [estocastico_rebote] CIERRE ZEC stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:25 [macd_sin_salida] CIERRE ZEC stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:25 [c_banda_atr_regimen] CIERRE ZEC stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:25 [c_banda_atr_evento] CIERRE ZEC stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:25 [macd_momentum] CIERRE XLM momentum perdido bruto -1.32% neto -1.82%
- 2026-10-01 07:25 [macd_momentum_regimen] CIERRE XLM momentum perdido bruto -1.32% neto -1.82%
- 2026-10-01 07:25 [macd_momentum_evento] CIERRE XLM momentum perdido bruto -1.32% neto -1.82%
- 2026-10-01 07:25 [macd_momentum] CIERRE TAO momentum perdido bruto -0.94% neto -1.44%
- 2026-10-01 07:25 [macd_momentum_regimen] CIERRE TAO momentum perdido bruto -0.94% neto -1.44%
- 2026-10-01 07:25 [macd_momentum_evento] CIERRE TAO momentum perdido bruto -0.94% neto -1.44%
- 2026-10-01 07:25 [macd_momentum] CIERRE UNI stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:25 [estocastico_rebote] CIERRE UNI stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:25 [macd_sin_salida] CIERRE UNI stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:25 [macd_momentum_regimen] CIERRE UNI stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:25 [macd_momentum_evento] CIERRE UNI stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:25 [macd_momentum] CIERRE LTC momentum perdido bruto -0.72% neto -1.22%
- 2026-10-01 07:25 [macd_momentum_regimen] CIERRE LTC momentum perdido bruto -0.72% neto -1.22%
- 2026-10-01 07:25 [macd_momentum_evento] CIERRE LTC momentum perdido bruto -0.72% neto -1.22%
- 2026-10-01 07:25 [c_banda_atr] CIERRE ARB stop-loss bruto -1.53% neto -2.03%
- 2026-10-01 07:25 [estocastico_rebote] CIERRE ARB stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:25 [c_banda_atr_regimen] CIERRE ARB stop-loss bruto -1.53% neto -2.03%
- 2026-10-01 07:25 [c_banda_atr_evento] CIERRE ARB stop-loss bruto -1.53% neto -2.03%
- 2026-10-01 07:25 [pullback_tendencia] CIERRE ONDO rotura de tendencia bruto -0.74% neto -1.24%
- 2026-10-01 07:25 [macd_sin_salida] CIERRE ONDO stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:25 [reversion_bb] CIERRE CRV stop-loss bruto -1.50% neto -2.60%
- 2026-10-01 07:25 [estocastico_rebote] CIERRE CRV stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:25 [macd_momentum] CIERRE NIGHT stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:25 [macd_sin_salida] CIERRE NIGHT stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:25 [macd_momentum_regimen] CIERRE NIGHT stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:25 [macd_momentum_evento] CIERRE NIGHT stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:25 [estocastico_rebote] CIERRE MON stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:25 [ruptura_volumen] CIERRE OP stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 07:25 [ruptura_volumen_regimen] CIERRE OP stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 07:25 [ruptura_volumen_evento] CIERRE OP stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 07:25 [c_banda_atr] CIERRE MINA stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:25 [c_banda_atr_regimen] CIERRE MINA stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:25 [c_banda_atr_evento] CIERRE MINA stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:25 [estocastico_rebote] CIERRE FIL stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:25 [estocastico_rebote] CIERRE VVV stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:25 [pullback_tendencia] CIERRE ASTER rotura de tendencia bruto -0.72% neto -1.22%
- 2026-10-01 07:20 [c_banda_atr_tope] ENTRADA DASH @ 53.636 (22.91 €, apertura)
- 2026-10-01 07:25 [estocastico_rebote] CIERRE PENGU stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:25 [estocastico_rebote] CIERRE TRUMP stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:25 [macd_sin_salida] CIERRE TRUMP stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:25 [c_banda_atr] CIERRE KAS stop-loss bruto -1.92% neto -2.42%
- 2026-10-01 07:25 [c_banda_atr_regimen] CIERRE KAS stop-loss bruto -1.92% neto -2.42%
- 2026-10-01 07:25 [c_banda_atr_evento] CIERRE KAS stop-loss bruto -1.92% neto -2.42%
- 2026-10-01 07:25 [ruptura_volumen] CIERRE SKY timeout bruto -0.21% neto -0.71%
- 2026-10-01 07:25 [ruptura_volumen_regimen] CIERRE SKY timeout bruto -0.21% neto -0.71%
- 2026-10-01 07:25 [ruptura_volumen_evento] CIERRE SKY timeout bruto -0.21% neto -0.71%
- 2026-10-01 07:20 [macd_momentum] ENTRADA XMR @ 486.07 (22.20 €, apertura)
- 2026-10-01 07:20 [ruptura_estricta] ENTRADA XMR @ 486.07 (22.48 €, apertura)
- 2026-10-01 07:20 [macd_sin_salida] ENTRADA XMR @ 486.07 (22.48 €, apertura)
- 2026-10-01 07:20 [macd_momentum_regimen] ENTRADA XMR @ 486.07 (22.42 €, apertura)
- 2026-10-01 07:20 [macd_momentum_evento] ENTRADA XMR @ 486.07 (22.32 €, apertura)
- 2026-10-01 07:25 [pullback_tendencia] CIERRE SEI rotura de tendencia bruto -0.15% neto -0.65%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
