# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 10:26 UTC · vueltas 414 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 888.78 € (-3.84%) | 343 | 26 | 40% | +0.140% | -0.436% | -0.555% | -34.09 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.381% | -4.66 € |
| ruptura_volumen | 857.63 € (-7.21%) | 444 | 9 | 26% | -0.107% | -0.666% | -0.773% | -66.07 € |
| rebote_extremo | 922.42 € (-0.20%) | 15 | 0 | 60% | +0.574% | -0.526% | -0.706% | -1.82 € |
| pullback_tendencia | 889.68 € (-3.74%) | 250 | 8 | 21% | -0.013% | -0.619% | -0.705% | -35.13 € |
| macd_momentum | 850.31 € (-8.00%) | 700 | 18 | 23% | +0.059% | -0.479% | -0.580% | -74.43 € |
| estocastico_rebote | 878.97 € (-4.90%) | 425 | 36 | 38% | +0.106% | -0.455% | -0.562% | -43.91 € |
| ruptura_estricta | 881.26 € (-4.65%) | 238 | 15 | 32% | -0.140% | -0.751% | -0.868% | -40.72 € |
| macd_sin_salida | 877.90 € (-5.01%) | 453 | 36 | 40% | +0.107% | -0.451% | -0.561% | -46.41 € |
| c_banda_atr_tope | 913.15 € (-1.20%) | 77 | 5 | 38% | +0.227% | -0.616% | -0.732% | -10.91 € |
| ruptura_volumen_tope | 900.01 € (-2.62%) | 133 | 5 | 23% | -0.101% | -0.800% | -0.912% | -24.29 € |
| c_banda_atr_regimen | 901.43 € (-2.47%) | 196 | 25 | 41% | +0.156% | -0.477% | -0.604% | -21.52 € |
| macd_momentum_regimen | 873.08 € (-5.54%) | 463 | 18 | 24% | +0.061% | -0.496% | -0.598% | -51.65 € |
| ruptura_volumen_regimen | 862.28 € (-6.70%) | 367 | 9 | 24% | -0.175% | -0.747% | -0.859% | -61.41 € |
| c_banda_atr_evento | 894.70 € (-3.20%) | 310 | 26 | 41% | +0.188% | -0.397% | -0.512% | -28.17 € |
| macd_momentum_evento | 855.02 € (-7.49%) | 653 | 18 | 23% | +0.061% | -0.480% | -0.578% | -69.72 € |
| ruptura_volumen_evento | 869.83 € (-5.89%) | 394 | 9 | 27% | -0.041% | -0.608% | -0.710% | -53.85 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 10:25 | ruptura_volumen_evento | INJ | timeout | -0.68% | -1.18% | -0.26 |
| 2026-10-02 10:25 | macd_momentum_evento | KSM | momentum perdido | -0.65% | -1.15% | -0.25 |
| 2026-10-02 10:25 | macd_momentum_evento | WLD | momentum perdido | -0.19% | -0.69% | -0.15 |
| 2026-10-02 10:25 | macd_momentum_evento | SUI | momentum perdido | -0.97% | -1.47% | -0.32 |
| 2026-10-02 10:25 | ruptura_volumen_regimen | INJ | timeout | -0.68% | -1.18% | -0.26 |
| 2026-10-02 10:25 | macd_momentum_regimen | KSM | momentum perdido | -0.65% | -1.15% | -0.25 |
| 2026-10-02 10:25 | macd_momentum_regimen | WLD | momentum perdido | -0.19% | -0.69% | -0.15 |
| 2026-10-02 10:25 | macd_momentum_regimen | SUI | momentum perdido | -0.97% | -1.47% | -0.32 |
| 2026-10-02 10:25 | macd_momentum | KSM | momentum perdido | -0.65% | -1.15% | -0.25 |
| 2026-10-02 10:25 | macd_momentum | WLD | momentum perdido | -0.19% | -0.69% | -0.15 |
| 2026-10-02 10:25 | macd_momentum | SUI | momentum perdido | -0.97% | -1.47% | -0.31 |
| 2026-10-02 10:25 | pullback_tendencia | ETH | rotura de tendencia | -0.28% | -0.78% | -0.17 |
| 2026-10-02 10:25 | ruptura_volumen | INJ | timeout | -0.68% | -1.18% | -0.26 |
| 2026-10-02 10:20 | ruptura_volumen_evento | TRUMP | timeout | +0.96% | +0.46% | +0.10 |
| 2026-10-02 10:20 | ruptura_volumen_evento | FIL | timeout | -0.97% | -1.47% | -0.32 |

## Eventos de la última vuelta

- 2026-10-02 10:25 [pullback_tendencia] CIERRE ETH rotura de tendencia bruto -0.28% neto -0.78%
- 2026-10-02 10:25 [macd_momentum] CIERRE SUI momentum perdido bruto -0.97% neto -1.47%
- 2026-10-02 10:25 [macd_momentum_regimen] CIERRE SUI momentum perdido bruto -0.97% neto -1.47%
- 2026-10-02 10:25 [macd_momentum_evento] CIERRE SUI momentum perdido bruto -0.97% neto -1.47%
- 2026-10-02 10:20 [ruptura_volumen] ENTRADA ZEC @ 1244.12 (21.46 €, apertura)
- 2026-10-02 10:20 [ruptura_estricta] ENTRADA ZEC @ 1244.12 (22.09 €, apertura)
- 2026-10-02 10:20 [ruptura_volumen_tope] ENTRADA ZEC @ 1244.12 (22.50 €, apertura)
- 2026-10-02 10:20 [ruptura_volumen_regimen] ENTRADA ZEC @ 1244.12 (21.58 €, apertura)
- 2026-10-02 10:20 [ruptura_volumen_evento] ENTRADA ZEC @ 1244.12 (21.77 €, apertura)
- 2026-10-02 10:25 [macd_momentum] CIERRE WLD momentum perdido bruto -0.19% neto -0.69%
- 2026-10-02 10:25 [macd_momentum_regimen] CIERRE WLD momentum perdido bruto -0.19% neto -0.69%
- 2026-10-02 10:25 [macd_momentum_evento] CIERRE WLD momentum perdido bruto -0.19% neto -0.69%
- 2026-10-02 10:20 [pullback_tendencia] ENTRADA NIGHT @ 0.03923 (22.23 €, apertura)
- 2026-10-02 10:25 [ruptura_volumen] CIERRE INJ timeout bruto -0.68% neto -1.18%
- 2026-10-02 10:25 [ruptura_volumen_regimen] CIERRE INJ timeout bruto -0.68% neto -1.18%
- 2026-10-02 10:25 [ruptura_volumen_evento] CIERRE INJ timeout bruto -0.68% neto -1.18%
- 2026-10-02 10:25 [macd_momentum] CIERRE KSM momentum perdido bruto -0.65% neto -1.15%
- 2026-10-02 10:25 [macd_momentum_regimen] CIERRE KSM momentum perdido bruto -0.65% neto -1.15%
- 2026-10-02 10:25 [macd_momentum_evento] CIERRE KSM momentum perdido bruto -0.65% neto -1.15%
- 2026-10-02 10:20 [estocastico_rebote] ENTRADA APT @ 0.7313 (22.01 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
