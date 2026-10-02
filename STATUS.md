# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 12:06 UTC · vueltas 394 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 886.78 € (-4.05%) | 366 | 10 | 40% | +0.141% | -0.430% | -0.548% | -35.88 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 1 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 854.64 € (-7.53%) | 456 | 8 | 26% | -0.125% | -0.682% | -0.789% | -69.36 € |
| rebote_extremo | 922.42 € (-0.20%) | 15 | 0 | 60% | +0.574% | -0.526% | -0.706% | -1.82 € |
| pullback_tendencia | 887.34 € (-3.99%) | 265 | 7 | 21% | -0.011% | -0.610% | -0.696% | -36.69 € |
| macd_momentum | 846.79 € (-8.38%) | 742 | 5 | 24% | +0.064% | -0.471% | -0.570% | -77.58 € |
| estocastico_rebote | 875.68 € (-5.25%) | 440 | 35 | 38% | +0.108% | -0.451% | -0.558% | -45.00 € |
| ruptura_estricta | 879.35 € (-4.86%) | 248 | 9 | 31% | -0.171% | -0.778% | -0.893% | -43.82 € |
| macd_sin_salida | 874.35 € (-5.40%) | 483 | 22 | 39% | +0.113% | -0.441% | -0.549% | -48.37 € |
| c_banda_atr_tope | 912.57 € (-1.26%) | 82 | 5 | 38% | +0.248% | -0.574% | -0.689% | -10.83 € |
| ruptura_volumen_tope | 898.17 € (-2.82%) | 139 | 1 | 22% | -0.129% | -0.819% | -0.932% | -25.96 € |
| c_banda_atr_regimen | 899.26 € (-2.70%) | 218 | 11 | 42% | +0.157% | -0.463% | -0.587% | -23.22 € |
| macd_momentum_regimen | 869.46 € (-5.93%) | 505 | 5 | 24% | +0.068% | -0.484% | -0.582% | -54.88 € |
| ruptura_volumen_regimen | 859.28 € (-7.03%) | 379 | 8 | 23% | -0.194% | -0.763% | -0.875% | -64.72 € |
| c_banda_atr_evento | 892.68 € (-3.41%) | 333 | 10 | 41% | +0.186% | -0.394% | -0.508% | -29.97 € |
| macd_momentum_evento | 851.48 € (-7.87%) | 695 | 5 | 23% | +0.066% | -0.472% | -0.568% | -72.88 € |
| ruptura_volumen_evento | 866.80 € (-6.21%) | 406 | 8 | 26% | -0.063% | -0.628% | -0.730% | -57.19 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
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
| 2026-10-02 12:05 | macd_momentum_regimen | ETH | momentum perdido | -0.17% | -0.67% | -0.14 |
| 2026-10-02 12:05 | c_banda_atr_regimen | BNB | timeout | +0.41% | -0.09% | -0.02 |
| 2026-10-02 12:05 | c_banda_atr_regimen | UNI | stop-loss | -1.50% | -2.00% | -0.45 |

## Eventos de la última vuelta

- 2026-10-02 12:00 [estocastico_rebote] ENTRADA XRP @ 1.36328 (22.00 €, apertura)
- 2026-10-02 12:05 [macd_momentum] CIERRE ETH momentum perdido bruto -0.17% neto -0.67%
- 2026-10-02 12:05 [macd_momentum_regimen] CIERRE ETH momentum perdido bruto -0.17% neto -0.67%
- 2026-10-02 12:05 [macd_momentum_evento] CIERRE ETH momentum perdido bruto -0.17% neto -0.67%
- 2026-10-02 12:05 [ruptura_estricta] CIERRE QNT stop-loss bruto -2.00% neto -2.50%
- 2026-10-02 12:05 [estocastico_rebote] CIERRE NEAR stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 12:05 [macd_momentum] CIERRE LINK momentum perdido bruto -0.56% neto -1.06%
- 2026-10-02 12:05 [macd_momentum_regimen] CIERRE LINK momentum perdido bruto -0.56% neto -1.06%
- 2026-10-02 12:05 [macd_momentum_evento] CIERRE LINK momentum perdido bruto -0.56% neto -1.06%
- 2026-10-02 12:05 [c_banda_atr] CIERRE SUI stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 12:05 [macd_sin_salida] CIERRE SUI stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 12:05 [c_banda_atr_regimen] CIERRE SUI stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 12:05 [c_banda_atr_evento] CIERRE SUI stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 12:00 [pullback_tendencia] ENTRADA HBAR @ 0.09426 (22.20 €, apertura)
- 2026-10-02 12:05 [c_banda_atr] CIERRE AAVE stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 12:05 [macd_sin_salida] CIERRE AAVE stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 12:05 [c_banda_atr_regimen] CIERRE AAVE stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 12:05 [c_banda_atr_evento] CIERRE AAVE stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 12:05 [c_banda_atr] CIERRE HYPE timeout bruto +0.75% neto +0.25%
- 2026-10-02 12:05 [c_banda_atr_regimen] CIERRE HYPE timeout bruto +0.75% neto +0.25%
- 2026-10-02 12:05 [c_banda_atr_evento] CIERRE HYPE timeout bruto +0.75% neto +0.25%
- 2026-10-02 12:05 [estocastico_rebote] CIERRE TAO stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 12:05 [c_banda_atr] CIERRE UNI stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 12:05 [c_banda_atr_regimen] CIERRE UNI stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 12:05 [c_banda_atr_evento] CIERRE UNI stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 12:05 [ruptura_volumen] CIERRE ONDO stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 12:05 [ruptura_volumen_regimen] CIERRE ONDO stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 12:05 [ruptura_volumen_evento] CIERRE ONDO stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 12:05 [macd_momentum] CIERRE NIGHT take-profit bruto +2.00% neto +1.50%
- 2026-10-02 12:05 [macd_sin_salida] CIERRE NIGHT take-profit bruto +2.00% neto +1.50%
- 2026-10-02 12:05 [macd_momentum_regimen] CIERRE NIGHT take-profit bruto +2.00% neto +1.50%
- 2026-10-02 12:05 [macd_momentum_evento] CIERRE NIGHT take-profit bruto +2.00% neto +1.50%
- 2026-10-02 12:05 [pullback_tendencia] CIERRE BCH rotura de tendencia bruto -0.58% neto -1.08%
- 2026-10-02 12:00 [estocastico_rebote] ENTRADA FIL @ 0.917 (21.98 €, apertura)
- 2026-10-02 12:05 [c_banda_atr] CIERRE BNB timeout bruto +0.41% neto -0.09%
- 2026-10-02 12:05 [c_banda_atr_regimen] CIERRE BNB timeout bruto +0.41% neto -0.09%
- 2026-10-02 12:05 [c_banda_atr_evento] CIERRE BNB timeout bruto +0.41% neto -0.09%
- 2026-10-02 12:05 [pullback_tendencia] CIERRE SEI rotura de tendencia bruto -0.62% neto -1.12%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
