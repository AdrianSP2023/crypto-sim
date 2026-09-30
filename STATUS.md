# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 00:51 UTC · vueltas 182 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 898.65 € (-2.77%) | 89 | 23 | 26% | -0.400% | -1.194% | -1.337% | -24.35 € |
| reversion_bb | 918.12 € (-0.66%) | 20 | 13 | 35% | -0.250% | -1.350% | -1.448% | -6.23 € |
| ruptura_volumen | 899.92 € (-2.63%) | 119 | 8 | 22% | -0.177% | -0.896% | -1.024% | -24.38 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 904.84 € (-2.10%) | 94 | 1 | 23% | -0.131% | -0.909% | -1.029% | -19.57 € |
| macd_momentum | 882.65 € (-4.50%) | 232 | 12 | 15% | -0.176% | -0.789% | -0.900% | -41.49 € |
| estocastico_rebote | 892.42 € (-3.44%) | 171 | 11 | 33% | -0.156% | -0.808% | -0.926% | -31.59 € |
| ruptura_estricta | 908.66 € (-1.69%) | 53 | 5 | 26% | -0.257% | -1.249% | -1.386% | -15.22 € |
| macd_sin_salida | 895.38 € (-3.12%) | 138 | 16 | 27% | -0.198% | -0.888% | -1.011% | -27.97 € |
| c_banda_atr_tope | 912.60 € (-1.26%) | 29 | 5 | 21% | -0.560% | -1.660% | -1.808% | -11.08 € |
| ruptura_volumen_tope | 913.49 € (-1.16%) | 40 | 5 | 15% | -0.097% | -1.197% | -1.319% | -11.01 € |
| c_banda_atr_regimen | 900.95 € (-2.52%) | 68 | 8 | 24% | -0.518% | -1.401% | -1.535% | -21.87 € |
| macd_momentum_regimen | 887.23 € (-4.00%) | 193 | 0 | 15% | -0.209% | -0.844% | -0.956% | -37.01 € |
| ruptura_volumen_regimen | 903.50 € (-2.24%) | 96 | 4 | 22% | -0.151% | -0.922% | -1.053% | -20.29 € |
| c_banda_atr_evento | 902.19 € (-2.39%) | 57 | 23 | 19% | -0.664% | -1.591% | -1.742% | -20.81 € |
| macd_momentum_evento | 895.06 € (-3.16%) | 112 | 12 | 8% | -0.401% | -1.137% | -1.244% | -29.08 € |
| ruptura_volumen_evento | 905.46 € (-2.03%) | 60 | 8 | 12% | -0.428% | -1.368% | -1.499% | -18.83 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 00:50 | ruptura_volumen_evento | NEAR | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 00:50 | ruptura_estricta | BCH | timeout | -0.64% | -1.14% | -0.26 |
| 2026-09-30 00:50 | estocastico_rebote | INJ | timeout | -0.88% | -1.38% | -0.31 |
| 2026-09-30 00:50 | ruptura_volumen | NEAR | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 00:45 | c_banda_atr_evento | ASTER | take-profit | +2.14% | +1.64% | +0.37 |
| 2026-09-30 00:45 | estocastico_rebote | ASTER | take-profit | +2.14% | +1.64% | +0.37 |
| 2026-09-30 00:45 | c_banda_atr | ASTER | take-profit | +2.14% | +1.64% | +0.37 |
| 2026-09-30 00:40 | estocastico_rebote | TRX | timeout | -0.13% | -0.63% | -0.14 |
| 2026-09-30 00:40 | estocastico_rebote | ICP | timeout | +0.89% | +0.39% | +0.09 |
| 2026-09-30 00:40 | estocastico_rebote | DOT | timeout | +0.00% | -0.50% | -0.11 |
| 2026-09-30 00:35 | c_banda_atr_evento | DASH | timeout | -1.30% | -2.10% | -0.48 |
| 2026-09-30 00:35 | c_banda_atr_regimen | DASH | timeout | -1.30% | -1.80% | -0.41 |
| 2026-09-30 00:35 | ruptura_estricta | ZRO | take-profit | +3.00% | +2.50% | +0.57 |
| 2026-09-30 00:35 | estocastico_rebote | NEAR | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-09-30 00:35 | c_banda_atr | DASH | timeout | -1.30% | -1.80% | -0.41 |

## Eventos de la última vuelta

- 2026-09-30 00:50 [ruptura_volumen] CIERRE NEAR stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 00:50 [ruptura_volumen_evento] CIERRE NEAR stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 00:50 [ruptura_estricta] CIERRE BCH timeout bruto -0.64% neto -1.14%
- 2026-09-30 00:45 [c_banda_atr] ENTRADA INJ @ 6.73 (22.50 €, apertura)
- 2026-09-30 00:50 [estocastico_rebote] CIERRE INJ timeout bruto -0.88% neto -1.38%
- 2026-09-30 00:45 [c_banda_atr_evento] ENTRADA INJ @ 6.73 (22.59 €, apertura)
- 2026-09-30 00:45 [ruptura_volumen] ENTRADA SPX @ 0.3706 (22.50 €, apertura)
- 2026-09-30 00:45 [ruptura_volumen_evento] ENTRADA SPX @ 0.3706 (22.64 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
