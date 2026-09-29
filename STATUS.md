# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 20:46 UTC · vueltas 133 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 909.33 € (-1.61%) | 60 | 15 | 33% | -0.204% | -1.139% | -1.283% | -15.74 € |
| reversion_bb | 918.96 € (-0.57%) | 15 | 4 | 33% | -0.498% | -1.598% | -1.717% | -5.53 € |
| ruptura_volumen | 905.26 € (-2.05%) | 96 | 11 | 25% | -0.095% | -0.867% | -0.998% | -19.08 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 906.96 € (-1.87%) | 76 | 1 | 24% | -0.160% | -1.004% | -1.122% | -17.50 € |
| macd_momentum | 897.55 € (-2.89%) | 160 | 20 | 21% | -0.068% | -0.731% | -0.851% | -26.75 € |
| estocastico_rebote | 894.88 € (-3.18%) | 150 | 9 | 31% | -0.212% | -0.886% | -1.006% | -30.39 € |
| ruptura_estricta | 911.84 € (-1.34%) | 44 | 4 | 30% | -0.193% | -1.280% | -1.414% | -12.97 € |
| macd_sin_salida | 904.45 € (-2.14%) | 103 | 23 | 32% | -0.081% | -0.835% | -0.965% | -19.72 € |
| c_banda_atr_tope | 915.47 € (-0.95%) | 24 | 5 | 25% | -0.585% | -1.685% | -1.845% | -9.32 € |
| ruptura_volumen_tope | 916.92 € (-0.79%) | 29 | 5 | 17% | -0.023% | -1.123% | -1.246% | -7.51 € |
| c_banda_atr_regimen | 908.81 € (-1.67%) | 52 | 10 | 31% | -0.275% | -1.277% | -1.415% | -15.31 € |
| macd_momentum_regimen | 897.67 € (-2.87%) | 151 | 18 | 19% | -0.090% | -0.763% | -0.879% | -26.34 € |
| ruptura_volumen_regimen | 907.30 € (-1.83%) | 83 | 6 | 25% | -0.088% | -0.902% | -1.036% | -17.20 € |
| c_banda_atr_evento | 914.65 € (-1.04%) | 28 | 15 | 29% | -0.516% | -1.616% | -1.777% | -10.43 € |
| macd_momentum_evento | 911.06 € (-1.43%) | 40 | 20 | 18% | -0.373% | -1.436% | -1.567% | -13.24 € |
| ruptura_volumen_evento | 911.80 € (-1.35%) | 37 | 11 | 16% | -0.372% | -1.472% | -1.611% | -12.54 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 20:45 | ruptura_volumen_evento | SHIB | timeout | -0.63% | -1.73% | -0.40 |
| 2026-09-29 20:45 | ruptura_volumen_evento | ICP | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-29 20:45 | ruptura_volumen_evento | DOGE | timeout | -0.11% | -1.21% | -0.28 |
| 2026-09-29 20:45 | ruptura_volumen_evento | SUI | timeout | +0.60% | -0.50% | -0.12 |
| 2026-09-29 20:45 | ruptura_volumen_evento | ADA | timeout | -0.13% | -1.23% | -0.28 |
| 2026-09-29 20:45 | ruptura_volumen_evento | SOL | timeout | -0.07% | -1.17% | -0.27 |
| 2026-09-29 20:45 | macd_momentum_evento | SEI | momentum perdido | +0.00% | -0.50% | -0.11 |
| 2026-09-29 20:45 | macd_momentum_evento | VIRTUAL | stop-loss | -1.50% | -2.30% | -0.52 |
| 2026-09-29 20:45 | c_banda_atr_evento | VIRTUAL | stop-loss | -1.50% | -2.60% | -0.59 |
| 2026-09-29 20:45 | ruptura_volumen_regimen | SHIB | timeout | -0.63% | -1.13% | -0.26 |
| 2026-09-29 20:45 | ruptura_volumen_regimen | ATOM | timeout | -0.23% | -0.73% | -0.17 |
| 2026-09-29 20:45 | ruptura_volumen_regimen | DOGE | timeout | -0.11% | -0.61% | -0.14 |
| 2026-09-29 20:45 | ruptura_volumen_regimen | UNI | timeout | +0.09% | -0.41% | -0.09 |
| 2026-09-29 20:45 | ruptura_volumen_regimen | SUI | timeout | +0.60% | +0.10% | +0.02 |
| 2026-09-29 20:45 | ruptura_volumen_regimen | ADA | timeout | -0.13% | -0.63% | -0.14 |

## Eventos de la última vuelta

- 2026-09-29 20:45 [ruptura_volumen] CIERRE SOL timeout bruto -0.07% neto -0.57%
- 2026-09-29 20:45 [ruptura_volumen_regimen] CIERRE SOL timeout bruto -0.07% neto -0.57%
- 2026-09-29 20:45 [ruptura_volumen_evento] CIERRE SOL timeout bruto -0.07% neto -1.17%
- 2026-09-29 20:45 [ruptura_volumen] CIERRE ADA timeout bruto -0.13% neto -0.63%
- 2026-09-29 20:45 [ruptura_volumen_regimen] CIERRE ADA timeout bruto -0.13% neto -0.63%
- 2026-09-29 20:45 [ruptura_volumen_evento] CIERRE ADA timeout bruto -0.13% neto -1.23%
- 2026-09-29 20:45 [ruptura_volumen] CIERRE SUI timeout bruto +0.60% neto +0.10%
- 2026-09-29 20:45 [ruptura_volumen_regimen] CIERRE SUI timeout bruto +0.60% neto +0.10%
- 2026-09-29 20:45 [ruptura_volumen_evento] CIERRE SUI timeout bruto +0.60% neto -0.50%
- 2026-09-29 20:45 [ruptura_volumen_regimen] CIERRE UNI timeout bruto +0.09% neto -0.41%
- 2026-09-29 20:45 [ruptura_volumen] CIERRE DOGE timeout bruto -0.11% neto -0.61%
- 2026-09-29 20:45 [ruptura_volumen_regimen] CIERRE DOGE timeout bruto -0.11% neto -0.61%
- 2026-09-29 20:45 [ruptura_volumen_evento] CIERRE DOGE timeout bruto -0.11% neto -1.21%
- 2026-09-29 20:40 [macd_momentum] ENTRADA DASH @ 54.014 (22.45 €, apertura)
- 2026-09-29 20:40 [macd_sin_salida] ENTRADA DASH @ 54.014 (22.62 €, apertura)
- 2026-09-29 20:40 [macd_momentum_regimen] ENTRADA DASH @ 54.014 (22.46 €, apertura)
- 2026-09-29 20:40 [macd_momentum_evento] ENTRADA DASH @ 54.014 (22.79 €, apertura)
- 2026-09-29 20:40 [macd_momentum] ENTRADA ENA @ 0.2223 (22.45 €, apertura)
- 2026-09-29 20:40 [macd_sin_salida] ENTRADA ENA @ 0.2223 (22.62 €, apertura)
- 2026-09-29 20:40 [macd_momentum_regimen] ENTRADA ENA @ 0.2223 (22.46 €, apertura)
- 2026-09-29 20:40 [macd_momentum_evento] ENTRADA ENA @ 0.2223 (22.79 €, apertura)
- 2026-09-29 20:45 [ruptura_volumen] CIERRE ICP stop-loss bruto -1.20% neto -1.70%
- 2026-09-29 20:45 [ruptura_volumen_evento] CIERRE ICP stop-loss bruto -1.20% neto -2.30%
- 2026-09-29 20:45 [ruptura_volumen_regimen] CIERRE ATOM timeout bruto -0.23% neto -0.73%
- 2026-09-29 20:45 [c_banda_atr] CIERRE VIRTUAL stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 20:45 [macd_momentum] CIERRE VIRTUAL stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 20:45 [macd_sin_salida] CIERRE VIRTUAL stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 20:45 [macd_momentum_regimen] CIERRE VIRTUAL stop-loss bruto -1.50% neto -2.00%
- 2026-09-29 20:45 [c_banda_atr_evento] CIERRE VIRTUAL stop-loss bruto -1.50% neto -2.60%
- 2026-09-29 20:45 [macd_momentum_evento] CIERRE VIRTUAL stop-loss bruto -1.50% neto -2.30%
- 2026-09-29 20:45 [macd_momentum] CIERRE SEI momentum perdido bruto +0.00% neto -0.50%
- 2026-09-29 20:45 [macd_momentum_regimen] CIERRE SEI momentum perdido bruto +0.00% neto -0.50%
- 2026-09-29 20:45 [macd_momentum_evento] CIERRE SEI momentum perdido bruto +0.00% neto -0.50%
- 2026-09-29 20:40 [macd_momentum] ENTRADA OP @ 0.1154 (22.44 €, apertura)
- 2026-09-29 20:40 [macd_sin_salida] ENTRADA OP @ 0.1154 (22.61 €, apertura)
- 2026-09-29 20:40 [macd_momentum_regimen] ENTRADA OP @ 0.1154 (22.45 €, apertura)
- 2026-09-29 20:40 [macd_momentum_evento] ENTRADA OP @ 0.1154 (22.78 €, apertura)
- 2026-09-29 20:45 [ruptura_volumen] CIERRE SHIB timeout bruto -0.63% neto -1.13%
- 2026-09-29 20:45 [ruptura_volumen_regimen] CIERRE SHIB timeout bruto -0.63% neto -1.13%
- 2026-09-29 20:45 [ruptura_volumen_evento] CIERRE SHIB timeout bruto -0.63% neto -1.73%
- 2026-09-29 20:45 [macd_sin_salida] CIERRE ASTER timeout bruto +0.44% neto -0.06%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
