# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-02 05:26 UTC · vueltas 400 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 890.65 € (-3.63%) | 322 | 13 | 39% | +0.113% | -0.469% | -0.589% | -34.39 € |
| reversion_bb | 919.58 € (-0.50%) | 73 | 0 | 62% | +0.581% | -0.276% | -0.382% | -4.66 € |
| ruptura_volumen | 867.63 € (-6.13%) | 374 | 30 | 27% | -0.114% | -0.684% | -0.792% | -57.44 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 891.77 € (-3.51%) | 210 | 9 | 20% | -0.068% | -0.694% | -0.781% | -33.12 € |
| macd_momentum | 858.20 € (-7.15%) | 603 | 18 | 23% | +0.046% | -0.497% | -0.598% | -66.93 € |
| estocastico_rebote | 878.36 € (-4.96%) | 375 | 7 | 35% | +0.022% | -0.548% | -0.657% | -46.55 € |
| ruptura_estricta | 887.90 € (-3.93%) | 199 | 33 | 33% | -0.199% | -0.832% | -0.946% | -37.78 € |
| macd_sin_salida | 882.17 € (-4.55%) | 410 | 19 | 40% | +0.107% | -0.457% | -0.567% | -42.70 € |
| c_banda_atr_tope | 912.88 € (-1.23%) | 71 | 4 | 34% | +0.148% | -0.724% | -0.833% | -11.81 € |
| ruptura_volumen_tope | 903.23 € (-2.27%) | 118 | 4 | 26% | -0.043% | -0.767% | -0.882% | -20.70 € |
| c_banda_atr_regimen | 903.28 € (-2.27%) | 175 | 12 | 39% | +0.118% | -0.532% | -0.660% | -21.42 € |
| macd_momentum_regimen | 881.18 € (-4.66%) | 366 | 18 | 22% | +0.040% | -0.531% | -0.633% | -43.96 € |
| ruptura_volumen_regimen | 872.34 € (-5.62%) | 297 | 30 | 24% | -0.200% | -0.788% | -0.901% | -52.73 € |
| c_banda_atr_evento | 896.58 € (-2.99%) | 289 | 13 | 40% | +0.161% | -0.431% | -0.546% | -28.47 € |
| macd_momentum_evento | 862.96 € (-6.63%) | 556 | 18 | 21% | +0.047% | -0.500% | -0.598% | -62.19 € |
| ruptura_volumen_evento | 879.97 € (-4.79%) | 324 | 30 | 28% | -0.035% | -0.616% | -0.718% | -45.10 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-02 05:25 | ruptura_volumen_evento | XMR | timeout | +0.22% | -0.28% | -0.06 |
| 2026-10-02 05:25 | ruptura_volumen_evento | JUP | stop-loss | -2.06% | -2.56% | -0.56 |
| 2026-10-02 05:25 | ruptura_volumen_evento | CRV | stop-loss | -1.40% | -1.90% | -0.41 |
| 2026-10-02 05:25 | macd_momentum_evento | SKY | momentum perdido | -0.12% | -0.62% | -0.13 |
| 2026-10-02 05:25 | macd_momentum_evento | WLD | momentum perdido | +0.67% | +0.17% | +0.04 |
| 2026-10-02 05:25 | macd_momentum_evento | ONDO | momentum perdido | -0.03% | -0.53% | -0.11 |
| 2026-10-02 05:25 | macd_momentum_evento | POL | momentum perdido | -0.43% | -0.93% | -0.20 |
| 2026-10-02 05:25 | macd_momentum_evento | ARB | momentum perdido | -0.49% | -0.99% | -0.21 |
| 2026-10-02 05:25 | macd_momentum_evento | DOT | momentum perdido | -0.17% | -0.67% | -0.14 |
| 2026-10-02 05:25 | macd_momentum_evento | TAO | momentum perdido | -0.25% | -0.75% | -0.16 |
| 2026-10-02 05:25 | macd_momentum_evento | HBAR | momentum perdido | -0.64% | -1.14% | -0.25 |
| 2026-10-02 05:25 | macd_momentum_evento | AVAX | momentum perdido | +0.56% | +0.06% | +0.01 |
| 2026-10-02 05:25 | macd_momentum_evento | SUI | momentum perdido | -0.19% | -0.69% | -0.15 |
| 2026-10-02 05:25 | macd_momentum_evento | LINK | momentum perdido | -0.26% | -0.76% | -0.16 |
| 2026-10-02 05:25 | macd_momentum_evento | NEAR | momentum perdido | -0.57% | -1.07% | -0.23 |

## Eventos de la última vuelta

- 2026-10-02 05:20 [pullback_tendencia] ENTRADA ETH @ 2426.74 (22.28 €, apertura)
- 2026-10-02 05:25 [macd_momentum] CIERRE NEAR momentum perdido bruto -0.57% neto -1.07%
- 2026-10-02 05:25 [macd_momentum_regimen] CIERRE NEAR momentum perdido bruto -0.57% neto -1.07%
- 2026-10-02 05:25 [macd_momentum_evento] CIERRE NEAR momentum perdido bruto -0.57% neto -1.07%
- 2026-10-02 05:25 [macd_momentum] CIERRE LINK momentum perdido bruto -0.26% neto -0.76%
- 2026-10-02 05:25 [macd_momentum_regimen] CIERRE LINK momentum perdido bruto -0.26% neto -0.76%
- 2026-10-02 05:25 [macd_momentum_evento] CIERRE LINK momentum perdido bruto -0.26% neto -0.76%
- 2026-10-02 05:25 [macd_momentum] CIERRE SUI momentum perdido bruto -0.19% neto -0.69%
- 2026-10-02 05:25 [macd_momentum_regimen] CIERRE SUI momentum perdido bruto -0.19% neto -0.69%
- 2026-10-02 05:25 [macd_momentum_evento] CIERRE SUI momentum perdido bruto -0.19% neto -0.69%
- 2026-10-02 05:20 [pullback_tendencia] ENTRADA AVAX @ 9.872 (22.28 €, apertura)
- 2026-10-02 05:25 [macd_momentum] CIERRE AVAX momentum perdido bruto +0.56% neto +0.06%
- 2026-10-02 05:25 [macd_momentum_regimen] CIERRE AVAX momentum perdido bruto +0.56% neto +0.06%
- 2026-10-02 05:25 [macd_momentum_evento] CIERRE AVAX momentum perdido bruto +0.56% neto +0.06%
- 2026-10-02 05:25 [macd_momentum] CIERRE HBAR momentum perdido bruto -0.64% neto -1.14%
- 2026-10-02 05:25 [macd_momentum_regimen] CIERRE HBAR momentum perdido bruto -0.64% neto -1.14%
- 2026-10-02 05:25 [macd_momentum_evento] CIERRE HBAR momentum perdido bruto -0.64% neto -1.14%
- 2026-10-02 05:25 [macd_momentum] CIERRE TAO momentum perdido bruto -0.25% neto -0.75%
- 2026-10-02 05:25 [macd_momentum_regimen] CIERRE TAO momentum perdido bruto -0.25% neto -0.75%
- 2026-10-02 05:25 [macd_momentum_evento] CIERRE TAO momentum perdido bruto -0.25% neto -0.75%
- 2026-10-02 05:25 [estocastico_rebote] CIERRE LTC take-profit bruto +1.80% neto +1.30%
- 2026-10-02 05:25 [macd_momentum] CIERRE DOT momentum perdido bruto -0.17% neto -0.67%
- 2026-10-02 05:25 [macd_momentum_regimen] CIERRE DOT momentum perdido bruto -0.17% neto -0.67%
- 2026-10-02 05:25 [macd_momentum_evento] CIERRE DOT momentum perdido bruto -0.17% neto -0.67%
- 2026-10-02 05:25 [macd_momentum] CIERRE ARB momentum perdido bruto -0.49% neto -0.99%
- 2026-10-02 05:25 [macd_momentum_regimen] CIERRE ARB momentum perdido bruto -0.49% neto -0.99%
- 2026-10-02 05:25 [macd_momentum_evento] CIERRE ARB momentum perdido bruto -0.49% neto -0.99%
- 2026-10-02 05:25 [macd_momentum] CIERRE POL momentum perdido bruto -0.43% neto -0.93%
- 2026-10-02 05:25 [macd_momentum_regimen] CIERRE POL momentum perdido bruto -0.43% neto -0.93%
- 2026-10-02 05:25 [macd_momentum_evento] CIERRE POL momentum perdido bruto -0.43% neto -0.93%
- 2026-10-02 05:25 [macd_momentum] CIERRE ONDO momentum perdido bruto -0.02% neto -0.52%
- 2026-10-02 05:25 [macd_momentum_regimen] CIERRE ONDO momentum perdido bruto -0.02% neto -0.52%
- 2026-10-02 05:25 [macd_momentum_evento] CIERRE ONDO momentum perdido bruto -0.02% neto -0.52%
- 2026-10-02 05:25 [ruptura_volumen] CIERRE CRV stop-loss bruto -1.40% neto -1.90%
- 2026-10-02 05:25 [ruptura_volumen_regimen] CIERRE CRV stop-loss bruto -1.40% neto -1.90%
- 2026-10-02 05:25 [ruptura_volumen_evento] CIERRE CRV stop-loss bruto -1.40% neto -1.90%
- 2026-10-02 05:25 [macd_momentum] CIERRE WLD momentum perdido bruto +0.67% neto +0.17%
- 2026-10-02 05:25 [macd_momentum_regimen] CIERRE WLD momentum perdido bruto +0.67% neto +0.17%
- 2026-10-02 05:25 [macd_momentum_evento] CIERRE WLD momentum perdido bruto +0.67% neto +0.17%
- 2026-10-02 05:25 [ruptura_volumen] CIERRE JUP stop-loss bruto -2.06% neto -2.56%
- 2026-10-02 05:25 [ruptura_estricta] CIERRE JUP stop-loss bruto -2.06% neto -2.56%
- 2026-10-02 05:25 [ruptura_volumen_regimen] CIERRE JUP stop-loss bruto -2.06% neto -2.56%
- 2026-10-02 05:25 [ruptura_volumen_evento] CIERRE JUP stop-loss bruto -2.06% neto -2.56%
- 2026-10-02 05:20 [macd_momentum] ENTRADA WLFI @ 0.05 (21.44 €, apertura)
- 2026-10-02 05:20 [ruptura_estricta] ENTRADA WLFI @ 0.05 (22.16 €, apertura)
- 2026-10-02 05:20 [macd_sin_salida] ENTRADA WLFI @ 0.05 (22.04 €, apertura)
- 2026-10-02 05:20 [macd_momentum_regimen] ENTRADA WLFI @ 0.05 (22.01 €, apertura)
- 2026-10-02 05:20 [macd_momentum_evento] ENTRADA WLFI @ 0.05 (21.56 €, apertura)
- 2026-10-02 05:25 [macd_momentum] CIERRE SKY momentum perdido bruto -0.12% neto -0.62%
- 2026-10-02 05:25 [macd_momentum_regimen] CIERRE SKY momentum perdido bruto -0.12% neto -0.62%
- 2026-10-02 05:25 [macd_momentum_evento] CIERRE SKY momentum perdido bruto -0.12% neto -0.62%
- 2026-10-02 05:25 [ruptura_volumen] CIERRE XMR timeout bruto +0.22% neto -0.28%
- 2026-10-02 05:25 [ruptura_volumen_tope] CIERRE XMR timeout bruto +0.22% neto -0.28%
- 2026-10-02 05:25 [ruptura_volumen_regimen] CIERRE XMR timeout bruto +0.22% neto -0.28%
- 2026-10-02 05:25 [ruptura_volumen_evento] CIERRE XMR timeout bruto +0.22% neto -0.28%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
