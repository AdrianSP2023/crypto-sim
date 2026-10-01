# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 02:26 UTC · vueltas 100 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 900.08 € (-2.61%) | 98 | 24 | 27% | -0.263% | -1.029% | -1.152% | -23.12 € |
| reversion_bb | 921.14 € (-0.34%) | 13 | 3 | 38% | +0.127% | -0.973% | -1.092% | -2.92 € |
| ruptura_volumen | 890.95 € (-3.60%) | 129 | 13 | 17% | -0.421% | -1.123% | -1.237% | -33.06 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 903.24 € (-2.27%) | 81 | 3 | 16% | -0.317% | -1.143% | -1.266% | -21.21 € |
| macd_momentum | 897.11 € (-2.93%) | 171 | 9 | 21% | -0.040% | -0.693% | -0.802% | -27.06 € |
| estocastico_rebote | 900.78 € (-2.54%) | 141 | 20 | 36% | -0.012% | -0.697% | -0.819% | -22.59 € |
| ruptura_estricta | 896.99 € (-2.95%) | 61 | 15 | 15% | -0.937% | -1.870% | -2.008% | -26.23 € |
| macd_sin_salida | 900.72 € (-2.55%) | 118 | 19 | 34% | -0.105% | -0.826% | -0.942% | -22.39 € |
| c_banda_atr_tope | 917.51 € (-0.73%) | 23 | 5 | 26% | -0.149% | -1.249% | -1.380% | -6.62 € |
| ruptura_volumen_tope | 914.98 € (-1.00%) | 35 | 3 | 17% | -0.072% | -1.172% | -1.259% | -9.45 € |
| c_banda_atr_regimen | 906.35 € (-1.94%) | 48 | 13 | 23% | -0.511% | -1.555% | -1.710% | -17.17 € |
| macd_momentum_regimen | 905.47 € (-2.03%) | 92 | 2 | 21% | -0.098% | -0.882% | -1.000% | -18.63 € |
| ruptura_volumen_regimen | 891.78 € (-3.51%) | 104 | 10 | 13% | -0.575% | -1.326% | -1.446% | -31.50 € |
| c_banda_atr_evento | 906.07 € (-1.97%) | 65 | 24 | 25% | -0.239% | -1.146% | -1.250% | -17.12 € |
| macd_momentum_evento | 902.08 € (-2.40%) | 124 | 9 | 15% | -0.066% | -0.779% | -0.878% | -22.09 € |
| ruptura_volumen_evento | 903.62 € (-2.23%) | 79 | 13 | 15% | -0.291% | -1.125% | -1.216% | -20.37 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 02:25 | ruptura_volumen_evento | APT | timeout | +0.63% | +0.13% | +0.03 |
| 2026-10-01 02:25 | ruptura_volumen_evento | MINA | timeout | +0.62% | +0.12% | +0.03 |
| 2026-10-01 02:25 | macd_momentum_evento | XLM | momentum perdido | -0.69% | -1.19% | -0.27 |
| 2026-10-01 02:25 | c_banda_atr_evento | ZEC | timeout | -0.69% | -1.19% | -0.27 |
| 2026-10-01 02:25 | c_banda_atr_evento | AAVE | timeout | +0.97% | +0.17% | +0.04 |
| 2026-10-01 02:25 | c_banda_atr_evento | ETH | timeout | +0.13% | -0.67% | -0.15 |
| 2026-10-01 02:25 | c_banda_atr_evento | XRP | timeout | -0.08% | -0.88% | -0.20 |
| 2026-10-01 02:25 | ruptura_volumen_tope | APT | timeout | +0.63% | -0.47% | -0.11 |
| 2026-10-01 02:25 | ruptura_volumen_tope | MINA | timeout | +0.62% | -0.48% | -0.11 |
| 2026-10-01 02:25 | macd_momentum | XLM | momentum perdido | -0.69% | -1.19% | -0.27 |
| 2026-10-01 02:25 | ruptura_volumen | APT | timeout | +0.63% | +0.13% | +0.03 |
| 2026-10-01 02:25 | ruptura_volumen | MINA | timeout | +0.62% | +0.12% | +0.03 |
| 2026-10-01 02:25 | c_banda_atr | ZEC | timeout | -0.69% | -1.19% | -0.27 |
| 2026-10-01 02:25 | c_banda_atr | AAVE | timeout | +0.97% | +0.47% | +0.11 |
| 2026-10-01 02:25 | c_banda_atr | ETH | timeout | +0.13% | -0.37% | -0.08 |

## Eventos de la última vuelta

- 2026-10-01 02:25 [c_banda_atr] CIERRE XRP timeout bruto -0.08% neto -0.58%
- 2026-10-01 02:25 [c_banda_atr_evento] CIERRE XRP timeout bruto -0.08% neto -0.88%
- 2026-10-01 02:25 [c_banda_atr] CIERRE ETH timeout bruto +0.13% neto -0.37%
- 2026-10-01 02:25 [c_banda_atr_evento] CIERRE ETH timeout bruto +0.13% neto -0.67%
- 2026-10-01 02:25 [c_banda_atr] CIERRE AAVE timeout bruto +0.97% neto +0.47%
- 2026-10-01 02:25 [c_banda_atr_evento] CIERRE AAVE timeout bruto +0.97% neto +0.17%
- 2026-10-01 02:25 [c_banda_atr] CIERRE ZEC timeout bruto -0.69% neto -1.19%
- 2026-10-01 02:25 [c_banda_atr_evento] CIERRE ZEC timeout bruto -0.69% neto -1.19%
- 2026-10-01 02:25 [macd_momentum] CIERRE XLM momentum perdido bruto -0.69% neto -1.19%
- 2026-10-01 02:25 [macd_momentum_evento] CIERRE XLM momentum perdido bruto -0.69% neto -1.19%
- 2026-10-01 02:20 [macd_momentum] ENTRADA XDC @ 0.03107 (22.43 €, apertura)
- 2026-10-01 02:20 [macd_momentum_evento] ENTRADA XDC @ 0.03107 (22.55 €, apertura)
- 2026-10-01 02:25 [ruptura_volumen] CIERRE MINA timeout bruto +0.62% neto +0.12%
- 2026-10-01 02:25 [ruptura_volumen_tope] CIERRE MINA timeout bruto +0.62% neto -0.48%
- 2026-10-01 02:25 [ruptura_volumen_evento] CIERRE MINA timeout bruto +0.62% neto +0.12%
- 2026-10-01 02:20 [estocastico_rebote] ENTRADA BNB @ 676.93 (22.54 €, apertura)
- 2026-10-01 02:25 [ruptura_volumen] CIERRE APT timeout bruto +0.63% neto +0.13%
- 2026-10-01 02:25 [ruptura_volumen_tope] CIERRE APT timeout bruto +0.63% neto -0.47%
- 2026-10-01 02:25 [ruptura_volumen_evento] CIERRE APT timeout bruto +0.63% neto +0.13%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
