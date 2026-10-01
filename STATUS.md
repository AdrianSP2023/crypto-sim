# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-10-01 21:52 UTC · vueltas 323 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 884.22 € (-4.33%) | 259 | 13 | 35% | -0.054% | -0.655% | -0.777% | -38.54 € |
| reversion_bb | 915.71 € (-0.92%) | 50 | 16 | 50% | +0.330% | -0.692% | -0.789% | -7.97 € |
| ruptura_volumen | 872.21 € (-5.63%) | 292 | 5 | 25% | -0.200% | -0.789% | -0.898% | -51.96 € |
| rebote_extremo | 922.21 € (-0.22%) | 14 | 0 | 57% | +0.472% | -0.628% | -0.806% | -2.03 € |
| pullback_tendencia | 889.00 € (-3.81%) | 185 | 2 | 15% | -0.200% | -0.842% | -0.932% | -35.38 € |
| macd_momentum | 864.14 € (-6.50%) | 476 | 5 | 21% | -0.011% | -0.566% | -0.668% | -60.34 € |
| estocastico_rebote | 872.07 € (-5.64%) | 307 | 22 | 31% | -0.133% | -0.718% | -0.829% | -49.78 € |
| ruptura_estricta | 882.93 € (-4.47%) | 165 | 1 | 25% | -0.432% | -1.092% | -1.208% | -40.99 € |
| macd_sin_salida | 872.36 € (-5.61%) | 330 | 18 | 35% | -0.092% | -0.671% | -0.784% | -50.13 € |
| c_banda_atr_tope | 910.75 € (-1.46%) | 61 | 3 | 30% | +0.002% | -0.931% | -1.047% | -13.04 € |
| ruptura_volumen_tope | 905.86 € (-1.99%) | 98 | 3 | 28% | -0.034% | -0.803% | -0.919% | -18.03 € |
| c_banda_atr_regimen | 896.19 € (-3.04%) | 130 | 8 | 31% | -0.218% | -0.919% | -1.055% | -27.34 € |
| macd_momentum_regimen | 885.34 € (-4.21%) | 273 | 3 | 19% | -0.037% | -0.633% | -0.738% | -39.17 € |
| ruptura_volumen_regimen | 875.43 € (-5.28%) | 225 | 5 | 20% | -0.343% | -0.959% | -1.074% | -48.73 € |
| c_banda_atr_evento | 890.11 € (-3.69%) | 226 | 13 | 35% | -0.017% | -0.634% | -0.750% | -32.64 € |
| macd_momentum_evento | 868.93 € (-5.98%) | 429 | 5 | 19% | -0.015% | -0.577% | -0.676% | -55.56 € |
| ruptura_volumen_evento | 884.62 € (-4.29%) | 242 | 5 | 26% | -0.112% | -0.721% | -0.821% | -39.54 € |
| rebote_desplome | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |
| rebote_desplome_mercado | 925.83 € (+0.17%) | 1 | 0 | 100% | +8.000% | +6.900% | +6.571% | +1.59 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-10-01 21:50 | c_banda_atr_evento | ASTER | stop-loss | -1.54% | -2.04% | -0.46 |
| 2026-10-01 21:50 | c_banda_atr_evento | USELESS | stop-loss | -1.90% | -2.40% | -0.54 |
| 2026-10-01 21:50 | c_banda_atr_regimen | ASTER | stop-loss | -1.54% | -2.04% | -0.46 |
| 2026-10-01 21:50 | c_banda_atr_regimen | USELESS | stop-loss | -1.90% | -2.40% | -0.54 |
| 2026-10-01 21:50 | estocastico_rebote | PUMP | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-01 21:50 | c_banda_atr | ASTER | stop-loss | -1.54% | -2.04% | -0.45 |
| 2026-10-01 21:50 | c_banda_atr | USELESS | stop-loss | -1.90% | -2.40% | -0.53 |
| 2026-10-01 21:45 | c_banda_atr_regimen | PEPE | stop-loss | -1.51% | -2.01% | -0.45 |
| 2026-10-01 21:45 | c_banda_atr_tope | UNI | stop-loss | -1.58% | -2.08% | -0.47 |
| 2026-10-01 21:45 | macd_sin_salida | PEPE | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-01 21:45 | macd_sin_salida | DOT | stop-loss | -1.50% | -2.00% | -0.44 |
| 2026-10-01 21:45 | estocastico_rebote | SPX | timeout | +0.23% | -0.27% | -0.06 |
| 2026-10-01 21:45 | estocastico_rebote | FIL | stop-loss | -1.65% | -2.15% | -0.47 |
| 2026-10-01 21:45 | pullback_tendencia | LTC | rotura de tendencia | +0.10% | -0.40% | -0.09 |
| 2026-10-01 21:45 | reversion_bb | CRV | stop-loss | -1.50% | -2.00% | -0.46 |

## Eventos de la última vuelta

- 2026-10-01 21:45 [reversion_bb] ENTRADA SOL @ 104.41 (22.91 €, apertura)
- 2026-10-01 21:50 [estocastico_rebote] CIERRE PUMP stop-loss bruto -1.50% neto -2.00%
- 2026-10-01 21:45 [reversion_bb] ENTRADA ONDO @ 0.43307 (22.91 €, apertura)
- 2026-10-01 21:50 [c_banda_atr] CIERRE USELESS stop-loss bruto -1.90% neto -2.40%
- 2026-10-01 21:50 [c_banda_atr_regimen] CIERRE USELESS stop-loss bruto -1.90% neto -2.40%
- 2026-10-01 21:50 [c_banda_atr_evento] CIERRE USELESS stop-loss bruto -1.90% neto -2.40%
- 2026-10-01 21:45 [estocastico_rebote] ENTRADA MINA @ 0.1322 (21.86 €, apertura)
- 2026-10-01 21:50 [c_banda_atr] CIERRE ASTER stop-loss bruto -1.54% neto -2.04%
- 2026-10-01 21:50 [c_banda_atr_regimen] CIERRE ASTER stop-loss bruto -1.54% neto -2.04%
- 2026-10-01 21:50 [c_banda_atr_evento] CIERRE ASTER stop-loss bruto -1.54% neto -2.04%
- 2026-10-01 21:45 [macd_momentum] ENTRADA WLFI @ 0.0495 (21.60 €, apertura)
- 2026-10-01 21:45 [macd_sin_salida] ENTRADA WLFI @ 0.0495 (21.85 €, apertura)
- 2026-10-01 21:45 [macd_momentum_evento] ENTRADA WLFI @ 0.0495 (21.72 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
