# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 05:41 UTC · vueltas 403 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 889.70 € (-3.74%) | 322 | 14 | 39% | +0.113% | -0.469% | -0.589% | -34.39 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.382% | -4.66 € |
| ruptura_volumen | 864.44 € (-6.47%) | 377 | 29 | 27% | -0.112% | -0.682% | -0.791% | -57.73 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 889.91 € (-3.71%) | 214 | 11 | 19% | -0.078% | -0.702% | -0.789% | -34.12 € |
| macd_momentum | 856.71 € (-7.31%) | 616 | 7 | 23% | +0.047% | -0.495% | -0.596% | -68.03 € |
| estocastico_rebote | 878.22 € (-4.98%) | 376 | 7 | 36% | +0.024% | -0.546% | -0.655% | -46.48 € |
| ruptura_estricta | 884.47 € (-4.30%) | 202 | 32 | 33% | -0.201% | -0.832% | -0.947% | -38.34 € |
| macd_sin_salida | 880.68 € (-4.71%) | 412 | 19 | 40% | +0.105% | -0.459% | -0.569% | -43.08 € |
| c_banda_atr_tope | 912.42 € (-1.28%) | 71 | 5 | 34% | +0.148% | -0.724% | -0.833% | -11.81 € |
| ruptura_volumen_tope | 902.60 € (-2.34%) | 120 | 4 | 26% | -0.063% | -0.783% | -0.898% | -21.49 € |
| c_banda_atr_regimen | 902.58 € (-2.34%) | 175 | 13 | 39% | +0.118% | -0.532% | -0.660% | -21.42 € |
| macd_momentum_regimen | 879.65 € (-4.82%) | 379 | 7 | 22% | +0.042% | -0.526% | -0.629% | -45.09 € |
| ruptura_volumen_regimen | 869.13 € (-5.96%) | 300 | 29 | 24% | -0.198% | -0.785% | -0.899% | -53.02 € |
| c_banda_atr_evento | 895.62 € (-3.10%) | 289 | 14 | 40% | +0.161% | -0.431% | -0.546% | -28.47 € |
| macd_momentum_evento | 861.46 € (-6.79%) | 569 | 7 | 21% | +0.049% | -0.498% | -0.595% | -63.29 € |
| ruptura_volumen_evento | 876.74 € (-5.14%) | 327 | 29 | 28% | -0.034% | -0.615% | -0.718% | -45.39 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 05:40 | ruptura_volumen_evento | SUI | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 05:40 | macd_momentum_evento | SEI | momentum perdido | +0.03% | -0.47% | -0.10 |
| 2026-10-02 05:40 | macd_momentum_evento | WLD | momentum perdido | -1.05% | -1.55% | -0.33 |
| 2026-10-02 05:40 | ruptura_volumen_regimen | SUI | stop-loss | -1.20% | -1.70% | -0.37 |
| 2026-10-02 05:40 | macd_momentum_regimen | SEI | momentum perdido | +0.03% | -0.47% | -0.10 |
| 2026-10-02 05:40 | macd_momentum_regimen | WLD | momentum perdido | -1.05% | -1.55% | -0.34 |
| 2026-10-02 05:40 | ruptura_volumen_tope | SUI | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-02 05:40 | macd_sin_salida | KSM | timeout | +0.88% | +0.38% | +0.08 |
| 2026-10-02 05:40 | ruptura_estricta | FET | stop-loss | -2.00% | -2.50% | -0.55 |
| 2026-10-02 05:40 | estocastico_rebote | WLFI | timeout | +0.81% | +0.31% | +0.07 |
| 2026-10-02 05:40 | macd_momentum | SEI | momentum perdido | +0.03% | -0.47% | -0.10 |
| 2026-10-02 05:40 | macd_momentum | WLD | momentum perdido | -1.05% | -1.55% | -0.33 |
| 2026-10-02 05:40 | pullback_tendencia | FET | rotura de tendencia | -0.90% | -1.40% | -0.31 |
| 2026-10-02 05:40 | pullback_tendencia | SUI | rotura de tendencia | -1.34% | -1.84% | -0.41 |
| 2026-10-02 05:40 | pullback_tendencia | LINK | rotura de tendencia | +0.37% | -0.13% | -0.03 |

## Eventos de la última vuelta

- 2026-10-02 05:40 [pullback_tendencia] CIERRE ETH rotura de tendencia bruto -0.61% neto -1.11%
- 2026-10-02 05:40 [pullback_tendencia] CIERRE LINK rotura de tendencia bruto +0.37% neto -0.13%
- 2026-10-02 05:40 [ruptura_volumen] CIERRE SUI stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 05:40 [pullback_tendencia] CIERRE SUI rotura de tendencia bruto -1.34% neto -1.84%
- 2026-10-02 05:40 [ruptura_volumen_tope] CIERRE SUI stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 05:40 [ruptura_volumen_regimen] CIERRE SUI stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 05:40 [ruptura_volumen_evento] CIERRE SUI stop-loss bruto -1.20% neto -1.70%
- 2026-10-02 05:40 [pullback_tendencia] CIERRE FET rotura de tendencia bruto -0.90% neto -1.40%
- 2026-10-02 05:40 [ruptura_estricta] CIERRE FET stop-loss bruto -2.00% neto -2.50%
- 2026-10-02 05:35 [pullback_tendencia] ENTRADA ALGO @ 0.11271 (22.25 €, apertura)
- 2026-10-02 05:40 [macd_momentum] CIERRE WLD momentum perdido bruto -1.05% neto -1.55%
- 2026-10-02 05:40 [macd_momentum_regimen] CIERRE WLD momentum perdido bruto -1.05% neto -1.55%
- 2026-10-02 05:40 [macd_momentum_evento] CIERRE WLD momentum perdido bruto -1.05% neto -1.55%
- 2026-10-02 05:35 [pullback_tendencia] ENTRADA NIGHT @ 0.03538 (22.25 €, apertura)
- 2026-10-02 05:35 [pullback_tendencia] ENTRADA OP @ 0.1175 (22.25 €, apertura)
- 2026-10-02 05:35 [macd_momentum] ENTRADA FIL @ 0.919 (21.41 €, apertura)
- 2026-10-02 05:35 [macd_sin_salida] ENTRADA FIL @ 0.919 (22.03 €, apertura)
- 2026-10-02 05:35 [macd_momentum_regimen] ENTRADA FIL @ 0.919 (21.98 €, apertura)
- 2026-10-02 05:35 [macd_momentum_evento] ENTRADA FIL @ 0.919 (21.53 €, apertura)
- 2026-10-02 05:35 [ruptura_volumen] ENTRADA ASTER @ 0.6666 (21.66 €, apertura)
- 2026-10-02 05:35 [ruptura_estricta] ENTRADA ASTER @ 0.6666 (22.15 €, apertura)
- 2026-10-02 05:35 [ruptura_volumen_tope] ENTRADA ASTER @ 0.6666 (22.57 €, apertura)
- 2026-10-02 05:35 [ruptura_volumen_regimen] ENTRADA ASTER @ 0.6666 (21.78 €, apertura)
- 2026-10-02 05:35 [ruptura_volumen_evento] ENTRADA ASTER @ 0.6666 (21.97 €, apertura)
- 2026-10-02 05:40 [estocastico_rebote] CIERRE WLFI timeout bruto +0.81% neto +0.31%
- 2026-10-02 05:40 [macd_sin_salida] CIERRE KSM timeout bruto +0.88% neto +0.38%
- 2026-10-02 05:40 [macd_momentum] CIERRE SEI momentum perdido bruto +0.03% neto -0.47%
- 2026-10-02 05:40 [macd_momentum_regimen] CIERRE SEI momentum perdido bruto +0.03% neto -0.47%
- 2026-10-02 05:40 [macd_momentum_evento] CIERRE SEI momentum perdido bruto +0.03% neto -0.47%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
