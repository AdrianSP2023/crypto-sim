# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 10:11 UTC · vueltas 192 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 896.21 € (-3.03%) | 173 | 7 | 35% | -0.044% | -0.695% | -0.817% | -27.51 € |
| reversion_bb | 918.07 € (-0.67%) | 23 | 10 | 35% | -0.013% | -1.113% | -1.221% | -5.91 € |
| ruptura_volumen | 884.48 € (-4.30%) | 210 | 5 | 23% | -0.205% | -0.829% | -0.939% | -39.55 € |
| rebote_extremo | 922.86 € (-0.15%) | 6 | 3 | 50% | +0.099% | -1.001% | -1.154% | -1.39 € |
| pullback_tendencia | 896.85 € (-2.96%) | 124 | 0 | 15% | -0.255% | -0.968% | -1.073% | -27.39 € |
| macd_momentum | 884.52 € (-4.30%) | 299 | 1 | 22% | +0.001% | -0.586% | -0.694% | -39.75 € |
| estocastico_rebote | 881.81 € (-4.59%) | 232 | 25 | 32% | -0.161% | -0.774% | -0.889% | -40.74 € |
| ruptura_estricta | 890.69 € (-3.63%) | 121 | 3 | 26% | -0.481% | -1.199% | -1.325% | -33.21 € |
| macd_sin_salida | 888.09 € (-3.91%) | 220 | 5 | 36% | -0.092% | -0.710% | -0.824% | -35.69 € |
| c_banda_atr_tope | 913.24 € (-1.19%) | 41 | 1 | 27% | -0.052% | -1.152% | -1.266% | -10.86 € |
| ruptura_volumen_tope | 911.84 € (-1.34%) | 62 | 3 | 27% | +0.067% | -0.859% | -0.976% | -12.25 € |
| c_banda_atr_regimen | 902.71 € (-2.33%) | 108 | 1 | 34% | -0.118% | -0.859% | -1.000% | -21.32 € |
| macd_momentum_regimen | 894.12 € (-3.26%) | 203 | 0 | 22% | -0.022% | -0.651% | -0.763% | -30.12 € |
| ruptura_volumen_regimen | 886.57 € (-4.08%) | 177 | 0 | 20% | -0.288% | -0.936% | -1.049% | -37.67 € |
| c_banda_atr_evento | 902.17 € (-2.39%) | 140 | 7 | 36% | +0.019% | -0.670% | -0.783% | -21.53 € |
| macd_momentum_evento | 889.42 € (-3.77%) | 252 | 1 | 19% | -0.004% | -0.609% | -0.711% | -34.84 € |
| ruptura_volumen_evento | 897.07 € (-2.94%) | 160 | 5 | 24% | -0.073% | -0.738% | -0.836% | -26.95 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 10:10 | ruptura_volumen_evento | VVV | stop-loss | -1.66% | -2.16% | -0.48 |
| 2026-10-01 10:10 | ruptura_volumen_evento | MINA | stop-loss | -1.22% | -1.72% | -0.39 |
| 2026-10-01 10:10 | macd_momentum_evento | BCH | momentum perdido | -0.20% | -0.70% | -0.16 |
| 2026-10-01 10:10 | macd_momentum_evento | HYPE | momentum perdido | -0.17% | -0.67% | -0.15 |
| 2026-10-01 10:10 | c_banda_atr_evento | APT | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 10:10 | c_banda_atr_evento | FIL | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 10:10 | c_banda_atr_evento | CRV | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 10:10 | c_banda_atr_evento | ICP | stop-loss | -1.50% | -2.00% | -0.45 |
| 2026-10-01 10:10 | ruptura_volumen_tope | VVV | stop-loss | -1.66% | -2.16% | -0.49 |
| 2026-10-01 10:10 | c_banda_atr_tope | APT | stop-loss | -1.50% | -2.60% | -0.59 |
| 2026-10-01 10:10 | c_banda_atr_tope | ICP | stop-loss | -1.50% | -2.60% | -0.59 |
| 2026-10-01 10:10 | estocastico_rebote | INJ | stop-loss | -1.58% | -2.08% | -0.46 |
| 2026-10-01 10:10 | macd_momentum | BCH | momentum perdido | -0.20% | -0.70% | -0.15 |
| 2026-10-01 10:10 | macd_momentum | HYPE | momentum perdido | -0.17% | -0.67% | -0.15 |
| 2026-10-01 10:10 | rebote_extremo | USELESS | stop-loss | -2.14% | -3.24% | -0.75 |

## Eventos de la última vuelta

- 2026-10-01 10:10 [macd_momentum] CIERRE HYPE momentum perdido bruto -0.16% neto -0.66%
- 2026-10-01 10:10 [macd_momentum_evento] CIERRE HYPE momentum perdido bruto -0.16% neto -0.66%
- 2026-10-01 10:10 [c_banda_atr] CIERRE ICP stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 10:10 [c_banda_atr_tope] CIERRE ICP stop-loss bruto -1.50% neto -2.60%
- 2026-10-01 10:10 [c_banda_atr_evento] CIERRE ICP stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 10:05 [reversion_bb] ENTRADA FET @ 0.2025 (22.96 €, apertura)
- 2026-10-01 10:10 [c_banda_atr] CIERRE CRV stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 10:10 [c_banda_atr_evento] CIERRE CRV stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 10:10 [rebote_extremo] CIERRE USELESS stop-loss bruto -2.14% neto -3.24%
- 2026-10-01 10:10 [macd_momentum] CIERRE BCH momentum perdido bruto -0.20% neto -0.70%
- 2026-10-01 10:10 [macd_momentum_evento] CIERRE BCH momentum perdido bruto -0.20% neto -0.70%
- 2026-10-01 10:05 [reversion_bb] ENTRADA INJ @ 6.546 (22.96 €, apertura)
- 2026-10-01 10:10 [estocastico_rebote] CIERRE INJ stop-loss bruto -1.58% neto -2.08%
- 2026-10-01 10:10 [ruptura_volumen] CIERRE MINA stop-loss bruto -1.22% neto -1.72%
- 2026-10-01 10:10 [ruptura_volumen_evento] CIERRE MINA stop-loss bruto -1.22% neto -1.72%
- 2026-10-01 10:10 [c_banda_atr] CIERRE FIL stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 10:05 [reversion_bb] ENTRADA FIL @ 0.896 (22.96 €, apertura)
- 2026-10-01 10:10 [c_banda_atr_evento] CIERRE FIL stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 10:10 [ruptura_volumen] CIERRE VVV stop-loss bruto -1.66% neto -2.16%
- 2026-10-01 10:10 [ruptura_volumen_tope] CIERRE VVV stop-loss bruto -1.66% neto -2.16%
- 2026-10-01 10:10 [ruptura_volumen_evento] CIERRE VVV stop-loss bruto -1.66% neto -2.16%
- 2026-10-01 10:10 [c_banda_atr] CIERRE APT stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 10:10 [c_banda_atr_tope] CIERRE APT stop-loss bruto -1.50% neto -2.60%
- 2026-10-01 10:10 [c_banda_atr_evento] CIERRE APT stop-loss bruto -1.50% neto -2.00%

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
