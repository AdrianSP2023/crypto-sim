# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 09:51 UTC · vueltas 407 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 889.35 € (-3.78%) | 341 | 24 | 40% | +0.136% | -0.441% | -0.561% | -34.27 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 859.67 € (-6.99%) | 428 | 20 | 27% | -0.104% | -0.665% | -0.775% | -63.71 € |
| rebote_extremo | 922.42 € (-0.20%) | 15 | 0 | 60% | +0.574% | -0.526% | -0.706% | -1.82 € |
| pullback_tendencia | 889.66 € (-3.74%) | 246 | 9 | 20% | -0.028% | -0.635% | -0.722% | -35.48 € |
| macd_momentum | 851.54 € (-7.87%) | 691 | 12 | 23% | +0.061% | -0.477% | -0.578% | -73.29 € |
| estocastico_rebote | 879.42 € (-4.85%) | 420 | 30 | 37% | +0.088% | -0.474% | -0.581% | -45.17 € |
| ruptura_estricta | 882.00 € (-4.57%) | 237 | 12 | 32% | -0.154% | -0.765% | -0.882% | -41.27 € |
| macd_sin_salida | 879.48 € (-4.84%) | 448 | 32 | 40% | +0.106% | -0.452% | -0.562% | -46.03 € |
| c_banda_atr_tope | 913.40 € (-1.17%) | 77 | 5 | 38% | +0.227% | -0.616% | -0.732% | -10.91 € |
| ruptura_volumen_tope | 900.06 € (-2.62%) | 132 | 1 | 23% | -0.100% | -0.800% | -0.913% | -24.11 € |
| c_banda_atr_regimen | 901.96 € (-2.41%) | 193 | 24 | 40% | +0.146% | -0.489% | -0.617% | -21.72 € |
| macd_momentum_regimen | 874.34 € (-5.40%) | 454 | 12 | 24% | +0.064% | -0.494% | -0.595% | -50.48 € |
| ruptura_volumen_regimen | 864.33 € (-6.48%) | 351 | 20 | 24% | -0.175% | -0.749% | -0.864% | -59.04 € |
| c_banda_atr_evento | 895.26 € (-3.14%) | 308 | 24 | 41% | +0.183% | -0.402% | -0.518% | -28.35 € |
| macd_momentum_evento | 856.25 € (-7.36%) | 644 | 12 | 23% | +0.063% | -0.478% | -0.576% | -68.57 € |
| ruptura_volumen_evento | 871.90 € (-5.66%) | 378 | 20 | 28% | -0.035% | -0.605% | -0.709% | -51.46 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 09:50 | ruptura_volumen_evento | CRV | timeout | +0.32% | -0.18% | -0.04 |
| 2026-10-02 09:50 | ruptura_volumen_evento | DOT | timeout | -0.47% | -0.97% | -0.21 |
| 2026-10-02 09:50 | macd_momentum_evento | ZEC | momentum perdido | -0.45% | -0.95% | -0.20 |
| 2026-10-02 09:50 | ruptura_volumen_regimen | CRV | timeout | +0.32% | -0.18% | -0.04 |
| 2026-10-02 09:50 | ruptura_volumen_regimen | DOT | timeout | -0.47% | -0.97% | -0.21 |
| 2026-10-02 09:50 | macd_momentum_regimen | ZEC | momentum perdido | -0.45% | -0.95% | -0.21 |
| 2026-10-02 09:50 | ruptura_volumen_tope | CRV | timeout | +0.32% | -0.18% | -0.04 |
| 2026-10-02 09:50 | ruptura_volumen_tope | DOT | timeout | -0.47% | -0.97% | -0.22 |
| 2026-10-02 09:50 | macd_momentum | ZEC | momentum perdido | -0.45% | -0.95% | -0.20 |
| 2026-10-02 09:50 | ruptura_volumen | CRV | timeout | +0.32% | -0.18% | -0.04 |
| 2026-10-02 09:50 | ruptura_volumen | DOT | timeout | -0.47% | -0.97% | -0.21 |
| 2026-10-02 09:45 | ruptura_volumen_evento | OP | timeout | -0.51% | -1.01% | -0.22 |
| 2026-10-02 09:45 | ruptura_volumen_evento | USELESS | stop-loss | -1.36% | -1.86% | -0.41 |
| 2026-10-02 09:45 | macd_momentum_evento | ADA | momentum perdido | -0.23% | -0.73% | -0.16 |
| 2026-10-02 09:45 | ruptura_volumen_regimen | OP | timeout | -0.51% | -1.01% | -0.22 |

## Eventos de la última vuelta

- 2026-10-02 09:45 [macd_momentum] ENTRADA BTC @ 76751.7 (21.28 €, apertura)
- 2026-10-02 09:45 [macd_momentum_regimen] ENTRADA BTC @ 76751.7 (21.85 €, apertura)
- 2026-10-02 09:45 [macd_momentum_evento] ENTRADA BTC @ 76751.7 (21.40 €, apertura)
- 2026-10-02 09:45 [estocastico_rebote] ENTRADA ETH @ 2441.74 (21.98 €, apertura)
- 2026-10-02 09:45 [macd_momentum] ENTRADA AVAX @ 9.875 (21.28 €, apertura)
- 2026-10-02 09:45 [macd_momentum_regimen] ENTRADA AVAX @ 9.875 (21.85 €, apertura)
- 2026-10-02 09:45 [macd_momentum_evento] ENTRADA AVAX @ 9.875 (21.40 €, apertura)
- 2026-10-02 09:50 [macd_momentum] CIERRE ZEC momentum perdido bruto -0.45% neto -0.95%
- 2026-10-02 09:50 [macd_momentum_regimen] CIERRE ZEC momentum perdido bruto -0.45% neto -0.95%
- 2026-10-02 09:50 [macd_momentum_evento] CIERRE ZEC momentum perdido bruto -0.45% neto -0.95%
- 2026-10-02 09:50 [ruptura_volumen] CIERRE DOT timeout bruto -0.47% neto -0.97%
- 2026-10-02 09:50 [ruptura_volumen_tope] CIERRE DOT timeout bruto -0.47% neto -0.97%
- 2026-10-02 09:50 [ruptura_volumen_regimen] CIERRE DOT timeout bruto -0.47% neto -0.97%
- 2026-10-02 09:50 [ruptura_volumen_evento] CIERRE DOT timeout bruto -0.47% neto -0.97%
- 2026-10-02 09:50 [ruptura_volumen] CIERRE CRV timeout bruto +0.32% neto -0.18%
- 2026-10-02 09:45 [estocastico_rebote] ENTRADA CRV @ 0.33928 (21.98 €, apertura)
- 2026-10-02 09:50 [ruptura_volumen_tope] CIERRE CRV timeout bruto +0.32% neto -0.18%
- 2026-10-02 09:50 [ruptura_volumen_regimen] CIERRE CRV timeout bruto +0.32% neto -0.18%
- 2026-10-02 09:50 [ruptura_volumen_evento] CIERRE CRV timeout bruto +0.32% neto -0.18%
- 2026-10-02 09:45 [estocastico_rebote] ENTRADA USELESS @ 0.22232 (21.98 €, apertura)
- 2026-10-02 09:45 [estocastico_rebote] ENTRADA VVV @ 26.235 (21.98 €, apertura)
- 2026-10-02 09:45 [estocastico_rebote] ENTRADA BNB @ 689.18 (21.98 €, apertura)
- 2026-10-02 09:45 [estocastico_rebote] ENTRADA SPX @ 0.4001 (21.98 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
