# Registro de versiones de configuración

Cada ajuste (in situ o en fase de análisis) sube `version` en config.json y se
anota aquí con fecha y hora UTC. Cada operación guarda la versión con la que se
abrió; `python report.py` desglosa el rendimiento por versión.

## P1-v1 — 2026-09-28 (arranque de P1)

Velas de 5 min, los 35 pares en EUR más líquidos de Kraken (sin stablecoins ni
pares con spread > 0,4%), 5 estrategias en paralelo, cada una con 924,24 € y 5%
del patrimonio por operación. Comisión 1,1% ida+vuelta; se mide además el
spread real de Kraken al entrar y salir.

| Estrategia | Entrada | TP / SL / tiempo máx. |
|---|---|---|
| c_banda_atr | Candidata C: cruce EMA3>EMA8, RSI(8) 20-80, hueco > 0,3×ATR(14). Sale también en cruce bajista | +2% / −1,5% / 4 h |
| reversion_bb | Cierre bajo Bollinger(20, 2σ) inferior, RSI(14)<30, ADX(14)<20 | +1,5% / −1,5% / 6 h |
| ruptura_volumen | Cierre sobre el máximo de las 2 h previas, volumen > 2× la media, precio sobre EMA50 | +2,5% / −1,2% / 2 h |
| rebote_extremo | Caída ≥ 3% en 1 h y RSI(14) < 20 | +2% / −2% / 3 h |
| pullback_tendencia | EMA20>EMA50>EMA100, la vela toca la EMA20 y cierra por encima. Sale también si cierra bajo la EMA50 | +2% / −1,5% / 4 h |

Take-profits por encima de la comisión (1,1%), para que una ganadora lo sea en
neto. Las dos primeras vienen del backtest de la Fase 1.5 (adaptadas a 5 min);
las otras tres son nuevas.

## P1-v2 — 2026-09-28 09:55 UTC (ajuste in situ, check-in 1)

- **c_banda_atr: desactivada la salida por cruce bajista** (`exit_on_cross: false`).
  Motivo: 8 de 8 operaciones cerradas por cruce bajista a los 10-35 min, bruto
  medio −0,61%, ninguna llegó al TP. En velas de 5 min, EMA3/8 se vuelve a
  cruzar por ruido antes de que el precio pueda moverse +2%. Con comisión de
  1,1%, esa salida garantiza pérdida. Ahora sale solo por TP +2%, SL −1,5% o 4 h.

## P1-v3 — 2026-09-28 12:00 UTC (ajuste in situ, check-in 3)

- **rebote_extremo: caída mínima 3% → 2,5% en 1 h** (`drop_min: 0.025`).
  Motivo: 3 h sin ninguna señal (su última operación fue a las 09:xx y solo
  con QNT). El objetivo de P1 es el máximo de operaciones y el mercado está
  tranquilo. RSI<20 se mantiene como filtro de sobreventa extrema.
- Sin cambios en las demás: pocos cierres por hora (5), sin fallos mecánicos.
  pullback_tendencia no opera porque no hay tendencia alcista (EMA20>50>100);
  es el régimen de mercado, no un fallo.

## P1-v4 — 2026-09-28 12:30 UTC (ampliación pedida por Maestro)

Objetivo: más operaciones por hora (~5 cierres/h con v1-v3), para que cada
revisión tenga más datos. Revisiones de Claude cada 30 min a partir de ahora.

- **Universo 35 → 60 pares** en EUR (mismo filtro: sin stablecoins/fiat, spread ≤ 0,4%).
- **Nueva: macd_momentum.** Histograma MACD(12,26,9) cruza a positivo con precio
  sobre EMA50. Sale con TP +2%, SL −1,5%, 3 h, o si el histograma lleva 2 velas negativo.
- **Nueva: estocastico_rebote.** Estocástico(14,3,3) %K cruza sobre %D desde
  sobreventa (<20), con EMA50 > EMA100. Sale con TP +1,8%, SL −1,5%, 3 h.
- Motor: pausa entre peticiones a Kraken 0,4 → 0,6 s (60 pares ≈ 55 s por vuelta,
  dentro del límite de la API pública).

## P1-v5 — 2026-09-28 13:00 UTC (ajuste in situ)

- **Tamaño por operación 5% → 2,5% del patrimonio** (hasta ~40 posiciones
  simultáneas por estrategia en lugar de 20).
  Motivo: con 60 pares, ruptura_volumen llegó a 20 posiciones abiertas y
  descartó 9 entradas por falta de caja. El objetivo de P1 es el máximo de
  operaciones. No afecta a los % por operación (bruto/neto), solo a los €.
- Confirmado el efecto de P1-v2 en c_banda_atr: sin la salida por cruce, 9 ops
  (v2+v3) con bruto medio +1,6% (frente a −0,32% en v1).
