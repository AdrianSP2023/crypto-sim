# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 00:16 UTC · vueltas 175 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 898.62 € (-2.77%) | 81 | 24 | 27% | -0.386% | -1.208% | -1.356% | -22.44 € |
| reversion_bb | 917.89 € (-0.69%) | 18 | 13 | 28% | -0.444% | -1.544% | -1.649% | -6.41 € |
| ruptura_volumen | 900.23 € (-2.60%) | 117 | 6 | 22% | -0.156% | -0.879% | -1.007% | -23.54 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 904.78 € (-2.11%) | 92 | 1 | 23% | -0.140% | -0.923% | -1.043% | -19.46 € |
| macd_momentum | 882.97 € (-4.47%) | 230 | 3 | 15% | -0.174% | -0.787% | -0.899% | -41.07 € |
| estocastico_rebote | 891.79 € (-3.51%) | 163 | 14 | 33% | -0.168% | -0.828% | -0.948% | -30.88 € |
| ruptura_estricta | 907.98 € (-1.76%) | 51 | 6 | 25% | -0.313% | -1.325% | -1.459% | -15.53 € |
| macd_sin_salida | 895.31 € (-3.13%) | 136 | 10 | 26% | -0.196% | -0.888% | -1.012% | -27.57 € |
| c_banda_atr_tope | 912.59 € (-1.26%) | 29 | 5 | 21% | -0.560% | -1.660% | -1.808% | -11.08 € |
| ruptura_volumen_tope | 913.09 € (-1.21%) | 40 | 3 | 15% | -0.097% | -1.197% | -1.319% | -11.01 € |
| c_banda_atr_regimen | 901.54 € (-2.46%) | 61 | 15 | 26% | -0.470% | -1.397% | -1.535% | -19.59 € |
| macd_momentum_regimen | 887.23 € (-4.00%) | 193 | 0 | 15% | -0.209% | -0.844% | -0.956% | -37.01 € |
| ruptura_volumen_regimen | 903.78 € (-2.21%) | 95 | 5 | 22% | -0.136% | -0.911% | -1.039% | -19.83 € |
| c_banda_atr_evento | 902.58 € (-2.34%) | 49 | 24 | 20% | -0.683% | -1.642% | -1.802% | -18.47 € |
| macd_momentum_evento | 895.38 € (-3.12%) | 110 | 3 | 8% | -0.400% | -1.140% | -1.248% | -28.65 € |
| ruptura_volumen_evento | 905.77 € (-2.00%) | 58 | 6 | 12% | -0.395% | -1.350% | -1.481% | -17.99 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 00:15 | ruptura_volumen_evento | DASH | stop-loss | -1.46% | -1.96% | -0.45 |
| 2026-09-30 00:15 | ruptura_volumen_evento | QNT | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 00:15 | c_banda_atr_evento | CRV | stop-loss | -1.67% | -2.17% | -0.49 |
| 2026-09-30 00:15 | ruptura_volumen_regimen | DASH | stop-loss | -1.46% | -1.96% | -0.44 |
| 2026-09-30 00:15 | c_banda_atr_regimen | CRV | stop-loss | -1.67% | -2.17% | -0.49 |
| 2026-09-30 00:15 | ruptura_volumen_tope | XLM | stop-loss | -1.46% | -2.56% | -0.59 |
| 2026-09-30 00:15 | ruptura_volumen_tope | QNT | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-30 00:15 | macd_sin_salida | AAVE | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 00:15 | ruptura_estricta | SPX | timeout | -1.08% | -1.58% | -0.36 |
| 2026-09-30 00:15 | ruptura_volumen | DASH | stop-loss | -1.46% | -1.96% | -0.44 |
| 2026-09-30 00:15 | ruptura_volumen | QNT | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 00:15 | c_banda_atr | CRV | stop-loss | -1.67% | -2.17% | -0.49 |
| 2026-09-30 00:10 | c_banda_atr_evento | LTC | stop-loss | -1.50% | -2.30% | -0.53 |
| 2026-09-30 00:10 | c_banda_atr_regimen | LTC | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 00:10 | macd_sin_salida | SHIB | timeout | +0.02% | -0.48% | -0.11 |

## Eventos de la última vuelta

- 2026-09-30 00:15 [ruptura_volumen] CIERRE QNT stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 00:15 [ruptura_volumen_tope] CIERRE QNT stop-loss bruto -1.20% neto -2.30%
- 2026-09-30 00:15 [ruptura_volumen_evento] CIERRE QNT stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 00:15 [ruptura_volumen_tope] CIERRE XLM stop-loss bruto -1.46% neto -2.56%
- 2026-09-30 00:15 [macd_sin_salida] CIERRE AAVE stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 00:15 [c_banda_atr] CIERRE CRV stop-loss bruto -1.67% neto -2.17%
- 2026-09-30 00:15 [c_banda_atr_regimen] CIERRE CRV stop-loss bruto -1.67% neto -2.17%
- 2026-09-30 00:15 [c_banda_atr_evento] CIERRE CRV stop-loss bruto -1.67% neto -2.17%
- 2026-09-30 00:15 [ruptura_volumen] CIERRE DASH stop-loss bruto -1.46% neto -1.96%
- 2026-09-30 00:15 [ruptura_volumen_regimen] CIERRE DASH stop-loss bruto -1.46% neto -1.96%
- 2026-09-30 00:15 [ruptura_volumen_evento] CIERRE DASH stop-loss bruto -1.46% neto -1.96%
- 2026-09-30 00:10 [macd_momentum] ENTRADA SHIB @ 5.088e-06 (22.08 €, apertura)
- 2026-09-30 00:10 [macd_momentum_evento] ENTRADA SHIB @ 5.088e-06 (22.39 €, apertura)
- 2026-09-30 00:10 [c_banda_atr] ENTRADA ASTER @ 0.64169 (22.54 €, apertura)
- 2026-09-30 00:10 [estocastico_rebote] ENTRADA ASTER @ 0.64169 (22.33 €, apertura)
- 2026-09-30 00:10 [c_banda_atr_evento] ENTRADA ASTER @ 0.64169 (22.64 €, apertura)
- 2026-09-30 00:15 [ruptura_estricta] CIERRE SPX timeout bruto -1.08% neto -1.58%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
