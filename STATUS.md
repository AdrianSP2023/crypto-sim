# Simulación P3 (sin dinero real)

Config `P3-v1` · inicio 2026-09-29 09:43 UTC · última vuelta 2026-09-29 09:56 UTC · vueltas 4 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 924.38 € (+0.02%) | 0 | 5 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| reversion_bb | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| ruptura_volumen | 923.91 € (-0.04%) | 1 | 9 | 0% | -1.200% | -2.300% | -2.512% | -0.53 € |
| rebote_extremo | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| pullback_tendencia | 924.32 € (+0.01%) | 0 | 2 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| macd_momentum | 925.14 € (+0.10%) | 0 | 26 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| estocastico_rebote | 924.23 € (-0.00%) | 1 | 2 | 100% | +1.800% | +0.700% | +0.487% | +0.16 € |
| ruptura_estricta | 923.70 € (-0.06%) | 1 | 6 | 0% | -2.000% | -3.100% | -3.312% | -0.72 € |
| macd_sin_salida | 925.14 € (+0.10%) | 0 | 26 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| c_banda_atr_tope | 924.38 € (+0.02%) | 0 | 5 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| ruptura_volumen_tope | 923.83 € (-0.04%) | 1 | 5 | 0% | -1.200% | -2.300% | -2.512% | -0.53 € |
| c_banda_atr_regimen | 924.38 € (+0.02%) | 0 | 5 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| macd_momentum_regimen | 925.14 € (+0.10%) | 0 | 26 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| ruptura_volumen_regimen | 923.91 € (-0.04%) | 1 | 9 | 0% | -1.200% | -2.300% | -2.512% | -0.53 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-29 09:55 | ruptura_volumen_regimen | PUMP | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-29 09:55 | ruptura_volumen_tope | PUMP | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-29 09:55 | ruptura_estricta | PUMP | stop-loss | -2.00% | -3.10% | -0.72 |
| 2026-09-29 09:55 | estocastico_rebote | QNT | take-profit | +1.80% | +0.70% | +0.16 |
| 2026-09-29 09:55 | ruptura_volumen | PUMP | stop-loss | -1.20% | -2.30% | -0.53 |

## Eventos de la última vuelta

- 2026-09-29 09:50 [macd_momentum] ENTRADA ETH @ 2399 (23.11 €, apertura)
- 2026-09-29 09:50 [macd_sin_salida] ENTRADA ETH @ 2399 (23.11 €, apertura)
- 2026-09-29 09:50 [macd_momentum_regimen] ENTRADA ETH @ 2399 (23.11 €, apertura)
- 2026-09-29 09:55 [estocastico_rebote] CIERRE QNT take-profit bruto +1.80% neto +0.70%
- 2026-09-29 09:50 [macd_momentum] ENTRADA LTC @ 60.65 (23.11 €, apertura)
- 2026-09-29 09:50 [macd_sin_salida] ENTRADA LTC @ 60.65 (23.11 €, apertura)
- 2026-09-29 09:50 [macd_momentum_regimen] ENTRADA LTC @ 60.65 (23.11 €, apertura)
- 2026-09-29 09:50 [macd_momentum] ENTRADA AVAX @ 10.182 (23.11 €, apertura)
- 2026-09-29 09:50 [macd_sin_salida] ENTRADA AVAX @ 10.182 (23.11 €, apertura)
- 2026-09-29 09:50 [macd_momentum_regimen] ENTRADA AVAX @ 10.182 (23.11 €, apertura)
- 2026-09-29 09:55 [ruptura_volumen] CIERRE PUMP stop-loss bruto -1.20% neto -2.30%
- 2026-09-29 09:55 [ruptura_estricta] CIERRE PUMP stop-loss bruto -2.00% neto -3.10%
- 2026-09-29 09:55 [ruptura_volumen_tope] CIERRE PUMP stop-loss bruto -1.20% neto -2.30%
- 2026-09-29 09:55 [ruptura_volumen_regimen] CIERRE PUMP stop-loss bruto -1.20% neto -2.30%
- 2026-09-29 09:50 [ruptura_volumen] ENTRADA ARB @ 0.1841 (23.09 €, apertura)
- 2026-09-29 09:50 [ruptura_estricta] ENTRADA ARB @ 0.1841 (23.09 €, apertura)
- 2026-09-29 09:50 [ruptura_volumen_tope] ENTRADA ARB @ 0.1841 (23.09 €, apertura)
- 2026-09-29 09:50 [ruptura_volumen_regimen] ENTRADA ARB @ 0.1841 (23.09 €, apertura)
- 2026-09-29 09:50 [ruptura_volumen] ENTRADA JUP @ 0.29368 (23.09 €, apertura)
- 2026-09-29 09:50 [ruptura_estricta] ENTRADA JUP @ 0.29368 (23.09 €, apertura)
- 2026-09-29 09:50 [ruptura_volumen_regimen] ENTRADA JUP @ 0.29368 (23.09 €, apertura)
- 2026-09-29 09:50 [ruptura_volumen] ENTRADA ATOM @ 1.5634 (23.09 €, apertura)
- 2026-09-29 09:50 [ruptura_volumen_regimen] ENTRADA ATOM @ 1.5634 (23.09 €, apertura)
- 2026-09-29 09:50 [pullback_tendencia] ENTRADA VIRTUAL @ 0.7231 (23.11 €, apertura)
- 2026-09-29 09:50 [ruptura_volumen] ENTRADA OP @ 0.1174 (23.09 €, apertura)
- 2026-09-29 09:50 [ruptura_estricta] ENTRADA OP @ 0.1174 (23.09 €, apertura)
- 2026-09-29 09:50 [ruptura_volumen_regimen] ENTRADA OP @ 0.1174 (23.09 €, apertura)
- 2026-09-29 09:50 [ruptura_volumen] ENTRADA TRUMP @ 1.799 (23.09 €, apertura)
- 2026-09-29 09:50 [ruptura_estricta] ENTRADA TRUMP @ 1.799 (23.09 €, apertura)
- 2026-09-29 09:50 [ruptura_volumen_regimen] ENTRADA TRUMP @ 1.799 (23.09 €, apertura)
- 2026-09-29 09:50 [macd_momentum] ENTRADA ASTER @ 0.63846 (23.11 €, apertura)
- 2026-09-29 09:50 [macd_sin_salida] ENTRADA ASTER @ 0.63846 (23.11 €, apertura)
- 2026-09-29 09:50 [macd_momentum_regimen] ENTRADA ASTER @ 0.63846 (23.11 €, apertura)

Universo: BTC, XRP, LINK, ETH, SOL, QNT, HBAR, ZEC, NEAR, ADA, SUI, LTC, XLM, AVAX, AAVE, UNI, PUMP, ALGO, TAO, HYPE, ARB, XDC, ONDO, DOGE, DOT, CRV, DASH, ENA, JUP, MON, ICP, BCH, INJ, VVV, TRX, ATOM, RENDER, WLD, ZRO, VIRTUAL, PEPE, USELESS, RAY, SEI, MINA, OP, NIGHT, FIL, SHIB, TON, PENGU, POL, BNB, TRUMP, GRT, ASTER, XPL, KAS, SPX, FET
