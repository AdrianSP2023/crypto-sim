# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 15:41 UTC · vueltas 41 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 914.19 € (-1.09%) | 30 | 10 | 33% | -0.317% | -1.417% | -1.579% | -9.83 € |
| reversion_bb | 923.86 € (-0.04%) | 2 | 2 | 50% | +0.000% | -1.100% | -1.219% | -0.51 € |
| ruptura_volumen | 905.25 € (-2.06%) | 50 | 0 | 16% | -0.627% | -1.649% | -1.799% | -18.99 € |
| rebote_extremo | 924.28 € (+0.00%) | 0 | 2 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 912.78 € (-1.24%) | 32 | 1 | 19% | -0.461% | -1.561% | -1.699% | -11.51 € |
| macd_momentum | 911.59 € (-1.37%) | 51 | 7 | 27% | -0.074% | -1.086% | -1.228% | -12.77 € |
| estocastico_rebote | 915.03 € (-1.00%) | 40 | 34 | 30% | -0.441% | -1.421% | -1.598% | -13.11 € |
| ruptura_estricta | 903.11 € (-2.29%) | 37 | 2 | 11% | -1.305% | -2.405% | -2.551% | -20.55 € |
| macd_sin_salida | 908.55 € (-1.70%) | 47 | 9 | 30% | -0.407% | -1.450% | -1.594% | -15.73 € |
| c_banda_atr_tope | 922.97 € (-0.14%) | 8 | 5 | 50% | +0.252% | -0.849% | -1.012% | -1.57 € |
| ruptura_volumen_tope | 921.18 € (-0.33%) | 9 | 0 | 22% | -0.373% | -1.473% | -1.564% | -3.06 € |
| c_banda_atr_regimen | 913.90 € (-1.12%) | 30 | 4 | 33% | -0.317% | -1.417% | -1.579% | -9.83 € |
| macd_momentum_regimen | 912.12 € (-1.31%) | 49 | 0 | 29% | -0.039% | -1.072% | -1.211% | -12.12 € |
| ruptura_volumen_regimen | 905.25 € (-2.06%) | 50 | 0 | 16% | -0.627% | -1.649% | -1.799% | -18.99 € |
| c_banda_atr_evento | 924.61 € (+0.04%) | 0 | 7 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| macd_momentum_evento | 922.17 € (-0.22%) | 4 | 7 | 0% | -1.276% | -2.376% | -2.562% | -2.19 € |
| ruptura_volumen_evento | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 15:40 | macd_sin_salida | BNB | timeout | -0.69% | -1.49% | -0.34 |
| 2026-09-30 15:40 | ruptura_estricta | TRUMP | timeout | +0.05% | -1.05% | -0.24 |
| 2026-09-30 15:35 | macd_sin_salida | WLFI | timeout | -1.00% | -1.80% | -0.42 |
| 2026-09-30 15:35 | macd_sin_salida | BTC | timeout | -0.32% | -1.12% | -0.26 |
| 2026-09-30 15:35 | ruptura_estricta | BNB | timeout | -0.73% | -1.83% | -0.42 |
| 2026-09-30 15:35 | ruptura_estricta | ETH | timeout | -1.31% | -2.41% | -0.56 |
| 2026-09-30 15:35 | ruptura_estricta | BTC | timeout | -0.32% | -1.42% | -0.33 |
| 2026-09-30 15:35 | estocastico_rebote | TRUMP | timeout | +0.00% | -0.80% | -0.18 |
| 2026-09-30 15:35 | estocastico_rebote | KSM | timeout | +1.12% | +0.32% | +0.07 |
| 2026-09-30 15:30 | macd_momentum_evento | MINA | stop-loss | -1.62% | -2.72% | -0.63 |
| 2026-09-30 15:30 | macd_sin_salida | MINA | stop-loss | -1.62% | -2.12% | -0.48 |
| 2026-09-30 15:30 | macd_sin_salida | ETH | timeout | -1.08% | -1.88% | -0.43 |
| 2026-09-30 15:30 | ruptura_estricta | SHIB | stop-loss | -2.06% | -3.16% | -0.73 |
| 2026-09-30 15:30 | estocastico_rebote | ALGO | stop-loss | -1.72% | -2.52% | -0.58 |
| 2026-09-30 15:30 | estocastico_rebote | POL | stop-loss | -1.66% | -2.46% | -0.56 |

## Eventos de la última vuelta

- 2026-09-30 15:35 [estocastico_rebote] ENTRADA XRP @ 1.3226 (22.78 €, apertura)
- 2026-09-30 15:35 [estocastico_rebote] ENTRADA NEAR @ 4.5996 (22.78 €, apertura)
- 2026-09-30 15:35 [macd_momentum] ENTRADA SUI @ 1.025 (22.79 €, apertura)
- 2026-09-30 15:35 [macd_sin_salida] ENTRADA SUI @ 1.025 (22.72 €, apertura)
- 2026-09-30 15:35 [macd_momentum_evento] ENTRADA SUI @ 1.025 (23.05 €, apertura)
- 2026-09-30 15:35 [c_banda_atr] ENTRADA UNI @ 7.8332 (22.86 €, apertura)
- 2026-09-30 15:35 [c_banda_atr_tope] ENTRADA UNI @ 7.8332 (23.07 €, apertura)
- 2026-09-30 15:35 [c_banda_atr_evento] ENTRADA UNI @ 7.8332 (23.11 €, apertura)
- 2026-09-30 15:35 [estocastico_rebote] ENTRADA ENA @ 0.2365 (22.78 €, apertura)
- 2026-09-30 15:35 [c_banda_atr] ENTRADA ICP @ 3.021 (22.86 €, apertura)
- 2026-09-30 15:35 [c_banda_atr_tope] ENTRADA ICP @ 3.021 (23.07 €, apertura)
- 2026-09-30 15:35 [c_banda_atr_evento] ENTRADA ICP @ 3.021 (23.11 €, apertura)
- 2026-09-30 15:35 [estocastico_rebote] ENTRADA WLD @ 0.4692 (22.78 €, apertura)
- 2026-09-30 15:35 [estocastico_rebote] ENTRADA NIGHT @ 0.03248 (22.78 €, apertura)
- 2026-09-30 15:35 [estocastico_rebote] ENTRADA PEPE @ 3.813e-06 (22.78 €, apertura)
- 2026-09-30 15:35 [macd_momentum] ENTRADA TRUMP @ 1.836 (22.79 €, apertura)
- 2026-09-30 15:40 [ruptura_estricta] CIERRE TRUMP timeout bruto +0.05% neto -1.05%
- 2026-09-30 15:35 [macd_sin_salida] ENTRADA TRUMP @ 1.836 (22.72 €, apertura)
- 2026-09-30 15:35 [c_banda_atr_evento] ENTRADA TRUMP @ 1.836 (23.11 €, apertura)
- 2026-09-30 15:35 [macd_momentum_evento] ENTRADA TRUMP @ 1.836 (23.05 €, apertura)
- 2026-09-30 15:40 [macd_sin_salida] CIERRE BNB timeout bruto -0.69% neto -1.49%
- 2026-09-30 15:35 [c_banda_atr] ENTRADA SPX @ 0.3877 (22.86 €, apertura)
- 2026-09-30 15:35 [macd_momentum] ENTRADA SPX @ 0.3877 (22.79 €, apertura)
- 2026-09-30 15:35 [c_banda_atr_evento] ENTRADA SPX @ 0.3877 (23.11 €, apertura)
- 2026-09-30 15:35 [macd_momentum_evento] ENTRADA SPX @ 0.3877 (23.05 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
