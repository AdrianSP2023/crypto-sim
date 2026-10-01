# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 07:31 UTC · vueltas 160 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 898.81 € (-2.75%) | 157 | 10 | 37% | +0.018% | -0.648% | -0.772% | -23.34 € |
| reversion_bb | 919.72 € (-0.49%) | 19 | 7 | 42% | +0.220% | -0.880% | -0.993% | -3.86 € |
| ruptura_volumen | 885.90 € (-4.15%) | 202 | 2 | 23% | -0.199% | -0.828% | -0.938% | -38.03 € |
| rebote_extremo | 924.11 € (-0.01%) | 3 | 0 | 67% | +0.913% | -0.187% | -0.281% | -0.13 € |
| pullback_tendencia | 898.21 € (-2.82%) | 117 | 2 | 16% | -0.237% | -0.963% | -1.067% | -25.73 € |
| macd_momentum | 885.37 € (-4.21%) | 286 | 3 | 22% | -0.001% | -0.592% | -0.699% | -38.41 € |
| estocastico_rebote | 890.46 € (-3.65%) | 199 | 12 | 35% | -0.050% | -0.681% | -0.798% | -31.00 € |
| ruptura_estricta | 892.11 € (-3.48%) | 111 | 11 | 28% | -0.431% | -1.169% | -1.296% | -29.75 € |
| macd_sin_salida | 889.91 € (-3.71%) | 204 | 11 | 38% | -0.057% | -0.685% | -0.798% | -31.95 € |
| c_banda_atr_tope | 914.94 € (-1.01%) | 34 | 2 | 26% | -0.031% | -1.131% | -1.253% | -8.85 € |
| ruptura_volumen_tope | 912.77 € (-1.24%) | 56 | 1 | 29% | +0.088% | -0.884% | -0.999% | -11.38 € |
| c_banda_atr_regimen | 903.32 € (-2.26%) | 102 | 7 | 36% | -0.071% | -0.827% | -0.968% | -19.39 € |
| macd_momentum_regimen | 894.35 € (-3.23%) | 200 | 3 | 22% | -0.014% | -0.645% | -0.756% | -29.42 € |
| ruptura_volumen_regimen | 886.75 € (-4.06%) | 175 | 2 | 21% | -0.284% | -0.934% | -1.047% | -37.18 € |
| c_banda_atr_evento | 904.79 € (-2.10%) | 124 | 10 | 39% | +0.106% | -0.607% | -0.722% | -17.33 € |
| macd_momentum_evento | 890.27 € (-3.68%) | 239 | 3 | 19% | -0.006% | -0.617% | -0.718% | -33.50 € |
| ruptura_volumen_evento | 898.50 € (-2.78%) | 152 | 2 | 24% | -0.058% | -0.731% | -0.829% | -25.41 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 07:30 | ruptura_volumen_evento | SPX | stop-loss | -2.50% | -3.00% | -0.68 |
| 2026-10-01 07:30 | ruptura_volumen_evento | SEI | stop-loss | -1.49% | -1.99% | -0.45 |
| 2026-10-01 07:30 | ruptura_volumen_evento | PEPE | stop-loss | -1.42% | -1.92% | -0.43 |
| 2026-10-01 07:30 | ruptura_volumen_evento | DOT | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-10-01 07:30 | macd_momentum_evento | APT | stop-loss | -1.57% | -2.07% | -0.47 |
| 2026-10-01 07:30 | macd_momentum_evento | SEI | momentum perdido | -1.49% | -1.99% | -0.45 |
| 2026-10-01 07:30 | macd_momentum_evento | KSM | stop-loss | -1.92% | -2.42% | -0.54 |
| 2026-10-01 07:30 | macd_momentum_evento | FET | stop-loss | -2.47% | -2.97% | -0.67 |
| 2026-10-01 07:30 | c_banda_atr_evento | APT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 07:30 | c_banda_atr_evento | KSM | stop-loss | -1.50% | -2.00% | -0.46 |
| 2026-10-01 07:30 | c_banda_atr_evento | DASH | stop-loss | -1.96% | -2.46% | -0.56 |
| 2026-10-01 07:30 | c_banda_atr_evento | VVV | stop-loss | -1.68% | -2.18% | -0.50 |
| 2026-10-01 07:30 | c_banda_atr_evento | PEPE | stop-loss | -1.57% | -2.07% | -0.47 |
| 2026-10-01 07:30 | c_banda_atr_evento | ICP | stop-loss | -1.65% | -2.15% | -0.49 |
| 2026-10-01 07:30 | c_banda_atr_evento | DOT | stop-loss | -1.50% | -2.00% | -0.46 |

## Eventos de la última vuelta

- 2026-10-01 07:25 [reversion_bb] ENTRADA XRP @ 1.315 (23.02 €, apertura)
- 2026-10-01 07:30 [estocastico_rebote] CIERRE SOL stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:30 [ruptura_estricta] CIERRE NEAR stop-loss bruto -2.00% neto -2.50%
- 2026-10-01 07:25 [reversion_bb] ENTRADA LINK @ 12.6134 (23.02 €, apertura)
- 2026-10-01 07:30 [estocastico_rebote] CIERRE LINK stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:25 [reversion_bb] ENTRADA SUI @ 1.0171 (23.02 €, apertura)
- 2026-10-01 07:30 [macd_sin_salida] CIERRE AVAX stop-loss bruto -1.52% neto -2.02%
- 2026-10-01 07:30 [c_banda_atr] CIERRE AAVE stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:30 [macd_sin_salida] CIERRE AAVE stop-loss bruto -1.52% neto -2.02%
- 2026-10-01 07:30 [c_banda_atr_regimen] CIERRE AAVE stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:30 [c_banda_atr_evento] CIERRE AAVE stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:30 [ruptura_estricta] CIERRE ZEC stop-loss bruto -2.00% neto -2.50%
- 2026-10-01 07:30 [c_banda_atr] CIERRE XLM stop-loss bruto -1.51% neto -2.01%
- 2026-10-01 07:25 [reversion_bb] ENTRADA XLM @ 0.198118 (23.02 €, apertura)
- 2026-10-01 07:30 [estocastico_rebote] CIERRE XLM stop-loss bruto -1.51% neto -2.01%
- 2026-10-01 07:30 [macd_sin_salida] CIERRE XLM stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:30 [c_banda_atr_regimen] CIERRE XLM stop-loss bruto -1.51% neto -2.01%
- 2026-10-01 07:30 [c_banda_atr_evento] CIERRE XLM stop-loss bruto -1.51% neto -2.01%
- 2026-10-01 07:30 [ruptura_estricta] CIERRE UNI timeout bruto -1.55% neto -2.05%
- 2026-10-01 07:30 [estocastico_rebote] CIERRE DOGE stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:30 [c_banda_atr] CIERRE DOT stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:30 [ruptura_volumen] CIERRE DOT stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 07:30 [ruptura_estricta] CIERRE DOT stop-loss bruto -2.00% neto -2.50%
- 2026-10-01 07:30 [ruptura_volumen_tope] CIERRE DOT stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 07:30 [c_banda_atr_regimen] CIERRE DOT stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:30 [ruptura_volumen_regimen] CIERRE DOT stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 07:30 [c_banda_atr_evento] CIERRE DOT stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:30 [ruptura_volumen_evento] CIERRE DOT stop-loss bruto -1.20% neto -1.70%
- 2026-10-01 07:25 [reversion_bb] ENTRADA ARB @ 0.1777 (23.02 €, apertura)
- 2026-10-01 07:30 [c_banda_atr] CIERRE ICP stop-loss bruto -1.65% neto -2.15%
- 2026-10-01 07:30 [estocastico_rebote] CIERRE ICP stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:30 [c_banda_atr_regimen] CIERRE ICP stop-loss bruto -1.65% neto -2.15%
- 2026-10-01 07:30 [c_banda_atr_evento] CIERRE ICP stop-loss bruto -1.65% neto -2.15%
- 2026-10-01 07:30 [macd_momentum] CIERRE FET stop-loss bruto -2.47% neto -2.97%
- 2026-10-01 07:30 [macd_sin_salida] CIERRE FET stop-loss bruto -2.47% neto -2.97%
- 2026-10-01 07:30 [macd_momentum_regimen] CIERRE FET stop-loss bruto -2.47% neto -2.97%
- 2026-10-01 07:30 [macd_momentum_evento] CIERRE FET stop-loss bruto -2.47% neto -2.97%
- 2026-10-01 07:30 [c_banda_atr_tope] CIERRE TRX timeout bruto -0.09% neto -1.19%
- 2026-10-01 07:30 [c_banda_atr_regimen] CIERRE TRX timeout bruto -0.09% neto -0.59%
- 2026-10-01 07:30 [macd_sin_salida] CIERRE POL stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:30 [estocastico_rebote] CIERRE ONDO stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:25 [pullback_tendencia] ENTRADA NIGHT @ 0.03674 (22.46 €, apertura)
- 2026-10-01 07:30 [estocastico_rebote] CIERRE BCH stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:30 [reversion_bb] CIERRE JUP stop-loss bruto -1.50% neto -2.60%
- 2026-10-01 07:30 [c_banda_atr] CIERRE PEPE stop-loss bruto -1.57% neto -2.07%
- 2026-10-01 07:30 [ruptura_volumen] CIERRE PEPE stop-loss bruto -1.42% neto -1.92%
- 2026-10-01 07:30 [macd_sin_salida] CIERRE PEPE stop-loss bruto -1.57% neto -2.07%
- 2026-10-01 07:30 [c_banda_atr_regimen] CIERRE PEPE stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:30 [ruptura_volumen_regimen] CIERRE PEPE stop-loss bruto -1.42% neto -1.92%
- 2026-10-01 07:30 [c_banda_atr_evento] CIERRE PEPE stop-loss bruto -1.57% neto -2.07%
- 2026-10-01 07:30 [ruptura_volumen_evento] CIERRE PEPE stop-loss bruto -1.42% neto -1.92%
- 2026-10-01 07:30 [estocastico_rebote] CIERRE RENDER stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:30 [ruptura_estricta] CIERRE RENDER stop-loss bruto -2.00% neto -2.50%
- 2026-10-01 07:30 [macd_sin_salida] CIERRE RENDER stop-loss bruto -1.69% neto -2.19%
- 2026-10-01 07:30 [macd_sin_salida] CIERRE OP timeout bruto -1.47% neto -1.97%
- 2026-10-01 07:30 [estocastico_rebote] CIERRE MINA stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:30 [ruptura_estricta] CIERRE MINA stop-loss bruto -2.00% neto -2.50%
- 2026-10-01 07:30 [c_banda_atr] CIERRE VVV stop-loss bruto -1.68% neto -2.18%
- 2026-10-01 07:30 [c_banda_atr_regimen] CIERRE VVV stop-loss bruto -1.68% neto -2.18%
- 2026-10-01 07:30 [c_banda_atr_evento] CIERRE VVV stop-loss bruto -1.68% neto -2.18%
- 2026-10-01 07:30 [macd_sin_salida] CIERRE SHIB stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:30 [c_banda_atr] CIERRE DASH stop-loss bruto -1.96% neto -2.46%
- 2026-10-01 07:30 [macd_sin_salida] CIERRE DASH stop-loss bruto -1.96% neto -2.46%
- 2026-10-01 07:30 [c_banda_atr_tope] CIERRE DASH stop-loss bruto -2.01% neto -3.11%
- 2026-10-01 07:30 [c_banda_atr_regimen] CIERRE DASH stop-loss bruto -1.96% neto -2.46%
- 2026-10-01 07:30 [c_banda_atr_evento] CIERRE DASH stop-loss bruto -1.96% neto -2.46%
- 2026-10-01 07:30 [c_banda_atr] CIERRE KSM stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:30 [macd_momentum] CIERRE KSM stop-loss bruto -1.91% neto -2.41%
- 2026-10-01 07:30 [macd_sin_salida] CIERRE KSM stop-loss bruto -1.91% neto -2.41%
- 2026-10-01 07:30 [ruptura_volumen_tope] CIERRE KSM stop-loss bruto -1.91% neto -2.41%
- 2026-10-01 07:30 [c_banda_atr_regimen] CIERRE KSM stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:30 [macd_momentum_regimen] CIERRE KSM stop-loss bruto -1.91% neto -2.41%
- 2026-10-01 07:30 [c_banda_atr_evento] CIERRE KSM stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:30 [macd_momentum_evento] CIERRE KSM stop-loss bruto -1.91% neto -2.41%
- 2026-10-01 07:30 [ruptura_estricta] CIERRE TON stop-loss bruto -2.00% neto -2.50%
- 2026-10-01 07:30 [macd_sin_salida] CIERRE TON stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:30 [macd_sin_salida] CIERRE SKY stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:30 [ruptura_volumen] CIERRE SEI stop-loss bruto -1.49% neto -1.99%
- 2026-10-01 07:30 [macd_momentum] CIERRE SEI momentum perdido bruto -1.49% neto -1.99%
- 2026-10-01 07:30 [ruptura_volumen_tope] CIERRE SEI stop-loss bruto -1.49% neto -1.99%
- 2026-10-01 07:30 [macd_momentum_regimen] CIERRE SEI momentum perdido bruto -1.49% neto -1.99%
- 2026-10-01 07:30 [ruptura_volumen_regimen] CIERRE SEI stop-loss bruto -1.49% neto -1.99%
- 2026-10-01 07:30 [macd_momentum_evento] CIERRE SEI momentum perdido bruto -1.49% neto -1.99%
- 2026-10-01 07:30 [ruptura_volumen_evento] CIERRE SEI stop-loss bruto -1.49% neto -1.99%
- 2026-10-01 07:30 [c_banda_atr] CIERRE APT stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:25 [reversion_bb] ENTRADA APT @ 0.6826 (23.01 €, apertura)
- 2026-10-01 07:30 [macd_momentum] CIERRE APT stop-loss bruto -1.57% neto -2.07%
- 2026-10-01 07:30 [estocastico_rebote] CIERRE APT stop-loss bruto -1.57% neto -2.07%
- 2026-10-01 07:30 [macd_sin_salida] CIERRE APT stop-loss bruto -1.57% neto -2.07%
- 2026-10-01 07:30 [c_banda_atr_regimen] CIERRE APT stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:30 [macd_momentum_regimen] CIERRE APT stop-loss bruto -1.57% neto -2.07%
- 2026-10-01 07:30 [c_banda_atr_evento] CIERRE APT stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 07:30 [macd_momentum_evento] CIERRE APT stop-loss bruto -1.57% neto -2.07%
- 2026-10-01 07:30 [ruptura_volumen] CIERRE SPX stop-loss bruto -2.50% neto -3.00%
- 2026-10-01 07:30 [estocastico_rebote] CIERRE SPX stop-loss bruto -1.53% neto -2.03%
- 2026-10-01 07:30 [ruptura_estricta] CIERRE SPX stop-loss bruto -2.81% neto -3.31%
- 2026-10-01 07:30 [ruptura_volumen_regimen] CIERRE SPX stop-loss bruto -2.50% neto -3.00%
- 2026-10-01 07:30 [ruptura_volumen_evento] CIERRE SPX stop-loss bruto -2.50% neto -3.00%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
