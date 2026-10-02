# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 08:21 UTC · vueltas 389 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 893.08 € (-3.37%) | 334 | 24 | 40% | +0.128% | -0.450% | -0.570% | -34.25 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 864.91 € (-6.42%) | 416 | 15 | 27% | -0.096% | -0.659% | -0.768% | -61.42 € |
| rebote_extremo | 922.42 € (-0.20%) | 15 | 0 | 60% | +0.574% | -0.526% | -0.706% | -1.82 € |
| pullback_tendencia | 890.59 € (-3.64%) | 238 | 8 | 21% | -0.027% | -0.638% | -0.725% | -34.51 € |
| macd_momentum | 858.35 € (-7.13%) | 648 | 37 | 23% | +0.052% | -0.488% | -0.590% | -70.46 € |
| estocastico_rebote | 885.18 € (-4.23%) | 391 | 36 | 37% | +0.062% | -0.505% | -0.613% | -44.80 € |
| ruptura_estricta | 882.85 € (-4.48%) | 234 | 6 | 32% | -0.173% | -0.786% | -0.903% | -41.84 € |
| macd_sin_salida | 885.00 € (-4.25%) | 434 | 38 | 40% | +0.118% | -0.443% | -0.553% | -43.76 € |
| c_banda_atr_tope | 913.88 € (-1.12%) | 76 | 5 | 37% | +0.213% | -0.634% | -0.750% | -11.08 € |
| ruptura_volumen_tope | 901.93 € (-2.41%) | 128 | 5 | 24% | -0.088% | -0.794% | -0.908% | -23.22 € |
| c_banda_atr_regimen | 905.52 € (-2.03%) | 186 | 24 | 40% | +0.138% | -0.502% | -0.631% | -21.50 € |
| macd_momentum_regimen | 881.33 € (-4.64%) | 411 | 37 | 22% | +0.050% | -0.513% | -0.617% | -47.58 € |
| ruptura_volumen_regimen | 869.61 € (-5.91%) | 339 | 15 | 24% | -0.168% | -0.745% | -0.859% | -56.74 € |
| c_banda_atr_evento | 899.02 € (-2.73%) | 301 | 24 | 41% | +0.176% | -0.411% | -0.528% | -28.33 € |
| macd_momentum_evento | 863.10 € (-6.61%) | 601 | 37 | 21% | +0.054% | -0.490% | -0.589% | -65.73 € |
| ruptura_volumen_evento | 877.22 € (-5.09%) | 366 | 15 | 28% | -0.024% | -0.596% | -0.700% | -49.14 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 08:20 | macd_momentum_evento | CRV | take-profit | +2.13% | +1.63% | +0.35 |
| 2026-10-02 08:20 | c_banda_atr_evento | ETH | timeout | +1.53% | +1.03% | +0.23 |
| 2026-10-02 08:20 | macd_momentum_regimen | CRV | take-profit | +2.13% | +1.63% | +0.36 |
| 2026-10-02 08:20 | c_banda_atr_regimen | ETH | timeout | +1.53% | +1.03% | +0.23 |
| 2026-10-02 08:20 | macd_sin_salida | WLFI | timeout | +0.00% | -0.50% | -0.11 |
| 2026-10-02 08:20 | macd_sin_salida | CRV | take-profit | +2.19% | +1.69% | +0.37 |
| 2026-10-02 08:20 | ruptura_estricta | WLFI | timeout | +0.00% | -0.50% | -0.11 |
| 2026-10-02 08:20 | estocastico_rebote | SPX | take-profit | +1.88% | +1.38% | +0.30 |
| 2026-10-02 08:20 | estocastico_rebote | APT | take-profit | +1.80% | +1.30% | +0.28 |
| 2026-10-02 08:20 | macd_momentum | CRV | take-profit | +2.13% | +1.63% | +0.35 |
| 2026-10-02 08:20 | pullback_tendencia | PUMP | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 08:20 | c_banda_atr | ETH | timeout | +1.53% | +1.03% | +0.23 |
| 2026-10-02 08:15 | ruptura_volumen_evento | WLFI | timeout | -0.20% | -0.70% | -0.15 |
| 2026-10-02 08:15 | macd_momentum_evento | KSM | momentum perdido | -0.22% | -0.72% | -0.15 |
| 2026-10-02 08:15 | ruptura_volumen_regimen | WLFI | timeout | -0.20% | -0.70% | -0.15 |

## Eventos de la última vuelta

- 2026-10-02 08:20 [c_banda_atr] CIERRE ETH timeout bruto +1.53% neto +1.03%
- 2026-10-02 08:20 [c_banda_atr_regimen] CIERRE ETH timeout bruto +1.53% neto +1.03%
- 2026-10-02 08:20 [c_banda_atr_evento] CIERRE ETH timeout bruto +1.53% neto +1.03%
- 2026-10-02 08:20 [pullback_tendencia] CIERRE PUMP take-profit bruto +2.00% neto +1.50%
- 2026-10-02 08:20 [macd_momentum] CIERRE CRV take-profit bruto +2.13% neto +1.63%
- 2026-10-02 08:20 [macd_sin_salida] CIERRE CRV take-profit bruto +2.19% neto +1.69%
- 2026-10-02 08:20 [macd_momentum_regimen] CIERRE CRV take-profit bruto +2.13% neto +1.63%
- 2026-10-02 08:20 [macd_momentum_evento] CIERRE CRV take-profit bruto +2.13% neto +1.63%
- 2026-10-02 08:20 [ruptura_estricta] CIERRE WLFI timeout bruto +0.00% neto -0.50%
- 2026-10-02 08:20 [macd_sin_salida] CIERRE WLFI timeout bruto +0.00% neto -0.50%
- 2026-10-02 08:20 [estocastico_rebote] CIERRE APT take-profit bruto +1.80% neto +1.30%
- 2026-10-02 08:15 [ruptura_volumen] ENTRADA SPX @ 0.4059 (21.57 €, apertura)
- 2026-10-02 08:20 [estocastico_rebote] CIERRE SPX take-profit bruto +1.88% neto +1.38%
- 2026-10-02 08:15 [ruptura_volumen_tope] ENTRADA SPX @ 0.4059 (22.53 €, apertura)
- 2026-10-02 08:15 [ruptura_volumen_regimen] ENTRADA SPX @ 0.4059 (21.69 €, apertura)
- 2026-10-02 08:15 [ruptura_volumen_evento] ENTRADA SPX @ 0.4059 (21.88 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
