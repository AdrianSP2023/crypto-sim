# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 13:11 UTC · vueltas 225 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 893.77 € (-3.30%) | 189 | 17 | 35% | -0.011% | -0.649% | -0.775% | -28.08 € |
| reversion_bb | 917.81 € (-0.70%) | 27 | 8 | 44% | +0.214% | -0.886% | -0.990% | -5.52 € |
| ruptura_volumen | 882.15 € (-4.55%) | 225 | 8 | 23% | -0.195% | -0.811% | -0.920% | -41.40 € |
| rebote_extremo | 922.08 € (-0.23%) | 9 | 0 | 44% | +0.060% | -1.040% | -1.178% | -2.16 € |
| pullback_tendencia | 894.53 € (-3.21%) | 135 | 0 | 14% | -0.271% | -0.966% | -1.072% | -29.72 € |
| macd_momentum | 880.59 € (-4.72%) | 327 | 3 | 21% | -0.009% | -0.589% | -0.698% | -43.58 € |
| estocastico_rebote | 878.39 € (-4.96%) | 263 | 8 | 30% | -0.163% | -0.763% | -0.873% | -45.42 € |
| ruptura_estricta | 886.97 € (-4.03%) | 128 | 7 | 24% | -0.538% | -1.244% | -1.368% | -36.36 € |
| macd_sin_salida | 884.39 € (-4.31%) | 230 | 18 | 36% | -0.109% | -0.722% | -0.838% | -37.88 € |
| c_banda_atr_tope | 912.56 € (-1.26%) | 44 | 3 | 27% | -0.045% | -1.131% | -1.251% | -11.45 € |
| ruptura_volumen_tope | 911.22 € (-1.41%) | 68 | 3 | 28% | +0.074% | -0.814% | -0.926% | -12.72 € |
| c_banda_atr_regimen | 902.16 € (-2.39%) | 109 | 1 | 34% | -0.130% | -0.870% | -1.010% | -21.77 € |
| macd_momentum_regimen | 893.92 € (-3.28%) | 204 | 2 | 22% | -0.022% | -0.650% | -0.762% | -30.24 € |
| ruptura_volumen_regimen | 884.20 € (-4.33%) | 182 | 3 | 20% | -0.318% | -0.961% | -1.076% | -39.75 € |
| c_banda_atr_evento | 899.72 € (-2.65%) | 156 | 17 | 37% | +0.052% | -0.617% | -0.736% | -22.11 € |
| macd_momentum_evento | 885.47 € (-4.19%) | 280 | 3 | 19% | -0.016% | -0.610% | -0.714% | -38.70 € |
| ruptura_volumen_evento | 894.70 € (-3.20%) | 175 | 8 | 24% | -0.072% | -0.722% | -0.820% | -28.83 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 13:10 | ruptura_volumen_evento | KAS | stop-loss | -1.30% | -1.80% | -0.41 |
| 2026-10-01 13:10 | ruptura_volumen_evento | OP | stop-loss | -1.22% | -1.72% | -0.39 |
| 2026-10-01 13:10 | macd_momentum_evento | SEI | momentum perdido | -0.94% | -1.44% | -0.32 |
| 2026-10-01 13:10 | c_banda_atr_evento | VVV | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 13:10 | ruptura_volumen_regimen | OP | stop-loss | -1.22% | -1.72% | -0.38 |
| 2026-10-01 13:10 | macd_sin_salida | VVV | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-01 13:10 | macd_sin_salida | JUP | stop-loss | -1.91% | -2.41% | -0.54 |
| 2026-10-01 13:10 | ruptura_estricta | SUI | stop-loss | -2.00% | -2.50% | -0.56 |
| 2026-10-01 13:10 | estocastico_rebote | LTC | timeout | -0.20% | -0.70% | -0.15 |
| 2026-10-01 13:10 | macd_momentum | SEI | momentum perdido | -0.94% | -1.44% | -0.32 |
| 2026-10-01 13:10 | ruptura_volumen | KAS | stop-loss | -1.30% | -1.80% | -0.40 |
| 2026-10-01 13:10 | ruptura_volumen | OP | stop-loss | -1.22% | -1.72% | -0.38 |
| 2026-10-01 13:10 | c_banda_atr | VVV | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 13:05 | macd_momentum_evento | NIGHT | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-01 13:05 | macd_momentum_evento | LINK | momentum perdido | -0.09% | -0.59% | -0.13 |

## Eventos de la última vuelta

- 2026-10-01 13:05 [reversion_bb] ENTRADA SOL @ 103.64 (22.97 €, apertura)
- 2026-10-01 13:10 [ruptura_estricta] CIERRE SUI stop-loss bruto -2.00% neto -2.50%
- 2026-10-01 13:10 [estocastico_rebote] CIERRE LTC timeout bruto -0.20% neto -0.70%
- 2026-10-01 13:05 [macd_momentum] ENTRADA XDC @ 0.03164 (22.02 €, apertura)
- 2026-10-01 13:05 [macd_sin_salida] ENTRADA XDC @ 0.03164 (22.18 €, apertura)
- 2026-10-01 13:05 [macd_momentum_evento] ENTRADA XDC @ 0.03164 (22.15 €, apertura)
- 2026-10-01 13:05 [reversion_bb] ENTRADA JUP @ 0.28171 (22.97 €, apertura)
- 2026-10-01 13:10 [macd_sin_salida] CIERRE JUP stop-loss bruto -1.91% neto -2.41%
- 2026-10-01 13:10 [ruptura_volumen] CIERRE OP stop-loss bruto -1.22% neto -1.72%
- 2026-10-01 13:10 [ruptura_volumen_regimen] CIERRE OP stop-loss bruto -1.22% neto -1.72%
- 2026-10-01 13:10 [ruptura_volumen_evento] CIERRE OP stop-loss bruto -1.22% neto -1.72%
- 2026-10-01 13:10 [c_banda_atr] CIERRE VVV stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 13:10 [macd_sin_salida] CIERRE VVV stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 13:10 [c_banda_atr_evento] CIERRE VVV stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 13:10 [ruptura_volumen] CIERRE KAS stop-loss bruto -1.30% neto -1.80%
- 2026-10-01 13:10 [ruptura_volumen_evento] CIERRE KAS stop-loss bruto -1.30% neto -1.80%
- 2026-10-01 13:10 [macd_momentum] CIERRE SEI momentum perdido bruto -0.94% neto -1.44%
- 2026-10-01 13:10 [macd_momentum_evento] CIERRE SEI momentum perdido bruto -0.94% neto -1.44%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
