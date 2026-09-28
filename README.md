# crypto-sim — paper trading automático (sin dinero real)

Plan en 7 fases de 24 h (P1…P7), definido en el proyecto "Crypto Trader".

- **STATUS.md**: resumen actualizado cada 5 min (patrimonio por estrategia,
  últimas operaciones).
- **state/state.json**: estado completo. **state/events.jsonl**: todas las
  entradas y salidas.
- **CHANGELOG.md**: estrategias y cada ajuste, con versión y hora.
- `python report.py [--hours N]`: análisis por estrategia, motivo de salida y
  versión.

Funcionamiento: GitHub Actions ejecuta `engine.py` en bucle (workflow "Motor
P1"). Al cerrarse cada vela de 5 min descarga datos públicos de Kraken, aplica
las estrategias de `strategies.py` con los parámetros de `config.json` y hace
commit del estado. Los cambios en `config.json` se aplican en la vela
siguiente, sin reiniciar.

- **Pausar**: `"enabled": false` en config.json, o Actions → Motor P1 → Disable
  workflow.
- **Verificar**: Actions → Verificación (manual) → Run workflow.
