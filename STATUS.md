# Simulación P4 (sin dinero real)

Config `P4-v1` · inicio 2026-09-30 12:23 UTC · última vuelta 2026-09-30 18:09 UTC · vueltas 42 · 60 activos · velas 5 min · comisión por tramos de volumen 30 d (ida+vuelta 1.10% / 0.50% / 0.42%)

**Avisos:** hueco de 147 min entre vueltas

| Estrategia | Patrimonio | Ops cerradas | Abiertas | Acierto neto | Bruto medio | Neto medio | Neto+spread | PnL realizado |
|---|---|---|---|---|---|---|---|---|
| c_banda_atr | 910.08 € (-1.53%) | 43 | 8 | 30% | -0.331% | -1.389% | -1.543% | -13.77 € |
| reversion_bb | 923.26 € (-0.11%) | 4 | 4 | 75% | +0.750% | -0.350% | -0.460% | -0.33 € |
| ruptura_volumen | 899.43 € (-2.68%) | 71 | 2 | 14% | -0.684% | -1.552% | -1.691% | -25.28 € |
| rebote_extremo | 923.90 € (-0.04%) | 2 | 0 | 50% | +0.370% | -0.731% | -0.847% | -0.34 € |
| pullback_tendencia | 907.37 € (-1.83%) | 51 | 3 | 16% | -0.416% | -1.428% | -1.560% | -16.72 € |
| macd_momentum | 911.27 € (-1.40%) | 68 | 3 | 31% | +0.035% | -0.849% | -0.988% | -13.30 € |
| estocastico_rebote | 912.60 € (-1.26%) | 74 | 33 | 47% | +0.293% | -0.560% | -0.701% | -9.62 € |
| ruptura_estricta | 900.59 € (-2.56%) | 43 | 3 | 9% | -1.345% | -2.438% | -2.588% | -24.15 € |
| macd_sin_salida | 907.19 € (-1.84%) | 62 | 5 | 34% | -0.262% | -1.183% | -1.321% | -16.92 € |
| c_banda_atr_tope | 922.31 € (-0.21%) | 10 | 5 | 50% | +0.251% | -0.849% | -1.019% | -1.96 € |
| ruptura_volumen_tope | 918.83 € (-0.59%) | 17 | 0 | 24% | -0.279% | -1.379% | -1.470% | -5.41 € |
| c_banda_atr_regimen | 909.99 € (-1.54%) | 40 | 5 | 28% | -0.418% | -1.518% | -1.671% | -14.00 € |
| macd_momentum_regimen | 911.47 € (-1.38%) | 59 | 1 | 31% | +0.004% | -0.938% | -1.077% | -12.76 € |
| ruptura_volumen_regimen | 898.81 € (-2.75%) | 70 | 2 | 13% | -0.741% | -1.614% | -1.754% | -25.91 € |
| c_banda_atr_evento | 920.37 € (-0.42%) | 10 | 9 | 30% | -0.477% | -1.577% | -1.709% | -3.64 € |
| macd_momentum_evento | 919.50 € (-0.51%) | 21 | 3 | 29% | +0.051% | -1.049% | -1.191% | -5.08 € |
| ruptura_volumen_evento | 915.40 € (-0.96%) | 21 | 2 | 10% | -0.821% | -1.921% | -2.034% | -9.32 € |
| rebote_desplome | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |
| rebote_desplome_mercado | 924.24 € (+0.00%) | 0 | 0 | 0% | +0.000% | +0.000% | +0.000% | +0.00 € |

## Últimas 15 operaciones cerradas

| Salida (UTC) | Estrategia | Activo | Motivo | Bruto | Neto | € |
|---|---|---|---|---|---|---|
| 2026-09-30 18:05 | ruptura_volumen_evento | JUP | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-30 18:05 | ruptura_volumen_evento | NIGHT | take-profit | +2.50% | +1.40% | +0.32 |
| 2026-09-30 18:05 | ruptura_volumen_evento | ONDO | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-30 18:05 | ruptura_volumen_evento | PUMP | stop-loss | -1.20% | -2.30% | -0.53 |
| 2026-09-30 18:05 | macd_momentum_evento | AVAX | momentum perdido | -0.31% | -1.41% | -0.32 |
| 2026-09-30 18:05 | c_banda_atr_evento | KAS | stop-loss | -1.53% | -2.63% | -0.61 |
| 2026-09-30 18:05 | c_banda_atr_evento | OP | stop-loss | -1.63% | -2.73% | -0.63 |
| 2026-09-30 18:05 | ruptura_volumen_regimen | JUP | stop-loss | -1.20% | -1.70% | -0.38 |
| 2026-09-30 18:05 | ruptura_volumen_regimen | ONDO | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 18:05 | ruptura_volumen_regimen | PUMP | stop-loss | -1.20% | -1.70% | -0.39 |
| 2026-09-30 18:05 | macd_momentum_regimen | AVAX | momentum perdido | -0.31% | -0.81% | -0.18 |
| 2026-09-30 18:05 | c_banda_atr_regimen | KAS | stop-loss | -1.53% | -2.63% | -0.60 |
| 2026-09-30 18:05 | c_banda_atr_regimen | OP | stop-loss | -1.63% | -2.73% | -0.62 |
| 2026-09-30 18:05 | ruptura_volumen_tope | NIGHT | take-profit | +2.50% | +1.40% | +0.32 |
| 2026-09-30 18:05 | macd_sin_salida | TON | timeout | +1.13% | +0.63% | +0.14 |

## Eventos de la última vuelta

- 2026-09-30 15:40 [pullback_tendencia] ENTRADA HBAR @ 0.0951 (22.82 €, apertura)
- 2026-09-30 15:40 [ruptura_volumen] ENTRADA XDC @ 0.03039 (22.63 €, apertura)
- 2026-09-30 15:40 [ruptura_estricta] ENTRADA XDC @ 0.03039 (22.59 €, apertura)
- 2026-09-30 15:40 [ruptura_volumen_tope] ENTRADA XDC @ 0.03039 (23.03 €, apertura)
- 2026-09-30 15:40 [ruptura_volumen_evento] ENTRADA XDC @ 0.03039 (23.11 €, apertura)
- 2026-09-30 15:45 [pullback_tendencia] CIERRE ASTER rotura de tendencia bruto -0.46% neto -1.56%
- 2026-09-30 15:45 [ruptura_estricta] CIERRE WLFI timeout bruto -1.20% neto -2.30%
- 2026-09-30 15:45 [macd_sin_salida] CIERRE XMR timeout bruto -0.69% neto -1.49%
- 2026-09-30 15:50 [estocastico_rebote] CIERRE SUI take-profit bruto +1.80% neto +1.00%
- 2026-09-30 15:50 [estocastico_rebote] CIERRE TRX timeout bruto -0.29% neto -1.09%
- 2026-09-30 15:50 [estocastico_rebote] CIERRE XDC take-profit bruto +2.48% neto +1.68%
- 2026-09-30 15:50 [estocastico_rebote] CIERRE MINA take-profit bruto +1.80% neto +1.00%
- 2026-09-30 15:50 [macd_momentum] CIERRE ASTER momentum perdido bruto -0.85% neto -1.35%
- 2026-09-30 15:50 [macd_momentum_evento] CIERRE ASTER momentum perdido bruto -0.85% neto -1.95%
- 2026-09-30 15:50 [macd_momentum] ENTRADA NEAR @ 4.6468 (22.78 €, apertura)
- 2026-09-30 15:50 [macd_sin_salida] ENTRADA NEAR @ 4.6468 (22.70 €, apertura)
- 2026-09-30 15:50 [macd_momentum_regimen] ENTRADA NEAR @ 4.6468 (22.80 €, apertura)
- 2026-09-30 15:50 [macd_momentum_evento] ENTRADA NEAR @ 4.6468 (23.04 €, apertura)
- 2026-09-30 15:50 [ruptura_volumen] ENTRADA HYPE @ 76.9 (22.63 €, apertura)
- 2026-09-30 15:50 [ruptura_volumen_tope] ENTRADA HYPE @ 76.9 (23.03 €, apertura)
- 2026-09-30 15:50 [ruptura_volumen_regimen] ENTRADA HYPE @ 76.9 (22.63 €, apertura)
- 2026-09-30 15:50 [ruptura_volumen_evento] ENTRADA HYPE @ 76.9 (23.11 €, apertura)
- 2026-09-30 15:55 [estocastico_rebote] CIERRE UNI take-profit bruto +1.87% neto +1.07%
- 2026-09-30 15:50 [macd_momentum] ENTRADA ENA @ 0.2381 (22.78 €, apertura)
- 2026-09-30 15:50 [macd_sin_salida] ENTRADA ENA @ 0.2381 (22.70 €, apertura)
- 2026-09-30 15:50 [macd_momentum_regimen] ENTRADA ENA @ 0.2381 (22.80 €, apertura)
- 2026-09-30 15:50 [macd_momentum_evento] ENTRADA ENA @ 0.2381 (23.04 €, apertura)
- 2026-09-30 15:50 [ruptura_volumen_regimen] ENTRADA XDC @ 0.03065 (22.63 €, apertura)
- 2026-09-30 15:55 [ruptura_volumen_regimen] CIERRE XDC stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 15:55 [estocastico_rebote] CIERRE USELESS take-profit bruto +1.80% neto +1.00%
- 2026-09-30 15:50 [macd_momentum] ENTRADA MON @ 0.02453 (22.78 €, apertura)
- 2026-09-30 15:50 [macd_sin_salida] ENTRADA MON @ 0.02453 (22.70 €, apertura)
- 2026-09-30 15:50 [macd_momentum_regimen] ENTRADA MON @ 0.02453 (22.80 €, apertura)
- 2026-09-30 15:50 [macd_momentum_evento] ENTRADA MON @ 0.02453 (23.04 €, apertura)
- 2026-09-30 15:50 [c_banda_atr] ENTRADA DASH @ 54.138 (22.86 €, apertura)
- 2026-09-30 15:50 [c_banda_atr_regimen] ENTRADA DASH @ 54.138 (22.86 €, apertura)
- 2026-09-30 15:50 [c_banda_atr_evento] ENTRADA DASH @ 54.138 (23.11 €, apertura)
- 2026-09-30 15:55 [c_banda_atr] ENTRADA ONDO @ 0.44205 (22.86 €, apertura)
- 2026-09-30 15:55 [c_banda_atr_regimen] ENTRADA ONDO @ 0.44205 (22.86 €, apertura)
- 2026-09-30 15:55 [c_banda_atr_evento] ENTRADA ONDO @ 0.44205 (23.11 €, apertura)
- 2026-09-30 15:55 [macd_momentum] ENTRADA VVV @ 24.725 (22.78 €, apertura)
- 2026-09-30 15:55 [macd_sin_salida] ENTRADA VVV @ 24.725 (22.70 €, apertura)
- 2026-09-30 15:55 [macd_momentum_regimen] ENTRADA VVV @ 24.725 (22.80 €, apertura)
- 2026-09-30 15:55 [macd_momentum_evento] ENTRADA VVV @ 24.725 (23.04 €, apertura)
- 2026-09-30 16:05 [estocastico_rebote] CIERRE NEAR take-profit bruto +1.80% neto +1.30%
- 2026-09-30 16:05 [macd_momentum] CIERRE SUI take-profit bruto +2.00% neto +1.50%
- 2026-09-30 16:05 [macd_sin_salida] CIERRE SUI take-profit bruto +2.00% neto +1.50%
- 2026-09-30 16:05 [macd_momentum_evento] CIERRE SUI take-profit bruto +2.00% neto +0.90%
- 2026-09-30 16:00 [ruptura_volumen] ENTRADA UNI @ 7.9478 (22.63 €, apertura)
- 2026-09-30 16:00 [ruptura_volumen_tope] ENTRADA UNI @ 7.9478 (23.03 €, apertura)
- 2026-09-30 16:00 [ruptura_volumen_regimen] ENTRADA UNI @ 7.9478 (22.62 €, apertura)
- 2026-09-30 16:00 [ruptura_volumen_evento] ENTRADA UNI @ 7.9478 (23.11 €, apertura)
- 2026-09-30 16:05 [estocastico_rebote] CIERRE DOT take-profit bruto +1.80% neto +1.00%
- 2026-09-30 16:05 [reversion_bb] CIERRE ARB take-profit bruto +1.50% neto +0.40%
- 2026-09-30 16:05 [estocastico_rebote] CIERRE ARB take-profit bruto +1.80% neto +1.00%
- 2026-09-30 16:05 [estocastico_rebote] CIERRE FET take-profit bruto +2.12% neto +1.32%
- 2026-09-30 16:05 [estocastico_rebote] CIERRE RENDER take-profit bruto +1.80% neto +1.00%
- 2026-09-30 16:05 [estocastico_rebote] CIERRE VVV take-profit bruto +2.00% neto +1.20%
- 2026-09-30 16:05 [c_banda_atr] CIERRE KSM take-profit bruto +2.00% neto +0.90%
- 2026-09-30 16:05 [macd_momentum] CIERRE KSM take-profit bruto +2.00% neto +1.50%
- 2026-09-30 16:05 [macd_sin_salida] CIERRE KSM take-profit bruto +2.00% neto +1.50%
- 2026-09-30 16:05 [c_banda_atr_tope] CIERRE KSM take-profit bruto +2.00% neto +0.90%
- 2026-09-30 16:05 [c_banda_atr_evento] CIERRE KSM take-profit bruto +2.00% neto +0.90%
- 2026-09-30 16:05 [macd_momentum_evento] CIERRE KSM take-profit bruto +2.00% neto +0.90%
- 2026-09-30 16:05 [macd_sin_salida] CIERRE SPX take-profit bruto +2.00% neto +1.50%
- 2026-09-30 16:10 [estocastico_rebote] CIERRE ADA take-profit bruto +1.80% neto +1.30%
- 2026-09-30 16:10 [estocastico_rebote] CIERRE ZEC take-profit bruto +1.80% neto +1.30%
- 2026-09-30 16:10 [estocastico_rebote] CIERRE TAO take-profit bruto +1.83% neto +1.03%
- 2026-09-30 16:05 [macd_momentum] ENTRADA WLD @ 0.4792 (22.80 €, apertura)
- 2026-09-30 16:10 [estocastico_rebote] CIERRE WLD take-profit bruto +2.13% neto +1.63%
- 2026-09-30 16:05 [macd_sin_salida] ENTRADA WLD @ 0.4792 (22.73 €, apertura)
- 2026-09-30 16:05 [macd_momentum_regimen] ENTRADA WLD @ 0.4792 (22.80 €, apertura)
- 2026-09-30 16:05 [macd_momentum_evento] ENTRADA WLD @ 0.4792 (23.05 €, apertura)
- 2026-09-30 16:10 [estocastico_rebote] CIERRE NIGHT stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 16:10 [macd_momentum] CIERRE MON take-profit bruto +2.00% neto +1.50%
- 2026-09-30 16:10 [macd_sin_salida] CIERRE MON take-profit bruto +2.00% neto +1.50%
- 2026-09-30 16:10 [macd_momentum_regimen] CIERRE MON take-profit bruto +2.00% neto +1.50%
- 2026-09-30 16:10 [macd_momentum_evento] CIERRE MON take-profit bruto +2.00% neto +0.90%
- 2026-09-30 16:05 [c_banda_atr_tope] ENTRADA XMR @ 477.46 (23.07 €, apertura)
- 2026-09-30 16:05 [c_banda_atr_evento] ENTRADA XMR @ 477.46 (23.11 €, apertura)
- 2026-09-30 16:05 [c_banda_atr] ENTRADA SEI @ 0.06468 (22.87 €, apertura)
- 2026-09-30 16:05 [c_banda_atr_regimen] ENTRADA SEI @ 0.06468 (22.86 €, apertura)
- 2026-09-30 16:05 [c_banda_atr_evento] ENTRADA SEI @ 0.06468 (23.11 €, apertura)
- 2026-09-30 16:10 [c_banda_atr] CIERRE SPX take-profit bruto +2.00% neto +0.90%
- 2026-09-30 16:05 [ruptura_volumen] ENTRADA SPX @ 0.3938 (22.63 €, apertura)
- 2026-09-30 16:10 [macd_momentum] CIERRE SPX take-profit bruto +2.00% neto +1.50%
- 2026-09-30 16:05 [ruptura_volumen_tope] ENTRADA SPX @ 0.3938 (23.03 €, apertura)
- 2026-09-30 16:05 [ruptura_volumen_regimen] ENTRADA SPX @ 0.3938 (22.62 €, apertura)
- 2026-09-30 16:10 [c_banda_atr_evento] CIERRE SPX take-profit bruto +2.00% neto +0.90%
- 2026-09-30 16:10 [macd_momentum_evento] CIERRE SPX take-profit bruto +2.00% neto +0.90%
- 2026-09-30 16:05 [ruptura_volumen_evento] ENTRADA SPX @ 0.3938 (23.11 €, apertura)
- 2026-09-30 16:10 [ruptura_volumen] ENTRADA SUI @ 1.0544 (22.63 €, apertura)
- 2026-09-30 16:10 [ruptura_volumen_tope] ENTRADA SUI @ 1.0544 (23.03 €, apertura)
- 2026-09-30 16:10 [ruptura_volumen_regimen] ENTRADA SUI @ 1.0544 (22.62 €, apertura)
- 2026-09-30 16:10 [ruptura_volumen_evento] ENTRADA SUI @ 1.0544 (23.11 €, apertura)
- 2026-09-30 16:15 [estocastico_rebote] CIERRE ENA take-profit bruto +1.80% neto +1.30%
- 2026-09-30 16:10 [ruptura_volumen] ENTRADA MON @ 0.0251 (22.63 €, apertura)
- 2026-09-30 16:15 [ruptura_volumen] CIERRE MON stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 16:10 [ruptura_estricta] ENTRADA MON @ 0.0251 (22.58 €, apertura)
- 2026-09-30 16:10 [ruptura_volumen_regimen] ENTRADA MON @ 0.0251 (22.62 €, apertura)
- 2026-09-30 16:15 [ruptura_volumen_regimen] CIERRE MON stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 16:10 [ruptura_volumen_evento] ENTRADA MON @ 0.0251 (23.11 €, apertura)
- 2026-09-30 16:15 [ruptura_volumen_evento] CIERRE MON stop-loss bruto -1.20% neto -2.30%
- 2026-09-30 16:20 [macd_sin_salida] CIERRE TRX timeout bruto -0.43% neto -1.23%
- 2026-09-30 16:20 [estocastico_rebote] ENTRADA NIGHT @ 0.0321 (22.87 €, apertura)
- 2026-09-30 16:25 [estocastico_rebote] CIERRE NIGHT take-profit bruto +1.80% neto +1.30%
- 2026-09-30 16:25 [pullback_tendencia] ENTRADA QNT @ 264.92 (22.81 €, apertura)
- 2026-09-30 16:30 [macd_momentum] CIERRE NEAR take-profit bruto +2.00% neto +1.50%
- 2026-09-30 16:30 [macd_sin_salida] CIERRE NEAR take-profit bruto +2.00% neto +1.50%
- 2026-09-30 16:30 [macd_momentum_regimen] CIERRE NEAR take-profit bruto +2.00% neto +1.50%
- 2026-09-30 16:30 [macd_momentum_evento] CIERRE NEAR take-profit bruto +2.00% neto +0.90%
- 2026-09-30 16:30 [reversion_bb] CIERRE CRV take-profit bruto +1.50% neto +0.40%
- 2026-09-30 16:30 [ruptura_estricta] CIERRE XMR timeout bruto -0.17% neto -1.27%
- 2026-09-30 16:25 [ruptura_estricta] ENTRADA SPX @ 0.3987 (22.57 €, apertura)
- 2026-09-30 16:35 [pullback_tendencia] CIERRE HBAR rotura de tendencia bruto -0.13% neto -1.23%
- 2026-09-30 16:30 [ruptura_volumen] ENTRADA FET @ 0.1992 (22.62 €, apertura)
- 2026-09-30 16:30 [ruptura_volumen_regimen] ENTRADA FET @ 0.1992 (22.61 €, apertura)
- 2026-09-30 16:30 [ruptura_volumen_evento] ENTRADA FET @ 0.1992 (23.09 €, apertura)
- 2026-09-30 16:30 [macd_momentum] ENTRADA NIGHT @ 0.03272 (22.82 €, apertura)
- 2026-09-30 16:30 [macd_sin_salida] ENTRADA NIGHT @ 0.03272 (22.74 €, apertura)
- 2026-09-30 16:30 [macd_momentum_regimen] ENTRADA NIGHT @ 0.03272 (22.82 €, apertura)
- 2026-09-30 16:30 [macd_momentum_evento] ENTRADA NIGHT @ 0.03272 (23.07 €, apertura)
- 2026-09-30 16:35 [macd_momentum] CIERRE VVV momentum perdido bruto -1.00% neto -1.50%
- 2026-09-30 16:35 [macd_momentum_regimen] CIERRE VVV momentum perdido bruto -1.00% neto -1.50%
- 2026-09-30 16:35 [macd_momentum_evento] CIERRE VVV momentum perdido bruto -1.00% neto -2.10%
- 2026-09-30 16:35 [c_banda_atr] CIERRE WLFI timeout bruto -0.80% neto -1.90%
- 2026-09-30 16:35 [c_banda_atr_regimen] CIERRE WLFI timeout bruto -0.80% neto -1.90%
- 2026-09-30 16:30 [ruptura_volumen] ENTRADA KSM @ 4.62 (22.62 €, apertura)
- 2026-09-30 16:30 [ruptura_estricta] ENTRADA KSM @ 4.62 (22.57 €, apertura)
- 2026-09-30 16:30 [ruptura_volumen_regimen] ENTRADA KSM @ 4.62 (22.61 €, apertura)
- 2026-09-30 16:30 [ruptura_volumen_evento] ENTRADA KSM @ 4.62 (23.09 €, apertura)
- 2026-09-30 16:35 [c_banda_atr] CIERRE TRUMP timeout bruto -0.54% neto -1.64%
- 2026-09-30 16:35 [c_banda_atr_regimen] CIERRE TRUMP timeout bruto -0.54% neto -1.64%
- 2026-09-30 16:35 [c_banda_atr] CIERRE BNB timeout bruto -0.41% neto -1.51%
- 2026-09-30 16:35 [c_banda_atr_regimen] CIERRE BNB timeout bruto -0.41% neto -1.51%
- 2026-09-30 16:30 [ruptura_volumen] ENTRADA XMR @ 479.63 (22.62 €, apertura)
- 2026-09-30 16:30 [ruptura_volumen_regimen] ENTRADA XMR @ 479.63 (22.61 €, apertura)
- 2026-09-30 16:30 [ruptura_volumen_evento] ENTRADA XMR @ 479.63 (23.09 €, apertura)
- 2026-09-30 16:40 [macd_momentum] CIERRE HBAR momentum perdido bruto -0.74% neto -1.24%
- 2026-09-30 16:40 [macd_momentum_evento] CIERRE HBAR momentum perdido bruto -0.74% neto -1.84%
- 2026-09-30 16:40 [ruptura_volumen] CIERRE HYPE take-profit bruto +2.50% neto +2.00%
- 2026-09-30 16:40 [ruptura_volumen_tope] CIERRE HYPE take-profit bruto +2.50% neto +1.40%
- 2026-09-30 16:40 [ruptura_volumen_regimen] CIERRE HYPE take-profit bruto +2.50% neto +2.00%
- 2026-09-30 16:40 [ruptura_volumen_evento] CIERRE HYPE take-profit bruto +2.50% neto +1.40%
- 2026-09-30 16:35 [pullback_tendencia] ENTRADA ARB @ 0.1801 (22.80 €, apertura)
- 2026-09-30 16:40 [pullback_tendencia] CIERRE ARB rotura de tendencia bruto +0.06% neto -1.04%
- 2026-09-30 16:40 [estocastico_rebote] CIERRE ONDO take-profit bruto +1.80% neto +1.00%
- 2026-09-30 16:40 [ruptura_estricta] CIERRE MON stop-loss bruto -2.00% neto -3.10%
- 2026-09-30 16:40 [macd_momentum] CIERRE TRUMP momentum perdido bruto -0.49% neto -0.99%
- 2026-09-30 16:40 [macd_momentum_evento] CIERRE TRUMP momentum perdido bruto -0.49% neto -1.59%
- 2026-09-30 16:35 [pullback_tendencia] ENTRADA TON @ 1.326 (22.80 €, apertura)
- 2026-09-30 16:40 [c_banda_atr] CIERRE XMR timeout bruto +0.32% neto -0.78%
- 2026-09-30 16:40 [c_banda_atr_regimen] CIERRE XMR timeout bruto +0.32% neto -0.78%
- 2026-09-30 16:45 [estocastico_rebote] CIERRE XLM take-profit bruto +1.80% neto +1.00%
- 2026-09-30 16:40 [pullback_tendencia] ENTRADA MON @ 0.02493 (22.80 €, apertura)
- 2026-09-30 16:40 [pullback_tendencia] ENTRADA BNB @ 678.88 (22.80 €, apertura)
- 2026-09-30 16:45 [ruptura_volumen] ENTRADA NEAR @ 4.8169 (22.63 €, apertura)
- 2026-09-30 16:45 [ruptura_estricta] ENTRADA NEAR @ 4.8169 (22.55 €, apertura)
- 2026-09-30 16:45 [ruptura_volumen_tope] ENTRADA NEAR @ 4.8169 (23.04 €, apertura)
- 2026-09-30 16:45 [ruptura_volumen_regimen] ENTRADA NEAR @ 4.8169 (22.62 €, apertura)
- 2026-09-30 16:45 [ruptura_volumen_evento] ENTRADA NEAR @ 4.8169 (23.10 €, apertura)
- 2026-09-30 16:50 [c_banda_atr] CIERRE ONDO take-profit bruto +2.00% neto +0.90%
- 2026-09-30 16:45 [ruptura_volumen] ENTRADA ONDO @ 0.45021 (22.63 €, apertura)
- 2026-09-30 16:50 [c_banda_atr_regimen] CIERRE ONDO take-profit bruto +2.00% neto +0.90%
- 2026-09-30 16:45 [ruptura_volumen_regimen] ENTRADA ONDO @ 0.45021 (22.62 €, apertura)
- 2026-09-30 16:50 [c_banda_atr_evento] CIERRE ONDO take-profit bruto +2.00% neto +0.90%
- 2026-09-30 16:45 [ruptura_volumen_evento] ENTRADA ONDO @ 0.45021 (23.10 €, apertura)
- 2026-09-30 16:45 [c_banda_atr] ENTRADA WLD @ 0.4793 (22.84 €, apertura)
- 2026-09-30 16:45 [c_banda_atr_regimen] ENTRADA WLD @ 0.4793 (22.83 €, apertura)
- 2026-09-30 16:45 [c_banda_atr_evento] ENTRADA WLD @ 0.4793 (23.12 €, apertura)
- 2026-09-30 16:45 [pullback_tendencia] ENTRADA XDC @ 0.03024 (22.80 €, apertura)
- 2026-09-30 16:50 [estocastico_rebote] CIERRE BCH take-profit bruto +1.84% neto +1.04%
- 2026-09-30 16:45 [c_banda_atr] ENTRADA INJ @ 6.558 (22.84 €, apertura)
- 2026-09-30 16:45 [c_banda_atr_regimen] ENTRADA INJ @ 6.558 (22.83 €, apertura)
- 2026-09-30 16:45 [c_banda_atr_evento] ENTRADA INJ @ 6.558 (23.12 €, apertura)
- 2026-09-30 16:45 [c_banda_atr] ENTRADA OP @ 0.1168 (22.84 €, apertura)
- 2026-09-30 16:45 [c_banda_atr_regimen] ENTRADA OP @ 0.1168 (22.83 €, apertura)
- 2026-09-30 16:45 [c_banda_atr_evento] ENTRADA OP @ 0.1168 (23.12 €, apertura)
- 2026-09-30 16:50 [estocastico_rebote] CIERRE PENGU take-profit bruto +1.80% neto +1.00%
- 2026-09-30 16:50 [pullback_tendencia] ENTRADA HBAR @ 0.09526 (22.80 €, apertura)
- 2026-09-30 16:50 [ruptura_volumen] ENTRADA AAVE @ 142.43 (22.63 €, apertura)
- 2026-09-30 16:50 [ruptura_volumen_regimen] ENTRADA AAVE @ 142.43 (22.62 €, apertura)
- 2026-09-30 16:50 [ruptura_volumen_evento] ENTRADA AAVE @ 142.43 (23.10 €, apertura)
- 2026-09-30 16:50 [ruptura_volumen] ENTRADA ZEC @ 1301.75 (22.63 €, apertura)
- 2026-09-30 16:50 [ruptura_volumen_regimen] ENTRADA ZEC @ 1301.75 (22.62 €, apertura)
- 2026-09-30 16:50 [ruptura_volumen_evento] ENTRADA ZEC @ 1301.75 (23.10 €, apertura)
- 2026-09-30 16:55 [pullback_tendencia] CIERRE XDC rotura de tendencia bruto -0.36% neto -1.46%
- 2026-09-30 16:50 [c_banda_atr] ENTRADA USELESS @ 0.22143 (22.84 €, apertura)
- 2026-09-30 16:50 [c_banda_atr_regimen] ENTRADA USELESS @ 0.22143 (22.83 €, apertura)
- 2026-09-30 16:50 [c_banda_atr_evento] ENTRADA USELESS @ 0.22143 (23.12 €, apertura)
- 2026-09-30 16:50 [ruptura_volumen] ENTRADA PEPE @ 3.856e-06 (22.63 €, apertura)
- 2026-09-30 16:50 [ruptura_volumen_regimen] ENTRADA PEPE @ 3.856e-06 (22.62 €, apertura)
- 2026-09-30 16:50 [ruptura_volumen_evento] ENTRADA PEPE @ 3.856e-06 (23.10 €, apertura)
- 2026-09-30 16:55 [estocastico_rebote] CIERRE ASTER timeout bruto -1.05% neto -1.85%
- 2026-09-30 16:50 [ruptura_volumen] ENTRADA DASH @ 54.609 (22.63 €, apertura)
- 2026-09-30 16:50 [ruptura_volumen_regimen] ENTRADA DASH @ 54.609 (22.62 €, apertura)
- 2026-09-30 16:50 [ruptura_volumen_evento] ENTRADA DASH @ 54.609 (23.10 €, apertura)
- 2026-09-30 16:50 [ruptura_volumen] ENTRADA PENGU @ 0.008832 (22.63 €, apertura)
- 2026-09-30 16:50 [ruptura_volumen_regimen] ENTRADA PENGU @ 0.008832 (22.62 €, apertura)
- 2026-09-30 16:50 [ruptura_volumen_evento] ENTRADA PENGU @ 0.008832 (23.10 €, apertura)
- 2026-09-30 16:55 [estocastico_rebote] CIERRE BNB timeout bruto +0.17% neto -0.63%
- 2026-09-30 16:50 [c_banda_atr] ENTRADA TON @ 1.338 (22.84 €, apertura)
- 2026-09-30 16:50 [c_banda_atr_regimen] ENTRADA TON @ 1.338 (22.83 €, apertura)
- 2026-09-30 16:50 [c_banda_atr_evento] ENTRADA TON @ 1.338 (23.12 €, apertura)
- 2026-09-30 16:50 [c_banda_atr] ENTRADA KAS @ 0.0385 (22.84 €, apertura)
- 2026-09-30 16:50 [ruptura_volumen] ENTRADA KAS @ 0.0385 (22.63 €, apertura)
- 2026-09-30 16:50 [c_banda_atr_regimen] ENTRADA KAS @ 0.0385 (22.83 €, apertura)
- 2026-09-30 16:50 [ruptura_volumen_regimen] ENTRADA KAS @ 0.0385 (22.62 €, apertura)
- 2026-09-30 16:50 [c_banda_atr_evento] ENTRADA KAS @ 0.0385 (23.12 €, apertura)
- 2026-09-30 16:50 [ruptura_volumen_evento] ENTRADA KAS @ 0.0385 (23.10 €, apertura)
- 2026-09-30 16:50 [ruptura_volumen] ENTRADA SEI @ 0.06564 (22.63 €, apertura)
- 2026-09-30 16:50 [ruptura_volumen_regimen] ENTRADA SEI @ 0.06564 (22.62 €, apertura)
- 2026-09-30 16:50 [ruptura_volumen_evento] ENTRADA SEI @ 0.06564 (23.10 €, apertura)
- 2026-09-30 16:55 [ruptura_volumen] ENTRADA PUMP @ 0.005211 (22.63 €, apertura)
- 2026-09-30 16:55 [ruptura_volumen_regimen] ENTRADA PUMP @ 0.005211 (22.62 €, apertura)
- 2026-09-30 16:55 [ruptura_volumen_evento] ENTRADA PUMP @ 0.005211 (23.10 €, apertura)
- 2026-09-30 16:55 [macd_momentum] ENTRADA VVV @ 24.584 (22.80 €, apertura)
- 2026-09-30 16:55 [macd_momentum_regimen] ENTRADA VVV @ 24.584 (22.81 €, apertura)
- 2026-09-30 16:55 [macd_momentum_evento] ENTRADA VVV @ 24.584 (23.03 €, apertura)
- 2026-09-30 16:55 [c_banda_atr] ENTRADA WLFI @ 0.0496 (22.84 €, apertura)
- 2026-09-30 16:55 [c_banda_atr_regimen] ENTRADA WLFI @ 0.0496 (22.83 €, apertura)
- 2026-09-30 16:55 [c_banda_atr_evento] ENTRADA WLFI @ 0.0496 (23.12 €, apertura)
- 2026-09-30 16:55 [estocastico_rebote] ENTRADA TRUMP @ 1.834 (22.89 €, apertura)
- 2026-09-30 17:05 [ruptura_volumen] CIERRE NEAR stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 17:05 [ruptura_volumen_tope] CIERRE NEAR stop-loss bruto -1.20% neto -2.30%
- 2026-09-30 17:05 [ruptura_volumen_regimen] CIERRE NEAR stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 17:05 [ruptura_volumen_evento] CIERRE NEAR stop-loss bruto -1.20% neto -2.30%
- 2026-09-30 17:05 [pullback_tendencia] CIERRE HBAR rotura de tendencia bruto -0.69% neto -1.79%
- 2026-09-30 17:00 [estocastico_rebote] ENTRADA TRX @ 0.297989 (22.89 €, apertura)
- 2026-09-30 17:05 [c_banda_atr] CIERRE USELESS stop-loss bruto -1.50% neto -2.30%
- 2026-09-30 17:05 [c_banda_atr_regimen] CIERRE USELESS stop-loss bruto -1.50% neto -2.60%
- 2026-09-30 17:05 [c_banda_atr_evento] CIERRE USELESS stop-loss bruto -1.50% neto -2.60%
- 2026-09-30 17:05 [ruptura_volumen] CIERRE KSM stop-loss bruto -1.30% neto -1.80%
- 2026-09-30 17:05 [ruptura_volumen_regimen] CIERRE KSM stop-loss bruto -1.30% neto -1.80%
- 2026-09-30 17:05 [ruptura_volumen_evento] CIERRE KSM stop-loss bruto -1.30% neto -2.40%
- 2026-09-30 17:00 [ruptura_volumen_tope] ENTRADA XMR @ 483.32 (23.02 €, apertura)
- 2026-09-30 17:05 [macd_momentum] ENTRADA QNT @ 268.39 (22.80 €, apertura)
- 2026-09-30 17:05 [macd_sin_salida] ENTRADA QNT @ 268.39 (22.74 €, apertura)
- 2026-09-30 17:05 [macd_momentum_regimen] ENTRADA QNT @ 268.39 (22.81 €, apertura)
- 2026-09-30 17:05 [macd_momentum_evento] ENTRADA QNT @ 268.39 (23.03 €, apertura)
- 2026-09-30 17:05 [ruptura_volumen] ENTRADA HYPE @ 79.77 (22.61 €, apertura)
- 2026-09-30 17:05 [ruptura_volumen_regimen] ENTRADA HYPE @ 79.77 (22.60 €, apertura)
- 2026-09-30 17:05 [ruptura_volumen_evento] ENTRADA HYPE @ 79.77 (23.07 €, apertura)
- 2026-09-30 17:05 [pullback_tendencia] ENTRADA LTC @ 59.31 (22.78 €, apertura)
- 2026-09-30 17:10 [macd_momentum] CIERRE ENA momentum perdido bruto +0.29% neto -0.21%
- 2026-09-30 17:10 [macd_momentum_regimen] CIERRE ENA momentum perdido bruto +0.29% neto -0.21%
- 2026-09-30 17:10 [macd_momentum_evento] CIERRE ENA momentum perdido bruto +0.29% neto -0.81%
- 2026-09-30 17:05 [pullback_tendencia] ENTRADA USELESS @ 0.2187 (22.78 €, apertura)
- 2026-09-30 17:05 [pullback_tendencia] ENTRADA KSM @ 4.61 (22.78 €, apertura)
- 2026-09-30 17:10 [estocastico_rebote] CIERRE APT take-profit bruto +1.85% neto +1.05%
- 2026-09-30 17:10 [pullback_tendencia] ENTRADA NEAR @ 4.7556 (22.78 €, apertura)
- 2026-09-30 17:10 [pullback_tendencia] ENTRADA ICP @ 3.08 (22.78 €, apertura)
- 2026-09-30 17:10 [ruptura_volumen] ENTRADA JUP @ 0.29425 (22.61 €, apertura)
- 2026-09-30 17:10 [ruptura_volumen_regimen] ENTRADA JUP @ 0.29425 (22.60 €, apertura)
- 2026-09-30 17:10 [ruptura_volumen_evento] ENTRADA JUP @ 0.29425 (23.07 €, apertura)
- 2026-09-30 17:10 [pullback_tendencia] ENTRADA SPX @ 0.394 (22.78 €, apertura)
- 2026-09-30 17:20 [ruptura_estricta] CIERRE NEAR stop-loss bruto -2.00% neto -3.10%
- 2026-09-30 17:20 [ruptura_volumen] CIERRE ZEC stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 17:20 [ruptura_volumen_regimen] CIERRE ZEC stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 17:20 [ruptura_volumen_evento] CIERRE ZEC stop-loss bruto -1.20% neto -2.30%
- 2026-09-30 17:20 [pullback_tendencia] CIERRE LTC rotura de tendencia bruto -0.35% neto -1.45%
- 2026-09-30 17:20 [pullback_tendencia] CIERRE MON take-profit bruto +2.00% neto +0.90%
- 2026-09-30 17:20 [c_banda_atr] CIERRE ASTER stop-loss bruto -1.50% neto -2.30%
- 2026-09-30 17:20 [macd_sin_salida] CIERRE ASTER stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 17:20 [c_banda_atr_tope] CIERRE ASTER stop-loss bruto -1.50% neto -2.60%
- 2026-09-30 17:20 [c_banda_atr_evento] CIERRE ASTER stop-loss bruto -1.50% neto -2.60%
- 2026-09-30 17:20 [ruptura_estricta] CIERRE SPX stop-loss bruto -2.00% neto -3.10%
- 2026-09-30 17:25 [macd_momentum] CIERRE QNT stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 17:25 [macd_sin_salida] CIERRE QNT stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 17:25 [macd_momentum_regimen] CIERRE QNT stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 17:25 [macd_momentum_evento] CIERRE QNT stop-loss bruto -1.50% neto -2.60%
- 2026-09-30 17:20 [pullback_tendencia] ENTRADA ADA @ 0.218582 (22.77 €, apertura)
- 2026-09-30 17:25 [pullback_tendencia] CIERRE ADA rotura de tendencia bruto -0.22% neto -1.32%
- 2026-09-30 17:20 [pullback_tendencia] ENTRADA ZEC @ 1288.89 (22.77 €, apertura)
- 2026-09-30 17:20 [estocastico_rebote] ENTRADA XDC @ 0.03023 (22.89 €, apertura)
- 2026-09-30 17:20 [ruptura_volumen] ENTRADA MON @ 0.02532 (22.60 €, apertura)
- 2026-09-30 17:20 [ruptura_estricta] ENTRADA MON @ 0.02532 (22.52 €, apertura)
- 2026-09-30 17:20 [ruptura_volumen_regimen] ENTRADA MON @ 0.02532 (22.59 €, apertura)
- 2026-09-30 17:20 [ruptura_volumen_evento] ENTRADA MON @ 0.02532 (23.06 €, apertura)
- 2026-09-30 17:20 [reversion_bb] ENTRADA ASTER @ 0.66973 (23.10 €, apertura)
- 2026-09-30 17:30 [pullback_tendencia] CIERRE QNT rotura de tendencia bruto -1.24% neto -2.04%
- 2026-09-30 17:30 [ruptura_volumen] CIERRE SUI stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 17:30 [ruptura_volumen_tope] CIERRE SUI stop-loss bruto -1.20% neto -2.30%
- 2026-09-30 17:30 [ruptura_volumen_regimen] CIERRE SUI stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 17:30 [ruptura_volumen_evento] CIERRE SUI stop-loss bruto -1.20% neto -2.30%
- 2026-09-30 17:30 [rebote_extremo] CIERRE AVAX timeout bruto +1.12% neto +0.02%
- 2026-09-30 17:30 [pullback_tendencia] CIERRE ICP rotura de tendencia bruto -1.46% neto -2.26%
- 2026-09-30 17:30 [ruptura_volumen] CIERRE FET stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 17:30 [ruptura_volumen_regimen] CIERRE FET stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 17:30 [ruptura_volumen_evento] CIERRE FET stop-loss bruto -1.20% neto -2.30%
- 2026-09-30 17:25 [pullback_tendencia] ENTRADA ONDO @ 0.448 (22.74 €, apertura)
- 2026-09-30 17:25 [estocastico_rebote] ENTRADA MINA @ 0.1292 (22.89 €, apertura)
- 2026-09-30 17:30 [macd_momentum] CIERRE VVV momentum perdido bruto +0.52% neto +0.02%
- 2026-09-30 17:30 [macd_momentum_regimen] CIERRE VVV momentum perdido bruto +0.52% neto +0.02%
- 2026-09-30 17:30 [macd_momentum_evento] CIERRE VVV momentum perdido bruto +0.52% neto -0.58%
- 2026-09-30 17:25 [estocastico_rebote] ENTRADA ASTER @ 0.66973 (22.89 €, apertura)
- 2026-09-30 17:30 [ruptura_volumen] CIERRE DASH stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 17:30 [ruptura_volumen_regimen] CIERRE DASH stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 17:30 [ruptura_volumen_evento] CIERRE DASH stop-loss bruto -1.20% neto -2.30%
- 2026-09-30 17:30 [estocastico_rebote] CIERRE TRUMP stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 17:30 [macd_sin_salida] CIERRE TRUMP stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 17:30 [c_banda_atr_evento] CIERRE TRUMP stop-loss bruto -1.50% neto -2.60%
- 2026-09-30 17:30 [rebote_extremo] CIERRE SKY timeout bruto -0.39% neto -1.49%
- 2026-09-30 17:35 [ruptura_volumen] CIERRE HYPE stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 17:35 [ruptura_volumen_regimen] CIERRE HYPE stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 17:35 [ruptura_volumen_evento] CIERRE HYPE stop-loss bruto -1.20% neto -2.30%
- 2026-09-30 17:35 [ruptura_volumen] CIERRE UNI stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 17:35 [ruptura_volumen_tope] CIERRE UNI stop-loss bruto -1.20% neto -2.30%
- 2026-09-30 17:35 [ruptura_volumen_regimen] CIERRE UNI stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 17:35 [ruptura_volumen_evento] CIERRE UNI stop-loss bruto -1.20% neto -2.30%
- 2026-09-30 17:35 [estocastico_rebote] CIERRE DOGE timeout bruto +0.12% neto -0.68%
- 2026-09-30 17:30 [pullback_tendencia] ENTRADA DOT @ 1.0979 (22.74 €, apertura)
- 2026-09-30 17:30 [c_banda_atr] ENTRADA XDC @ 0.03028 (22.82 €, apertura)
- 2026-09-30 17:30 [c_banda_atr_tope] ENTRADA XDC @ 0.03028 (23.06 €, apertura)
- 2026-09-30 17:30 [c_banda_atr_regimen] ENTRADA XDC @ 0.03028 (22.82 €, apertura)
- 2026-09-30 17:30 [c_banda_atr_evento] ENTRADA XDC @ 0.03028 (23.08 €, apertura)
- 2026-09-30 17:30 [estocastico_rebote] ENTRADA RENDER @ 1.709 (22.88 €, apertura)
- 2026-09-30 17:35 [ruptura_volumen] CIERRE PENGU stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 17:35 [ruptura_volumen_regimen] CIERRE PENGU stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 17:35 [ruptura_volumen_evento] CIERRE PENGU stop-loss bruto -1.20% neto -2.30%
- 2026-09-30 17:30 [reversion_bb] ENTRADA TRUMP @ 1.808 (23.10 €, apertura)
- 2026-09-30 17:35 [ruptura_volumen] CIERRE SEI stop-loss bruto -1.25% neto -1.75%
- 2026-09-30 17:35 [ruptura_volumen_regimen] CIERRE SEI stop-loss bruto -1.25% neto -1.75%
- 2026-09-30 17:35 [ruptura_volumen_evento] CIERRE SEI stop-loss bruto -1.25% neto -2.35%
- 2026-09-30 17:35 [ruptura_volumen] CIERRE SPX stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 17:35 [pullback_tendencia] CIERRE SPX rotura de tendencia bruto -1.32% neto -2.12%
- 2026-09-30 17:35 [ruptura_volumen_tope] CIERRE SPX stop-loss bruto -1.20% neto -2.30%
- 2026-09-30 17:35 [ruptura_volumen_regimen] CIERRE SPX stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 17:35 [ruptura_volumen_evento] CIERRE SPX stop-loss bruto -1.20% neto -2.30%
- 2026-09-30 17:40 [estocastico_rebote] CIERRE BTC timeout bruto +0.58% neto -0.22%
- 2026-09-30 17:40 [estocastico_rebote] CIERRE SOL timeout bruto +0.39% neto -0.41%
- 2026-09-30 17:35 [estocastico_rebote] ENTRADA HBAR @ 0.0942 (22.87 €, apertura)
- 2026-09-30 17:40 [macd_sin_salida] CIERRE HBAR stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 17:40 [pullback_tendencia] CIERRE ZEC rotura de tendencia bruto -0.81% neto -1.31%
- 2026-09-30 17:35 [pullback_tendencia] ENTRADA HYPE @ 78.7 (22.72 €, apertura)
- 2026-09-30 17:40 [estocastico_rebote] CIERRE LTC timeout bruto +0.49% neto -0.31%
- 2026-09-30 17:40 [pullback_tendencia] CIERRE ONDO rotura de tendencia bruto -0.45% neto -0.95%
- 2026-09-30 17:40 [c_banda_atr] CIERRE WLD stop-loss bruto -1.61% neto -2.41%
- 2026-09-30 17:40 [macd_momentum] CIERRE WLD stop-loss bruto -1.59% neto -2.09%
- 2026-09-30 17:40 [macd_sin_salida] CIERRE WLD stop-loss bruto -1.59% neto -2.09%
- 2026-09-30 17:40 [c_banda_atr_regimen] CIERRE WLD stop-loss bruto -1.61% neto -2.71%
- 2026-09-30 17:40 [macd_momentum_regimen] CIERRE WLD stop-loss bruto -1.59% neto -2.09%
- 2026-09-30 17:40 [c_banda_atr_evento] CIERRE WLD stop-loss bruto -1.61% neto -2.71%
- 2026-09-30 17:40 [macd_momentum_evento] CIERRE WLD stop-loss bruto -1.59% neto -2.69%
- 2026-09-30 17:40 [ruptura_volumen] CIERRE XDC timeout bruto -0.39% neto -0.89%
- 2026-09-30 17:35 [macd_momentum] ENTRADA XDC @ 0.03027 (22.78 €, apertura)
- 2026-09-30 17:35 [macd_sin_salida] ENTRADA XDC @ 0.03027 (22.68 €, apertura)
- 2026-09-30 17:40 [ruptura_volumen_tope] CIERRE XDC timeout bruto -0.39% neto -1.49%
- 2026-09-30 17:35 [macd_momentum_regimen] ENTRADA XDC @ 0.03027 (22.79 €, apertura)
- 2026-09-30 17:35 [macd_momentum_evento] ENTRADA XDC @ 0.03027 (23.00 €, apertura)
- 2026-09-30 17:40 [ruptura_volumen_evento] CIERRE XDC timeout bruto -0.39% neto -1.49%
- 2026-09-30 17:40 [ruptura_volumen] CIERRE PEPE stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 17:40 [ruptura_volumen_regimen] CIERRE PEPE stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 17:40 [ruptura_volumen_evento] CIERRE PEPE stop-loss bruto -1.20% neto -2.30%
- 2026-09-30 17:40 [estocastico_rebote] CIERRE SHIB timeout bruto -0.35% neto -0.85%
- 2026-09-30 17:40 [pullback_tendencia] CIERRE KSM rotura de tendencia bruto -1.30% neto -2.10%
- 2026-09-30 17:35 [estocastico_rebote] ENTRADA TRUMP @ 1.806 (22.87 €, apertura)
- 2026-09-30 17:40 [pullback_tendencia] CIERRE BNB rotura de tendencia bruto -0.30% neto -1.10%
- 2026-09-30 17:40 [pullback_tendencia] CIERRE TON rotura de tendencia bruto +0.30% neto -0.50%
- 2026-09-30 17:40 [ruptura_volumen] CIERRE KAS stop-loss bruto -1.30% neto -1.80%
- 2026-09-30 17:40 [ruptura_volumen_regimen] CIERRE KAS stop-loss bruto -1.30% neto -1.80%
- 2026-09-30 17:40 [ruptura_volumen_evento] CIERRE KAS stop-loss bruto -1.30% neto -2.40%
- 2026-09-30 17:45 [estocastico_rebote] CIERRE ETH timeout bruto +0.38% neto -0.12%
- 2026-09-30 17:45 [ruptura_volumen] CIERRE AAVE stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 17:45 [estocastico_rebote] CIERRE AAVE timeout bruto +0.57% neto +0.07%
- 2026-09-30 17:45 [ruptura_volumen_regimen] CIERRE AAVE stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 17:45 [ruptura_volumen_evento] CIERRE AAVE stop-loss bruto -1.20% neto -2.30%
- 2026-09-30 17:40 [estocastico_rebote] ENTRADA ICP @ 3.015 (22.87 €, apertura)
- 2026-09-30 17:45 [macd_momentum] CIERRE NIGHT take-profit bruto +2.00% neto +1.50%
- 2026-09-30 17:45 [macd_sin_salida] CIERRE NIGHT take-profit bruto +2.00% neto +1.50%
- 2026-09-30 17:45 [macd_momentum_regimen] CIERRE NIGHT take-profit bruto +2.00% neto +1.50%
- 2026-09-30 17:45 [macd_momentum_evento] CIERRE NIGHT take-profit bruto +2.00% neto +0.90%
- 2026-09-30 17:45 [c_banda_atr] CIERRE INJ stop-loss bruto -1.50% neto -2.30%
- 2026-09-30 17:45 [c_banda_atr_regimen] CIERRE INJ stop-loss bruto -1.50% neto -2.60%
- 2026-09-30 17:45 [c_banda_atr_evento] CIERRE INJ stop-loss bruto -1.50% neto -2.60%
- 2026-09-30 17:40 [reversion_bb] ENTRADA WLFI @ 0.0492 (23.10 €, apertura)
- 2026-09-30 17:40 [estocastico_rebote] ENTRADA DASH @ 53.969 (22.87 €, apertura)
- 2026-09-30 17:45 [macd_momentum] CIERRE TON momentum perdido bruto +0.08% neto -0.42%
- 2026-09-30 17:45 [macd_momentum_evento] CIERRE TON momentum perdido bruto +0.08% neto -1.02%
- 2026-09-30 17:45 [ruptura_volumen_tope] CIERRE XMR stop-loss bruto -1.20% neto -2.30%
- 2026-09-30 17:40 [estocastico_rebote] ENTRADA SPX @ 0.3868 (22.87 €, apertura)
- 2026-09-30 17:45 [estocastico_rebote] ENTRADA FET @ 0.1957 (22.87 €, apertura)
- 2026-09-30 17:45 [estocastico_rebote] ENTRADA ALGO @ 0.10986 (22.87 €, apertura)
- 2026-09-30 17:45 [ruptura_volumen] ENTRADA NIGHT @ 0.03368 (22.49 €, apertura)
- 2026-09-30 17:45 [ruptura_estricta] ENTRADA NIGHT @ 0.03368 (22.52 €, apertura)
- 2026-09-30 17:45 [ruptura_volumen_tope] ENTRADA NIGHT @ 0.03368 (22.96 €, apertura)
- 2026-09-30 17:45 [ruptura_volumen_evento] ENTRADA NIGHT @ 0.03368 (22.90 €, apertura)
- 2026-09-30 17:50 [pullback_tendencia] CIERRE USELESS rotura de tendencia bruto -1.07% neto -1.87%
- 2026-09-30 17:45 [pullback_tendencia] ENTRADA MON @ 0.02508 (22.69 €, apertura)
- 2026-09-30 17:50 [estocastico_rebote] ENTRADA BTC @ 74153 (22.87 €, apertura)
- 2026-09-30 17:50 [estocastico_rebote] ENTRADA ETH @ 2366.22 (22.87 €, apertura)
- 2026-09-30 17:50 [estocastico_rebote] ENTRADA SOL @ 105.22 (22.87 €, apertura)
- 2026-09-30 17:50 [pullback_tendencia] ENTRADA QNT @ 265.72 (22.69 €, apertura)
- 2026-09-30 17:50 [estocastico_rebote] ENTRADA NEAR @ 4.7664 (22.87 €, apertura)
- 2026-09-30 17:50 [estocastico_rebote] ENTRADA ADA @ 0.217836 (22.87 €, apertura)
- 2026-09-30 17:50 [estocastico_rebote] ENTRADA SUI @ 1.0404 (22.87 €, apertura)
- 2026-09-30 17:50 [macd_momentum] ENTRADA AVAX @ 9.723 (22.78 €, apertura)
- 2026-09-30 17:50 [macd_sin_salida] ENTRADA AVAX @ 9.723 (22.69 €, apertura)
- 2026-09-30 17:50 [macd_momentum_regimen] ENTRADA AVAX @ 9.723 (22.80 €, apertura)
- 2026-09-30 17:50 [macd_momentum_evento] ENTRADA AVAX @ 9.723 (22.99 €, apertura)
- 2026-09-30 17:50 [macd_momentum] ENTRADA XLM @ 0.199008 (22.78 €, apertura)
- 2026-09-30 17:50 [macd_sin_salida] ENTRADA XLM @ 0.199008 (22.69 €, apertura)
- 2026-09-30 17:50 [macd_momentum_regimen] ENTRADA XLM @ 0.199008 (22.80 €, apertura)
- 2026-09-30 17:50 [macd_momentum_evento] ENTRADA XLM @ 0.199008 (22.99 €, apertura)
- 2026-09-30 17:50 [estocastico_rebote] ENTRADA TAO @ 269.329 (22.87 €, apertura)
- 2026-09-30 17:50 [estocastico_rebote] ENTRADA UNI @ 7.8339 (22.87 €, apertura)
- 2026-09-30 17:50 [estocastico_rebote] ENTRADA DOT @ 1.0968 (22.87 €, apertura)
- 2026-09-30 17:50 [estocastico_rebote] ENTRADA ARB @ 0.1807 (22.87 €, apertura)
- 2026-09-30 17:50 [estocastico_rebote] ENTRADA ENA @ 0.2367 (22.87 €, apertura)
- 2026-09-30 17:55 [macd_sin_salida] CIERRE ENA stop-loss bruto -1.50% neto -2.00%
- 2026-09-30 17:55 [ruptura_estricta] CIERRE KSM stop-loss bruto -2.16% neto -2.96%
- 2026-09-30 17:50 [estocastico_rebote] ENTRADA BNB @ 677.87 (22.87 €, apertura)
- 2026-09-30 17:55 [estocastico_rebote] ENTRADA ZEC @ 1272 (22.87 €, apertura)
- 2026-09-30 17:55 [estocastico_rebote] ENTRADA HYPE @ 78.56 (22.87 €, apertura)
- 2026-09-30 18:00 [macd_momentum] CIERRE XLM momentum perdido bruto -0.25% neto -0.75%
- 2026-09-30 18:00 [macd_momentum_regimen] CIERRE XLM momentum perdido bruto -0.25% neto -0.75%
- 2026-09-30 18:00 [macd_momentum_evento] CIERRE XLM momentum perdido bruto -0.25% neto -1.35%
- 2026-09-30 17:55 [estocastico_rebote] ENTRADA DOGE @ 0.0831768 (22.87 €, apertura)
- 2026-09-30 17:55 [estocastico_rebote] ENTRADA ONDO @ 0.44495 (22.87 €, apertura)
- 2026-09-30 17:55 [estocastico_rebote] ENTRADA WLD @ 0.4701 (22.87 €, apertura)
- 2026-09-30 18:00 [pullback_tendencia] CIERRE MON take-profit bruto +2.00% neto +1.50%
- 2026-09-30 17:55 [macd_momentum] ENTRADA MON @ 0.02548 (22.78 €, apertura)
- 2026-09-30 17:55 [macd_sin_salida] ENTRADA MON @ 0.02548 (22.68 €, apertura)
- 2026-09-30 17:55 [macd_momentum_evento] ENTRADA MON @ 0.02548 (22.99 €, apertura)
- 2026-09-30 17:55 [macd_momentum] ENTRADA TON @ 1.339 (22.78 €, apertura)
- 2026-09-30 17:55 [macd_momentum_evento] ENTRADA TON @ 1.339 (22.99 €, apertura)
- 2026-09-30 18:05 [macd_momentum] CIERRE AVAX momentum perdido bruto -0.31% neto -0.81%
- 2026-09-30 18:05 [macd_momentum_regimen] CIERRE AVAX momentum perdido bruto -0.31% neto -0.81%
- 2026-09-30 18:05 [macd_momentum_evento] CIERRE AVAX momentum perdido bruto -0.31% neto -1.41%
- 2026-09-30 18:05 [ruptura_volumen] CIERRE PUMP stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 18:05 [ruptura_volumen_regimen] CIERRE PUMP stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 18:05 [ruptura_volumen_evento] CIERRE PUMP stop-loss bruto -1.20% neto -2.30%
- 2026-09-30 18:05 [pullback_tendencia] CIERRE DOT rotura de tendencia bruto -0.65% neto -1.15%
- 2026-09-30 18:05 [ruptura_volumen] CIERRE ONDO stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 18:05 [ruptura_volumen_regimen] CIERRE ONDO stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 18:05 [ruptura_volumen_evento] CIERRE ONDO stop-loss bruto -1.20% neto -2.30%
- 2026-09-30 18:05 [ruptura_volumen] CIERRE NIGHT take-profit bruto +2.50% neto +2.00%
- 2026-09-30 18:05 [ruptura_volumen_tope] CIERRE NIGHT take-profit bruto +2.50% neto +1.40%
- 2026-09-30 18:05 [ruptura_volumen_evento] CIERRE NIGHT take-profit bruto +2.50% neto +1.40%
- 2026-09-30 18:05 [ruptura_volumen] CIERRE JUP stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 18:05 [ruptura_volumen_regimen] CIERRE JUP stop-loss bruto -1.20% neto -1.70%
- 2026-09-30 18:05 [ruptura_volumen_evento] CIERRE JUP stop-loss bruto -1.20% neto -2.30%
- 2026-09-30 18:05 [c_banda_atr] CIERRE OP stop-loss bruto -1.63% neto -2.43%
- 2026-09-30 18:05 [c_banda_atr_regimen] CIERRE OP stop-loss bruto -1.63% neto -2.73%
- 2026-09-30 18:05 [c_banda_atr_evento] CIERRE OP stop-loss bruto -1.63% neto -2.73%
- 2026-09-30 18:00 [reversion_bb] ENTRADA MINA @ 0.1287 (23.10 €, apertura)
- 2026-09-30 18:00 [estocastico_rebote] ENTRADA VVV @ 24.401 (22.87 €, apertura)
- 2026-09-30 18:05 [macd_sin_salida] CIERRE TON timeout bruto +1.13% neto +0.63%
- 2026-09-30 18:05 [c_banda_atr] CIERRE KAS stop-loss bruto -1.53% neto -2.33%
- 2026-09-30 18:05 [c_banda_atr_regimen] CIERRE KAS stop-loss bruto -1.53% neto -2.63%
- 2026-09-30 18:05 [c_banda_atr_evento] CIERRE KAS stop-loss bruto -1.53% neto -2.63%
- 2026-09-30 18:00 [estocastico_rebote] ENTRADA XMR @ 481.1 (22.87 €, apertura)

Universo: BTC, XRP, ETH, SOL, QNT, NEAR, LINK, ADA, SUI, AVAX, HBAR, AAVE, ZEC, PUMP, HYPE, XLM, TAO, UNI, LTC, ZRO, DOGE, DOT, ARB, ENA, ICP, FET, TRX, POL, ALGO, ONDO, CRV, WLD, XDC, NIGHT, USELESS, BCH, JUP, PEPE, MON, RENDER, INJ, OP, MINA, FIL, VVV, ASTER, WLFI, SHIB, DASH, PENGU, KSM, TRUMP, BNB, TON, KAS, SKY, XMR, SEI, APT, SPX
