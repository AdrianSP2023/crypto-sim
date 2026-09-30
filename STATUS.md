# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 01:21 UTC · vueltas 188 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 903.50 € (-2.24%) | 92 | 25 | 27% | -0.343% | -1.127% | -1.271% | -23.78 € |
| reversion_bb | 919.62 € (-0.50%) | 25 | 9 | 48% | +0.128% | -0.972% | -1.069% | -5.61 € |
| ruptura_volumen | 900.23 € (-2.60%) | 124 | 11 | 23% | -0.141% | -0.852% | -0.977% | -24.16 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 905.16 € (-2.06%) | 94 | 4 | 23% | -0.131% | -0.909% | -1.029% | -19.57 € |
| macd_momentum | 885.65 € (-4.17%) | 235 | 20 | 16% | -0.148% | -0.759% | -0.871% | -40.46 € |
| estocastico_rebote | 894.19 € (-3.25%) | 176 | 8 | 34% | -0.122% | -0.770% | -0.902% | -30.98 € |
| ruptura_estricta | 909.01 € (-1.65%) | 55 | 8 | 27% | -0.215% | -1.189% | -1.324% | -15.04 € |
| macd_sin_salida | 898.22 € (-2.82%) | 146 | 17 | 28% | -0.149% | -0.828% | -0.951% | -27.61 € |
| c_banda_atr_tope | 912.68 € (-1.25%) | 29 | 5 | 21% | -0.560% | -1.660% | -1.808% | -11.08 € |
| ruptura_volumen_tope | 913.20 € (-1.19%) | 43 | 5 | 19% | -0.011% | -1.104% | -1.222% | -10.92 € |
| c_banda_atr_regimen | 903.02 € (-2.30%) | 68 | 8 | 24% | -0.518% | -1.401% | -1.535% | -21.87 € |
| macd_momentum_regimen | 887.23 € (-4.00%) | 193 | 0 | 15% | -0.209% | -0.844% | -0.956% | -37.01 € |
| ruptura_volumen_regimen | 903.34 € (-2.26%) | 100 | 0 | 21% | -0.152% | -0.913% | -1.039% | -20.91 € |
| c_banda_atr_evento | 907.00 € (-1.87%) | 60 | 25 | 22% | -0.564% | -1.474% | -1.625% | -20.30 € |
| macd_momentum_evento | 898.10 € (-2.83%) | 115 | 20 | 10% | -0.337% | -1.067% | -1.174% | -28.03 € |
| ruptura_volumen_evento | 905.78 € (-2.00%) | 65 | 11 | 14% | -0.341% | -1.247% | -1.372% | -18.61 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 01:20 | c_banda_atr_evento | BCH | timeout | -0.21% | -1.01% | -0.23 |
| 2026-09-30 01:20 | c_banda_atr | BCH | timeout | -0.21% | -0.71% | -0.16 |
| 2026-09-30 01:15 | ruptura_volumen_evento | BNB | timeout | +0.02% | -0.48% | -0.11 |
| 2026-09-30 01:15 | ruptura_volumen_evento | ZRO | take-profit | +2.50% | +2.00% | +0.45 |
| 2026-09-30 01:15 | macd_momentum_evento | ZRO | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 01:15 | c_banda_atr_evento | WLD | take-profit | +2.26% | +1.76% | +0.40 |
| 2026-09-30 01:15 | ruptura_volumen_regimen | BNB | timeout | +0.02% | -0.48% | -0.11 |
| 2026-09-30 01:15 | ruptura_volumen_regimen | PEPE | timeout | -0.45% | -0.95% | -0.21 |
| 2026-09-30 01:15 | ruptura_volumen_tope | ZRO | take-profit | +2.50% | +1.70% | +0.39 |
| 2026-09-30 01:15 | macd_sin_salida | ZRO | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-09-30 01:15 | ruptura_estricta | ASTER | take-profit | +3.00% | +2.50% | +0.57 |
| 2026-09-30 01:15 | ruptura_estricta | XLM | timeout | -1.20% | -1.70% | -0.39 |
| 2026-09-30 01:15 | estocastico_rebote | PENGU | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-09-30 01:15 | estocastico_rebote | QNT | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-09-30 01:15 | macd_momentum | ZRO | take-profit | +2.00% | +1.50% | +0.33 |

## Eventos de la última vuelta

- 2026-09-30 01:15 [macd_momentum] ENTRADA QNT @ 240.68 (22.09 €, apertura)
- 2026-09-30 01:15 [macd_sin_salida] ENTRADA QNT @ 240.68 (22.42 €, apertura)
- 2026-09-30 01:15 [macd_momentum_evento] ENTRADA QNT @ 240.68 (22.41 €, apertura)
- 2026-09-30 01:15 [ruptura_volumen] ENTRADA SUI @ 1.032 (22.50 €, apertura)
- 2026-09-30 01:15 [ruptura_estricta] ENTRADA SUI @ 1.032 (22.73 €, apertura)
- 2026-09-30 01:15 [ruptura_volumen_evento] ENTRADA SUI @ 1.032 (22.64 €, apertura)
- 2026-09-30 01:20 [c_banda_atr] CIERRE BCH timeout bruto -0.21% neto -0.71%
- 2026-09-30 01:20 [c_banda_atr_evento] CIERRE BCH timeout bruto -0.21% neto -1.01%
- 2026-09-30 01:15 [ruptura_estricta] ENTRADA WLD @ 0.4396 (22.73 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
