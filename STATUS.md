# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 04:56 UTC · vueltas 394 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 892.87 € (-3.39%) | 317 | 18 | 39% | +0.114% | -0.469% | -0.588% | -33.88 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.382% | -4.66 € |
| ruptura_volumen | 872.76 € (-5.57%) | 360 | 39 | 26% | -0.137% | -0.710% | -0.818% | -57.42 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 892.82 € (-3.40%) | 208 | 9 | 19% | -0.088% | -0.715% | -0.802% | -33.79 € |
| macd_momentum | 864.77 € (-6.43%) | 581 | 38 | 23% | +0.054% | -0.491% | -0.592% | -63.77 € |
| estocastico_rebote | 879.75 € (-4.81%) | 372 | 10 | 35% | +0.021% | -0.549% | -0.658% | -46.28 € |
| ruptura_estricta | 891.82 € (-3.51%) | 190 | 37 | 31% | -0.235% | -0.874% | -0.990% | -37.89 € |
| macd_sin_salida | 885.17 € (-4.23%) | 402 | 25 | 40% | +0.097% | -0.468% | -0.577% | -42.91 € |
| c_banda_atr_tope | 912.96 € (-1.22%) | 70 | 5 | 33% | +0.134% | -0.743% | -0.854% | -11.95 € |
| ruptura_volumen_tope | 904.04 € (-2.19%) | 117 | 5 | 26% | -0.045% | -0.771% | -0.885% | -20.64 € |
| c_banda_atr_regimen | 905.36 € (-2.04%) | 170 | 17 | 39% | +0.120% | -0.534% | -0.661% | -20.90 € |
| macd_momentum_regimen | 887.93 € (-3.93%) | 344 | 38 | 22% | +0.054% | -0.522% | -0.625% | -40.71 € |
| ruptura_volumen_regimen | 877.50 € (-5.06%) | 283 | 39 | 22% | -0.234% | -0.827% | -0.940% | -52.72 € |
| c_banda_atr_evento | 898.81 € (-2.75%) | 284 | 18 | 40% | +0.163% | -0.430% | -0.545% | -27.95 € |
| macd_momentum_evento | 869.57 € (-5.92%) | 534 | 38 | 21% | +0.056% | -0.493% | -0.591% | -59.00 € |
| ruptura_volumen_evento | 885.18 € (-4.23%) | 310 | 39 | 26% | -0.059% | -0.644% | -0.745% | -45.08 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 04:55 | ruptura_volumen_evento | TRUMP | timeout | +1.47% | +0.97% | +0.21 |
| 2026-10-02 04:55 | ruptura_volumen_evento | KSM | timeout | +1.53% | +1.03% | +0.23 |
| 2026-10-02 04:55 | ruptura_volumen_regimen | TRUMP | timeout | +1.47% | +0.97% | +0.21 |
| 2026-10-02 04:55 | ruptura_volumen_regimen | KSM | timeout | +1.53% | +1.03% | +0.23 |
| 2026-10-02 04:55 | macd_sin_salida | JUP | take-profit | +2.17% | +1.68% | +0.36 |
| 2026-10-02 04:55 | ruptura_estricta | AAVE | take-profit | +3.00% | +2.50% | +0.55 |
| 2026-10-02 04:55 | ruptura_estricta | ETH | timeout | +0.89% | +0.39% | +0.09 |
| 2026-10-02 04:55 | estocastico_rebote | TRUMP | take-profit | +1.80% | +1.30% | +0.28 |
| 2026-10-02 04:55 | estocastico_rebote | AVAX | take-profit | +1.80% | +1.30% | +0.28 |
| 2026-10-02 04:55 | ruptura_volumen | TRUMP | timeout | +1.47% | +0.97% | +0.21 |
| 2026-10-02 04:55 | ruptura_volumen | KSM | timeout | +1.53% | +1.03% | +0.22 |
| 2026-10-02 04:50 | ruptura_volumen_evento | HBAR | timeout | +0.95% | +0.45% | +0.10 |
| 2026-10-02 04:50 | macd_momentum_evento | UNI | take-profit | +2.00% | +1.50% | +0.32 |
| 2026-10-02 04:50 | macd_momentum_evento | SOL | take-profit | +2.00% | +1.50% | +0.32 |
| 2026-10-02 04:50 | c_banda_atr_evento | APT | take-profit | +2.00% | +1.50% | +0.34 |

## Eventos de la última vuelta

- 2026-10-02 04:55 [ruptura_estricta] CIERRE ETH timeout bruto +0.89% neto +0.39%
- 2026-10-02 04:55 [estocastico_rebote] CIERRE AVAX take-profit bruto +1.80% neto +1.30%
- 2026-10-02 04:55 [ruptura_estricta] CIERRE AAVE take-profit bruto +3.00% neto +2.50%
- 2026-10-02 04:50 [ruptura_volumen] ENTRADA XLM @ 0.198692 (21.66 €, apertura)
- 2026-10-02 04:50 [ruptura_volumen_regimen] ENTRADA XLM @ 0.198692 (21.78 €, apertura)
- 2026-10-02 04:50 [ruptura_volumen_evento] ENTRADA XLM @ 0.198692 (21.97 €, apertura)
- 2026-10-02 04:50 [ruptura_estricta] ENTRADA USELESS @ 0.22454 (22.16 €, apertura)
- 2026-10-02 04:50 [ruptura_volumen] ENTRADA JUP @ 0.30298 (21.66 €, apertura)
- 2026-10-02 04:50 [ruptura_estricta] ENTRADA JUP @ 0.30298 (22.16 €, apertura)
- 2026-10-02 04:55 [macd_sin_salida] CIERRE JUP take-profit bruto +2.18% neto +1.68%
- 2026-10-02 04:50 [ruptura_volumen_regimen] ENTRADA JUP @ 0.30298 (21.78 €, apertura)
- 2026-10-02 04:50 [ruptura_volumen_evento] ENTRADA JUP @ 0.30298 (21.97 €, apertura)
- 2026-10-02 04:50 [ruptura_estricta] ENTRADA INJ @ 6.792 (22.16 €, apertura)
- 2026-10-02 04:55 [ruptura_volumen] CIERRE KSM timeout bruto +1.54% neto +1.04%
- 2026-10-02 04:55 [ruptura_volumen_regimen] CIERRE KSM timeout bruto +1.54% neto +1.04%
- 2026-10-02 04:55 [ruptura_volumen_evento] CIERRE KSM timeout bruto +1.54% neto +1.04%
- 2026-10-02 04:55 [ruptura_volumen] CIERRE TRUMP timeout bruto +1.47% neto +0.97%
- 2026-10-02 04:55 [estocastico_rebote] CIERRE TRUMP take-profit bruto +1.80% neto +1.30%
- 2026-10-02 04:55 [ruptura_volumen_regimen] CIERRE TRUMP timeout bruto +1.47% neto +0.97%
- 2026-10-02 04:55 [ruptura_volumen_evento] CIERRE TRUMP timeout bruto +1.47% neto +0.97%
- 2026-10-02 04:50 [ruptura_estricta] ENTRADA KAS @ 0.03796 (22.16 €, apertura)
- 2026-10-02 04:50 [ruptura_volumen] ENTRADA APT @ 0.7296 (21.67 €, apertura)
- 2026-10-02 04:50 [macd_momentum] ENTRADA APT @ 0.7296 (21.51 €, apertura)
- 2026-10-02 04:50 [ruptura_estricta] ENTRADA APT @ 0.7296 (22.16 €, apertura)
- 2026-10-02 04:50 [macd_sin_salida] ENTRADA APT @ 0.7296 (22.03 €, apertura)
- 2026-10-02 04:50 [macd_momentum_regimen] ENTRADA APT @ 0.7296 (22.09 €, apertura)
- 2026-10-02 04:50 [ruptura_volumen_regimen] ENTRADA APT @ 0.7296 (21.79 €, apertura)
- 2026-10-02 04:50 [macd_momentum_evento] ENTRADA APT @ 0.7296 (21.63 €, apertura)
- 2026-10-02 04:50 [ruptura_volumen_evento] ENTRADA APT @ 0.7296 (21.98 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
