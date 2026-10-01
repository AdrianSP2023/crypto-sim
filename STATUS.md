# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 11:53 UTC · vueltas 209 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

**Avisos:** hueco de 22 min entre vueltas

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 897.51 € (-2.89%) | 177 | 25 | 35% | -0.037% | -0.685% | -0.809% | -27.73 € |
| reversion_bb | 919.26 € (-0.54%) | 27 | 6 | 44% | +0.214% | -0.886% | -0.990% | -5.52 € |
| ruptura_volumen | 884.61 € (-4.29%) | 215 | 8 | 23% | -0.203% | -0.824% | -0.934% | -40.24 € |
| rebote_extremo | 922.08 € (-0.23%) | 9 | 0 | 44% | +0.060% | -1.040% | -1.178% | -2.16 € |
| pullback_tendencia | 896.44 € (-3.01%) | 125 | 3 | 15% | -0.255% | -0.966% | -1.072% | -27.55 € |
| macd_momentum | 883.53 € (-4.41%) | 308 | 14 | 21% | -0.012% | -0.597% | -0.705% | -41.61 € |
| estocastico_rebote | 880.51 € (-4.73%) | 259 | 7 | 31% | -0.149% | -0.750% | -0.860% | -44.01 € |
| ruptura_estricta | 889.74 € (-3.73%) | 124 | 6 | 25% | -0.489% | -1.202% | -1.327% | -34.08 € |
| macd_sin_salida | 888.72 € (-3.84%) | 224 | 18 | 36% | -0.092% | -0.709% | -0.824% | -36.24 € |
| c_banda_atr_tope | 913.83 € (-1.13%) | 42 | 5 | 29% | -0.003% | -1.103% | -1.222% | -10.66 € |
| ruptura_volumen_tope | 911.66 € (-1.36%) | 65 | 5 | 28% | +0.049% | -0.857% | -0.972% | -12.80 € |
| c_banda_atr_regimen | 902.48 € (-2.35%) | 109 | 0 | 34% | -0.130% | -0.870% | -1.010% | -21.77 € |
| macd_momentum_regimen | 894.12 € (-3.26%) | 203 | 0 | 22% | -0.022% | -0.651% | -0.763% | -30.12 € |
| ruptura_volumen_regimen | 886.57 € (-4.08%) | 177 | 0 | 20% | -0.288% | -0.936% | -1.049% | -37.67 € |
| c_banda_atr_evento | 903.49 € (-2.25%) | 144 | 25 | 36% | +0.025% | -0.658% | -0.774% | -21.76 € |
| macd_momentum_evento | 888.42 € (-3.88%) | 261 | 14 | 19% | -0.019% | -0.620% | -0.723% | -36.72 € |
| ruptura_volumen_evento | 897.20 € (-2.93%) | 165 | 8 | 24% | -0.074% | -0.734% | -0.832% | -27.65 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 11:50 | ruptura_volumen_evento | BNB | timeout | +0.16% | -0.34% | -0.08 |
| 2026-10-01 11:50 | macd_sin_salida | MINA | timeout | +1.00% | +0.50% | +0.11 |
| 2026-10-01 11:50 | ruptura_estricta | TRX | timeout | -1.37% | -1.87% | -0.42 |
| 2026-10-01 11:50 | ruptura_estricta | UNI | timeout | -0.01% | -0.51% | -0.11 |
| 2026-10-01 11:50 | estocastico_rebote | INJ | take-profit | +1.80% | +1.30% | +0.29 |
| 2026-10-01 11:50 | ruptura_volumen | BNB | timeout | +0.16% | -0.34% | -0.08 |
| 2026-10-01 11:45 | ruptura_volumen_evento | NIGHT | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-01 11:45 | c_banda_atr_evento | SKY | take-profit | +2.03% | +1.53% | +0.35 |
| 2026-10-01 11:45 | c_banda_atr_evento | KSM | take-profit | +2.00% | +1.50% | +0.34 |
| 2026-10-01 11:45 | ruptura_volumen_tope | NIGHT | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-10-01 11:45 | c_banda_atr_tope | KSM | take-profit | +2.00% | +0.90% | +0.21 |
| 2026-10-01 11:45 | estocastico_rebote | KSM | take-profit | +1.98% | +1.48% | +0.33 |
| 2026-10-01 11:45 | ruptura_volumen | NIGHT | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-01 11:45 | c_banda_atr | SKY | take-profit | +2.03% | +1.53% | +0.34 |
| 2026-10-01 11:45 | c_banda_atr | KSM | take-profit | +2.00% | +1.50% | +0.34 |

## Eventos de la última vuelta

- 2026-10-01 11:35 [ruptura_volumen] CIERRE XRP timeout bruto -0.27% neto -0.77%
- 2026-10-01 11:35 [ruptura_volumen_tope] CIERRE XRP timeout bruto -0.27% neto -0.77%
- 2026-10-01 11:35 [ruptura_volumen_evento] CIERRE XRP timeout bruto -0.27% neto -0.77%
- 2026-10-01 11:30 [c_banda_atr] ENTRADA HBAR @ 0.09273 (22.40 €, apertura)
- 2026-10-01 11:30 [c_banda_atr_evento] ENTRADA HBAR @ 0.09273 (22.54 €, apertura)
- 2026-10-01 11:30 [ruptura_volumen_tope] ENTRADA XDC @ 0.03159 (22.80 €, apertura)
- 2026-10-01 11:35 [reversion_bb] CIERRE INJ take-profit bruto +1.57% neto +0.47%
- 2026-10-01 11:35 [pullback_tendencia] CIERRE MINA rotura de tendencia bruto -0.23% neto -0.73%
- 2026-10-01 11:35 [macd_momentum] CIERRE MINA momentum perdido bruto -0.23% neto -0.73%
- 2026-10-01 11:35 [macd_momentum_evento] CIERRE MINA momentum perdido bruto -0.23% neto -0.73%
- 2026-10-01 11:35 [ruptura_volumen] CIERRE TON timeout bruto +0.15% neto -0.35%
- 2026-10-01 11:35 [ruptura_volumen_evento] CIERRE TON timeout bruto +0.15% neto -0.35%
- 2026-10-01 11:40 [macd_momentum] CIERRE PENGU momentum perdido bruto -0.70% neto -1.20%
- 2026-10-01 11:40 [macd_momentum_evento] CIERRE PENGU momentum perdido bruto -0.70% neto -1.20%
- 2026-10-01 11:40 [macd_momentum] CIERRE TON momentum perdido bruto +0.15% neto -0.35%
- 2026-10-01 11:40 [macd_momentum_evento] CIERRE TON momentum perdido bruto +0.15% neto -0.35%
- 2026-10-01 11:40 [c_banda_atr] ENTRADA LINK @ 12.6994 (22.40 €, apertura)
- 2026-10-01 11:40 [c_banda_atr_evento] ENTRADA LINK @ 12.6994 (22.54 €, apertura)
- 2026-10-01 11:40 [c_banda_atr] ENTRADA DOGE @ 0.0838728 (22.40 €, apertura)
- 2026-10-01 11:40 [c_banda_atr_evento] ENTRADA DOGE @ 0.0838728 (22.54 €, apertura)
- 2026-10-01 11:40 [c_banda_atr] ENTRADA ENA @ 0.229 (22.40 €, apertura)
- 2026-10-01 11:40 [c_banda_atr_evento] ENTRADA ENA @ 0.229 (22.54 €, apertura)
- 2026-10-01 11:40 [c_banda_atr] ENTRADA ICP @ 2.919 (22.40 €, apertura)
- 2026-10-01 11:40 [c_banda_atr_evento] ENTRADA ICP @ 2.919 (22.54 €, apertura)
- 2026-10-01 11:45 [ruptura_volumen] CIERRE NIGHT stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 11:45 [ruptura_volumen_tope] CIERRE NIGHT stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 11:45 [ruptura_volumen_evento] CIERRE NIGHT stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 11:40 [macd_momentum] ENTRADA OP @ 0.1145 (22.07 €, apertura)
- 2026-10-01 11:40 [macd_momentum_evento] ENTRADA OP @ 0.1145 (22.19 €, apertura)
- 2026-10-01 11:45 [c_banda_atr] CIERRE KSM take-profit bruto +2.00% neto +1.50%
- 2026-10-01 11:45 [estocastico_rebote] CIERRE KSM take-profit bruto +1.98% neto +1.48%
- 2026-10-01 11:45 [c_banda_atr_tope] CIERRE KSM take-profit bruto +2.00% neto +0.90%
- 2026-10-01 11:45 [c_banda_atr_evento] CIERRE KSM take-profit bruto +2.00% neto +1.50%
- 2026-10-01 11:45 [c_banda_atr] CIERRE SKY take-profit bruto +2.03% neto +1.53%
- 2026-10-01 11:45 [c_banda_atr_evento] CIERRE SKY take-profit bruto +2.03% neto +1.53%
- 2026-10-01 11:45 [c_banda_atr] ENTRADA UNI @ 7.9876 (22.41 €, apertura)
- 2026-10-01 11:50 [ruptura_estricta] CIERRE UNI timeout bruto -0.01% neto -0.51%
- 2026-10-01 11:45 [c_banda_atr_tope] ENTRADA UNI @ 7.9876 (22.84 €, apertura)
- 2026-10-01 11:45 [c_banda_atr_evento] ENTRADA UNI @ 7.9876 (22.56 €, apertura)
- 2026-10-01 11:50 [ruptura_estricta] CIERRE TRX timeout bruto -1.37% neto -1.87%
- 2026-10-01 11:45 [macd_momentum] ENTRADA PEPE @ 3.835e-06 (22.07 €, apertura)
- 2026-10-01 11:45 [macd_sin_salida] ENTRADA PEPE @ 3.835e-06 (22.20 €, apertura)
- 2026-10-01 11:45 [macd_momentum_evento] ENTRADA PEPE @ 3.835e-06 (22.19 €, apertura)
- 2026-10-01 11:50 [estocastico_rebote] CIERRE INJ take-profit bruto +1.80% neto +1.30%
- 2026-10-01 11:50 [macd_sin_salida] CIERRE MINA timeout bruto +1.00% neto +0.50%
- 2026-10-01 11:45 [ruptura_volumen] ENTRADA KSM @ 4.65 (22.10 €, apertura)
- 2026-10-01 11:45 [ruptura_estricta] ENTRADA KSM @ 4.65 (22.25 €, apertura)
- 2026-10-01 11:45 [ruptura_volumen_tope] ENTRADA KSM @ 4.65 (22.79 €, apertura)
- 2026-10-01 11:45 [ruptura_volumen_evento] ENTRADA KSM @ 4.65 (22.42 €, apertura)
- 2026-10-01 11:50 [ruptura_volumen] CIERRE BNB timeout bruto +0.16% neto -0.34%
- 2026-10-01 11:50 [ruptura_volumen_evento] CIERRE BNB timeout bruto +0.16% neto -0.34%
- 2026-10-01 11:45 [macd_momentum] ENTRADA TON @ 1.34 (22.07 €, apertura)
- 2026-10-01 11:45 [macd_momentum_evento] ENTRADA TON @ 1.34 (22.19 €, apertura)
- 2026-10-01 11:45 [ruptura_estricta] ENTRADA SKY @ 0.0704 (22.25 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
