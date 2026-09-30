# Simulación P3 (sin dinero real)

Config `P3-v2` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-30 03:26 UTC · vueltas 188 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 896.44 € (-3.01%) | 112 | 14 | 27% | -0.286% | -1.020% | -1.155% | -26.16 € |
| reversion_bb | 918.10 € (-0.66%) | 29 | 9 | 48% | +0.205% | -0.895% | -0.997% | -5.98 € |
| ruptura_volumen | 893.42 € (-3.33%) | 144 | 7 | 21% | -0.233% | -0.914% | -1.042% | -30.02 € |
| rebote_extremo | 922.70 € (-0.17%) | 7 | 0 | 43% | +0.146% | -0.954% | -1.104% | -1.54 € |
| pullback_tendencia | 904.93 € (-2.09%) | 109 | 0 | 26% | -0.034% | -0.773% | -0.900% | -19.31 € |
| macd_momentum | 881.35 € (-4.64%) | 267 | 1 | 17% | -0.113% | -0.711% | -0.821% | -42.98 € |
| estocastico_rebote | 890.36 € (-3.67%) | 185 | 17 | 34% | -0.109% | -0.751% | -0.883% | -31.73 € |
| ruptura_estricta | 904.35 € (-2.15%) | 65 | 4 | 25% | -0.348% | -1.249% | -1.393% | -18.63 € |
| macd_sin_salida | 893.57 € (-3.32%) | 156 | 15 | 29% | -0.151% | -0.818% | -0.942% | -29.12 € |
| c_banda_atr_tope | 910.08 € (-1.53%) | 36 | 5 | 19% | -0.494% | -1.594% | -1.730% | -13.18 € |
| ruptura_volumen_tope | 910.35 € (-1.50%) | 51 | 3 | 18% | -0.128% | -1.146% | -1.269% | -13.42 € |
| c_banda_atr_regimen | 900.57 € (-2.56%) | 77 | 1 | 22% | -0.490% | -1.329% | -1.458% | -23.47 € |
| macd_momentum_regimen | 886.75 € (-4.06%) | 196 | 0 | 15% | -0.209% | -0.842% | -0.955% | -37.49 € |
| ruptura_volumen_regimen | 899.02 € (-2.73%) | 110 | 6 | 19% | -0.244% | -0.981% | -1.113% | -24.66 € |
| c_banda_atr_evento | 899.49 € (-2.68%) | 80 | 14 | 22% | -0.429% | -1.259% | -1.397% | -23.10 € |
| macd_momentum_evento | 893.74 € (-3.30%) | 147 | 1 | 13% | -0.232% | -0.912% | -1.019% | -30.58 € |
| ruptura_volumen_evento | 898.92 € (-2.74%) | 85 | 7 | 13% | -0.450% | -1.260% | -1.390% | -24.51 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 03:25 | ruptura_volumen_evento | DOT | timeout | -0.65% | -1.15% | -0.26 |
| 2026-09-30 03:25 | ruptura_volumen_evento | XRP | timeout | -0.47% | -0.97% | -0.22 |
| 2026-09-30 03:25 | macd_momentum_evento | BNB | momentum perdido | -0.50% | -1.00% | -0.23 |
| 2026-09-30 03:25 | macd_momentum_evento | VVV | momentum perdido | -1.33% | -1.83% | -0.41 |
| 2026-09-30 03:25 | macd_momentum_evento | HBAR | momentum perdido | -0.22% | -0.72% | -0.16 |
| 2026-09-30 03:25 | ruptura_volumen_regimen | DOT | timeout | -0.65% | -1.15% | -0.26 |
| 2026-09-30 03:25 | ruptura_volumen_regimen | XRP | timeout | -0.47% | -0.97% | -0.22 |
| 2026-09-30 03:25 | macd_sin_salida | PUMP | stop-loss | -1.60% | -2.10% | -0.47 |
| 2026-09-30 03:25 | estocastico_rebote | BTC | timeout | -0.24% | -0.74% | -0.17 |
| 2026-09-30 03:25 | macd_momentum | BNB | momentum perdido | -0.50% | -1.00% | -0.22 |
| 2026-09-30 03:25 | macd_momentum | VVV | momentum perdido | -1.33% | -1.83% | -0.40 |
| 2026-09-30 03:25 | macd_momentum | HBAR | momentum perdido | -0.22% | -0.72% | -0.16 |
| 2026-09-30 03:25 | ruptura_volumen | DOT | timeout | -0.65% | -1.15% | -0.26 |
| 2026-09-30 03:25 | ruptura_volumen | XRP | timeout | -0.47% | -0.97% | -0.22 |
| 2026-09-30 03:20 | ruptura_volumen_evento | RENDER | stop-loss | -1.28% | -1.78% | -0.40 |

## Eventos de la última vuelta

- 2026-09-30 03:25 [estocastico_rebote] CIERRE BTC timeout bruto -0.24% neto -0.74%
- 2026-09-30 03:25 [ruptura_volumen] CIERRE XRP timeout bruto -0.47% neto -0.97%
- 2026-09-30 03:25 [ruptura_volumen_regimen] CIERRE XRP timeout bruto -0.47% neto -0.97%
- 2026-09-30 03:25 [ruptura_volumen_evento] CIERRE XRP timeout bruto -0.47% neto -0.97%
- 2026-09-30 03:25 [macd_momentum] CIERRE HBAR momentum perdido bruto -0.22% neto -0.72%
- 2026-09-30 03:25 [macd_momentum_evento] CIERRE HBAR momentum perdido bruto -0.22% neto -0.72%
- 2026-09-30 03:20 [estocastico_rebote] ENTRADA ZEC @ 1243.11 (22.31 €, apertura)
- 2026-09-30 03:20 [reversion_bb] ENTRADA AVAX @ 9.904 (22.96 €, apertura)
- 2026-09-30 03:25 [macd_sin_salida] CIERRE PUMP stop-loss bruto -1.60% neto -2.10%
- 2026-09-30 03:20 [reversion_bb] ENTRADA ARB @ 0.1788 (22.96 €, apertura)
- 2026-09-30 03:20 [reversion_bb] ENTRADA DOGE @ 0.0821686 (22.96 €, apertura)
- 2026-09-30 03:25 [ruptura_volumen] CIERRE DOT timeout bruto -0.64% neto -1.14%
- 2026-09-30 03:25 [ruptura_volumen_regimen] CIERRE DOT timeout bruto -0.64% neto -1.14%
- 2026-09-30 03:25 [ruptura_volumen_evento] CIERRE DOT timeout bruto -0.64% neto -1.14%
- 2026-09-30 03:25 [macd_momentum] CIERRE VVV momentum perdido bruto -1.33% neto -1.83%
- 2026-09-30 03:25 [macd_momentum_evento] CIERRE VVV momentum perdido bruto -1.33% neto -1.83%
- 2026-09-30 03:25 [macd_momentum] CIERRE BNB momentum perdido bruto -0.50% neto -1.00%
- 2026-09-30 03:25 [macd_momentum_evento] CIERRE BNB momentum perdido bruto -0.50% neto -1.00%

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
