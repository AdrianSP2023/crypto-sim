# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 14:16 UTC · vueltas 420 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 881.97 € (-4.57%) | 384 | 19 | 39% | +0.116% | -0.452% | -0.573% | -39.43 € |
| reversion_bb | 919.70 € (-0.49%) | 74 | 3 | 62% | +0.594% | -0.259% | -0.363% | -4.43 € |
| ruptura_volumen | 852.69 € (-7.74%) | 484 | 13 | 26% | -0.099% | -0.653% | -0.763% | -70.47 € |
| rebote_extremo | 922.62 € (-0.17%) | 16 | 0 | 62% | +0.663% | -0.437% | -0.608% | -1.62 € |
| pullback_tendencia | 881.21 € (-4.66%) | 297 | 2 | 19% | -0.050% | -0.639% | -0.724% | -42.91 € |
| macd_momentum | 838.64 € (-9.26%) | 800 | 4 | 23% | +0.049% | -0.484% | -0.584% | -85.47 € |
| estocastico_rebote | 872.69 € (-5.58%) | 479 | 16 | 37% | +0.093% | -0.461% | -0.567% | -49.92 € |
| ruptura_estricta | 878.25 € (-4.98%) | 259 | 17 | 32% | -0.120% | -0.722% | -0.837% | -42.50 € |
| macd_sin_salida | 868.63 € (-6.02%) | 518 | 20 | 39% | +0.101% | -0.450% | -0.558% | -52.71 € |
| c_banda_atr_tope | 912.12 € (-1.31%) | 85 | 4 | 38% | +0.237% | -0.573% | -0.693% | -11.21 € |
| ruptura_volumen_tope | 897.93 € (-2.85%) | 147 | 1 | 22% | -0.108% | -0.787% | -0.903% | -26.40 € |
| c_banda_atr_regimen | 894.34 € (-3.23%) | 237 | 18 | 40% | +0.108% | -0.502% | -0.631% | -27.27 € |
| macd_momentum_regimen | 861.10 € (-6.83%) | 563 | 4 | 23% | +0.046% | -0.500% | -0.600% | -62.99 € |
| ruptura_volumen_regimen | 857.32 € (-7.24%) | 407 | 13 | 24% | -0.159% | -0.724% | -0.838% | -65.84 € |
| c_banda_atr_evento | 893.31 € (-3.35%) | 341 | 2 | 41% | +0.184% | -0.393% | -0.508% | -30.62 € |
| macd_momentum_evento | 851.50 € (-7.87%) | 700 | 0 | 23% | +0.070% | -0.468% | -0.564% | -72.75 € |
| ruptura_volumen_evento | 867.09 € (-6.18%) | 414 | 1 | 26% | -0.052% | -0.616% | -0.719% | -57.21 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 14:15 | ruptura_volumen_regimen | POL | timeout | +0.21% | -0.29% | -0.06 |
| 2026-10-02 14:15 | ruptura_volumen_regimen | ICP | timeout | +0.38% | -0.12% | -0.03 |
| 2026-10-02 14:15 | ruptura_volumen_regimen | UNI | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 14:15 | ruptura_volumen_regimen | TAO | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 14:15 | macd_momentum_regimen | ALGO | momentum perdido | -0.76% | -1.26% | -0.27 |
| 2026-10-02 14:15 | c_banda_atr_regimen | ZEC | stop-loss | -1.56% | -2.06% | -0.47 |
| 2026-10-02 14:15 | ruptura_volumen_tope | POL | timeout | +0.21% | -0.29% | -0.06 |
| 2026-10-02 14:15 | ruptura_volumen_tope | ICP | timeout | +0.38% | -0.12% | -0.03 |
| 2026-10-02 14:15 | ruptura_volumen_tope | TAO | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-02 14:15 | macd_sin_salida | SPX | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-02 14:15 | macd_sin_salida | ETH | timeout | -0.92% | -1.42% | -0.31 |
| 2026-10-02 14:15 | ruptura_estricta | ZRO | take-profit | +3.00% | +2.50% | +0.55 |
| 2026-10-02 14:15 | estocastico_rebote | USELESS | stop-loss | -1.59% | -2.10% | -0.46 |
| 2026-10-02 14:15 | estocastico_rebote | HBAR | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-02 14:15 | macd_momentum | ALGO | momentum perdido | -0.76% | -1.26% | -0.27 |

## Eventos de la última vuelta

- 2026-10-02 14:15 [macd_sin_salida] CIERRE ETH timeout bruto -0.91% neto -1.41%
- 2026-10-02 14:15 [estocastico_rebote] CIERRE HBAR stop-loss bruto -1.50% neto -2.00%
- 2026-10-02 14:15 [c_banda_atr] CIERRE ZEC stop-loss bruto -1.56% neto -2.06%
- 2026-10-02 14:15 [c_banda_atr_regimen] CIERRE ZEC stop-loss bruto -1.56% neto -2.06%
- 2026-10-02 14:15 [ruptura_volumen] CIERRE TAO stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 14:15 [ruptura_volumen_tope] CIERRE TAO stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 14:15 [ruptura_volumen_regimen] CIERRE TAO stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 14:15 [ruptura_volumen] CIERRE UNI stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 14:15 [ruptura_volumen_regimen] CIERRE UNI stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 14:10 [ruptura_volumen] ENTRADA ZRO @ 1.732 (21.35 €, apertura)
- 2026-10-02 14:15 [ruptura_estricta] CIERRE ZRO take-profit bruto +3.00% neto +2.50%
- 2026-10-02 14:10 [ruptura_volumen_tope] ENTRADA ZRO @ 1.732 (22.45 €, apertura)
- 2026-10-02 14:10 [ruptura_volumen_regimen] ENTRADA ZRO @ 1.732 (21.46 €, apertura)
- 2026-10-02 14:10 [ruptura_volumen_evento] ENTRADA ZRO @ 1.732 (21.68 €, apertura)
- 2026-10-02 14:15 [ruptura_volumen] CIERRE ICP timeout bruto +0.38% neto -0.12%
- 2026-10-02 14:15 [ruptura_volumen_tope] CIERRE ICP timeout bruto +0.38% neto -0.12%
- 2026-10-02 14:15 [ruptura_volumen_regimen] CIERRE ICP timeout bruto +0.38% neto -0.12%
- 2026-10-02 14:15 [ruptura_volumen] CIERRE POL timeout bruto +0.21% neto -0.29%
- 2026-10-02 14:10 [estocastico_rebote] ENTRADA POL @ 0.09842 (21.87 €, apertura)
- 2026-10-02 14:15 [ruptura_volumen_tope] CIERRE POL timeout bruto +0.21% neto -0.29%
- 2026-10-02 14:15 [ruptura_volumen_regimen] CIERRE POL timeout bruto +0.21% neto -0.29%
- 2026-10-02 14:15 [macd_momentum] CIERRE ALGO momentum perdido bruto -0.76% neto -1.26%
- 2026-10-02 14:15 [macd_momentum_regimen] CIERRE ALGO momentum perdido bruto -0.76% neto -1.26%
- 2026-10-02 14:15 [estocastico_rebote] CIERRE USELESS stop-loss bruto -1.60% neto -2.10%
- 2026-10-02 14:10 [estocastico_rebote] ENTRADA DASH @ 53.017 (21.86 €, apertura)
- 2026-10-02 14:10 [estocastico_rebote] ENTRADA BNB @ 693.54 (21.86 €, apertura)
- 2026-10-02 14:10 [reversion_bb] ENTRADA SEI @ 0.06333 (23.00 €, apertura)
- 2026-10-02 14:15 [macd_sin_salida] CIERRE SPX stop-loss bruto -1.50% neto -2.00%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
