# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 00:21 UTC · vueltas 339 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 885.57 € (-4.18%) | 272 | 20 | 34% | -0.047% | -0.643% | -0.765% | -39.74 € |
| reversion_bb | 918.64 € (-0.61%) | 53 | 16 | 51% | +0.343% | -0.650% | -0.747% | -7.94 € |
| ruptura_volumen | 872.60 € (-5.59%) | 297 | 16 | 25% | -0.199% | -0.787% | -0.895% | -52.64 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 888.58 € (-3.86%) | 189 | 5 | 15% | -0.199% | -0.839% | -0.928% | -35.99 € |
| macd_momentum | 864.15 € (-6.50%) | 491 | 13 | 20% | -0.007% | -0.560% | -0.663% | -61.58 € |
| estocastico_rebote | 873.42 € (-5.50%) | 331 | 13 | 31% | -0.115% | -0.694% | -0.804% | -51.84 € |
| ruptura_estricta | 882.96 € (-4.47%) | 166 | 1 | 25% | -0.434% | -1.093% | -1.208% | -41.27 € |
| macd_sin_salida | 872.47 € (-5.60%) | 348 | 15 | 34% | -0.097% | -0.672% | -0.783% | -52.84 € |
| c_banda_atr_tope | 911.70 € (-1.36%) | 61 | 5 | 30% | +0.002% | -0.931% | -1.047% | -13.04 € |
| ruptura_volumen_tope | 905.97 € (-1.98%) | 101 | 5 | 27% | -0.042% | -0.803% | -0.919% | -18.58 € |
| c_banda_atr_regimen | 895.81 € (-3.08%) | 138 | 1 | 29% | -0.213% | -0.902% | -1.036% | -28.48 € |
| macd_momentum_regimen | 885.30 € (-4.21%) | 276 | 2 | 20% | -0.029% | -0.623% | -0.729% | -39.01 € |
| ruptura_volumen_regimen | 875.38 € (-5.29%) | 230 | 10 | 20% | -0.338% | -0.951% | -1.066% | -49.41 € |
| c_banda_atr_evento | 891.46 € (-3.55%) | 239 | 20 | 34% | -0.011% | -0.622% | -0.738% | -33.85 € |
| macd_momentum_evento | 868.94 € (-5.98%) | 444 | 13 | 19% | -0.011% | -0.570% | -0.670% | -56.80 € |
| ruptura_volumen_evento | 885.02 € (-4.24%) | 247 | 16 | 26% | -0.112% | -0.719% | -0.819% | -40.23 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 00:20 | macd_momentum_evento | SKY | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 00:20 | c_banda_atr_evento | SKY | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 00:20 | macd_sin_salida | SKY | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 00:20 | estocastico_rebote | JUP | take-profit | +1.80% | +1.30% | +0.28 |
| 2026-10-02 00:20 | estocastico_rebote | AVAX | timeout | +0.13% | -0.37% | -0.08 |
| 2026-10-02 00:20 | macd_momentum | SKY | take-profit | +2.00% | +1.50% | +0.32 |
| 2026-10-02 00:20 | reversion_bb | OP | take-profit | +1.69% | +1.19% | +0.27 |
| 2026-10-02 00:20 | c_banda_atr | SKY | take-profit | +2.00% | +1.50% | +0.33 |
| 2026-10-02 00:15 | estocastico_rebote | FET | take-profit | +2.08% | +1.58% | +0.34 |
| 2026-10-02 00:10 | c_banda_atr_evento | DASH | timeout | -0.87% | -1.37% | -0.31 |
| 2026-10-02 00:10 | pullback_tendencia | AAVE | rotura de tendencia | +0.18% | -0.32% | -0.07 |
| 2026-10-02 00:10 | c_banda_atr | DASH | timeout | -0.87% | -1.37% | -0.30 |
| 2026-10-02 00:05 | macd_momentum_evento | PUMP | momentum perdido | -0.10% | -0.60% | -0.13 |
| 2026-10-02 00:05 | c_banda_atr_evento | APT | timeout | -0.86% | -1.36% | -0.30 |
| 2026-10-02 00:05 | c_banda_atr_evento | FIL | timeout | -0.22% | -0.72% | -0.16 |

## Eventos de la última vuelta

- 2026-10-02 00:15 [macd_sin_salida] ENTRADA ETH @ 2405.21 (21.78 €, apertura)
- 2026-10-02 00:15 [macd_momentum_regimen] ENTRADA ETH @ 2405.21 (22.13 €, apertura)
- 2026-10-02 00:15 [macd_sin_salida] ENTRADA SOL @ 105.32 (21.78 €, apertura)
- 2026-10-02 00:15 [macd_momentum_regimen] ENTRADA SOL @ 105.32 (22.13 €, apertura)
- 2026-10-02 00:20 [estocastico_rebote] CIERRE AVAX timeout bruto +0.13% neto -0.37%
- 2026-10-02 00:15 [ruptura_volumen] ENTRADA TAO @ 271.028 (21.79 €, apertura)
- 2026-10-02 00:15 [ruptura_volumen_regimen] ENTRADA TAO @ 271.028 (21.87 €, apertura)
- 2026-10-02 00:15 [ruptura_volumen_evento] ENTRADA TAO @ 271.028 (22.10 €, apertura)
- 2026-10-02 00:15 [ruptura_volumen] ENTRADA FET @ 0.2064 (21.79 €, apertura)
- 2026-10-02 00:15 [ruptura_volumen_regimen] ENTRADA FET @ 0.2064 (21.87 €, apertura)
- 2026-10-02 00:15 [ruptura_volumen_evento] ENTRADA FET @ 0.2064 (22.10 €, apertura)
- 2026-10-02 00:15 [estocastico_rebote] ENTRADA TRX @ 0.297215 (21.80 €, apertura)
- 2026-10-02 00:15 [ruptura_volumen] ENTRADA XDC @ 0.03064 (21.79 €, apertura)
- 2026-10-02 00:15 [ruptura_volumen_regimen] ENTRADA XDC @ 0.03064 (21.87 €, apertura)
- 2026-10-02 00:15 [ruptura_volumen_evento] ENTRADA XDC @ 0.03064 (22.10 €, apertura)
- 2026-10-02 00:20 [estocastico_rebote] CIERRE JUP take-profit bruto +1.80% neto +1.30%
- 2026-10-02 00:15 [ruptura_volumen] ENTRADA INJ @ 6.605 (21.79 €, apertura)
- 2026-10-02 00:15 [ruptura_volumen_regimen] ENTRADA INJ @ 6.605 (21.87 €, apertura)
- 2026-10-02 00:15 [ruptura_volumen_evento] ENTRADA INJ @ 6.605 (22.10 €, apertura)
- 2026-10-02 00:20 [reversion_bb] CIERRE OP take-profit bruto +1.69% neto +1.19%
- 2026-10-02 00:15 [ruptura_volumen_regimen] ENTRADA TRUMP @ 1.843 (21.87 €, apertura)
- 2026-10-02 00:20 [c_banda_atr] CIERRE SKY take-profit bruto +2.00% neto +1.50%
- 2026-10-02 00:20 [macd_momentum] CIERRE SKY take-profit bruto +2.00% neto +1.50%
- 2026-10-02 00:20 [macd_sin_salida] CIERRE SKY take-profit bruto +2.00% neto +1.50%
- 2026-10-02 00:20 [c_banda_atr_evento] CIERRE SKY take-profit bruto +2.00% neto +1.50%
- 2026-10-02 00:20 [macd_momentum_evento] CIERRE SKY take-profit bruto +2.00% neto +1.50%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
