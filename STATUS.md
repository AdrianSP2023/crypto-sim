# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 00:31 UTC · vueltas 341 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 885.82 € (-4.16%) | 272 | 21 | 34% | -0.047% | -0.643% | -0.765% | -39.74 € |
| reversion_bb | 918.69 € (-0.60%) | 53 | 16 | 51% | +0.343% | -0.650% | -0.747% | -7.94 € |
| ruptura_volumen | 872.55 € (-5.59%) | 297 | 27 | 25% | -0.199% | -0.787% | -0.895% | -52.64 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 888.39 € (-3.88%) | 190 | 5 | 15% | -0.201% | -0.840% | -0.929% | -36.21 € |
| macd_momentum | 864.10 € (-6.51%) | 491 | 15 | 20% | -0.007% | -0.560% | -0.663% | -61.58 € |
| estocastico_rebote | 873.08 € (-5.54%) | 333 | 14 | 31% | -0.107% | -0.686% | -0.795% | -51.52 € |
| ruptura_estricta | 882.97 € (-4.47%) | 166 | 5 | 25% | -0.434% | -1.093% | -1.208% | -41.27 € |
| macd_sin_salida | 872.39 € (-5.61%) | 348 | 17 | 34% | -0.097% | -0.672% | -0.783% | -52.84 € |
| c_banda_atr_tope | 911.70 € (-1.36%) | 61 | 5 | 30% | +0.002% | -0.931% | -1.047% | -13.04 € |
| ruptura_volumen_tope | 905.92 € (-1.98%) | 101 | 5 | 27% | -0.042% | -0.803% | -0.919% | -18.58 € |
| c_banda_atr_regimen | 895.77 € (-3.08%) | 138 | 4 | 29% | -0.213% | -0.902% | -1.036% | -28.48 € |
| macd_momentum_regimen | 885.34 € (-4.21%) | 276 | 4 | 20% | -0.029% | -0.623% | -0.729% | -39.01 € |
| ruptura_volumen_regimen | 875.38 € (-5.29%) | 230 | 22 | 20% | -0.338% | -0.951% | -1.066% | -49.41 € |
| c_banda_atr_evento | 891.72 € (-3.52%) | 239 | 21 | 34% | -0.011% | -0.622% | -0.738% | -33.85 € |
| macd_momentum_evento | 868.89 € (-5.99%) | 444 | 15 | 19% | -0.011% | -0.570% | -0.670% | -56.80 € |
| ruptura_volumen_evento | 884.96 € (-4.25%) | 247 | 27 | 26% | -0.112% | -0.719% | -0.819% | -40.23 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 00:30 | estocastico_rebote | USELESS | take-profit | +1.80% | +1.30% | +0.28 |
| 2026-10-02 00:30 | pullback_tendencia | PUMP | rotura de tendencia | -0.50% | -1.00% | -0.22 |
| 2026-10-02 00:25 | estocastico_rebote | ARB | timeout | +0.68% | +0.17% | +0.04 |
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

## Eventos de la última vuelta

- 2026-10-02 00:25 [ruptura_volumen] ENTRADA ADA @ 0.21914 (21.79 €, apertura)
- 2026-10-02 00:25 [ruptura_volumen_regimen] ENTRADA ADA @ 0.21914 (21.87 €, apertura)
- 2026-10-02 00:25 [ruptura_volumen_evento] ENTRADA ADA @ 0.21914 (22.10 €, apertura)
- 2026-10-02 00:25 [c_banda_atr_regimen] ENTRADA AAVE @ 153.38 (22.39 €, apertura)
- 2026-10-02 00:30 [pullback_tendencia] CIERRE PUMP rotura de tendencia bruto -0.50% neto -1.00%
- 2026-10-02 00:25 [ruptura_volumen] ENTRADA DOT @ 1.0494 (21.79 €, apertura)
- 2026-10-02 00:25 [ruptura_volumen_regimen] ENTRADA DOT @ 1.0494 (21.87 €, apertura)
- 2026-10-02 00:25 [ruptura_volumen_evento] ENTRADA DOT @ 1.0494 (22.10 €, apertura)
- 2026-10-02 00:25 [ruptura_volumen] ENTRADA CRV @ 0.3364 (21.79 €, apertura)
- 2026-10-02 00:25 [ruptura_volumen_regimen] ENTRADA CRV @ 0.3364 (21.87 €, apertura)
- 2026-10-02 00:25 [ruptura_volumen_evento] ENTRADA CRV @ 0.3364 (22.10 €, apertura)
- 2026-10-02 00:30 [estocastico_rebote] CIERRE USELESS take-profit bruto +1.80% neto +1.30%
- 2026-10-02 00:25 [ruptura_volumen] ENTRADA PEPE @ 3.946e-06 (21.79 €, apertura)
- 2026-10-02 00:25 [ruptura_volumen_regimen] ENTRADA PEPE @ 3.946e-06 (21.87 €, apertura)
- 2026-10-02 00:25 [ruptura_volumen_evento] ENTRADA PEPE @ 3.946e-06 (22.10 €, apertura)
- 2026-10-02 00:25 [macd_momentum] ENTRADA MINA @ 0.1356 (21.57 €, apertura)
- 2026-10-02 00:25 [macd_sin_salida] ENTRADA MINA @ 0.1356 (21.79 €, apertura)
- 2026-10-02 00:25 [macd_momentum_regimen] ENTRADA MINA @ 0.1356 (22.13 €, apertura)
- 2026-10-02 00:25 [macd_momentum_evento] ENTRADA MINA @ 0.1356 (21.69 €, apertura)
- 2026-10-02 00:25 [ruptura_volumen] ENTRADA KSM @ 4.55 (21.79 €, apertura)
- 2026-10-02 00:25 [ruptura_volumen_regimen] ENTRADA KSM @ 4.55 (21.87 €, apertura)
- 2026-10-02 00:25 [ruptura_volumen_evento] ENTRADA KSM @ 4.55 (22.10 €, apertura)
- 2026-10-02 00:25 [ruptura_volumen] ENTRADA BNB @ 686.43 (21.79 €, apertura)
- 2026-10-02 00:25 [ruptura_volumen_regimen] ENTRADA BNB @ 686.43 (21.87 €, apertura)
- 2026-10-02 00:25 [ruptura_volumen_evento] ENTRADA BNB @ 686.43 (22.10 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
