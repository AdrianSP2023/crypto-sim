# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 00:56 UTC · vueltas 183 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 898.45 € (-2.79%) | 89 | 24 | 26% | -0.400% | -1.194% | -1.337% | -24.35 € |
| reversion_bb | 917.96 € (-0.68%) | 20 | 13 | 35% | -0.250% | -1.350% | -1.448% | -6.23 € |
| ruptura_volumen | 899.86 € (-2.64%) | 119 | 8 | 22% | -0.177% | -0.896% | -1.024% | -24.38 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 904.93 € (-2.09%) | 94 | 2 | 23% | -0.131% | -0.909% | -1.029% | -19.57 € |
| macd_momentum | 882.69 € (-4.50%) | 232 | 13 | 15% | -0.176% | -0.789% | -0.900% | -41.49 € |
| estocastico_rebote | 892.29 € (-3.46%) | 172 | 12 | 33% | -0.152% | -0.804% | -0.936% | -31.61 € |
| ruptura_estricta | 908.62 € (-1.69%) | 53 | 5 | 26% | -0.257% | -1.249% | -1.386% | -15.22 € |
| macd_sin_salida | 895.34 € (-3.13%) | 138 | 16 | 27% | -0.198% | -0.888% | -1.011% | -27.97 € |
| c_banda_atr_tope | 912.60 € (-1.26%) | 29 | 5 | 21% | -0.560% | -1.660% | -1.808% | -11.08 € |
| ruptura_volumen_tope | 913.42 € (-1.17%) | 40 | 5 | 15% | -0.097% | -1.197% | -1.319% | -11.01 € |
| c_banda_atr_regimen | 900.77 € (-2.54%) | 68 | 8 | 24% | -0.518% | -1.401% | -1.535% | -21.87 € |
| macd_momentum_regimen | 887.23 € (-4.00%) | 193 | 0 | 15% | -0.209% | -0.844% | -0.956% | -37.01 € |
| ruptura_volumen_regimen | 903.40 € (-2.25%) | 96 | 4 | 22% | -0.151% | -0.922% | -1.053% | -20.29 € |
| c_banda_atr_evento | 901.99 € (-2.41%) | 57 | 24 | 19% | -0.664% | -1.591% | -1.742% | -20.81 € |
| macd_momentum_evento | 895.10 € (-3.15%) | 112 | 13 | 8% | -0.401% | -1.137% | -1.244% | -29.08 € |
| ruptura_volumen_evento | 905.40 € (-2.04%) | 60 | 8 | 12% | -0.428% | -1.368% | -1.499% | -18.83 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 00:55 | estocastico_rebote | SPX | timeout | +0.38% | -0.12% | -0.03 |
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

## Eventos de la última vuelta

- 2026-09-30 00:50 [estocastico_rebote] ENTRADA QNT @ 237.41 (22.32 €, apertura)
- 2026-09-30 00:50 [pullback_tendencia] ENTRADA ZEC @ 1250.5 (22.62 €, apertura)
- 2026-09-30 00:50 [c_banda_atr] ENTRADA RAY @ 1.686 (22.50 €, apertura)
- 2026-09-30 00:50 [estocastico_rebote] ENTRADA RAY @ 1.686 (22.32 €, apertura)
- 2026-09-30 00:50 [c_banda_atr_evento] ENTRADA RAY @ 1.686 (22.59 €, apertura)
- 2026-09-30 00:50 [macd_momentum] ENTRADA NIGHT @ 0.02866 (22.07 €, apertura)
- 2026-09-30 00:50 [macd_momentum_evento] ENTRADA NIGHT @ 0.02866 (22.38 €, apertura)
- 2026-09-30 00:55 [estocastico_rebote] CIERRE SPX timeout bruto +0.38% neto -0.12%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
