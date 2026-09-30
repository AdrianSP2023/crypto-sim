# P3 (P3-v2) cerrada 30/09/2026 10:13 UTC

- 208 vueltas, 2.479 cierres = 2.479 eventos `exit`, 221 posiciones abiertas sin cerrar (el motor no las cierra al terminar la fase).
- Ninguna de las 18 estrategias gana neta de comisión. `decide_p7.py`: 0 ciclos completos (la última foto horaria fue a las 09:30Z y el ciclo de 24 h desde 09:43Z necesitaba una a las 09:33Z); ninguna pasa por vía diaria ni semanal.
- Incidentes del contador (sin efecto en operaciones): `loops` retrocedió el 30/09 a las 01:47Z (193→168) y a las 07:34Z (237→176), y `loop_gaps` recoge dos huecos falsos de 131,9 y 312,2 min (hubo commits cada 5 min). Caja, posiciones y cierres idénticos antes y después. Causa desconocida. Con estos huecos `decide_p7.py` marcaría `motor_sano = false` en cualquier ciclo que los contenga; hay que ignorarlos a mano.
- El paper trader del modelo (`modelo/`) no se archiva ni se reinicia: sigue en marcha.
