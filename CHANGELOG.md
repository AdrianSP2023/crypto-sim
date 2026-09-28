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
