# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 14:21 UTC · vueltas 421 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 882.65 € (-4.50%) | 384 | 19 | 39% | +0.116% | -0.452% | -0.573% | -39.43 € |
| reversion_bb | 919.80 € (-0.48%) | 74 | 3 | 62% | +0.594% | -0.259% | -0.363% | -4.43 € |
| ruptura_volumen | 853.20 € (-7.69%) | 485 | 12 | 26% | -0.100% | -0.654% | -0.763% | -70.68 € |
| rebote_extremo | 922.62 € (-0.17%) | 16 | 0 | 62% | +0.663% | -0.437% | -0.608% | -1.62 € |
| pullback_tendencia | 881.43 € (-4.63%) | 297 | 3 | 19% | -0.050% | -0.639% | -0.724% | -42.91 € |
| macd_momentum | 838.54 € (-9.27%) | 802 | 2 | 23% | +0.049% | -0.483% | -0.583% | -85.59 € |
| estocastico_rebote | 873.25 € (-5.52%) | 480 | 22 | 37% | +0.090% | -0.464% | -0.570% | -50.37 € |
| ruptura_estricta | 878.47 € (-4.95%) | 260 | 16 | 32% | -0.127% | -0.729% | -0.845% | -43.07 € |
| macd_sin_salida | 869.23 € (-5.95%) | 518 | 20 | 39% | +0.101% | -0.450% | -0.558% | -52.71 € |
| c_banda_atr_tope | 912.15 € (-1.31%) | 85 | 4 | 38% | +0.237% | -0.573% | -0.693% | -11.21 € |
| ruptura_volumen_tope | 898.25 € (-2.81%) | 147 | 1 | 22% | -0.108% | -0.787% | -0.903% | -26.40 € |
| c_banda_atr_regimen | 894.95 € (-3.17%) | 237 | 18 | 40% | +0.108% | -0.502% | -0.631% | -27.27 € |
| macd_momentum_regimen | 860.99 € (-6.84%) | 565 | 2 | 23% | +0.047% | -0.500% | -0.600% | -63.11 € |
| ruptura_volumen_regimen | 857.83 € (-7.19%) | 408 | 12 | 24% | -0.160% | -0.724% | -0.838% | -66.06 € |
| c_banda_atr_evento | 893.34 € (-3.34%) | 341 | 2 | 41% | +0.184% | -0.393% | -0.508% | -30.62 € |
| macd_momentum_evento | 851.50 € (-7.87%) | 700 | 0 | 23% | +0.070% | -0.468% | -0.564% | -72.75 € |
| ruptura_volumen_evento | 867.41 € (-6.15%) | 414 | 1 | 26% | -0.052% | -0.616% | -0.719% | -57.21 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 14:20 | ruptura_volumen_regimen | BTC | timeout | -0.50% | -1.00% | -0.21 |
| 2026-10-02 14:20 | macd_momentum_regimen | FIL | momentum perdido | +1.30% | +0.80% | +0.17 |
| 2026-10-02 14:20 | macd_momentum_regimen | AAVE | momentum perdido | -0.87% | -1.37% | -0.30 |
| 2026-10-02 14:20 | ruptura_estricta | TRUMP | stop-loss | -2.10% | -2.60% | -0.57 |
| 2026-10-02 14:20 | estocastico_rebote | TRUMP | stop-loss | -1.55% | -2.05% | -0.45 |
| 2026-10-02 14:20 | macd_momentum | FIL | momentum perdido | +1.30% | +0.80% | +0.17 |
| 2026-10-02 14:20 | macd_momentum | AAVE | momentum perdido | -0.87% | -1.37% | -0.29 |
| 2026-10-02 14:20 | ruptura_volumen | BTC | timeout | -0.50% | -1.00% | -0.21 |
| 2026-10-02 14:15 | ruptura_volumen_regimen | POL | timeout | +0.21% | -0.29% | -0.06 |
| 2026-10-02 14:15 | ruptura_volumen_regimen | ICP | timeout | +0.38% | -0.12% | -0.03 |
| 2026-10-02 14:15 | ruptura_volumen_regimen | UNI | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 14:15 | ruptura_volumen_regimen | TAO | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 14:15 | macd_momentum_regimen | ALGO | momentum perdido | -0.76% | -1.26% | -0.27 |
| 2026-10-02 14:15 | c_banda_atr_regimen | ZEC | stop-loss | -1.56% | -2.06% | -0.47 |
| 2026-10-02 14:15 | ruptura_volumen_tope | POL | timeout | +0.21% | -0.29% | -0.06 |

## Eventos de la última vuelta

- 2026-10-02 14:20 [ruptura_volumen] CIERRE BTC timeout bruto -0.50% neto -1.00%
- 2026-10-02 14:20 [ruptura_volumen_regimen] CIERRE BTC timeout bruto -0.50% neto -1.00%
- 2026-10-02 14:15 [estocastico_rebote] ENTRADA ETH @ 2424.6 (21.86 €, apertura)
- 2026-10-02 14:15 [estocastico_rebote] ENTRADA ADA @ 0.225241 (21.86 €, apertura)
- 2026-10-02 14:20 [macd_momentum] CIERRE AAVE momentum perdido bruto -0.87% neto -1.37%
- 2026-10-02 14:20 [macd_momentum_regimen] CIERRE AAVE momentum perdido bruto -0.87% neto -1.37%
- 2026-10-02 14:15 [pullback_tendencia] ENTRADA PUMP @ 0.005359 (22.03 €, apertura)
- 2026-10-02 14:15 [estocastico_rebote] ENTRADA HYPE @ 79.93 (21.86 €, apertura)
- 2026-10-02 14:15 [estocastico_rebote] ENTRADA DOGE @ 0.0856581 (21.86 €, apertura)
- 2026-10-02 14:15 [estocastico_rebote] ENTRADA BCH @ 278.09 (21.86 €, apertura)
- 2026-10-02 14:15 [estocastico_rebote] ENTRADA INJ @ 6.611 (21.86 €, apertura)
- 2026-10-02 14:15 [estocastico_rebote] ENTRADA OP @ 0.1176 (21.86 €, apertura)
- 2026-10-02 14:20 [macd_momentum] CIERRE FIL momentum perdido bruto +1.30% neto +0.80%
- 2026-10-02 14:20 [macd_momentum_regimen] CIERRE FIL momentum perdido bruto +1.30% neto +0.80%
- 2026-10-02 14:20 [estocastico_rebote] CIERRE TRUMP stop-loss bruto -1.55% neto -2.05%
- 2026-10-02 14:20 [ruptura_estricta] CIERRE TRUMP stop-loss bruto -2.10% neto -2.60%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
