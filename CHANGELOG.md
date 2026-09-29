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

## P1-v6 — 2026-09-28 14:12 UTC (ajuste in situ: filtro de mercado, prueba A/B)

Motivo: entre las 13:35 y las 14:05 UTC se cerraron 46 operaciones, casi todas
con pérdida (−23,7 €), en las 7 estrategias a la vez. Fue una bajada general del
mercado. Todas las estrategias solo compran, así que en un mercado que cae
pierden juntas.

- **Filtro de amplitud de mercado:** solo se abren compras si al menos el 50%
  de los 60 activos cierra por encima de su EMA50 (velas de 5 min).
- **Prueba A/B:** se añaden 4 variantes con filtro (`*_filtro`) de las 4
  estrategias más activas (c_banda_atr, ruptura_volumen, macd_momentum,
  pullback_tendencia), con los mismos parámetros. Las originales siguen igual
  para comparar en P2 en las mismas condiciones de mercado. Cada variante nueva
  tiene su propia caja de 924,24 €.
- report.py muestra cuántas entradas ha bloqueado el filtro ("filtradas").

## P1-v7 — 2026-09-28 14:46 UTC (ajuste in situ)

- **Nueva variante A/B: estocastico_rebote_filtro** (mismo filtro de amplitud ≥50%).
  Motivo: en la bajada general, estocastico_rebote siguió comprando cada rebote
  (15 posiciones abiertas; 5 de 5 cierres por stop-loss entre 14:13 y 14:43 UTC).
  Su filtro EMA50>EMA100 reacciona tarde en una caída. La original no se toca.
- Filtro P1-v6 sin datos todavía: desde las 14:11 UTC las 4 estrategias
  originales no han abierto nada nuevo. Las pérdidas de estos 30 min (26 cierres,
  −19,3 €) son posiciones abiertas antes de la bajada.

## P1-v8 — 2026-09-28 17:30 UTC (ajuste in situ, variante A/B)

- **Nueva: ruptura_estricta** (misma lógica que ruptura_volumen, más exigente).
  Rompe el máximo de 4 h (antes 2 h) con volumen > 3× la media (antes 2×).
  Stop más holgado, −2% (antes −1,2%), TP +3% y tiempo máximo 3 h.
  Motivo: ruptura_volumen lleva 57 cierres con bruto medio −0,41%: 39 por
  stop-loss (68%, 12 de ellos en ≤3 velas), 7 por TP y 11 por timeout. La
  mayoría de sus rupturas son falsas. La original sigue igual para comparar.

## P1-v9 — 2026-09-28 19:10 UTC (ajuste in situ, variante A/B)

- **Nueva: macd_sin_salida** (macd_momentum sin la salida por "momentum perdido";
  sale solo por TP +2%, SL −1,5% o 3 h).
  Motivo: 43 de 60 cierres de macd_momentum son por "momentum perdido", con bruto
  medio −0,46% a las ~10 velas. Es el mismo patrón que tenía c_banda_atr en v1:
  una salida por señal que corta por ruido y fija la comisión. La original sigue igual.

## P1-v10 — 2026-09-29 01:33 UTC (ajuste in situ, variantes A/B, cambio de código)

- **Nuevo parámetro de estrategia `max_open`** (tope de posiciones simultáneas por estrategia; `core.py`).
  Los bloqueos se cuentan en `blocked_exposure` y `report.py` los suma a la columna "filtradas".
- **Nuevas variantes A/B: `c_banda_atr_tope` y `ruptura_volumen_tope`**, iguales a sus originales pero con
  `max_open: 5`. Cada una tiene su propia caja de 924,24 €. Las originales no se tocan.
  T0 del A/B (tope) = primera entrada de la variante (ver `entry_ts` mínimo de cada `*_tope`).
- Motivo: entre las 01:00 y las 01:31 UTC hubo 114 cierres, todos perdedores (0% de acierto en las 14
  estrategias), con c_banda_atr 17 cierres (-9,74 €), ruptura_volumen 15 (-7,75 €) y sus variantes con filtro
  de amplitud sin bloquear ninguna entrada nueva. Antes tenían 22-25 posiciones abiertas a la vez: las
  pérdidas son de un mismo episodio de mercado, no de señales independientes. Se prueba en vivo el límite de
  exposición previsto para P2, en vez de esperar a una re-simulación que aún no existe.
- Sesgo conocido: al alcanzar el tope, entra el primer activo que dé señal en el orden del universo (no el mejor).
- Pruebas: `tests/test_core.py` pasa entero, con un nuevo `test_max_open` (con tope 1, nunca hay más de 1
  posición simultánea y se registran los bloqueos).

## P3-v1 — 2026-09-29 (fin de P1; ajustes de P2, cambio de código y de config)

**Arranque limpio de P3**: `state/` de P1 archivado en `archive/P1/`; todas las cuentas parten de 924,24 €.
La duración de P3 es de 24 h (ver `phase_end_utc`). Como cambian el precio de ejecución y la comisión, P3 no es
comparable con P1: las cuentas empiezan de nuevo y los conteos de ciclos del criterio de P7 también.

**Cambios del motor (auditoría de P2)**
- **Auditoría:** los indicadores y el filtro de amplitud son causales (sin look-ahead) y solo se procesan velas
  cerradas. Optimista en P1: la entrada se fijaba al *cierre* de la vela que daba la señal.
- **Entrada a la apertura de la vela siguiente** (`entry_fill: "next_open"`): la señal se guarda como pendiente y
  se ejecuta al precio de apertura de la vela siguiente. La vela de entrada ya evalúa SL/TP. `entry_ts` pasa a ser
  la apertura de esa vela (la salida por señal sigue siendo al cierre de la vela de la señal de salida).
- **Comisión por tramos de Bit2Me** (`fee_tiers`, por lado, según volumen de 30 días de cada cuenta): 0,55 % por
  debajo de 2.000 €, 0,25 % de 2.000 a 50.000 €, 0,21 % de 50.000 a 250.000 € (ida+vuelta 1,10 / 0,50 / 0,42 %).
  Cada cierre guarda `fee_pct`. [Suposición] las cifras por lado son la mitad de las de ida y vuelta del plan.
- **Fotos horarias** en `state["snapshots"]` (precios y patrimonio por estrategia valorando lo abierto a mercado,
  menos comisiones) y `state["loop_gaps"]` (huecos > 15 min entre vueltas), para medir ciclos de 24 h.
- **`tools/decide_p7.py`** (y `report.py --ciclos`): decisión determinista de paso a P7 con las salvaguardas del
  plan (PnL con no realizado, neto de comisión y spread, ≥ 30 cierres, versión actual, motor sano, sin la mejor
  operación, sin el mejor activo, superar a la cesta, ciclo no concluyente si la cesta sube > 2 %).
- Pruebas nuevas: referencia independiente de la entrada a la apertura, comisión por tramos y volumen,
  incremental == de golpe en el modo nuevo, y `tests/test_engine_e2e.py` (motor completo con Kraken simulado).

**Cambios de estrategias**
- **Retiradas las 5 variantes `*_filtro`** (amplitud sobre EMA50): en P1 no mostraron ventaja y con menos
  estrategias baja el riesgo de falsos positivos en el criterio de P7. Sustituidas por:
- **Nuevas `c_banda_atr_regimen`, `macd_momentum_regimen`, `ruptura_volumen_regimen`**: igual que la original,
  pero solo entran si ≥ 50 % de los activos cierra sobre su EMA200 de 5 min (≈ 16,7 h), una lectura de régimen
  más lenta que la anterior. Parámetro nuevo `market_filter_ema`.
- Se mantienen: las 7 originales, `ruptura_estricta`, `macd_sin_salida` y los dos `*_tope`. Sin retirar más por
  falta de base estadística (A/B de P1 inconclusos).

## P3-v1 (sin cambio de versión) — 2026-09-29 ~10:30 UTC: registro CSV permanente

Solo registro; el comportamiento de las estrategias no cambia (tests idénticos), así que no se reinicia ningún conteo.
- **`registro/operaciones.csv`**: una fila por operación cerrada (fase, estrategia, familia, versión, activo, tipo,
  entrada/salida UTC, precios, cantidad, bruto, comisión, neto, spread, comisión y resultado en €, motivo de salida,
  velas, hora de entrada y **contexto de la señal**). El motor lo actualiza en cada vuelta con `registro.sync`
  (idempotente: añade solo lo que falta; se autorrepara). P1 está rellenado desde `archive/P1/` (1.395 filas, sin
  contexto de señal porque entonces no se guardaba).
- **Contexto de la señal** (`ctx` en cada posición y cierre): valores de los indicadores de la estrategia en la vela
  de la señal (RSI, ATR, EMA, volumen relativo...) y amplitud de mercado con EMA50 y EMA200. Solo para operaciones
  abiertas a partir de este cambio.
- `tests/test_registro.py`. `registro.py` se añade a los ficheros de código vigilados por el motor y al workflow.

## P3-v1 (sin cambio de versión) — 2026-09-29 ~11:05 UTC: registro de velas de precio

Solo registro (no cambia ninguna estrategia ni reinicia conteos).
- **`datos/velas_5m/<ACTIVO>.csv`**: todas las velas cerradas de 5 min de los 60 activos (time, open, high, low,
  close, vwap, volume, count), sin duplicar (`state["velas_last"]`). Kraken solo devuelve las últimas 720 velas
  (60 h), así que la primera vuelta con este cambio guarda esas 60 h (cubren todo P1 y lo que va de P3) y desde
  ahí se acumulan. Sirve para medir qué hizo el precio tras cada entrada o salida (recorrido máximo a favor y en
  contra, rebotes posteriores), buscar patrones y re-simular sin depender de la ventana de la API.
- Crecimiento estimado: ~1-1,5 MB/día de CSV en el repo.

## Herramientas de datos (sin cambio de versión) — 2026-09-29

- **`tools/historico_kraken.py` + workflow manual "Histórico Kraken"** (`mode=probe|full`): descarga en streaming las
  13 partes (~26 GB) del histórico de trades de Kraken (hasta 30/06/2026), filtra los activos que usamos (EUR y USD) y
  guarda velas de 1 h en `datos/historico_1h/<QUOTE>_<BASE>.csv.gz` más un informe. Para contrastar patrones con años de
  datos (caída y rebote, eventos). Test: `tests/test_historico.py`.
