# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 20:46 UTC · vueltas 74 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 907.37 € (-1.83%) | 51 | 28 | 25% | -0.442% | -1.447% | -1.599% | -16.99 € |
| reversion_bb | 922.26 € (-0.21%) | 8 | 4 | 50% | +0.000% | -1.100% | -1.225% | -2.04 € |
| ruptura_volumen | 898.09 € (-2.83%) | 74 | 15 | 14% | -0.665% | -1.518% | -1.656% | -25.76 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 905.77 € (-2.00%) | 59 | 3 | 15% | -0.431% | -1.378% | -1.517% | -18.66 € |
| macd_momentum | 907.94 € (-1.76%) | 80 | 13 | 26% | -0.031% | -0.857% | -0.992% | -15.77 € |
| estocastico_rebote | 906.08 € (-1.97%) | 102 | 21 | 37% | -0.047% | -0.803% | -0.936% | -18.86 € |
| ruptura_estricta | 899.05 € (-2.73%) | 46 | 5 | 11% | -1.277% | -2.350% | -2.498% | -24.89 € |
| macd_sin_salida | 905.60 € (-2.02%) | 67 | 15 | 33% | -0.287% | -1.177% | -1.316% | -18.17 € |
| c_banda_atr_tope | 921.09 € (-0.34%) | 14 | 5 | 36% | +0.100% | -1.000% | -1.153% | -3.23 € |
| ruptura_volumen_tope | 918.58 € (-0.61%) | 18 | 5 | 22% | -0.331% | -1.431% | -1.522% | -5.94 € |
| c_banda_atr_regimen | 908.76 € (-1.67%) | 43 | 2 | 26% | -0.480% | -1.573% | -1.728% | -15.58 € |
| macd_momentum_regimen | 911.23 € (-1.41%) | 60 | 0 | 30% | -0.005% | -0.940% | -1.079% | -13.01 € |
| ruptura_volumen_regimen | 898.23 € (-2.81%) | 72 | 0 | 12% | -0.713% | -1.576% | -1.715% | -26.01 € |
| c_banda_atr_evento | 916.69 € (-0.82%) | 19 | 27 | 16% | -0.679% | -1.779% | -1.917% | -7.80 € |
| macd_momentum_evento | 914.48 € (-1.06%) | 33 | 13 | 18% | -0.115% | -1.215% | -1.346% | -9.22 € |
| ruptura_volumen_evento | 913.61 € (-1.15%) | 24 | 15 | 8% | -0.746% | -1.846% | -1.960% | -10.23 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 20:45 | macd_momentum_evento | XDC | momentum perdido | -0.40% | -1.50% | -0.34 |
| 2026-09-30 20:45 | estocastico_rebote | ALGO | timeout | -0.41% | -0.91% | -0.21 |
| 2026-09-30 20:45 | macd_momentum | XDC | momentum perdido | -0.40% | -0.90% | -0.20 |
| 2026-09-30 20:45 | reversion_bb | ICP | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-30 20:40 | pullback_tendencia | XDC | rotura de tendencia | +0.10% | -0.40% | -0.09 |
| 2026-09-30 20:35 | c_banda_atr_evento | USELESS | stop-loss | -1.50% | -2.60% | -0.60 |
| 2026-09-30 20:35 | c_banda_atr_evento | ICP | stop-loss | -1.59% | -2.69% | -0.62 |
| 2026-09-30 20:35 | macd_sin_salida | XDC | timeout | +0.30% | -0.20% | -0.05 |
| 2026-09-30 20:35 | estocastico_rebote | TRUMP | timeout | -0.06% | -0.56% | -0.13 |
| 2026-09-30 20:35 | estocastico_rebote | ICP | stop-loss | -1.66% | -2.16% | -0.49 |
| 2026-09-30 20:35 | c_banda_atr | USELESS | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-09-30 20:35 | c_banda_atr | ICP | stop-loss | -1.59% | -2.09% | -0.47 |
| 2026-09-30 20:25 | estocastico_rebote | ASTER | timeout | +0.17% | -0.33% | -0.08 |
| 2026-09-30 20:25 | estocastico_rebote | FET | take-profit | +1.99% | +1.49% | +0.34 |
| 2026-09-30 20:25 | pullback_tendencia | FET | take-profit | +2.00% | +1.50% | +0.34 |

## Eventos de la última vuelta

- 2026-09-30 20:40 [macd_momentum] ENTRADA PUMP @ 0.005163 (22.72 €, apertura)
- 2026-09-30 20:40 [macd_sin_salida] ENTRADA PUMP @ 0.005163 (22.65 €, apertura)
- 2026-09-30 20:40 [macd_momentum_evento] ENTRADA PUMP @ 0.005163 (22.88 €, apertura)
- 2026-09-30 20:45 [reversion_bb] CIERRE ICP stop-loss bruto -1.50% neto -2.60%
- 2026-09-30 20:45 [estocastico_rebote] CIERRE ALGO timeout bruto -0.41% neto -0.91%
- 2026-09-30 20:45 [macd_momentum] CIERRE XDC momentum perdido bruto -0.40% neto -0.90%
- 2026-09-30 20:45 [macd_momentum_evento] CIERRE XDC momentum perdido bruto -0.40% neto -1.50%
- 2026-09-30 20:40 [ruptura_volumen] ENTRADA SHIB @ 5.086e-06 (22.46 €, apertura)
- 2026-09-30 20:40 [ruptura_volumen_evento] ENTRADA SHIB @ 5.086e-06 (22.85 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
